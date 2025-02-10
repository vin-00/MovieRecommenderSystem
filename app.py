
import streamlit as st
import pickle

import helper

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies_list = movies['title'].values

def recommend(movie , number):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]

    store = sorted(list(enumerate(distances)) , reverse=True , key=lambda x : x[1])[1:(number+1)]

    names= []
    images =[]
    for i in store:
        movie_idx = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        images.append(helper.fetch_poster(movie_idx))
    return names , images

st.title("Movie Recommender System")

col1 ,col2 = st.columns([3,1])
with col1 : 
    selected_movie  = st.selectbox(
        'Select a movie',
        movies_list
    )
with col2 :
    selected_number = st.selectbox(
        "Select the number of recommendations you want",
        (5,10,15,20)
    )

if st.button("Recommend" ,type='primary'):
    names , images = recommend(selected_movie , selected_number)

    for i in range((len(names)//5)):
        column = st.columns(5)
        for j in range(5):
            with column[j]:
                st.header(names[i*5 + j])
                st.image(images[i*5 + j])


