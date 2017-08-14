import simplejson
import json
import sys


def put(data, filename):
    try:
        json_data = simplejson.dumps(data, indent=4, skipkeys=True, sort_keys=True)
        fd = open(filename, 'w')
        fd.write(json_data)
        fd.close()
    except:
        print('ERROR writing', filename)
        pass


def get(filename):
    return_data = {}
    try:
        fd = open(filename, 'r')
        text = fd.read()
        fd.close()
        return_data = simplejson.loads(text)
    except:
        print('COULD NOT LOAD:', filename)
    return return_data

if __name__ == '__main__':
    o = get(sys.argv[1])
    if o:
        put(o, sys.argv[1])
