# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-25 11:51:07
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-25 11:52:27
# @Email: liangchaowu5@gmail.com

import sys
import urllib2
import json


# fill in your YouDao key and keyfrom  here
KEY = '782091608'
KEY_FROM = 'words1'

class YoudaoTranslate:
    def __init__(self, key, keyfrom):
        """init YouDao API with key and keyform, fetch your own on http://fanyi.youdao.com/openapi?path=data-mode
        
        Args:
            key (str): API key that you got from http://fanyi.youdao.com/openapi?path=data-mode
            keyfrom (str): keyform you got from http://fanyi.youdao.com/openapi?path=data-mode
        """
        if key and keyfrom:
            self.key = key 
            self.keyfrom = keyfrom
        else:
            print "key and keyform can't be empty, fetch your own on http://fanyi.youdao.com/openapi?path=data-mode"
            sys.exit()

    def get_translation(self,word):
        url = 'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=json&version=1.1&q=%s'%(self.keyfrom, self.key, word)
        result = urllib2.urlopen(url).read()
        json_result = json.loads(result)

        # 
        if json_result['errorCode'] != 0:
            print 'key and keyfrom not match,check it carefully'
            sys.exit()

        # 有道翻译
        if "translation" in json_result:
            print '============================================'
            print u'有道翻译:'
            for val in json_result["translation"]:
                print val
            print '-------'

        # 有道词典-基本词典
        if 'basic' in json_result and 'explains' in json_result['basic']:
            print u'有道词典-基本词典:'
            for val in json_result['basic']['explains']:
                print val
            print '-------'

        # 网络释义
        if 'web' in json_result:
            print u'网络释义:'
            for i in xrange(len(json_result['web'])):
                print '%s)'%(i+1),
                for val in json_result['web'][i]['value']:
                    print val,
                print ''
            print '============================================'


if __name__ == '__main__':
    youdao = YoudaoTranslate(key=KEY,keyfrom=KEY_FROM)
    while True:
        msg=raw_input('>')
        if msg == 'quit':
            break
        youdao.get_translation(msg)