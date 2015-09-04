#!/usr/bin/env python

"""
Reimplementation of the bconsole program in python.
"""

from   bareos.bsock.bsock import BSock
from   pprint import pformat, pprint
import json

class BSockJson(BSock):
    """
    use to send and receive the response from director
    """

    def __init__(self,
                 address="localhost",
                 port=9101,
                 dirname=None,
                 clientname="*UserAgent*",
                 password=None):
        super(BSockJson, self).__init__(
            address, port, dirname, clientname,
            password)
        self.call(".api 2")


    def call(self, command):
        json = self.call_fullresult(command)
        #self.logger.debug( pformat(json) )
        return json['result']


    def call_fullresult(self, command):
        resultstring = super(BSockJson, self).call(command)
        data = None
        if resultstring:
            try:
                data = json.loads(resultstring)
            except ValueError as e:
                # in case result is not valid json,
                # create a JSON-RPC wrapper
                data = json.dumps( {
                    'error': {
                        'code': 2,
                        'message': str(e),
                        'data': resultstring
                    },
                } )
        return data


    def interactive(self):
        """
        Enter the interactive mode.
        """
        self._set_state_director_prompt()
        command = ""
        while command != "exit" and command != "quit":
            command = raw_input(">>")
            if command:
                pprint(self.call(command))
        return True
