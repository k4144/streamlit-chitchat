# A simple streamlit add-on

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")
this module allows you to display chat messages in streamlit, aligned right or left and displaying an avatar image of your choosing.

example use:

from streamlit_chitchat import message

user=message('hello', is_user=True)
user.write('sorry, I meant to say goodbye')

[The source for this project is available here][src].
