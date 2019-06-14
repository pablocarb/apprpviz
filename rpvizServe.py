'''
doeServe (c) University of Manchester 2018

doeServe is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  Pablo Carbonell, SYNBIOCHEM
@description: A REST service for OptDes 
'''
import os
from datetime import datetime
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import tempfile
from rpviz.main import run

app = Flask(__name__)
api = Api(app)

def stamp( data, status=1 ):
    appinfo = {'app': 'rpviz', 'version': '1.0', 
               'author': 'Anaelle Badier, Pablo Carbonell',
               'organization': 'Synbiochem',
               'time': datetime.now().isoformat(), 
               'status': status}
    out = appinfo.copy()
    out['data'] = data
    return out

class RestApp( Resource ):
    """ REST App."""
    def post(self):
        return jsonify( stamp(None) )
    def get(self):
        return jsonify( stamp(None) )


class RestQuery( Resource ):
    """ REST interface that generates the Design.
        Avoid returning numpy or pandas object in
        order to keep the client lighter.
    """
    def post(self):
        file_upload = request.files['file']
        content = file_upload.read()
        infile = os.path.join( os.path.dirname(__file__), 'in.html')
        open(infile, 'w').write(content)
        tmpin = tempfile.NamedTemporaryFile()
        tmpin.write(content)
        infile = tmpin.name
        outfile = tempfile.NamedTemporaryFile().name
        outfile = os.path.join( os.path.dirname(__file__), 'test.html')
        run( infile, outfile )
        with open(outfile) as h:
            html = h.read()
#        data = {'html': html}
        data = {'html': ''}
        return jsonify( stamp(data, 1) )

api.add_resource(RestApp, '/REST')
api.add_resource(RestQuery, '/REST/Query')

if __name__== "__main__":  
    debug = os.getenv('USER') == 'pablo'
    app.run(host="0.0.0.0", port=8998, debug=debug, threaded=True)

