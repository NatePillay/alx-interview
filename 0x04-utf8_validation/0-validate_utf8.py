#!/usr/bin/python3
'''
utf-8 interview question
'''
def validUTF8(data):
    ''' function used for checking'''
    try:
        char.encode('utf-8')
        return True
    except UnicodeEncodeError:
        return False
