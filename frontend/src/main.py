
from bottle import get, run

@get('/')
def index():
    with open("index.html", "r") as f:
        contents = f.read()
    return contents

run(host='localhost', port=8080)
