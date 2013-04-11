#!/usr/bin/env python

import re
import sys

options = {}

def parse_args(args):
    global options

    if len(args) != 2:
        return -1

    options['location_file'] = args[1]
    return 0

parse_location_re = re.compile("id=(\d+)")

def parse_location(s):
    if s.find('<a') != -1:
        m = parse_location_re.search(s)
        return int(m.group(1))
    return s

location_re = re.compile("(\d+) '(.*)'")

def main():
    if parse_args(sys.argv) < 0:
        exit(1)

    locations = {}
    for l in open(options['location_file'], 'r'):
        l = l.rstrip()
        m = location_re.match(l)
        user_id = int(m.group(1))
        location = parse_location(m.group(2))
        loc_members = locations.get(location, None)
        if loc_members is None:
            loc_members = []
            locations[location] = loc_members
        loc_members.append(user_id)
    print 'var location_map = ',
    print locations,
    print(';')

main()
