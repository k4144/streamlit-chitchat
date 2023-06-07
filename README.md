<br>

  

<img  src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png"  alt="Streamlit logo"  style="margin-top:50px"></img>

  

# streamlit-chitchat

  

**make chat messages easier to style in streamlit**

  

streamlit-chitchat lets you style messages from the user and responses from a bot differently. you can also update an existing message, so that streamed tokens render as they are received. 


  

## Installation

  

Open a terminal and run:

  

```bash

$  pip  install  streamlit-chitchat

```

## example use
  

in your streamlit app, insert:

  

```bash

from streamlit-chitchat.chitchat import message
message('hello, how are you?', is_user=True)
bot=message()
for w in 'excellent! have any plans for tonight?'.split(' '):
	bot.write(w+' ')
```


