#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rpvizTest (c) University of Manchester 2019

rpvizTest is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

Created on Wed May  1 09:54:39 2019

@author:  Pablo Carbonell, SYNBIOCHEM
@description: Test the rpviz server 
"""
import requests
import json
import os
import csv

url = 'http://127.0.0.1:8998/REST'
url = 'http://rpviz.synbiochem.co.uk/REST'

def testApp(url=url):
    r = requests.get( url )
    res = json.loads( r.content.decode('utf-8') )
    print( res )
    
def testUpload(url=url):
    example = os.path.join( 'test', 'path.gz' )
    files = { 'file': open(example, 'rb' ) }
    r = requests.post( os.path.join(url, 'Query' ), files=files )
    res = json.loads( r.content.decode('utf-8') )
    M = res['data']['html']
    out = os.path.join( 'test', 'out.html')
    with open(out, 'w') as h:
        cw = csv.writer(h)      
        for row in M:
            cw.writerow( row )
    print( 'Success!' )

if __name__ == '__main__':
    testApp()
    testUpload()
