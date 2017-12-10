#!/usr/bin/env python
import argparse
import requests
import sys

def parse_args():
    """Parse arguments passed at the command line"""
    parser = argparse.ArgumentParser(description='Takes a Zoom Personal Link and returns a Zoom Personal Meeting ID')
    parser.add_argument('-u', type=str, help='Zoom Personal Link URL')
    parser.add_argument('-a', type=str, help='Alias portion of a user\'s Zoom Personal Link (https://factset.zoom.us/my/[ALIAS])')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    
    if(args.u):
        url = args.u
    elif(args.a):
        url = 'https://factset.zoom.us/my/' + args.a
    else:
        sys.exit('Error: Must specify a Zoom Personal Link URL or Alias to fetch an ID for')

    r = requests.get(url)
    #print(r.url)
    if '404' in r.text:
        sys.exit('Error: Zoom Personal Link URL or Alias does not exist')
    
    url_arr = r.url.split('/')
    print url_arr[-1]
