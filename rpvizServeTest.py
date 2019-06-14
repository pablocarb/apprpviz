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
import argparse


def arguments():
    parser = argparse.ArgumentParser(description='toolRPViz: Pathway visualizer. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('infile', 
                        help='Pathways in SBML format.')
    parser.add_argument('outfile', 
                        help='HTML visualizer file.')
    parser.add_argument('-server', default='http://rpviz.synbiochem.co.uk/REST',
                        help='RPViz server.')
    return parser

def testApp(url):
    r = requests.get( url )
    res = json.loads( r.content.decode('utf-8') )
    print( res )
    
def testUpload(infile, outfile, url):
    files = { 'file': open(infile, 'rb' ) }
    r = requests.post( os.path.join(url, 'Query' ), files=files )
    res = json.loads( r.content.decode('utf-8') )
    html = res['data']['html']
    with open(outfile, 'w') as h:
        h.write(html)      
    print( 'Success!' )

if __name__ == '__main__':
    parser = arguments()
    arg = parser.parse_args()
    testApp(arg.server)
    testUpload(arg.infile,arg.outfile,arg.server)
