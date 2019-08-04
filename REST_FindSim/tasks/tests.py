from django.test import TestCase
from django.test import Client
from django.urls import reverse

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
OUTPUT_STATUS = True
OUTPUT_JSON = True

class TestCalculation(TestCase):

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

    def setUp(self):
        # build client
        self.test_client = Client()
        # set url
        self.test_url = reverse('calculation-list')

    def test_calculation_BC(self):
        """ Test calculation. Type: BarChart """
        # bc_ratio_sb8.tsv
        tsv = os.path.join(TSV_DIR, 'bc_ratio_sb8.tsv')
        model = os.path.join(MODEL_DIR, 'synSynth7.g')
        r = self.send_request(tsv,model)
        self.handle_response(r)

    def test_calculation_DP(self):
        """ Test calculation. Type: DirectParameter """
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

    def test_calculation_DR(self):
        """ Test calculation. Type: DoseResponse """
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

    def test_calculation_TS(self):
        """ Test calculation. Type: TimeSeries """
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
    Test files are following:
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

    def setUp(self):
        # build client
        self.test_client = Client()
        # set url
        self.test_url = reverse('optimization-list')

    # With num_processes as '1'
    def test_single_process(self):
        """ Test optimization request: multi processes """
        tsvs = TSV_ZIP_PATH
        model = os.path.join(MODEL_DIR, 'Gs_To_PKA_31_May_2019.g')
        r = self.send_request(1, 0.8, tsvs, model)
        self.handle_response(r)

    # With num_processes more than '1'
    def test_multi_process(self):
        """ Test optimization request: single process """
        tsvs = TSV_ZIP_PATH
        model = os.path.join(MODEL_DIR, 'Gs_To_PKA_31_May_2019.g')
        r = self.send_request(6, 0.6, tsvs, model)
        self.handle_response(r)
