import streamlit as st
import pickle
import pandas as pd

def recommendation(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similar.pkl','rb'))
st.title('Movie Recommendation System')

option=st.selectbox('select any one option',movies['title'].values)

if st.button('Recommend'):
    recommend=recommendation(option)
    for i in recommend:
        st.write(i)