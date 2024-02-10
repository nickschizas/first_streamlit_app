import streamlit as st
import pandas as pd
import random

#search for questionmark
def contains_questionmark(text):
    return True if '?' in text else False

#import the data
jokes = pd.read_csv('all_jokes.csv', sep = ';', index_col=False)

st.header('May I tell you a joke?', divider = 'gray')
if st.button('Hit me!'):
    index = random.randint(0, len(jokes)-1)
    joke = jokes.iloc[index,0]
    if contains_questionmark(joke):
        question = joke.split('?')[0]+'?'
        answer = joke.split('?')[1]
        st.write(question)
        st.write(answer)
    else:
        st.write(joke)
