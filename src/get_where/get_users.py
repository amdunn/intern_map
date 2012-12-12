#!/usr/bin/env python

# Get user ids and names from a group.  Needs a FB access token as
# input - you can actually just use one you generate from the Graph
# API Explorer.

import json
import sys
import urllib, urllib2
import time

from conf import group_number

options = {}

def error(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()

def out(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()

class FBAPIException(Exception):
    def __init__(self, msg):
        super(FBAPIException, self).__init__(msg)

class FBrequestor(object):
    """Basic low-level requestor of graph API data."""
    def __init__(self, access_token):
        self._access_token = access_token

    def make_request(self, request):
        try:
            full_request = 'https://graph.facebook.com/' + request + \
                '?access_token=' + self._access_token
            result = json.load(urllib2.urlopen(full_request))
            if ('error' in result):
                msg = result['error'].get_key('message', 'Unknown error')
                error_type = result['error'].get_key('type', None)
                if (error_type is not None):
                    msg = error_type + ': ' + msg
                msg = request + ' -> ' + msg
                raise FBAPIException(msg)
        except urllib2.HTTPError as e:
            raise FBAPIException(request + ' -> ' + str(e))

        return result

def parse_args(args):
    global options

    if (len(args) != 2):
        return -1

    options['access_token'] = args[1]
    return 0

def get_username(member_data):
    if ('username' in member_data):
        return member_data['username']
    if ('link' in member_data):
        link = member_data['link']
        slash_pos = link.rfind('/')
        if (slash_pos == -1):
            return None
        return link[slash_pos+1:]
    return None

def main():
    global options, group_number
    if (parse_args(sys.argv) < 0):
        exit(1)

    requestor = FBrequestor(options['access_token'])

    member_result = requestor.make_request(str(group_number) + '/members')
    for member in member_result['data']:
        user_id = str(member['id'])
        num_tries = 3
        for attempt in range(num_tries):
            try:
                member_data = requestor.make_request(user_id)
                username = get_username(member_data)
                if (username is not None):
                    out(user_id + ',' + username + '\n')
                    break
            except FBAPIException as e:
                error(str(e) + '\n')
                if attempt == num_tries - 1:
                    out('Error: ' + user_id + '\n')

main()
