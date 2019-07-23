import unittest
import os
import subprocess
import time

'''
def http_request_optimization():

    # Set url and data here:
    # url
    url = 'http://127.0.0.1:8000/tasks/Optimization'
    # data
    raw_data = {"username": "unittest"}
    raw_data["tsv_files"] =
    raw_data["model_file"] =
    raw_data["num_processes"] = 1
    raw_data["tolerance"] = 0.5

    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
'''

global p_server

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


    def test_calculation(self):
        """ Test calculation request """

    def test_optimization(self):
        """ Test optimization request """



if __name__ == '__main__':

    # 1.Launch server:
    print("---Launching server...")
    path_parent = os.path.abspath('..')
    path_APIs = os.path.join(path_parent, 'REST_FindSim/manage.py')

    command = 'python ' + path_APIs + ' runserver'
    p_server = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

    # 2.Running tests:
    print("---Running tests...")
    suite = unittest.TestSuite()
    # Control test order here:
    # test_server runs server program in background
    # test_terminate terminates the server
    tests = [TestEnv("test_findsim"),
        # APIs' tests here
        TestAPIs("test_calculation"),
        TestAPIs("test_optimization")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)

    # 3.Terminate server
    print("---Terminating server...")
    p_server.kill()
    print("---Finished.")
