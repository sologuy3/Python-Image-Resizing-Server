from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import imghdr
from resizer import *

_SRC_DIR = 'img_src'
_SERVER_ADDRESS = 'localhost'
_SERVER_PORT = 12312


def parse_path(path):
    req_type, path = path.split('@', 1)
    print(req_type)
    if req_type in ['/original']:
        print(_SRC_DIR + path)
        with open(_SRC_DIR +'/'+ path, 'rb') as returnfile:
            file = returnfile.read()
            image_type = imghdr.what(path, h=file)
            return ('image/' + image_type, file)

    elif req_type in ['/resize']:
        resize_dims, path = path.split(':', 1)
        resize_dims = [int(x) for x in resize_dims.split('x')]
        with open(_SRC_DIR +'/'+ path, 'rb') as returnfile:
            file = resize_image(_SRC_DIR + '/' + path, resize_dims)
            image_type = imghdr.what(path, h=returnfile.read())
            return ('image/' + image_type, file)

    else:
        return False


class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        print(self.path)
        if self.path in '/favicon.ico':
            self.send_response(501)
            self.end_headers()
        else:
            return_image = parse_path(self.path)
            if return_image:
                self.send_response(200)
                self.send_header('Content-type', 'image/jpeg')
                self.end_headers()
                self.wfile.write(return_image[1])
                return
            else:
                self.send_response(404)
                self.end_headers()
                return


if __name__ == "__main__":
    # Create a web server and define the handler to manage the
    # incoming request
    server = ThreadingHTTPServer(('', _SERVER_PORT), myHandler)
    print('Started httpserver on port ', _SERVER_PORT)

    # Wait forever for incoming htto requests
    server.serve_forever()
