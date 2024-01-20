import streamlit as st
import pandas as pd
import random

#search for questionmark
def contains_questionmark(text):
    return True if '?' in text else False

#import the data
jokes = pd.read_csv('all_jokes.csv', sep = ';', index_col=False)

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

with st.expander('Want to contribute? Tell us a joke'):
new_joke = st.text_input('Tell us a joke!', placeholder = 'Write here...')

#read the template df for new jokes
new_jokes = pd.read_csv('new_jokes.csv', sep = ';', index_col=False)
if new_joke and new_joke not in jokes[['Joke']] and new_joke not in new_jokes:
   new_jokes.loc[len(new_jokes)] = new_joke

new_jokes.to_csv('new_jokes.csv', sep=';', index = False)
