import pickle
import pandas as pd
import streamlit as st

def recommend(book):

    book_index = books[books['Title'] == book].index[0]
    distances = similarity[book_index]
    books_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_books= []
    for i in books_list:
        recommended_books.append(books.iloc[i[0]].Title)
    return recommended_books


book_dict = pickle.load(open('Books_dict.pkl', 'rb'))
books = pd.DataFrame(book_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Book Recommender System')

Selected_Book_Name = st.selectbox(
    'What do you like to read today ?',
    books['Title'].values)

if st.button('Recommend'):
    recommendations = recommend(Selected_Book_Name)
    for i in recommendations:
            st.write(i)
