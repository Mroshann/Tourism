import streamlit as st
import pickle
import pandas as pd
import requests
import googlemaps


page_bg_img = """<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1536257104079-aa99c6460a5a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80");

background-size: cover;
}
[data-testid="stHeader"]{
background-color:rgba(0,0,0,0);
}
</style>"""
st.markdown(page_bg_img,unsafe_allow_html=True)

def fetch_poster(travel_id):
    response = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key=AIzaSyB0BjY4f1JSU7V9cipik8R2LakBNXfM35E'.format(travel_id))
    data = response.json()
    if 'results' in data and len(data['results']) > 0:
        photo_reference = data['results'][0].get('photos', [])[0].get('photo_reference', '')
        if photo_reference:
            return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference={photo_reference}&key=AIzaSyB0BjY4f1JSU7V9cipik8R2LakBNXfM35E"
    return None


def recommend(travels):
    travel_index = travel[travel['POIs']==travels].index[0]
    distances = similarity[travel_index]
    travel_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommended_travel=[]
    recommended_travel_posters=[]
    for i in travel_list:
        travel_id=travel.iloc[i[0]].POIs
        # travel_id = i[0]

        recommended_travel.append(travel.iloc[i[0]].POIs)
        recommended_travel_posters.append(fetch_poster(travel_id))
    return recommended_travel, recommended_travel_posters


travel_dict=pickle.load(open('travel_dict.pkl','rb'))
travel= pd.DataFrame(travel_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Tourist Recommendation System!!")



selected_travel_name = st.selectbox(
    'What would you like to be recommended?',
    travel['POIs'].values,
    # format_func=format_text
)


if st.button('Recommend'):
   names,posters =recommend(selected_travel_name)
  # st.write[i]
   col1, col2, col3, col4, col5 = st.columns(5)
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


st.markdown(
    '<div class="button-container"><a href="http://127.0.0.1:5000/" target="_self" style="color:black;background-color:white;padding:10px;border-radius:5px;text-decoration:none;">Back To Home Page</a></div>',
    unsafe_allow_html=True,
)


