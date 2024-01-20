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
st.write('Greetings, '+name+'! Good to see you !')

names = pd.read_csv('names.csv', sep = ';')
names.iloc[len(new_jokes),0] = datetime.now().date().strftime("%d/%m/%Y")
names.iloc[len(new_jokes),0] = name
