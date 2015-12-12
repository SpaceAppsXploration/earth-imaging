#!/usr/bin/env python

import sys
import webapp2

from config.config import DEBUG

sys.path.insert(0, 'lib')


class Hello(webapp2.RequestHandler):
    """Homepage"""
    def get(self):
        self.response.set_status(200)
        self.response.headers['Content-Type'] = 'text/html'
        return self.response.write("This is a <a href='http://projectchronos.eu'>Project Chronos</a>' app")


class FetchImage(webapp2.RequestHandler):
    """Handler to manage the app's image fetching functionalities."""
    def get(self):
        self.response.set_status(403)
        return self.response.write("403")

    def post(self):
        from config.secret import app_token

        if self.request.get('token') != app_token:
            # request not authenticated
            self.response.set_status(403)
            self.response.write('Not Authenticated')
        else:
            # request authenticated
            self.response.set_status(200)
            self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/fetchimage', FetchImage),
    ('/', Hello)
], debug=DEBUG)
