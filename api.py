import flask,os
from pyresparser import ResumeParser
from flask import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        data = ResumeParser(f.filename).get_extracted_data()
        os.remove(f.filename)
        return data


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()