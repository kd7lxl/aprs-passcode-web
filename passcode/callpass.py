#!/usr/bin/env python
'''
Port of Xastir's callpass.c to Python.
'''

KKEY = 0x73e2

def do_hash(callsign):
    rootCall = ''
    ptr = rootCall
    
    for c in callsign:
        if c == '-':
            break
        rootCall += c.upper()
    
    hash = KKEY
    i = 0
    length = len(rootCall)
    
    while (i < length):
        hash ^= ord(rootCall[i])<<8
        hash ^= ord(rootCall[i+1])
        i += 2
    
    return int(hash & 0x7fff)


def check_hash(callsign, hash):
    return do_hash(callsign) == hash


if __name__ == '__main__':
    from sys import argv
    
    if len(argv) > 1:
        print 'Passcode for %s is %d' % (argv[1], do_hash(argv[1]))
    else:
        print 'Usage: ./callpass.py <callsign>'