
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

i0 = '''<div></div>'''
i1 = '<img src="{image}" alt="" style="border:1px solid transparent;{border_radius};{width};{height};">'
t1 = '''
    <div style="display:flex;{font_size}{font}{color}flex-direction:row-reverse;{margin}">
        {img}
        <div
            style="display:flex;text-align:left;align-items:center;border:1px solid transparent;border-radius:5px;{background}{width}{height}{padding}">
            {message}
        </div>
    </div>
    '''
t2 = '''
    <div style="display:flex;{font_size}{font}{color}flex-direction:row;{margin}">
        {img}
        <div
            style="display:flex;text-align:left;align-items:center;border:1px solid transparent;border-radius:5px;{background}{width}{height}{padding}">
            {message}
        </div>

    </div>
    '''

t3 = '''
     <img src="{image}" alt="blue dot" />
    '''
