#!/usr/bin/env python

import sys
import webapp2

sys.path.insert(0, 'lib')


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
