import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import random

#search for questionmark
def contains_questionmark(text):
    return True if '?' in text else False

code = '''class Creator:
	def __init__(self, first_name, last_name):
		self.first_name = Nick
    		self.last_name = Schizas''' 

#import the data
jokes = pd.read_csv('all_jokes.csv', sep = ';', index_col=False)

#Page visible elements
with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ['Hello', 'Joke?']
    )
if selected == 'Hello':
    st.header('Hello :wave:', divider = 'gray')
    st.code(code, language='python')
    name = st.text_input('', placeholder = 'Name')
    if st.button('Say hi'):
        if name:
            st.write('Greetings, '+name+'. Good to see you !')
        else:
            st.write('*Please enter your name above first*')
if selected == 'Joke?':
    st.header('Joke?', divider = 'gray')
    if st.button('Hit me'):
        index = random.randint(0, len(jokes)-1)
        joke = jokes.iloc[index,0]
        if contains_questionmark(joke):
            question = joke.split('?')[0]+'?'
            answer = joke.split('?')[1]
            st.write(question)
            st.write(answer)
        else:
            st.write(joke)
