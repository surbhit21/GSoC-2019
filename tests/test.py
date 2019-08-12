import unittest
import os
import subprocess
import signal
import multiprocessing
import time
import requests
import argparse


TSV_ZIP_PATH = 'test_files/test_opt.zip'
MODEL_DIR = 'test_files/model/'
TSV_DIR = 'test_files/tsv/'
URL_BASE = 'http://127.0.0.1:8000/'
OUTPUTRES = False
OUTPUTJSN = False

def http_request_optimization(n_p, trl, tsv_zip_path, model_path):
    # 1.Set url and data:
    # url
    url = URL_BASE + 'tasks/Optimization/'
    # data
    data = {
        "username": "unittest",
        "num_processes": n_p,
        "tolerance": trl
    }
    # files
    files = {
        'tsv_files': open(tsv_zip_path, 'rb'),
        'model_file': open(model_path, 'rb')
    }
    # 2. Send REST request, get response
    response = requests.post(url, files=files, data=data)
    return response


def http_request_calculation(tsv_path, model_path):
    # 1.Set url and data:
    # url
    url = URL_BASE + 'tasks/Calculation/'
    # data
    data = {
        "username": "unittest",
    }
    # files
    files = {
        'tsv_file': open(tsv_path, 'rb'),
        'model_file': open(model_path, 'rb')
    }
    # 2. Send REST request, get response
    response = requests.post(url, files=files, data=data)
    return response


class TestEnv(unittest.TestCase):

    def test_findsim(self):
        ''' Test FindSim exists '''
        path_parent = os.path.abspath('..')
        path_findsim = os.path.join(
            path_parent,'REST_FindSim/third_party/FindSim/findSim.py')
        path_optimization = os.path.join(
            path_parent,'REST_FindSim/third_party/FindSim/multi_param_minimization.py')

        self.assertTrue(os.path.isfile(path_findsim))
        self.assertTrue(os.path.isfile(path_optimization))


class TestAPIs(unittest.TestCase):

    def handle_response(self,r):
        if OUTPUTRES:
            print(r)
        if OUTPUTJSN:
            print(r.json())
        self.assertEqual('', r.json()['error'])

    '''
    BarChart:
        bc_ratio_sb8.tsv synSynth7.g
    DirectParameter:
        dp_Kd_tau.tsv synSynth7.g
        dp.tsv synSynth7.g
    DoseResponse:
        dr_j2c.tsv synSynth7.g
        dr_ratio_b2c.tsv synSynth7.g
    TimeSeries:
        iclamp_hh13.tsv loadhh.py
        ts_j4d.tsv synSynth7.g
        ts_norm_m3b.tsv synSynth7.g
        ts_ratio_t2a.tsv synSynth7.g
        vclamp_hh.tsv loadhh.py
    '''
    def test_calculation_DP(self):
        """ Test calculation. Type: DirectParameter """
        # dp_Kd_tau.tsv
        tsv = os.path.join(TSV_DIR, 'dp_Kd_tau.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = http_request_calculation(tsv,model)
        self.handle_response(r)
        # dp.tsv
        tsv = os.path.join(TSV_DIR, 'dp.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = http_request_calculation(tsv,model)
        self.handle_response(r)


    def test_calculation_BC(self):
        """ Test calculation. Type: BarChart """
        # bc_ratio_sb8.tsv
        tsv = os.path.join(TSV_DIR, 'bc_ratio_sb8.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = http_request_calculation(tsv,model)
        self.handle_response(r)

    def test_calculation_TS(self):
        """ Test calculation. Type: TimeSeries """
        # iclamp_hh13.tsv
        tsv = os.path.join(TSV_DIR, 'iclamp_hh13.tsv')
        model = os.path.join(MODEL_DIR, 'loadhh.py')
        r = http_request_calculation(tsv,model)
        self.handle_response(r)
        # vclamp_hh.tsv
        tsv = os.path.join(TSV_DIR, 'vclamp_hh.tsv')
        model = os.path.join(MODEL_DIR, 'loadhh.py')
        r = http_request_calculation(tsv,model)
        self.handle_response(r)
        # ts_j4d.tsv
        tsv = os.path.join(TSV_DIR, 'ts_j4d.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = http_request_calculation(tsv,model)
        self.handle_response(r)
        # ts_norm_m3b.tsv
        tsv = os.path.join(TSV_DIR, 'ts_norm_m3b.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = http_request_calculation(tsv,model)
        self.handle_response(r)
        # ts_ratio_t2a.tsv
        tsv = os.path.join(TSV_DIR, 'ts_ratio_t2a.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = http_request_calculation(tsv,model)
        self.handle_response(r)

    def test_calculation_DR(self):
        """ Test calculation. Type: DoseResponse """
        # dr_j2c.tsv
        tsv = os.path.join(TSV_DIR, 'dr_j2c.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = http_request_calculation(tsv,model)
        self.handle_response(r)
        # dr_ratio_b2c.tsv
        tsv = os.path.join(TSV_DIR, 'dr_ratio_b2c.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = http_request_calculation(tsv,model)
        self.handle_response(r)

    def test_optimization_multi_process(self):
        """ Test optimization request: single process """
        tsvs = TSV_ZIP_PATH
        model = os.path.join(MODEL_DIR, 'Gs_To_PKA_31_May_2019.g')
        r = http_request_optimization(6, 0.6, tsvs, model)
        self.handle_response(r)

    def test_optimization(self):
        """ Test optimization request: multi processes """
        tsvs = TSV_ZIP_PATH
        model = os.path.join(MODEL_DIR, 'Gs_To_PKA_31_May_2019.g')
        r = http_request_optimization(1, 0.8, tsvs, model)
        self.handle_response(r)


def launch_API_server():
    path_parent = os.path.abspath('..')
    path_APIs = os.path.join(path_parent, 'REST_FindSim/manage.py')
    command = 'python ' + path_APIs + ' runserver'
    p = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    p.wait()

def main():
    parser = argparse.ArgumentParser()
    # All
    parser.add_argument( '-a', '--All', action="store_true", help='Run all test cases.')
    # Optimization
    parser.add_argument( '-op', '--Optimization', action="store_true", help='Run optimization test cases.')
    # Calculation
    parser.add_argument( '-bc', '--BarChart', action="store_true", help='Run BarChart test cases.')
    parser.add_argument( '-dp', '--DirectParameter', action="store_true", help='Run DirectParameter test cases.')
    parser.add_argument( '-dr', '--DoseResponse', action="store_true", help='Run DoseResponse test cases.')
    parser.add_argument( '-ts', '--TimeSeries', action="store_true", help='Run TimeSeries test cases.')
    # Output
    parser.add_argument( '-or', '--OutputResponse', action="store_true", help='Output http response status when testing.')
    parser.add_argument( '-oj', '--OutputJson', action="store_true", help='Output http response content when testing.')
    parser.add_argument( '-v', '--Verbosity', type = int, default = 2, help='Set verbosity of unittest, default=2')

    args = parser.parse_args()
    global OUTPUTRES
    global OUTPUTJSN
    if args.OutputResponse:
        OUTPUTRES = True
    if args.OutputJson:
        OUTPUTJSN = True

    # TODO(Chen): Try to start server inside the test.py
    # 1.Launch server:
    '''
    print("---Launching server...")
    p_server = multiprocessing.Process(target =launch_API_server, args = ())
    p_server.start()
    '''

    # 2.Running tests:
    print("---Running tests...")

    suite = unittest.TestSuite()
    if args.All :
        tests = [TestEnv("test_findsim"),
            # APIs' tests here
            TestAPIs("test_calculation_BC"),
            TestAPIs("test_calculation_DP"),
            TestAPIs("test_calculation_DR"),
            TestAPIs("test_calculation_TS"),
            TestAPIs("test_optimization"),
            TestAPIs("test_optimization_multi_process")]
    else:
        tests = [TestEnv("test_findsim")]
        if args.Optimization:
            tests.append(TestAPIs("test_optimization"))
            tests.append(TestAPIs("test_optimization_multi_process"))
        if args.BarChart:
            tests.append(TestAPIs("test_calculation_BC"))
        if args.DirectParameter:
            tests.append(TestAPIs("test_calculation_DP"))
        if args.DoseResponse:
            tests.append(TestAPIs("test_calculation_DR"))
        if args.TimeSeries:
            tests.append(TestAPIs("test_calculation_TS"))
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=args.Verbosity)
    res = runner.run(suite)

    '''
    # 3.Terminate server
    print("---Terminating server...")
    os.killpg(os.getpgid(p_server.pid), signal.SIGTERM)
    # p_server.kill()
    print("---Finished.")
    '''

if __name__ == '__main__':

    main()
