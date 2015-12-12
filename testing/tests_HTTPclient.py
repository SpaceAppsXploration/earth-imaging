"""
This is a test suite meant to be run from a local computer, to hit
the remote server ('online') or the development server ('offline')
running locally.
"""

import unittest
import json
from utils.remote import get_curling, post_curling
from config.config import SERVICE
from config.secret import app_token

__author__ = 'Lorenzo'


class HTTPrequest(unittest.TestCase):
    def __init__(self, env=None):
        """
        Constructor is overidden to take the argument that defines the
        online or offline mode.

        Usage:
            test = HTTPrequest(env='online')
            test.runTest()

        """
        super(HTTPrequest, self).__init__()
        if env is not None and env == 'online':
            self.test_env = env
        else:
            self.test_env = 'offline'


class EndpointFetchImage(HTTPrequest):
    def test_image_fetching(self):
        """
    Test Image Fetching Endpoint: /fetchimage
    """
        import urllib
        import urllib2

        print "Running test_image_fetching"

        base_url = SERVICE + "fetchimage"  # the service to be tested is <url>/fetchimage
        tested = False

        try:
            post_data = {'token': app_token}

            request = urllib2.Request(base_url)
            request.add_data(urllib.urlencode(post_data))

            response = urllib2.urlopen(request)
            # use read() or getcode() to print the body/status of the response
            print response.getcode()
            if response.getcode() == 200:
                tested = True
                print "Client Authenticated"
        except Exception as e:
            print e

        assert tested

    @classmethod
    def runTest(cls):
        run = cls(env='offline')
        run.test_image_fetching()


if __name__ == '__main__':
    two = EndpointFetchImage()
    two.runTest()
