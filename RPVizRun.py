# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:47:22 2019

@author: anael
"""
import os
import argparse
from rpviz.main import run




def arguments():
    parser = argparse.ArgumentParser(description='toolRPViz: Pathway visualizer. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('infile', 
                        help='Input folder with sbml files as in tar format.')
    parser.add_argument('outfolder',
                        help='folder for the output')
    parser.add_argument('--choice',
                        default="2",
                        help='What kind of input do you want ? \n 1/Single HTML file \n 2/Separated HTML files \n 3/View directly in Cytoscape \n 4/Generate a file readable in Cytoscape \n')
    parser.add_argument('--format',
                        help='What kind of input is it ? sbml/csv')
    parser.add_argument('--selenzyme_table',
                        default="N",
                        help='Do you want to display the selenzyme information ? Y/N')
    parser.add_argument('--filenames',
                        help='import a csv file matching smiles and products names')
    return parser


if __name__ == '__main__':
    parser = arguments()
    arg = parser.parse_args()
    outFolder=arg.outfolder
    if not os.path.exists( outFolder ): 
        os.mkdir(outFolder)
    run(arg.infile,outFolder,arg.format,arg.choice,arg.selenzyme_table,arg.filenames)
