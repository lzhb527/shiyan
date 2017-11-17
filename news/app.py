#!/usr/bin/env python3
import os
import json
from flask import Flask,reder_template,abort

app=Flask(__name__)

class Files(object):
    dir=os.path.join(os.path.dirname(__name__),'..','files')
    def __init__(self):
        pass
    def _read_all_files(self):
        pass
    def get_title_list(self):
        pass
    def get_by_filename(self):
        pass

files=Files()
@app.route('/')

@app.route('/files/<filename>')

@app.errorhandler(404)

if __name__=='__main__':
    app.run()
