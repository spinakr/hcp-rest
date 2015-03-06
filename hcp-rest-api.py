import json
import bottle
from bottle import route, run, request, abort

@route('/data', method='PUT')
def put_data():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    f = open('data', 'a')
    f.write(data + "\n")
    f.close()
    print entity

run(host='localhost', port=8080)
