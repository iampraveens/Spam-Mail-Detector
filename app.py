import requests
from io import BytesIO
import streamlit as st 
from PIL import Image
import joblib

url = "https://cdn-icons-png.flaticon.com/512/9275/9275788.png"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
page_title = 'Spam Mail Detector'
page_icon = image
layout = 'wide'

st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout
                   )

hide_style = '''
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            <style>
            
            '''
header_style = '''
             <style>
             .navbar {
                 position: fixed;
                 top: 0;
                 left: 0;
                 width: 100%;
                 z-index: 1;
                 display: flex;
                 justify-content: center;
                 align-items: center;
                 height: 80px;
                 background-color: #50717b;
                 box-sizing: border-box;
             }
             
             .navbar-brand {
                 color: white !important;
                 font-size: 23px;
                 text-decoration: none;
                 margin-right: auto;
                 margin-left: 50px;
             }
             
             .navbar-brand img {
                margin-bottom: 6px;
                margin-right: 1px;
                width: 40px;
                height: 40px;
                justify-content: center;
            }
            
            /* Add the following CSS to change the color of the text */
            .navbar-brand span {
                color: #EF6E04;
                justify-content: center;
            }
            
             </style>
             
             <nav class="navbar">
                 <div class="navbar-brand">
                <img src="https://cdn-icons-png.flaticon.com/512/9275/9275788.png" alt="Logo">
                    Spam Mail Detector
                 </div>
             </nav>
               '''
st.markdown(hide_style, unsafe_allow_html=True)
st.markdown(header_style, unsafe_allow_html=True)

# feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)

user_input = st.text_area(label='Enter the mail:', height=150, 
             max_chars=1000, 
             help='Enter the Ham or Spam mail and Press crtl + enter')

vectorizer = joblib.load(open('vectorizer.pkl', 'rb'))
model = joblib.load(open('model.pkl', 'rb'))

vector_iput = vectorizer.transform([user_input])
    
predict_button =  st.button(label='Predict')
if predict_button:
    prediction = model.predict(vector_iput)
    
    column_1, column_2 = st.columns([20,40])
    with column_1:
        if prediction[0] == 1:
            st.success("It is a Ham Mail")
        else:
            st.error("It is a Spam Mail")