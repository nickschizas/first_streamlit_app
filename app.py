#My first streamlit deployed app

import streamlit as st

#Making the text of the st.code
code = '''class Creator:
	def __init__(self, first_name, last_name):
		self.first_name = Nick
    		self.last_name = Schizas''' 

#Visible elements of the page
st.header('Hello all, this is my first deployed app', divider = 'gray')
st.code(code, language='python')

name = st.text_input('', placeholder = 'Name')
if st.button('Say hi'):
	if name:
		st.write('Hi, '+name+'. Good to see you !')
	else:
		st.write('*Please enter your name above first*')