#!/usr/bin/env python3

__author__ = "Aurryon SCHWARTZ"
__copyright__ = "Copyright (C) 2019 StarAurryon"
__license__ = "MIT"
__version__ = "1.0"

from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
import os, stat as st

in_path = 'data/in/'
out_path = 'data/out/'

app = Flask(__name__)

@app.route("/", methods=["GET"])
def download():
    in_files = os.listdir(in_path)
    in_files = [(os.stat(in_path + path), path) for path in in_files]
    in_files = [(stat[st.ST_MTIME], path)
           for stat, path in in_files if st.S_ISREG(stat[st.ST_MODE])]
    in_files = sorted(in_files)
    out_files = [f for f in os.listdir(out_path) if isfile(join(mypath, f))]
    in_files = [f[1] for f in in_files if f[1] not in out_files]
    if in_files:
        result = send_from_directory(in_path, in_files[0], as_attachment=True)
        result
        return result
    return ""

@app.route("/", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return 'ERROR: No file part'

    file = request.files['file']

    if file.filename == '':
        return 'ERROR: No selected file'

    filename = secure_filename(file.filename)
    file.save(out_path + filename)
    return "OK"

if __name__ == '__main__':
    app.run()
