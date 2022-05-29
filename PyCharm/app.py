import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(layout="wide")

#CSS styles 
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

kdramas_dict = pickle.load(open('kdramas_dict.pkl', 'rb'))
kdramas = pd.DataFrame(kdramas_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(kdrama_id):
    response = requests.get('https://api.themoviedb.org/3/tv/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(kdrama_id))
    data = response.json()
    if data['poster_path'] != None:
        return "https://www.themoviedb.org/t/p/w1280" + data['poster_path']
    else:
        return "images.jpg"

def recommend(kdrama):
    kdrama_index = kdramas[kdramas['title'] == kdrama].index[0]
    distances = similarity[kdrama_index]
    kdramas_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_kdramas = []
    recommended_kdramas_posters = []
    for i in kdramas_list:
        kdrama_id = kdramas.iloc[i[0]].id
        # fetch movie title & poster from API
        recommended_kdramas.append(kdramas.iloc[i[0]].title)
        recommended_kdramas_posters.append(fetch_poster(kdrama_id))
    return recommended_kdramas, recommended_kdramas_posters


st.title('K-Drama Recommendation System')

st.caption('Welcome to the K-Drama Recommendation System ^_^ Select your favourite K-Drama to get more recommendations.')
option = st.selectbox(
     'Choose a K-drama to get 10 similar K-Dramas recommendation.',
     kdramas['title'].values)

if st.button('Recommend K-Dramas'):
    names, posters = recommend(option)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    with col1:
        st.write(names[0])
        st.image(posters[0])
    with col2:
        st.write(names[1])
        st.image(posters[1])
    with col3:
        st.write(names[2])
        st.image(posters[2])
    with col4:
        st.write(names[3])
        st.image(posters[3])
    with col5:
        st.write(names[4])
        st.image(posters[4])
    with col6:
        st.write(names[5])
        st.image(posters[5])
    with col7:
        st.write(names[6])
        st.image(posters[6])
    with col8:
        st.write(names[7])
        st.image(posters[7])
    with col9:
        st.write(names[8])
        st.image(posters[8])
    with col10:
        st.write(names[9])
        st.image(posters[9])