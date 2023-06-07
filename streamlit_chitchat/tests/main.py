from src.streamlit_chitchat.chitchat import message


# example test code
def test():
    import time
    message('hello', is_user=True, avatar='fun-emoji', seed=100)
    bot = message('hello as well', is_user=False, avatar='bottts', seed=100)
    message('what do you mean?', is_user=True, avatar='images/user.png', seed=100)
    time.sleep(1)
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
    message(text)


if __name__ == '__main__':
    test()
