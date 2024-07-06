
from bottle import route, run, static_file

@route('/')
def index():
    with open("index.html", "r") as f:
        contents = f.read()
    return contents

run(host='localhost', port=8080)
