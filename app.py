import streamlit as st
import pandas as pd
import pickle
import requests

st.set_page_config(layout="wide")

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl', 'rb'))



# Display the image centered
st.markdown("<div style='text-align: center;'><img src='https://i.pinimg.com/originals/6b/4a/73/6b4a738dd051ec314307435efa574807.png' width='200' height='200'></div>", unsafe_allow_html=True)

# Display the title centered
st.markdown("<h1 style='text-align: center;'>Movie Recommendation System</h1>", unsafe_allow_html=True)
st.write("[Dataset Source: TMDB 10000 Movies Dataset](https://www.kaggle.com/datasets/gazu468/tmdb-10000-movies-dataset?select=10000+Credits+Data)")



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


def recommendation(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x: x[1])

    recommended_posters=[]
    recommended_movies=[]
    for i in distances[1:6]:
        movies_id=movies.iloc[i[0]].Movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movies_id))
    return recommended_movies,recommended_posters



selection=st.selectbox("list of 10000 movies",movies['title'].values)

if st.button('Search'):
    names, posters=recommendation(selection)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


#background
background_image = 'https://user-images.githubusercontent.com/33485020/108069438-5ee79d80-7089-11eb-8264-08fdda7e0d11.jpg' 
st.markdown(f"""
    <style>
        .reportview-container {{
            background: url("blue.jpg") no-repeat center center fixed;
            background-size: cover;
        }}
    </style>
""", unsafe_allow_html=True)