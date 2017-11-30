import socket
from flask import Flask
from flask import request
from flask import jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    #return "Hello World!"
    #return jsonify({'ip': request.remote_addr})
    return "This is an example wsgi app served from {} from proxy {} to client {}".format(socket.gethostname(), request.remote_addr, request.environ['REMOTE_ADDR'])

if __name__ == "__main__":
    application.run()
