#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
doeTest (c) University of Manchester 2019

doeTest is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

Created on Wed May  1 09:54:39 2019

@author:  Pablo Carbonell, SYNBIOCHEM
@description: Test the DoE server 
"""
import requests
import json
import os
import csv

def testApp(url='http://127.0.0.1:8989/REST'):
    r = requests.get( url )
    res = json.loads( r.content.decode('utf-8') )
    print( res )
    
def testUpload(url='http://127.0.0.1:8989/REST'):
    example = os.path.join( 'test', 'DoE_sheet.xlsx' )
    files = { 'file': open(example, 'rb' ) }
    values = {'size': 64}
    r = requests.post( os.path.join(url, 'Query' ), files=files, data=values )
    res = json.loads( r.content.decode('utf-8') )
    M = res['data']['M']
    out = os.path.join( 'test', 'DoE_run.csv')
    with open(out, 'w') as h:
        cw = csv.writer(h)      
        cw.writerow( res['data']['names'] )
        for row in M:
            cw.writerow( row )
    print( 'Size:', res['data']['libsize'], 'Efficiency:', res['data']['J'] )

if __name__ == '__main__':
    testApp()
    testUpload()
