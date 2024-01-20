import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='MyFirstApp', layout='centered')

code = '''class Me:
	def __init__(self, first_name, last_name):
		self.first_name = Nick
    		self.last_name = Schizas''' 

st.header('Hello there! :wave:', divider = 'gray')
st.code(code, language='python')

name = st.text_input('Say hi', placeholder = 'Enter your name here...')
if name:
	st.write('Greetings, '+name+' ! Nice to meet you !')


ADMIN_USERS = {'sxizasboy@gmail.com'}
if st.experimental_user.email in ADMIN_USERS:
	st.write('user found')
else:
	st.write('user not found')
