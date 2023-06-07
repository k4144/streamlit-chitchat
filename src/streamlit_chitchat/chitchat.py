import re
import os
import time
import cv2
import base64
import streamlit as st


# helpers
# image to base64
def encode_image(image, ext='jpg'):
    try:
        return base64.b64encode(cv2.imencode(f'.{ext}', cv2.imread(image))[1]).decode('utf-8')
    except Exception as e:
        print('image error:', e)
        return ''


# avatar templates
bot_avatars = ['https://img.uxwing.com/wp-content/themes/uxwing/download/internet-network-technology/robot-icon.svg',
               'https://img.uxwing.com/wp-content/themes/uxwing/download/internet-network-technology/robot-line-icon.svg']
user_avatars = [
    'https://img.uxwing.com/wp-content/themes/uxwing/download/peoples-avatars-thoughts/boy-glasses-icon.svg',
    'https://img.uxwing.com/wp-content/themes/uxwing/download/peoples-avatars-thoughts/man-face-with-glasses-icon.svg',
    'https://img.uxwing.com/wp-content/themes/uxwing/download/peoples-avatars-thoughts/girl-icon.svg',
    'https://img.uxwing.com/wp-content/themes/uxwing/download/peoples-avatars-thoughts/girl-eyeglasses-icon.svg']
dicebear_avatars = ['adventurer', 'adventurer-neutral', 'avataaars', 'avataaars-neutral', 'big-ears',
                    'big-ears-neutral', 'big-smile', 'bottts', 'bottts-neutral', 'croodles', 'croodles-neutral',
                    'fun-emoji', 'icons', 'identicon', 'initials', 'lorelei', 'lorelei-neutral', 'micah', 'miniavs',
                    'open-peeps', 'personas', 'pixel-art', 'pixel-art-neutral', 'shapes', 'thumbs']

# html templates
t1 = '''
    <div style="display:flex;{font_size}{font}{color}flex-direction:row-reverse;{margin}">
        <img src="{image}" style="border:1px solid transparent;border-radius:50%;width:3rem;height:3rem;">
        <div
            style="display:flex;text-align:left;align-items:center;border:1px solid transparent;border-radius:5px;{background}{width}{padding}">
            {message}
        </div>
    </div>
    '''
t2 = '''
    <div style="display:flex;{font_size}{font}{color}flex-direction:row;{margin}">
        <img src="{image}" style="border:1px solid transparent;border-radius:50%;width:3rem;height:3rem;">
        <div
            style="display:flex;text-align:left;align-items:center;border:1px solid transparent;border-radius:5px;{background}{width}{padding}">
            {message}
        </div>

    </div>
    '''
t3 = '''
     <img src="{image}" alt="Red dot" />
    '''

def _is_url(url):
    if not url:
        return False
    p = re.compile(
        '^http(s)?://(((([a-z0-9-]{1,10}\.){1,3})([a-z0-9-]{1,3})+)|((\d{1,3}\.)4))(/[a-z0-9-]+)?((\?[a-z0-9-]+=['
        'a-z0-9-.]+)(&[a-z0-9-]+=[a-z0-9%.-]+)*)?$',
        flags=re.I | re.M | re.X)
    return bool(re.match(p, url))


class message:
    def __init__(self, text=None, element=None, is_user=None, font=None, font_size=None, color=None, background=None,
                 width=None, avatar=None, seed=None, margin=None, padding=None):
        self.element = element if element is not None else st.empty()
        self.is_user = is_user
        self.font = 'Geneva, Verdana, sans-serif' if font is None else font
        self.font_size = '1rem;' if font_size is None else font_size
        self.padding='4px 10px 4px 10px;' if padding is None else padding
        self.margin = '2px' if margin is None else margin
        self.background = 'rgb(240, 242, 246)' if background is None else background
        self.color = 'rgb(49, 51, 63)' if color is None else color
        self.width = '70%;' if width is None else width
        self.ext = 'jpg'
        if avatar in dicebear_avatars:
            seed = 10 if seed is None else seed
            self.avatar = 'https://api.dicebear.com/5.x/{av}/svg?seed={seed}'.format(av=avatar, seed=seed)
        elif _is_url(avatar):
            self.avatar = f'{avatar}'
        elif avatar and os.path.isfile(avatar):
            ex = os.path.splitext(avatar)[1]
            ex = ex[1:] if ex else ex
            self.ext = 'jpg' if not ex else ex
            fs = f'data:image/{self.ext};base64,'
            self.avatar = f'{fs}{encode_image(avatar)}'
        else:
            self.avatar = user_avatars[0] if self.is_user else bot_avatars[0]
        if text:
            self.write(text)

    def _message(self, text):
        h1 = t1 if self.is_user else t2
        width = f'width:{self.width};'  # max-width
        font = f'font-family: {self.font};'# 'font-family: Geneva, Verdana, sans-serif;'
        font_size = f'font-size: {self.font_size};'
        color = 'color:{color};'.format(color=self.color)
        background = 'background-color:{background};'.format(background=self.background)
        image = self.avatar
        margin = f'margin:{self.margin};'
        padding = f'padding:{self.padding};'
        return h1.format(image=image, message=text, width=width, font=font, font_size=font_size, color=color,
                           background=background, margin=margin, padding=padding)

    def write(self, text=None):
        if text is not None:
            text=text.replace('\n', '<br>')
            self.element.write(self._message(text), unsafe_allow_html=True)
        return self.element



if __name__ == '__main__':
    pass
