from streamlit_chitchat.streamlit_chitchat.chitchat import message
import streamlit as st


# example test code
def test1():
    import time
    message('hello', is_user=True, avatar='fun-emoji', seed=100)
    bot = message('hello as well', is_user=False, avatar='bottts', seed=100)
    message('what do you mean?', is_user=True, avatar='images/user.png', seed=100)
    time.sleep(0.3)
    bot.write('actually, i wanted to say sorry')
    message('ok, i understand', is_user=True,
            avatar='https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80')
    message()
    message('hello')
    message('hello as well', is_user=True)
    text = '''Wikipedia is an online encyclopedia written and maintained by a community of volunteers, known as Wikipedians,
             through open collaboration and using a wiki-based editing system called MediaWiki. 
             Wikipedia is the largest and most-read reference work in history, and has consistently been 
             one of the 10 most popular websites.'''
    m1 = message()
    t=''
    for word in text.split(' '):
        t+=word+' '
        m1.write(t)
        time.sleep(0.05)
def test2():
    with st.container():
        # image file
        st.write('\n')
        st.write('\nimage file')
        message('hello ', is_user=True, avatar='images/man.png', background='lightgreen')
        # default avatar (different for bot and user)
        st.write('\n')
        st.write('\ndefault')
        message('hello', is_user=False, avatar='', seed=142, background='lightblue')
        # inline svg
        st.write('\n')
        st.write('\ninline svg')
        svg = '''<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="60px" height="40px" viewBox="0 0 122.88 80.593" enable-background="new 0 0 122.88 80.593" xml:space="preserve"><g><polygon points="122.88,0 122.88,30.82 61.44,80.593 0,30.82 0,0 61.44,49.772 122.88,0"/></g></svg>'''
        message('hello', is_user=False, avatar=svg, seed=142, background='lightblue')
        st.write('\n')
        st.write('\nsvg file')
        message('hello', is_user=False, avatar='images/angle-bottom-icon.svg', seed=142, background='lightblue')

        # no avatar
        st.write('\n')
        st.write('\nno avatar')
        message('hello', is_user=True, background='lightgreen')
        message('hello', is_user=False, background='lightblue')
        # background as rgb color
        st.write('\n')
        st.write('\nrgb background')
        message('hello', is_user=True, background='rgb(50,150,150)')
        message('hello', is_user=False, background='rgb(160,150,141)')
        # background as rgb color with alpha channel
        st.write('\n')
        st.write('\nrgb with alpha channel')
        message('hello', is_user=True, background='rgb(50,150,150,0.5)')
        message('hello', is_user=False, background='rgb(160,150,141,0.5)')
        st.write('\n')
        st.write('\n other styles')
        st.write('\n color, width, margin')
        message('hello', color='rgb(220,20,30)', width='60%', margin='20px')
        st.write('\n other styles')
        st.write('\n font size')
        message('hello', font_size='3rem')
        st.write('\n other styles')
        st.write('\n padding')
        message('hello', padding='30px')


if __name__ == '__main__':
    test1()
    test2()
