"""
Tools for remote interaction with the servers
"""

__author__ = 'lorenzo'

import sys
sys.path.insert(0, '../..')


def post_curling(url, params, file=None, display=False):
    """
    POST to a remote url and print the response in a file or on screen or return the body of the response
    :param url: target url
    :param params: parameters in the request
    :param file: path and name of the output file
    :param display: true if you want to print output on console/command line
    :return: file > None, body of the response
    """
    import pycurl
    from urllib import urlencode
    from StringIO import StringIO

    c = pycurl.Curl()
    c.setopt(c.URL, url)
    # if request is GET
    #if params: c.setopt(c.URL, url + '?' + urlencode(params))

    # if request is POST
    post_data = params
    # Form data must be provided already urlencoded.
    postfields = urlencode(post_data)
    # Sets request method to POST,
    # Content-Type header to application/x-www-form-urlencoded
    # and data to send in request body.
    c.setopt(c.POSTFIELDS, postfields)

    if file and not display:
        # if a path is specified, it prints on file
        c.setopt(c.WRITEDATA, file)
        c.perform()
        c.close()
        return None
    if display:
        # if display flag is on, print in the server debug stream
        storage = StringIO()
        c.setopt(c.WRITEFUNCTION, storage.write)
        c.perform()
        c.close()
        print storage.getvalue()
        return None

    # else it returns a string
    storage = StringIO()
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    c.close()
    return storage.getvalue()


def get_curling(url, params=None, display=False):
    """
    GET from a remote URL

    :param url:
    :param params:
    :param display:
    :return:
    """
    if params is None:
        params = dict()

    import pycurl
    import urllib
    from StringIO import StringIO

    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    if params:
        c.setopt(c.URL, url + '?' + urllib.urlencode(params))
    else:
        c.setopt(c.URL, url)

    if display:
        # if display flag is on, print in the server debug stream
        storage = StringIO()
        c.setopt(c.WRITEFUNCTION, storage.write)
        c.perform()
        c.close()
        print storage.getvalue()
        return storage.getvalue()

    print "pyCURLing url:" + str(c.getinfo(pycurl.EFFECTIVE_URL))
    # For older PycURL versions:
    #c.setopt(c.WRITEFUNCTION, buffer.write)
    c.perform()
    c.close()

    body = buffer.getvalue()
    # Body is a string in some encoding.
    # In Python 2, we can print it without knowing what the encoding is.
    return body


def google_urlfetch(url, params=None):
    """
    GET to a remote url (meant to be used inside sandboxed environment)
    :param url:
    :param params:
    :return:
    """
    if params is None:
        params = dict()

    import urllib

    from google.appengine.api import urlfetch

    data = urllib.urlencode(params)
    url = url + '?' + data
    result = urlfetch.fetch(url=url, deadline=300)

    if result.status_code == 200:
        return result.content
    else:
        raise Exception('Cannot urlfetch resource: status ' + str(result.status_code))
