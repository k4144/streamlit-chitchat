import base64
import cv2
import re


# helpers
# image to base64
def encode_image(image, ext='jpg'):
    try:
        return base64.b64encode(cv2.imencode(f'.{ext}', cv2.imread(image))[1]).decode('utf-8')
    except Exception as e:
        print('image error:', e)
        return ''


def _is_url(url):
    if not url:
        return False
    p = re.compile(
        '^http(s)?://(((([a-z0-9-]{1,10}\.){1,3})([a-z0-9-]{1,3})+)|((\d{1,3}\.)4))(/[a-z0-9-]+)?((\?[a-z0-9-]+=['
        'a-z0-9-.]+)(&[a-z0-9-]+=[a-z0-9%.-]+)*)?$',
        flags=re.I | re.M | re.X)
    return bool(re.match(p, url))


def _is_svg(svg):
    if not svg or not isinstance(svg, str):
        return False
    svg = svg.strip()
    return (svg.startswith('<svg') or svg.startswith('<?xml')) and svg.endswith('</svg>')
