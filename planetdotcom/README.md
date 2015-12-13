# Scenes API
## Scene Types

A “scene” refers to a single image as taken by a satellite. The Scenes API offers REST API access to listing, searching, and downloading available scene images and their associated metadata. There are three scene types available through the API:

    The API for Planet’s Dove satellites uses scene type ortho, and more specific docs can be found here.
    The RapidEye Scenes API uses scene type rapideye, and more specific docs can be found here.
    The Landsat Scenes API uses scene type landsat, and more specific docs can be found here.

The Planet Scenes API offers REST API access to listing, searching, and downloading available scenes and their associated metadata.
Metadata Properties

    Example of a metadata dictionary response for the ortho type

```
{
  "acquired": "2015-03-06T02:24:15.531315+00:00",
  "camera": {
    "bit_depth": 12,
    "color_mode": "RGB",
    "exposure_time": 1170,
    "gain": 300,
    "tdi_pulses": 12
  },
  "cloud_cover": {
    "estimated": 2.54
  },
  "data": {
    "products": {
      "analytic": {
        "full": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/full?product=analytic"
      },
      "visual": {
        "full": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/full?product=visual"
      }
    }
  },
  "image_statistics": {
    "gsd": 4.21102057224,
    "image_quality": "standard",
    "snr": 101.70912559458553
  },
  "links": {
    "full": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/full",
    "self": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908",
    "square_thumbnail": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/square-thumb",
    "thumbnail": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/thumb"
  },
  "published": "2015-03-15T22:40:13.111413+00:00",
  "sat": {
    "alt": 616.276611532,
    "id": "0908",
    "lat": 43.9489913571,
    "lng": 118.244180673,
    "off_nadir": 0.84527087801144
  },
  "strip_id": 1425608509.962405,
  "sun": {
    "altitude": 33.981625460539135,
    "azimuth": 145.0357748740408,
    "local_time_of_day": 10.287112044866667
  }
}
```

Each scene has associated metadata tha records properties about the scene, such as the geographic location recorded in the image and when it was taken. The metadata changes slightly depending on which scene type is being accessed.
Products

Each scene is distributed as a few different products over the API, with the exact products available being dependant on the scene’s type. For example, both visual and analytic products can be downloaded for PlanetScope and RapidEye scenes, but only PlanetScope scenes may be downloaded as unrectified images. These vary based on the scene type.

We know that the scene has visual and analytic products available based on the keys within the data.products content of the scene response.
Note

A user’s permissions may constrain their access to a subset of the available data products listed below.
Products by Scene Type
* Landsat

    band_n where n is 1-11 inclusive. E.g. band_1 through band_11.

* Ortho

    analytic
    unrectified
    visual

* RapidEye

    analytic
    visual

## API Endpoints

The following API endpoints are shared between all three scene types.
List all scene types

    The HTTP endpoint returns JSON structured like this:
```
{
  "landsat": "https://api.planet.com/v0/scenes/landsat/",
  "ortho": "https://api.planet.com/v0/scenes/ortho/",
  "rapideye": "https://api.planet.com/v0/scenes/rapideye/"
}
```
This endpoint retrieves all available scene types, and returns a dictionary from name to scene type endpoint.
HTTP Request

`GET /v0/scenes/`
### Query Parameters

None
Response Format

Dictionary with scene types as keys, and url links as values.
Get scene list

    The HTTP endpoint returns JSON structured like this:
```
{
  "count": 248485,
  "links": {
    "next":  "https://api.planet.com/v0/scenes/ortho/?next_options",
    "prev": "https://api.planet.com/v0/scenes/ortho/?prev_options",
    "self":  "https://api.planet.com/v0/scenes/ortho/?self_options",
    "first":  "https://api.planet.com/v0/scenes/ortho/?first_options"
  },
  "type": "FeatureCollection",
  "features": [{
    "geometry": {
      "coordinates": [
        [
          [
            118.2596173268622,
            43.90046678196599
          ],
          [
            118.23024375959055,
            44.001012079878194
          ],
          [
            118.02130239437746,
            43.96907020632453
          ],
          [
            118.05104753524252,
            43.86856360597364
          ],
          [
            118.2596173268622,
            43.90046678196599
          ]
        ]
      ],
      "type": "Polygon"
    },
    "id": "20150306_022415_0908",
    "properties": {
      "acquired": "2015-03-06T02:24:15.531315+00:00",
      "camera": {
        "bit_depth": 12,
        "color_mode": "RGB",
        "exposure_time": 1170,
        "gain": 300,
        "tdi_pulses": 12
      },
      "cloud_cover": {
        "estimated": 2.54
      },
      "data": {
        "products": {
          "analytic": {
            "full": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/full?product=analytic"
          },
          "visual": {
            "full": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/full?product=visual"
          }
        }
      },
      "image_statistics": {
        "gsd": 4.21102057224,
        "image_quality": "standard",
        "snr": 101.70912559458553
      },
      "links": {
        "full": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/full",
        "self": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908",
        "square_thumbnail": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/square-thumb",
        "thumbnail": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/thumb"
      },
      "published": "2015-03-15T22:40:13.111413+00:00",
      "sat": {
        "alt": 616.276611532,
        "id": "0908",
        "lat": 43.9489913571,
        "lng": 118.244180673,
        "off_nadir": 0.84527087801144
      },
      "strip_id": 1425608509.962405,
      "sun": {
        "altitude": 33.981625460539135,
        "azimuth": 145.0357748740408,
        "local_time_of_day": 10.287112044866667
      }
    },
    "type": "Feature"
  }, {"more": "scenes"}]
}
```

This endpoint returns a paginated list of scenes that match the query filter parameters. Each response is valid GeoJSON, and includes links to the next and previous pages under response.links.prev and response.links.next. POST may be used in place of GET for large intersects query payloads. Read more about pagination here.
HTTP Request

`GET /v0/scenes/{scene_type}`

`POST /v0/scenes/{scene_type}`
Query Parameters

intersects and all metadata comparator queries are and'ed together to filter the scenes returned.

Parameter 	Type 	Default 	Description
order_by 	One of ‘acquired asc’, ‘acquired desc’ 	acquired desc 	Which date to order by, and ordering direction
count 	Integer 	50 	The number of results to return per call. Maximum of 1000.
intersects 	WKT or GeoJSON 	None 	Part of the scene must intersect with this shape (tutorial here)
[metadata name].[comparator] 	Varying 	None 	Filtering by available metadata fields
Response Format
Field 	Type 	Description
links 	dictionary 	Links to the more results in the paginated API
links.next 	string url 	Link to next results, if there may be more
links.prev 	string url 	Link to previous results, if there may be more
links.self 	string url 	Link to this page
links.first 	string url 	Link to the first page of results
type 	string 	Always “FeatureCollection” to be valid GeoJSON
features 	list / array 	List of scenes returned — at most count from the query parameters. Additional results are available at links.next and links.prev
features[index] 	dictionary 	Data describing a particular scene, as described here
count 	integer 	Number of results on this and subsequent next (not previous) pages
Relevant Tutorials (see below)

    Get All Scenes
    Get Most Recently Acquired scenes
    Get Recently Published scenes
    Get Scenes by AOI
    Get Scenes by Time Range

### Fetch information for a given scene

    The HTTP endpoint returns JSON structured like this:
```
{
  "geometry": {
    "coordinates": [
      [
        [
          118.2596173268622,
          43.90046678196599
        ],
        [
          118.23024375959055,
          44.001012079878194
        ],
        [
          118.02130239437746,
          43.96907020632453
        ],
        [
          118.05104753524252,
          43.86856360597364
        ],
        [
          118.2596173268622,
          43.90046678196599
        ]
      ]
    ],
    "type": "Polygon"
  },
  "id": "20150306_022415_0908",
  "properties": {
    "acquired": "2015-03-06T02:24:15.531315+00:00",
    "camera": {
      "bit_depth": 12,
      "color_mode": "RGB",
      "exposure_time": 1170,
      "gain": 300,
      "tdi_pulses": 12
    },
    "cloud_cover": {
      "estimated": 2.54
    },
    "data": {
      "products": {
        "analytic": {
          "full": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/full?product=analytic"
        },
        "visual": {
          "full": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/full?product=visual"
        }
      }
    },
    "image_statistics": {
      "gsd": 4.21102057224,
      "image_quality": "standard",
      "snr": 101.70912559458553
    },
    "links": {
      "full": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/full",
      "self": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908",
      "square_thumbnail": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/square-thumb",
      "thumbnail": "https://api.planet.com/v0/scenes/ortho/20150306_022415_0908/thumb"
    },
    "published": "2015-03-15T22:40:13.111413+00:00",
    "sat": {
      "alt": 616.276611532,
      "id": "0908",
      "lat": 43.9489913571,
      "lng": 118.244180673,
      "off_nadir": 0.84527087801144
    },
    "strip_id": 1425608509.962405,
    "sun": {
      "altitude": 33.981625460539135,
      "azimuth": 145.0357748740408,
      "local_time_of_day": 10.287112044866667
    }
  },
  "type": "Feature"
}
```

### Returns information about a scene, given its type and id.
HTTP Request

`GET /v0/scenes/{scene_type}/{scene_id}`
Query Parameters

None
Response Format
Field 	Type 	Description
geometry 	dictionary 	GeoJSON describing the polygon that the scene covers. Includes 5 longitude, latitude pairs, with the first being a repeat of the last. If the scene overlaps the antimeridian, a MultiPolygon will be returned.
type 	string 	Always “Feature” to be valid GeoJSON
id 	string 	A unique identifier for this scene
properties 	dictionary 	A dictionary of metadata about this scene
properties.data 	dictionary 	Links and information about different available data download options
properties.data.products 	dictionary 	Product names keyed to dictionaries of related links
properties.data.products.[product] 	dictionary 	A dictionary of links specific to the given product
properties.data.products.[product].full 	string 	Link to the full scene download for the specified product
properties.links 	dictionary 	A dictionary of links related to this scene
properties.links.full 	string 	Link to download scene GeoTIFF
properties.links.self 	string 	Link to scene information
properties.links.thumbnail 	string 	Link to image thumbnail
Fetch GeoTIFF for scene

    Example gdalinfo response
```
Driver: GTiff/GeoTIFF
Files: 20140922_174539_planet_ortho_51.55N_118.14E.tif
Size is 4832, 4229
Coordinate System is:
PROJCS["WGS 84 / UTM zone 11N",
    GEOGCS["WGS 84",
        DATUM["WGS_1984",
            SPHEROID["WGS 84",6378137,298.257223563,
                AUTHORITY["EPSG","7030"]],
            AUTHORITY["EPSG","6326"]],
        PRIMEM["Greenwich",0],
        UNIT["degree",0.0174532925199433],
        AUTHORITY["EPSG","4326"]],
    PROJECTION["Transverse_Mercator"],
    PARAMETER["latitude_of_origin",0],
    PARAMETER["central_meridian",-117],
    PARAMETER["scale_factor",0.9996],
    PARAMETER["false_easting",500000],
    PARAMETER["false_northing",0],
    UNIT["metre",1,
        AUTHORITY["EPSG","9001"]],
    AUTHORITY["EPSG","32611"]]
Origin = (413595.599999999976717,5718319.799999999813735)
Pixel Size = (2.999813741721861,-3.000283755024872)
Metadata:
  AREA_OR_POINT=Area
Image Structure Metadata:
  COMPRESSION=LZW
  INTERLEAVE=PIXEL
Corner Coordinates:
Upper Left  (  413595.600, 5718319.800) (118d14'52.08"W, 51d36'33.40"N)
Lower Left  (  413595.600, 5705631.600) (118d14'40.86"W, 51d29'42.78"N)
Upper Right (  428090.700, 5718319.800) (118d 2'18.64"W, 51d36'40.73"N)
Lower Right (  428090.700, 5705631.600) (118d 2' 9.30"W, 51d29'50.08"N)
Center      (  420843.150, 5711975.700) (118d 8'30.22"W, 51d33'11.92"N)
Band 1 Block=4832x1 Type=Byte, ColorInterp=Red
  Mask Flags: PER_DATASET ALPHA
Band 2 Block=4832x1 Type=Byte, ColorInterp=Green
  Mask Flags: PER_DATASET ALPHA
Band 3 Block=4832x1 Type=Byte, ColorInterp=Blue
  Mask Flags: PER_DATASET ALPHA
Band 4 Block=4832x1 Type=Byte, ColorInterp=Alpha
```

Returns the GeoTIFF of the requested scene.
HTTP Request

`GET /v0/scenes/{scene_type}/{scene_id}/full`

Query Parameters
Parameter 	Type 	Default 	Description
product 	A valid product name for the given scene type. 	visual 	Name of product type to download
Response Format

Attached GeoTIFF. Data is projected in Universal Transverse Mercator (UTM), and uses WGS 84. Other format details depend on product type.
Tutorials

    Download Images.

Fetch thumbnail for scene

Returns downsampled thumbnail of the scene for previewing. Rectified products' thumbs will be shown rotated so that north is up.
Example

Thumbnail Example
HTTP Request

`GET /v0/scenes/{scene_type}/{scene_id}/thumb`
Query Parameters
Parameter 	Type 	Default 	Description
size 	One of ‘sm’, ‘md’, ‘lg’ 	md 	Named size of thumbnail
format 	One of ‘png’, ‘jpg’, ‘jpeg’ 	png 	Image format for thumbnail
Sizes
Size 	Width
sm 	64px
md 	128px
lg 	640px
Response Format

Attached image of format specified.

# Get Scenes by Area of Interest (Scenes V0 API Tutorial)

First, determine what geometry (polygon, point, line, multipolygon, etc.) you would like the returned images to intersect. This geometry can be expressed as Well Known Text or GeoJSON with (longitude, latitude) pairs.

Then, request the scenes in that area using the intersects parameter.

Then, use links.next to get additional scenes in the time range. When no more scenes are returned, you’ve retrieved all the new scenes in the time range.

```
import requests

url = "https://api.planet.com/v0/scenes/ortho/"
key = "YOUR-KEY-HERE"

# (longitude, latitude)
sf_nw = (-122.545373, 37.815798)
sf_se = (-122.340066, 37.709403)
sf_ne = (sf_se[0], sf_nw[1])
sf_sw = (sf_nw[0], sf_se[1])

# Using WKT

from shapely.geometry import Polygon
from shapely.wkt import dumps as wkt_dumps

poly = Polygon([sf_nw, sf_ne, sf_se, sf_sw, sf_nw])
intersects = wkt_dumps(poly)

# Or, using GeoJSON

import geojson

poly = geojson.Polygon([[sf_nw, sf_ne, sf_se, sf_sw, sf_nw]])
intersects = geojson.dumps(poly)

# Back to shared code between WKT and GeoJSON

params = {
    "intersects": intersects,
}

data = requests.get(url, params=params, auth=(key, ''))

scenes_data = data.json()["features"]

# do something with scenes_data
```


# Python Stack Finder Example

Given a GeoJSON file that defines an area of interest (AOI), find the locations where there are multiple overlapping Planet scenes – called a stack. This script finds the stacks, downloads each of the scenes in one of the stacks, finds the largest area rectangle that sits within all of the scenes, and crops each scene to this rectangle.

The output is a set of rectangular images of the same location at different points in time. These stacks might be of use to visually inspect for change over time or to design algorithms that automatically analyze time series of satellite images.

In this tutorial, we will initially introduce the functions and then invoke them, inspecting the results.
Imports

import argparse
import copy
import json
import os
import subprocess

# Planet Libraries
from planet import api
from stackfinder import findstacks
from maxrect import get_intersection, get_maximal_rectangle, rect2poly

Import the required libraries. Notice that we are going to use three different Planet libraries for this task. The required Planet libraries include planet, stackfinder, and maxrect.

In addition, to crop the inscribed rectangle from the GeoTIFFs, we will be using GDAL’s command line utility.
Initialize Planet Client

def init_client():
    '''Initialize planet client using api key'''
    KEY = os.getenv("PL_API_KEY")
    return api.Client(KEY)

Using the Planet library, init_client initializes a client that allows simple access to the API.
Find the Scenes that Fit an AOI

def get_metadata(client, geojson, verbose=True):
    '''find the metadata for scenes within the GeoJSON geometry'''
    aoi = json.dumps(geojson)
    r = client.get_scenes_list(intersects=aoi)

    if verbose:
        print("Found %i scenes" % r.get()['count'])

    scenes_md = []
    for s in r.iter():
        scenes_md.extend(s.get()['features'])

    return scenes_md

The get_metadata function returns a list of metadata for scenes that overlap the AOI defined in a GeoJSON file.
Download Scenes

def download_scenes_in_list(client, dest_dir, _stack):
    '''Download scenes in stack to the destination directory'''
    stack = copy.deepcopy(_stack)

    scene_ids = [i['id'] for i in stack]
    results = client.fetch_scene_geotiffs(
        scene_ids, callback=api.write_to_file(dest_dir))
    response = map(lambda r: r.await(), results)
    fnames = [r.name for r in response]

    for indx in range(len(stack)):
        stack[indx]['local_gtiff'] = os.path.join(dest_dir, fnames[indx])

    return stack

download_scenes_in_list uses the client to download the GeoTIFF version of scenes.
Finding the Stacks

def get_stacks(scenes_md):
    '''Find the stacks of imagery from a set of scenes
    '''
    return findstacks(scenes_md)

Using findstacks get a list of stacks and the centers of those stacks.
Finding the Maximal Inscribed Rectangle

def max_inscribed_rectangle(stack, rect_fname="inscr_rect.geojson"):
    '''Calculate the maximal area, axis-aligned rectangle
    that fits within all of the scenes in the stack
    ''' 
    def save_geojson(geojson, out_fname):
        '''save GeoJSON format dictionary to output filename'''
        with open(out_fname, 'w') as outfile:
            json.dump(geojson, outfile)
        return out_fname

    coords = [i['geometry']['coordinates'][0] for i in stack]
    inter_gj, inter_coords = get_intersection(coords)

    # get the top left and bottom right corners of the inscribed rectangle,
    # and turn that into a geojson polygon for cropping use
    rect_corners = get_maximal_rectangle(inter_coords)
    rect_poly = rect2poly(*rect_corners)
    rect_gj = {'type': "Feature",
               "geometry": {"type": "Polygon",
                            "coordinates": [rect_poly]}}

    return rect_gj, save_geojson(rect_gj, rect_fname)

max_inscribed_rectangle finds the maximal area rectangle that is inscribed in a set of scenes.

First we find the intersection polygon from all of the geometries, and use this polygon to define the bounds of a maximal area inscribed rectangle.

Lastly – for easy compatitibility with gdal’s command line utility – the function dumps the rectangle geometry to disk.
Cropping Geotiff to Polygon

def crop_to_rectangle(stack, rect_gj_fname):
    '''Use gdalwarp to crop scenes in a stack to a rectangle. The 
    function assumes that the input filenames of each scene
    in the stack have a 3 letter extension like .tif.
    '''
    cropped_fnames = []
    for scene in stack:
        crop_fname = scene['local_gtiff'][:-4]+"_crop.tif"
        cmd = ['gdalwarp -of GTiff -crop_to_cutline -cutline',
                rect_gj_fname, scene['local_gtiff'], crop_fname]
        subprocess.call(cmd, shell=True)
        cropped_fnames.append(crop_fname)
    return cropped_fnames

Use gdalwarp to crop the scene to the rectangular shape, saving the output to disk and returning the filenames of the output files.

Note that the vignetting mask has not been removed from the images, so the cropline might have no-data regions.
Putting it Together

    $ export PL_API_KEY=[[your_api_key]]

if __name__ == "__main__"
    parser = argparse.ArgumentParser(description='Crop stacks from planet imagery.')
    parser.add_argument('-geom', action="store",
                         help='filename of GeoJSON describing AOI',
                         required=True)
    parser.add_argument('-dest', action="store",
                         help='directory in which to store output data',
                         required=True)
    args = parser.parse_args()


    geojson_fname = args.geom
    dest_dir = args.dest

    geojson = json.load(open(geojson_fname))

    client = init_client()

    scenes_md = get_metadata(client, geojson)

    stacks, stack_centers = get_stacks(scenes_md)

    rect_gj, rect_gj_fname = max_inscribed_rectangle(stacks[0])

    stack = download_scenes_in_list(client, dest_dir, stacks[0])

    cropped_images = crop_to_rectangle(stack, rect_gj_fname)


# Examples

### Get All Scenes (Scenes V0 API Tutorial)

import requests
import urllib
from datetime import datetime
from datetime import timedelta
import pytz

filters = {
    # Your filters here, for example:
    # Get images taken in the last 3 days
    "acquired.gte": (datetime.now(pytz.utc) - timedelta(days=3)).isoformat(),
}

next_url = "https://api.planet.com/v0/scenes/ortho/?" \
    + urllib.urlencode(filters)

key = "YOUR-KEY-HERE"

while next_url:
    # Note: you don't have to pass the filters in again
    # here, they will always be included in data.links.next
    r = requests.get(next_url, auth=(key, ''))
    r.raise_for_status()
    data = r.json()
    scenes_data = data["features"]
    # do something with scenes_data
    next_url = data["links"].get("next", None)
    
    
### Get Most Recently Acquired Scenes (Scenes V0 API Tutorial)

```
import requests

url = "https://api.planet.com/v0/scenes/ortho/"
key = "YOUR-KEY-HERE"

params = {
    'order_by': 'acquired desc'
}

data = requests.get(url, params=params, auth=(key, ''))

# do something with data.json()
```

### Get Recently Published Scenes (Scenes V0 API Tutorial)

```
from datetime import datetime, timedelta
import requests
from pytz import UTC
from urllib import urlencode


url = "https://api.planet.com/v0/scenes/ortho/"
key = "YOUR-KEY-HERE"

yesterday = datetime.now(UTC) - timedelta(days=1)

params = {
    'published.gte': yesterday.isoformat()
    # Add any other query filters you want here
}

next_url = url + '?' + urlencode(params)

while next_url:
    r = requests.get(next_url, auth=(key, ''))
    r.raise_for_status()
    data = r.json()
    scenes_data = data["features"]

    # Do something with scenes_data. Example:
    for s in scenes_data:
        print s["id"]

    next_url = data["links"].get("next", None)
```


### Get Scenes by Area of Interest (Scenes V0 API Tutorial)

```
import requests

url = "https://api.planet.com/v0/scenes/ortho/"
key = "YOUR-KEY-HERE"

# (longitude, latitude)
sf_nw = (-122.545373, 37.815798)
sf_se = (-122.340066, 37.709403)
sf_ne = (sf_se[0], sf_nw[1])
sf_sw = (sf_nw[0], sf_se[1])

# Using WKT

from shapely.geometry import Polygon
from shapely.wkt import dumps as wkt_dumps

poly = Polygon([sf_nw, sf_ne, sf_se, sf_sw, sf_nw])
intersects = wkt_dumps(poly)

# Or, using GeoJSON

import geojson

poly = geojson.Polygon([[sf_nw, sf_ne, sf_se, sf_sw, sf_nw]])
intersects = geojson.dumps(poly)

# Back to shared code between WKT and GeoJSON

params = {
    "intersects": intersects,
}

data = requests.get(url, params=params, auth=(key, ''))

scenes_data = data.json()["features"]

# do something with scenes_data
```

First, determine what geometry (polygon, point, line, multipolygon, etc.) you would like the returned images to intersect. This geometry can be expressed as Well Known Text or GeoJSON with (longitude, latitude) pairs.

Then, request the scenes in that area using the intersects parameter.

Then, use links.next to get additional scenes in the time range. When no more scenes are returned, you’ve retrieved all the new scenes in the time range.

### Download Thumbnails and Full Images (Scenes V0 API Tutorial)

    General method to download a file from a URL

If you’re using Python requests, you must use version 2.3.0 or later.
```
import requests

def download_image(url, key):
    r = requests.get(url, stream=True, auth=(key, ''))
    if 'content-disposition' in r.headers:
        local_filename = r.headers['content-disposition'] \
            .split("filename=")[-1].strip("'\"")
    else:
        local_filename = '.'.join(url.split('/')[-2:])

    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()

    return local_filename

    You can then use download_image with links provided by the API. For example, here we’re downloading all of the thumbnails on the first page of results of scenes with cloud cover less than 1%.

filters = {
    # Your filters here, for example:
    # Cloud cover less than 1%
    "cloud_cover.estimated.lte": 1,
}

url = "https://api.planet.com/v0/scenes/ortho/"

key = "YOUR-KEY-HERE"

r = requests.get(url, params=filters, auth=(key, ''))
r.raise_for_status()
data = r.json()
scenes_data = data["features"]
for scene in scenes_data:
    thumb_link = scene["properties"]["links"]["thumbnail"]
    download_image(thumb_link, key)
```

Image data—thumbnails or full data—can be downloaded to your local computer or server to load into other analysis software, or be visually inspected.


### Using JS LeafLet Library

## Mosaic Tiles in Leaflet Map

In this example, we’ll create a slippy map with a Planet Labs mosaic using Leaflet.
Authentication

For all API and tile requests you will need to provide an API key for authentication. We strongly recommend creating a separate API key for each application. API keys can be created from your account page.
Requesting mosaic information
```
var API_KEY = 'YOUR-KEY-HERE';

$.ajax({
  type: 'GET',
  url: 'https://api.planet.com/v0/mosaics/color_balance_mosaic',
  //Add the authorization header
  beforeSend: function(xhr){xhr.setRequestHeader('Authorization', 'api-key '+API_KEY);},
  success: function(data) {
    //Here we will handle the result of our API call
  }
});
```
First, we’ll need to make a call to the Planet API and request information about the mosaic we want to display. This is done by calling the Mosaics endpoint. In this case we’ll use jQuery to perform the API call. As described by here we will be sending the Authorization header to access the API.
Formatting the URL
```
// First, we identify the range of subdomains
var subdomainInfo = /{(\d)-(\d)}/.exec(data.links.tiles);
var subdomains = ""
// Now we can construct a list of subdomains, which we'll pass to leaflet as an option
for (var i = parseInt(subdomainInfo[1]); i <= parseInt(subdomainInfo[2]); i++) {
  subdomains += i;
}
//And finally, we can construct the url
var tileUrl = data.links.tiles.replace(subdomainInfo[0], '{s}')  + '?api_key=' + API_KEY;
```
The Mosaics endpoint provides a description of the JSON object returned by the api. Here we are interested in the “links” section, and specifically in the link to the mosaic tiles. We will use that to create our Leaflet map.

We will need to slightly modify the URL that is returned by the mosaic endpoint to fit in the Leaflet url scheme for map tiles. The mosaics endpoint return URLs in a format which describes the different available hostname aliases that can be used to increase the number of parallel tile requests.

A typical url would be something like this:
```
https://tiles{0-3}.planet.com/v0/mosaics/color_balance_mosaic/{z}/{x}/{y}.png
```
This means that there are 4 different hostnames available (tiles0, tiles1, tiles2, and tiles3) that can be used by the library to request map tiles. In Leaflet, however, this is specified a little differently, so we need to reformat the URL accordingly.
Instantiating the Leaflet Map
```
var map = L.map('map').setView([0, 0], 2);

L.tileLayer(tileUrl, {
  subdomains: subdomains,
  attribution: 'Imagery &copy; <a href="https://planet.com">Planet Labs</a>',
  maxZoom: 18
}).addTo(map);
```
Now that we have our reformatted URL and the list of available subdomains, we can instantiate the leaflet map
Putting it all together
```
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.css" />
    <style>
    body, html {
      width: '100%';
      height: '100%';
      margin: 0;
      padding: 0;
    }
    #map {
      height: 600px;
      width: '100%';
    }
    .leaflet-container {
        background-color:rgba(255,0,0,0.0);
    }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.js"></script>
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script>
      var API_KEY = 'YOUR-KEY-HERE';

      $.ajax({
        type: 'GET',
        url: 'https://api.planet.com/v0/mosaics/color_balance_mosaic',
        beforeSend: function(xhr){xhr.setRequestHeader('Authorization', 'api-key '+API_KEY);},
        success: function(data) {

          var subdomainInfo = /{(\d)-(\d)}/.exec(data.links.tiles);
          var subdomains = ""
          for (var i = parseInt(subdomainInfo[1]); i <= parseInt(subdomainInfo[2]); i++) {
            subdomains += i;
          }
          var tileUrl = data.links.tiles.replace(subdomainInfo[0], '{s}')  + '?api_key=' + API_KEY;

          var map = L.map('map').setView([0, 0], 2);

          L.tileLayer(tileUrl, {
            subdomains: subdomains,
            attribution: 'Imagery &copy; <a href="https://planet.com">Planet Labs</a>',
            maxZoom: 18
          }).addTo(map);
        }
      });
    </script>
  </body>
</html>
```
## Scene Tiles in a Leaflet Map

In this example, we’ll create a slippy map with an Open Street Map (OSM) base layer, on top of which we’ll overlay a tiled layer with a single Planet Labs scene.
Authentication

For all API and tile requests you will need to provide an API key for authentication. We strongly recommend creating a separate API key for each application. API keys can be created from your account page.
Requesting scene information
```
var API_KEY = 'YOUR-KEY-HERE';
var SCENE_ID = '20150907_203535_0b0f';

$.ajax({
    url: 'https://api.planet.com/v0/scenes/ortho/' + SCENE_ID,
    type: 'GET',
    beforeSend: function(xhr){xhr.setRequestHeader('Authorization', 'api-key ' + API_KEY);},
    success: function(data) {
    //Here we will handle the result of our API call
  }
});
```
First, we’ll need to make a call to the Planet API and request information about the scene we want to display. This is done by calling the Scenes endpoint. In this case we’ll use jQuery to perform the API call. As described here we will be sending the Authorization header to access the API.
Parsing the scene object
```
var geometry = data.geometry.coordinates[0];

var coords = data.geometry.coordinates[0].map(function(coord) {
  return [coord[1], coord[0]];
});

var bounds = L.latLngBounds(coords);
var center = bounds.getCenter();
```
The scene object returned from the API is a valid GeoJSON feature. We need to find the center and bounds for the feature. To do this, we can use L.latLngBounds (docs).

There is a catch though: the GeoJSON spec details that each position array should be in X,Y,Z order (easting / northing / altitude) which means that it is in the [lng, lat] format, while Leaflet works in ISO 6709 which means it expects coordinates to be in [lat, lng] format.

Therefore, we need to flip all coordinates in the geometry array before we pass it to L.latLngBounds.
Creating the map
```
var map = L.map('map', {minZoom: 10, maxZoom: 14}).setView(center, 12);

//Add a base layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

//Add a scene layer
L.tileLayer('https://tiles.planet.com/v0/scenes/ortho/' +
                data.id + '/{z}/{x}/{y}.png?api_key=' +
                API_KEY, {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    bounds: bounds
}).addTo(map);
```
Now that we can create the map. We will add two layers, an OSM base layer and a layer containing the scene we are interested in.

We will set the map’s center to the center of the scene, and constrain the zoom range to a reasonable range for a single image.

Note that when instantiating the scene layer, we add a bounds option to the tile source set to the bounds of the scene. This ensures that only tiles within those bounds are loaded for that layer, avoiding the overhead of requesting a large number of surrounding tiles - which would be empty.
Putting it all together
```
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ol3/3.8.2/ol.min.css" />
    <style>
    body, html {
      width: '100%';
      height: '100%';
      margin: 0;
      padding: 0;
    }
    #map {
      height: '100%';
      width: '100%';
    }
    </style>
  </head>
<body>
    <div id="map"></div>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.js"></script>
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script>
      var API_KEY = 'YOUR-API-KEY';
      var SCENE_ID = '20150910_192050_0b0f';

      //Get scene data
      $.ajax({
        url: 'https://api.planet.com/v0/scenes/ortho/' + SCENE_ID,
        type: 'GET',
        beforeSend: function(xhr){xhr.setRequestHeader('Authorization', 'api-key ' + API_KEY);},
        success: function(data) {

          //Understand the scene's bounds
          var geometry = data.geometry.coordinates[0];

          var coords = data.geometry.coordinates[0].map(function(coord) {
            return [coord[1], coord[0]];
          });

          var bounds = L.latLngBounds(coords);
          var center = bounds.getCenter();
          // Create the map, centered on the scene
          var map = L.map('map', {minZoom: 10, maxZoom: 14}).setView(center, 12);

          //Add a base layer
          L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
              attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          }).addTo(map);

          //Add a scene layer
          L.tileLayer('https://tiles.planet.com/v0/scenes/ortho/' +
                          data.id + '/{z}/{x}/{y}.png?api_key=' +
                          API_KEY, {
              attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
              bounds: bounds
          }).addTo(map);
        }
      })
    </script>
  </body>
</html>
```
Here is the complete code for this example, wrapped in a simple HTML file which loads all resources from the cloudflare CDN. You can take this code, add your API key, save it in an HTML file, and open it in your browser of choice to see the example in action.
