import pickle
import streamlit as st
import pandas as pd

# Load the data and precomputed similarity matrix
books_df = pd.read_csv('books.csv')  # Assuming you have a CSV file with book data
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(book_title):
    index = books_df[books_df['title'] == book_title].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_books = []
    for i in distances[1:7]:
        book_title = books_df.iloc[i[0]]['title']
        recommended_books.append(book_title)

    return recommended_books

# Streamlit UI
st.title("Book Recommendation System")
st.write("Find similar books from a dataset of books!")

book_list = books_df['title'].values
selected_book = st.selectbox("Type or select a book you like:", book_list)

if st.button('Show Recommended Books'):
    st.write("Recommended Books based on your interests are:")
    recommended_books = recommend(selected_book)
    for book in recommended_books:
        st.text(book)

    st.markdown("<h6 style='text-align: center; color: red;'>Copyright reserved by Book Authors and Publishers</h6>", unsafe_allow_html=True)
