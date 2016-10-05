# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-30 20:02:20
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-05 15:41:08
# @Email: liangchaowu5@gmail.com

###################################################
# build a simple http server 
##################################################

import os
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    status_code = 200
    
    # deal with GET Request
    def do_GET(self):
        self.send_response(self.status_code)
        # find the local path of the  directory from the requested url
        path = os.getcwd().replace('\\','/') + self.path 
        if self.path == '/': # make request to the root directory
            path += 'index.html'
        if os.path.isfile(path):
            # show on the page
            if path.endswith(('html','htm','txt')):
                with open(path) as f:
                    self.send_page(f.read())
            else: # send a file to the client
                self.send_file(path)
        elif os.path.isdir(path):
            self.list_dir(path)
        else:
            error_message = '404, file %s not exists'%self.path.split('/')[-1]
            self.handle_error(404, error_message)
        

    def send_page(self, content):
        """show content on the browser
        
        Args:
            content (str): content to be shown on the browser
        
        Returns:None
        """
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)


    def send_file(self, file_path): 
        """offer the binary file to be downloaded by user
        
        Args:
            file_path (str): file path on the server
        """
        self.send_header('Content-Type','application/octet-stream')
        self.send_header('Content-Length', os.path.getsize(file_path))
        self.end_headers()
        # send a big file
        size = 1024*100
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(size)
                if chunk:
                    self.wfile.write(chunk)
                else:
                    return


    def list_dir(self, dir_path):
        """show all files under a directory and add url for each item
        
        Args:
            dir_path (str): local path of directory
        
        Returns:None
        """
        files = os.listdir(dir_path)
        content = ''
        for f in files:
            content += '<a href = "{0}">{1}</a></br>'.format(self.path+'/'+f, f) 
        self.send_page(content)


    def user_info_page(self):
        """show information of the user on the browser,including request headers and ip address
        
        Returns:
            TYPE
        """
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


    def handle_error(self, error_code, error_message):
        """deal with error
        
        Args:
            error_code (int): http code represents the error
            error_message (str): detail infomation of the error
        
        Returns:None
        """
        self.status_code = 404
        content = 'Error:'+ error_message
        self.send_page(content)


if __name__ == '__main__':
    server_address = ('', 10086)
    server = HTTPServer(server_address, RequestHandler)
    server.serve_forever()
