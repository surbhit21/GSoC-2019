'''
This is the test file.
'''
from django.test import TestCase, SimpleTestCase
from django.test import Client
from django.test import tag
from django.urls import reverse

import os
import subprocess
import signal
import multiprocessing
import time
import requests
import argparse

# -------Some Configurations-------
# Paths to test file
TSV_ZIP_PATH = 'test_files/test_opt.zip'
MODEL_DIR = 'test_files/model/'
TSV_DIR = 'test_files/tsv/'
HTML_DIR = 'test_files/output/html/'
# After each testcase, output http response status if set'True'
OUTPUT_STATUS = True
# After each testcase, output http response json data if set'True'
OUTPUT_JSON = True
# After each experiment, save html of figure into loacl file if set'True'
OUTPUT_HTML = True
# Global variable for naming html file
TIME_STAMP = ''

# Test API for experiment
class TestExperiment(TestCase):

    # Open output html file:
    @classmethod
    def setUpClass(cls):
        global TIME_STAMP
        TIME_STAMP = time.strftime("%Y_%m_%d_%H:%M:%S", time.localtime())

    @classmethod
    def tearDownClass(cls):
        print('-------Testing experiments finished-------')

    # Output necessary info;
    # Check if there is errors.
    def handle_response(self,response):
        self.assertEqual('', response.json()['error'])
        # Output some info
        if OUTPUT_STATUS:
            print('Status: '+str(response.status_code))
        if OUTPUT_JSON:
            print(response.json())
        if OUTPUT_HTML:
            self.html_file.write(response.json()['figure'])

    # According to tsv_path and model_path,
    # send REST request django.test.Client
    def send_request(self, tsv_path, model_path):
        # 1.Set data
        contents = {
            "username": "unittest",
            'tsv_file': open(tsv_path, 'rb'),
            'model_file': open(model_path, 'rb')
        }
        # 2. Send REST request, get response
        response = self.test_client.post(self.test_url, contents)
        return response

    # 1.Build django.test.Client for sending REST requests.
    # 2.Get utl using django.urls.reverse().
    # 3.Open html file for writing figures.
    def setUp(self):
        # build client
        self.test_client = Client()
        # set url
        self.test_url = reverse('experiment-list')
        # Open file
        html_path = TIME_STAMP + '.html'
        html_path = os.path.join(HTML_DIR, html_path)
        self.html_file = open(html_path,"a")

    # Close html file.
    def tearDown(self):
        self.html_file.close()

    @tag('BC','experiment')
    def test_experiment_BC(self):
        """ Test experiment. Type: BarChart """
        # bc_ratio_sb8.tsv
        tsv = os.path.join(TSV_DIR, 'bc_ratio_sb8.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = self.send_request(tsv,model)
        self.handle_response(r)

    @tag('DP','experiment')
    def test_experiment_DP(self):
        """ Test experiment. Type: DirectParameter """
        # dp_Kd_tau.tsv
        tsv = os.path.join(TSV_DIR, 'dp_Kd_tau.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = self.send_request(tsv,model)
        self.handle_response(r)
        # dp.tsv
        tsv = os.path.join(TSV_DIR, 'dp.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = self.send_request(tsv,model)
        self.handle_response(r)

    @tag('DR','experiment')
    def test_experiment_DR(self):
        """ Test experiment. Type: DoseResponse """
        # dr_ratio_b2c.tsv
        tsv = os.path.join(TSV_DIR, 'dr_ratio_b2c.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = self.send_request(tsv,model)
        self.handle_response(r)
        # dr_j2c.tsv
        tsv = os.path.join(TSV_DIR, 'dr_j2c.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = self.send_request(tsv,model)
        self.handle_response(r)

    @tag('TS','experiment')
    def test_experiment_TS(self):
        """ Test experiment. Type: TimeSeries """
        # iclamp_hh13.tsv
        tsv = os.path.join(TSV_DIR, 'iclamp_hh13.tsv')
        model = os.path.join(MODEL_DIR, 'loadhh.py')
        r = self.send_request(tsv,model)
        self.handle_response(r)
        # vclamp_hh.tsv
        tsv = os.path.join(TSV_DIR, 'vclamp_hh.tsv')
        model = os.path.join(MODEL_DIR, 'loadhh.py')
        r = self.send_request(tsv,model)
        self.handle_response(r)
        # ts_j4d.tsv
        tsv = os.path.join(TSV_DIR, 'ts_j4d.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = self.send_request(tsv,model)
        self.handle_response(r)
        # ts_norm_m3b.tsv
        tsv = os.path.join(TSV_DIR, 'ts_norm_m3b.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = self.send_request(tsv,model)
        self.handle_response(r)
        # ts_ratio_t2a.tsv
        tsv = os.path.join(TSV_DIR, 'ts_ratio_t2a.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = self.send_request(tsv,model)
        self.handle_response(r)

    '''
    Testing files are following:
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
# Test API for optimizatin
class TestOptimization(TestCase):

    # Output necessary info;
    # Check if there is errors.
    def handle_response(self,response):
        if OUTPUT_STATUS:
            print('Status: '+str(response.status_code))
        if OUTPUT_JSON:
            print(response.json())
        self.assertEqual('', response.json()['error'])

    # According to tsv_path and model_path,
    # send REST request django.test.Client
    def send_request(self, n_p, trl, tsv_path, model_path):
        # 1.Set data
        contents = {
            "username": "unittest",
            "num_processes": n_p,
            "tolerance": trl,
            'tsv_files': open(tsv_path, 'rb'),
            'model_file': open(model_path, 'rb')
        }
        # 2. Send REST request, get response
        response = self.test_client.post(self.test_url, contents)
        return response

    # 1.Build django.test.Client for sending REST requests
    #  2. Get url using django.urls.reverse().
    def setUp(self):
        # build client
        self.test_client = Client()
        # set url
        self.test_url = reverse('optimization-list')

    # With num_processes as '1'
    @tag('optimization')
    def test_single_process(self):
        """ Test optimization request: multi processes """
        tsvs = TSV_ZIP_PATH
        model = os.path.join(MODEL_DIR, 'Gs_To_PKA_31_May_2019.g')
        r = self.send_request(1, 0.8, tsvs, model)
        self.handle_response(r)

    # With num_processes more than '1'
    @tag('optimization')
    def test_multi_process(self):
        """ Test optimization request: single process """
        tsvs = TSV_ZIP_PATH
        model = os.path.join(MODEL_DIR, 'Gs_To_PKA_31_May_2019.g')
        r = self.send_request(6, 0.6, tsvs, model)
        self.handle_response(r)

# django.SimpleTestCase is guaranteed to be ran after django.TestCase
# This class is for printing info after tests.
class TestFinishing(SimpleTestCase):

    @tag('TS','BC','DR','DP','experiment')
    def test_finishing_experiments(self):
        print('-------TestCases finished-------')

        html_path = TIME_STAMP + '.html'
        html_path = os.path.join(HTML_DIR, html_path)
        if OUTPUT_HTML:
            print('==================================================Notice==================================================')
            print('||')
            print('|| You can find figures in ', html_path)
            print('||')
            print('==========================================================================================================')
