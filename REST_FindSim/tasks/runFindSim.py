from third_party.FindSim.findSim import *

# Atfer running the task, return this to front-end/client
class Task_result():

    def __init__(self):
        self.score = 0.0
        self.time = 0.0
        self.figure = ""
        # When something is wrong, front-end/client can get info from this
        self.error = ""


    def set_score(self, _score):
        self.score = _score

    def set_time(self, _time):
        self.time = _time

    def set_figure(self, _figure):
        self.figure = _figure

    def set_error(self, _error):
        self.error = _error



def runTask( script, modelFile , dumpFname = "", paramFname = "", optimizeElec=True, silent = False, scaleParam=[], settleTime = 0, settleDict = {} ):
    ''' If *settleTime* > 0, then we need to return a dict of concs of
    all variable pools in the chem model obtained after loading in model,
    applying all modifications, and running for specified settle time.\n
    If the *settleDict* is not empty, then the system goes through and
    matches up pools to assign initial concentrations.
    '''

    tResult = Task_result()
    if not isinstance(script, type('')) or not isinstance(modelFile, type('')):
        tResult.set_error("Script file or model file is not valid")
        return tResult

    global pause
    solver = "gsl"  # Pick any of gsl, gssa, ee..
    modelWarning = ""
    modelId = ""
    expt, stims, readouts, model = loadTsv( script )

    model.fileName = modelFile
    model.pauseHsolve = PauseHsolve( optimizeElec )
    #This list holds the entire models Reac/Enz sub/prd list for reference
    erSPlist = {}
    # First we load in the model using EE so it is easier to tweak
    try:
        if not os.path.isfile(model.fileName):
            #raise SimError( "Model file name {} not found".format( model.fileName ) )
            tResult.set_error("Model file name {} not found".format( model.fileName ))
            return tResult
        fileName, file_extension = os.path.splitext(model.fileName)
        if file_extension == '.xml':
            modelId, errormsg = moose.mooseReadSBML( model.fileName, 'model', 'ee' )
        elif file_extension == '.g':
            modelId = moose.loadModel( model.fileName, 'model', 'ee' )
        # moose.delete('/model[0]/kinetics[0]/compartment_1[0]')
        elif file_extension == '.py':
            # Assume a moose script for creating the model. It must have a
            # function load() which returns the id of the object containing
            # the model. At this point the model must be in the current dir
            mscript = imp.load_source( "mscript", model.fileName )
            #mscript = __import__( fileName )
            modelId = mscript.load()


        for f in moose.wildcardFind('/model/##[ISA=ReacBase],/model/##[ISA=EnzBase]'):
            erSPlist[f] = {'s':len(f.neighbors['sub']), 'p':len(f.neighbors['prd'])}
        # Then we apply whatever modifications are specified by user or protocol

        modelWarning = ""
        model.modify( modelId, erSPlist,modelWarning )
        model._scaleParams( scaleParam )
        if len(dumpFname) > 2:
            if dumpFname[-2:] == '.g':
                moose.mooseWriteKkit( modelId.path, dumpFname )
            elif len(dumpFname) > 4 and dumpFname[-4:] == '.xml':
                moose.mooseWriteSBML( modelId.path, dumpFname )
            else:
                #raise SimError( "Subset file type not known for '{}'".format( dumpFname ) )
                tResult.set_error("Subset file type not known for '{}'".format( dumpFname ))
                return tResult

        if len(paramFname) > 0:
            generateParamFile( modelId.path, paramFname )
            quit()


        model.buildModelLookup()


        if expt.exptType == 'directparameter':
            score = Readout.directParamScore( readouts, model.modelLookup, model.scoringFormula )
            tResult.set_score(score)

            moose.delete( modelId )
            if moose.exists( '/library' ):
                moose.delete( '/library' )
            return tResult

        '''
        for i in stims:
            if i.field == 'Vclamp':
                buildVclamp( i, model.modelLookup )
        '''


        '''
        if stims[0].field == 'Vclamp':
            readouts[0].entities = ['vclamp']
            #readouts[0].field = 'current'
            buildVclamp( stims[0], model.modelLookup )
        '''


        hasVclamp = False
        readoutStim = stims[0]
        for i in stims:
            if i.field.lower() == 'vclamp':
                hasVclamp = True
                buildVclamp( i, model.modelLookup )
            elif i.field.lower() == 'inject':
                readoutStim = i
            if len(i.entities) > 0 and i.entities[0].lower() == 'syninput':
                readoutStim = i
        if readouts[0].field in ( epspFields + epscFields ):
            readouts[0].stim = readoutStim
        makeReadoutPlots( readouts, model.modelLookup )
        if hasVclamp:
            #build the solver with a flag to say rebuild the hsolve.
            buildSolver( modelId, model.solver, useVclamp = True )
        else:
            buildSolver( modelId, model.solver )
        if file_extension != '.py': # rdesigneur sims will set own clocks
            for i in range( 10, 20 ):
                moose.setClock( i, 0.1 )

        ##############################################################
        # Here we handle presettling. First to generate, then to apply
        # the dict of settled values.
        if settleTime > 0:
            t0 = time.time()
            moose.reinit()
            #print settleTime
            moose.start( settleTime )
            w = moose.wildcardFind( modelId.path + "/##[ISA=PoolBase]" )
            ret = {}
            for i in w:
                if not i.isBuffered:
                    ret[i.path] = i.n
                    #print( "{}.nInit =   {:.3f}".format( i.path, i.n ))
            #print "-------------------- settle done -------------------"
            moose.delete( modelId )
            if moose.exists( '/library' ):
                moose.delete( '/library' )
            #print( "Done settling in {:.2f} seconds".format( time.time()-t0))
            print( "s", end = '' )
            sys.stdout.flush()
            tResult.set_score(ret)

            return tResult

        for key, value in settleDict.items():
            moose.element( key ).nInit = value
        ##############################################################

        t0 = time.time()
        score = runit( expt, model,stims, readouts, modelId )
        elapsedTime = time.time() - t0
        '''
        if not hidePlot:
            print( "Score = {:.3f} for\t{}\tElapsed Time = {:.1f} s".format( score, os.path.basename(script), elapsedTime ) )
            for i in readouts:
                pyplot.figure(1)
                i.displayPlots( script, model.modelLookup, stims[0], hideSubplots, expt.exptType )

            pyplot.show()
            #pyplot_fig = mpld3.fig_to_html(pyplot.figure(1))
            #mpld3.show()
        '''
        moose.delete( modelId )
        if moose.exists( '/library' ):
            moose.delete( '/library' )
        tResult.set_score(score)
        tResult.set_time(elapsedTime)
        tResult.set_figure(mpld3.fig_to_html(pyplot.figure(1)))
        return tResult

    except SimError as msg:
        if not silent:
            print( "Error: findSim failed for script {}: {}".format(script, msg ))
            tResult.set_error("Error: findSim failed for script {}: {}".format(script, msg ))
        if modelId:
            moose.delete( modelId )
            if moose.exists( '/library' ):
                moose.delete( '/library' )
        return tResult
