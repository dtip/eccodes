# Copyright 2005-2015 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.


#
# Python implementation: bufr_read_header
#
# Description: how to read the header from BUFR messages.
#
#

import traceback
import sys

from eccodes import *

INPUT='../../data/bufr/tropical_cyclone.bufr'
VERBOSE=1 # verbose error reporting

def example():

    # open bufr file
    f = open(INPUT)

    # define the keys to be printed
    keys = [
        'dataCategory',
        'dataSubCategory',
        'typicalDate',
        'bufrHeaderCentre',
        'bufrHeaderSubCentre',
        'masterTablesVersionNumber',
        'localTablesVersionNumber',
        'numberOfSubsets',
        ]

    cnt=0

    # loop for the messages in the file
    while 1:
        # get handle for message
        gid = codes_bufr_new_from_file(f)
        if gid is None: break

        print "message: %s" % cnt

        # print the values for the selected keys from the message
        for key in keys:
            try:
                print '  %s: %s' % (key,codes_get(gid,key))
            except CodesInternalError,err:
                print 'Error with key="%s" : %s' % (key,err.msg)       
            
        cnt+=1

        # delete handle
        codes_release(gid)

    # close the file
    f.close()

def main():
    try:
        example()
    except CodesInternalError,err:
        if VERBOSE:
            traceback.print_exc(file=sys.stderr)
        else:
            print >>sys.stderr,err.msg

        return 1

if __name__ == "__main__":
    sys.exit(main())
