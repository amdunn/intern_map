#!/usr/bin/env python

import sys
import subprocess
import sqlite3
import time
import os
import codecs

from conf import chrome_local_storage_db

options = {}

# Write a string to a file.  We encode the output as UTF-8, with the
# idea that the other side probably is OK with this encoding.  Not
# doing this can cause an error when redirecting the output (as we
# want to do), e.g. can try to interpret codepoint as ascii.
def out(msg):
    sys.stdout.write(codecs.encode(msg, 'utf-8'))
    sys.stdout.flush()

def parse_args(args):
    global options

    # XXX: use optparse
    if len(args) != 2:
        return -1

    options['userfile'] = args[1]
    return 0

def get_where(user):
    global chrome_local_storage_db

    subprocess.call(["google-chrome", "https://www.facebook.com/" + user])

    conn = sqlite3.connect(chrome_local_storage_db)
    c = conn.cursor()
    c.execute("SELECT value FROM ItemTable WHERE key = 'XXX'")
    result = str(c.fetchone()[0]).decode('utf-16')

    return result

def main():
    global options

    if (parse_args(sys.argv) < 0):
        exit(1)

    for l in open(options['userfile'], 'r'):
        l = l.rstrip()
        l_pieces = l.split(',')
        user_id = l_pieces[0]
        user = l_pieces[1]
        out(user_id + ' \'' + get_where(user) + '\'' + '\n')

main()
