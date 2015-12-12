#!/usr/bin/env python

import sys
import webapp2

from config.config import DEBUG

sys.path.insert(0, 'lib')


class FetchImage(webapp2.RequestHandler):
    def get(self):
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
    ('/fetchimage', FetchImage)
], debug=DEBUG)
