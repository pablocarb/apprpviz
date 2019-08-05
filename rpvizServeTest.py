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
import argparse




def arguments():
    parser = argparse.ArgumentParser(description='toolRPViz: Pathway visualizer. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('infile', 
                        help='Input folder with sbml files as in tar format.')
    parser.add_argument('outfile',
                        help='tar file.')
    parser.add_argument('--choice',
                        default="5",
                        help='What kind of input do you want ? \n 1/Single HTML file \n 2/Separated HTML files \n 3/View directly in Cytoscape \n 4/Generate a file readable in Cytoscape \n')
    parser.add_argument('--selenzyme_table',
                        default="N",
                        help='Do you want to display the selenzyme information ? Y/N')
    parser.add_argument('-server', default='http://localhost:8998/REST',
                        help='RPViz server.')
    return parser

def testApp(url):
    r = requests.get( url )
    res = json.loads( r.content.decode('utf-8') )
    print( res )
    
def testUpload(infile, outfile,choice,selenzyme_table,url):
    data = {'selenzyme_table': 'N', 'input_format': 'sbml'}
    files = { 'file': open(infile, 'rb' ), 'data': ('data.json', json.dumps(data)) }
    r=requests.post(url+'/Query',files=files)
    open(outfile,'wb').write( r.content )
    print( 'Success!' )

if __name__ == '__main__':
    parser = arguments()
    arg = parser.parse_args()
    testApp(arg.server)
    testUpload(arg.infile,arg.outfile,arg.choice, arg.selenzyme_table,arg.server)
