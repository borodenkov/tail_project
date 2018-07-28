# encoding: utf-8

from flask import Flask, request, Response, render_template
import datetime
from os import listdir
import string
import codecs

app = Flask(__name__)


from optparse import OptionParser

p = OptionParser()
p.add_option('-i', '--ip', action="store", dest='socket_host', default='0.0.0.0', type="string", 
             help="specify socket host ip")
p.add_option('-p', '--port', action="store", dest='socket_port', default=8088, type="int",
             help="specify socket host port")

options, args = p.parse_args()

if options.socket_host:
    HOST = options.socket_host

if options.socket_port:
    PORT = options.socket_port

@app.route("/",methods = ["GET","POST"])
def fakeword():
    headers = {"Content-Type":"text/html"}
    
    return (render_template('tile.html', request = request), 200, headers)


if __name__ == "__main__":
    #WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host=HOST,
            port=PORT,
            use_reloader=True,
            #processes=1000,
            threaded=True,
            debug=True
            )
