import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(travel_id):
    response = requests.get(''.format(travel_id))
    response.json

def recommend(travels):
    travel_index = travel[travel['POIs']==travels].index[0]
    distances = similarity[travel_index]
    travel_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommended_travel=[]
    for i in travel_list:
        travel_id=i[0]
         
        recommended_travel.append(travel.iloc[i[0]].POIs)
    return recommended_travel


travel_dict=pickle.load(open('travel_dict.pkl','rb'))
travel= pd.DataFrame(travel_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Tourist System")

selected_travel_name = st.selectbox(
    'How would you like to be contacted?',
    travel['POIs'].values
)


if st.button('Recommend'):
   recommendation= recommend(selected_travel_name)
   for i in recommendation:
        st.write(i)