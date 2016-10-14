# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-14 10:34:05
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-14 11:42:44
# @Email: liangchaowu5@gmail.com

######################################################################################
# show information of the user on the browser,including request headers and ip address
######################################################################################


def show_user_info(handler):   
    response = '<html><h1>Client information</h1><table border=1>'

    user_values = {
    'client_address': handler.client_address[0]+':'+str(handler.client_address[1]),
    'request_version': handler.request_version,
    'request_method': handler.command,
    'path': handler.path
    }

    for k,v in user_values.items():
        response += '<tr><td>%s</td><td>%s</td></tr>'%(k,v)
    for k,v in handler.headers.items():
        response += '<tr><td>%s</td><td>%s</td></tr>'%(k,v)
    response += '</table></html>'

    print response