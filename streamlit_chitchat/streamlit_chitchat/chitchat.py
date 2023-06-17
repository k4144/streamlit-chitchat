import os
import streamlit as st
from streamlit_chitchat.streamlit_chitchat.utils import _is_svg, _is_url, encode_image
from streamlit_chitchat.streamlit_chitchat.data import i0, i1, t1, t2, bot_avatars, user_avatars, dicebear_avatars


class message:
    def __init__(self, text=None, element=None, is_user=None, font=None, font_size=None, color=None, background=None,
                 width=None, height=None, avatar=None, avatar_size=None, avatar_mode=None, seed=None, margin=None,
                 padding=None):
        self.element = element if element is not None else st.empty()
        self.is_user = is_user
        self.font = 'Geneva, Verdana, sans-serif' if font is None else font
        self.font_size = '1rem;' if font_size is None else font_size
        self.padding = '4px 10px 4px 10px;' if padding is None else padding
        self.margin = '2px' if margin is None else margin
        self.background = 'rgb(240, 242, 246)' if background is None else background
        self.color = 'rgb(49, 51, 63)' if color is None else color
        self.width = '70%;' if width is None else width
        self.height = '3rem' if height is None else height
        self.ext = 'jpg'
        self.svg = False
        self.avatar_size = avatar_size if avatar_size else '3rem'
        self.avatar_mode = '15%' if avatar_mode == 'square' else '50%'
        if avatar in dicebear_avatars:
            seed = 10 if seed is None else seed
            self.avatar = f'https://api.dicebear.com/5.x/{avatar}/svg?seed={seed}'
        elif _is_url(avatar):
            self.avatar = f'{avatar}'
        elif avatar and os.path.isfile(avatar):
            # svg file
            if avatar.endswith('.svg'):
                avtr = open(avatar, 'r').read()
                if _is_svg(avtr):
                    self.avatar = f'{avtr}'
                    self.svg = True
                else:
                    print(f'{avatar}: does not appear to be an svg file despite of its extension')
                    self.avatar = ''
            # image file
            else:
                ex = os.path.splitext(avatar)[1]
                ex = ex[1:] if ex else ex
                self.ext = 'jpg' if not ex else ex
                fs = f'data:image/{self.ext};base64,'
                self.avatar = f'{fs}{encode_image(avatar)}'
        elif _is_svg(avatar):
            self.avatar = f'{avatar}'
            self.svg = True
        # use default bot/user avatar
        elif avatar == '':
            self.avatar = user_avatars[0] if self.is_user else bot_avatars[0]
        # default case: no avatar
        else:
            self.avatar = None

        if text:
            self.write(text)

    def _message(self, text):
        h1 = t1 if self.is_user else t2
        width = f'width:{self.width};'  # max-width
        height = f'min-height:{self.height};'
        font = f'font-family: {self.font};'  # 'font-family: Geneva, Verdana, sans-serif;'
        font_size = f'font-size: {self.font_size};'
        color = f'color:{self.color};'
        background = f'background-color:{self.background};'
        margin = f'margin:{self.margin};'
        padding = f'padding:{self.padding};'
        border_radius = f'border-radius:{self.avatar_mode};'
        avatar_width = f'width:{self.avatar_size}'
        avatar_height = f'height:{self.avatar_size}'

        img = self.avatar if self.svg else i0 if self.avatar is None else i1.format(image=self.avatar,
                                                                                    border_radius=border_radius,
                                                                                    width=avatar_width,
                                                                                    height=avatar_height)

        ret = h1.format(img=img, message=text, width=width, height=height, font=font, font_size=font_size, color=color,
                        background=background, margin=margin, padding=padding)
        # print(f'svg: {self.svg}\n', ret)
        return ret

    def write(self, text=None):
        if text is not None:
            text = text.replace('\n', '<br>')
            self.element.write(self._message(text), unsafe_allow_html=True)
        return self.element


def test_message():
    pass


if __name__ == '__main__':
    pass
