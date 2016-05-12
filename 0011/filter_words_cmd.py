# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-12 22:36:49
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-12 23:00:58
# @Email: liangchaowu5@gmail.com

import cmd
import sys

#reload(sys)
#sys.setdefaultencoding('utf8')

filtered_words_filepath = 'filtered_words.txt'

class CLI(cmd.Cmd):

    def __init__(self):
        # 初始化，提取敏感词列表
        cmd.Cmd.__init__(self)
        self.intro = 'Filtered Words Detective'
        self.words = map(lambda i: i.strip(), open(filtered_words_filepath))
        self.prompt = ">>"    # define command prompt

    def default(self, line):
        if any([i in line for i in self.words]):
            print 'Freedom'
        else:
            print 'Human Rights'

    def do_quit(self, arg):
        exit()
        return True

if __name__ =="__main__":
    cli = CLI()
    cli.cmdloop()