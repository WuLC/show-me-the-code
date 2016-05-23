# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-23 10:44:10
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-23 14:51:15
# @Email: liangchaowu5@gmail.com
# @Function: encrypt the password with specified algorithm, use salt to avoid dictionary attacks


import hashlib
import random

def encrypt_passwd(raw_passwd, algo='sha1'):
    """enrypt the raw_passwd with specified password
    
    Args:
        raw_passwd (str): clear-text password
        algo (str, optional): algorithm provided by hashlib.algorithms to encrypt the raw_passwd
    
    Returns:
        encrypted(str): password that has been encrypted 
    """
    if algo not in hashlib.algorithms:
        print 'encrypt algorithm %s not supported'%algo
        return
    salt = hashlib.sha1(str(random.random())).hexdigest()[:8]
    h = hashlib.new(algo) 
    h.update(salt+raw_passwd)
    # another way to encrypt
    # hashlib.sha1(salt+encrypt).hexdigest()
    encrypted = '$'.join([algo,salt,h.hexdigest()]) 
    return encrypted


def auth_passwd(raw_passwd,encryptd_passwd):
    """authenticate whether the password is right 
    
    Args:
        raw_passwd (str): clear-text password to be authenticated
        encryptd_passwd (str): encrypted password of the user
    
    Returns:
        bool: whether the input-password is right(True) or not(False)
    """
    algo, salt, passwd = encryptd_passwd.split('$')
    h = hashlib.new(algo)
    h.update(salt+raw_passwd)
    if passwd != h.hexdigest():
        return False
    else:
        return True


if __name__ == '__main__':
    r1 = 'test'
    r2 = 'test1'
    e1 = encrypt_passwd(r1)

    if auth_passwd(r1, e1):
        print 'right'
    else:
        print 'wrong'
    
    if auth_passwd(r2, e1):
        print 'right'
    else:
        print 'wrong'

 





