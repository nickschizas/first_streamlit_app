import streamlit as st

code = '''class Me:
	def __init__(self, first_name, last_name):
		self.first_name = Nick
    		self.last_name = Schizas''' 

st.header('Hello there! :wave:', divider = 'gray')
st.code(code, language='python')
name = st.text_input('', placeholder = 'Name')
if st.button('Say hi'):
    if name:
        st.write('Greetings, '+name+'. Good to see you !')
    else:
        st.write('*Please enter your name above first*')