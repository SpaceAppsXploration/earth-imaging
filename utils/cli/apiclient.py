"""
Client to third parties' APIs
"""

import urllib
import urllib2

from config.secret import app_token

__author__ = 'Lorenzo'


class Stork(object):
    """
    This is the client for the Planet Labs API.

    APIs allowed:
    * Scenes
    * Mosaics
    * ...

    Usage:
        ...

    Scenes API interface:
        {
          "landsat": "https://api.planet.com/v0/scenes/landsat/",
          "ortho": "https://api.planet.com/v0/scenes/ortho/",
          "rapideye": "https://api.planet.com/v0/scenes/rapideye/"
        }
    """

    def __new__(cls, api):
        cls.endpoint = 'https://api.planet.com/v0/{}/'
        cls.allowed_apis = ('scenes', 'mosaics',)
        cls.providers = ('ortho', 'landsat', 'rapideye')

    def __init__(self, api):
        if api in self.allowed_apis:
            self.api = api
            self.base_url = self.endpoint.format(api)

    def find_scenes_by_area(self, lat, long):
        """
        Fetch image by coordinates. Using Area of Interest (AoI).

        Determine what geometry (polygon, point, line, multipolygon, etc.) you
        would like the returned images to intersect. This geometry can be
        expressed as Well Known Text or GeoJSON with (longitude, latitude) pairs.
        Using the `intersect` parameter in the request.

        :param lat:
        :param long:
        :return:
        """
        pass

    def fetch_ids(self, limit):
        """
        Fetch the list of the scenes' ids.

        Once retrieved a sequence of ids from the API or from the cache:
        `GET /v0/scenes/{scene_type}/{scene_id}` can be used

        :param limit:
        :return:
        """

        pass

    def load_planet_scene(self, provider=None, post_data=None):
        """
        Order the app to fetch a scene from the API.

        :param provider:
        :param post_data:
        :return:
        """

        if not provider or provider not in self.providers:
            # check if provider is right, default is `ortho`
            provider = 'ortho'

        request = urllib2.Request("".join((self.base_url, provider)))

        if isinstance(post_data, dict) and post_data:
            # a dictionary is passed for form-data, request is a POST
            post_data['token'] = app_token
            request.add_data(urllib.urlencode(post_data))

        response = urllib2.urlopen(request)
        # use read() or getcode() to print the body/status of the response
        print response.getcode()
        if response.getcode() == 200:
            print request.__dict__
            print "Client Authenticated"
