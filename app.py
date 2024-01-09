from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><head><title>Test</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous"></head><body><p>Test file.</p></body></html>'