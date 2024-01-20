import streamlit as st
import pandas as pd
import random

#search for questionmark
def contains_questionmark(text):
    return True if '?' in text else False

#import the data
jokes = pd.read_csv('all_jokes.csv', sep = ';', index_col=False)

st.header('May I tell you a joke?', divider = 'gray')
if st.button('yeap'):
    index = random.randint(0, len(jokes)-1)
    joke = jokes.iloc[index,0]
    if contains_questionmark(joke):
        question = joke.split('?')[0]+'?'
        answer = joke.split('?')[1]
        st.write(question)
        st.write(answer)
    else:
        st.write(joke)
        
new_joke = st.text_input('Want to contribute?', placeholder = 'Write you joke here')
#Update the new data
conn = st.connection('entries_db', type='sql')
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS new_jokes (Joke TEXT);')
    s.execute('INSERT INTO new_jokes (Joke) VALUES (new_joke);')
    s.commit()

#See the results
new_jokes = conn.query('select * from new_jokes')
st.dataframe(new_jokes)
