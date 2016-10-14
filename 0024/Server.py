# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-30 20:02:20
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-14 12:00:50
# @Email: liangchaowu5@gmail.com

###################################################
# build a simple http server 
##################################################

import os
import cPickle as pickle
import subprocess
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
            # execute the file and show the output to the client, CGI protocal
            elif path.endswith('.py'):
                content = self.run_cgi(path)
                self.send_page(content)
            # send a file to the client
            else: 
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


    def run_cgi(self, file_path):
        """run the script of the file_path and print its' output
        
        Args:
            file_path (str): file path of the script 
        
        Returns:
            content(str): std_out of the script
        """
        # how to pass the status of current object to the subprocess
        command = 'python ' + file_path
        p = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out


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
