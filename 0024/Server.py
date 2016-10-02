# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-30 20:02:20
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-02 23:17:30
# @Email: liangchaowu5@gmail.com

###################################################
# build a simple http server 
##################################################
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    
    # deal with GET Request
    def do_GET(self, status_code = 200):
        self.send_response(status_code)
        self.send_content(self.show_user_info())

    def send_content(self, content):
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def show_user_info(self):
        response = '<html><h1>Client information</h1><table border=1>'

        user_values = {
        'client_address': self.client_address[0]+':'+str(self.client_address[1]),
        'request_version': self.request_version,
        'request_method': self.command,
        'path': self.path
        }

        for k,v in user_values.items():
            response += '<tr><td>%s</td><td>%s</td></tr>'%(k,v)
        for k,v in self.headers.items():
            response += '<tr><td>%s</td><td>%s</td></tr>'%(k,v)
        response += '</table></html>'
        return response

    def handle_error(self, error_message):
        content = 'Error:'+ error_message
        self.send_content(content)


if __name__ == '__main__':
    server_address = ('', 10086)
    server = HTTPServer(server_address, RequestHandler)
    server.serve_forever()
