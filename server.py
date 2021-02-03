
from os import name as os_name
import sys

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
import json
import random
import string

from weatherAPI import collectData



PORT = 8888 


def write_out(str):
    sys.stdout.write(str)


class GetDataHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def get(self):
        response = dict()
        print(collectData())
        response['data'] = collectData()
        self.write(response)

def make_app():
    return Application([
        (r"/getData", GetDataHandler)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    write_out('Server listening on port ' + str(PORT))
    IOLoop.current().start()



