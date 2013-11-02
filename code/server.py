from flask import Flask
from werkzeug.serving import run_simple

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return '<html><head><title>Ubicacion</title></head><body><h1>En la 38</h1></body></html>'

if __name__ == '__main__':
    run_simple('localhost', 9000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)
