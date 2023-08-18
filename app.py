import streamlit as st
import pandas as pd
import plotly.express as px
st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">',
    unsafe_allow_html=True,
)
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
st.markdown("""""", unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
                header{visibility:hidden;}
                .main {
                    margin-top: -20px;
                    padding-top:10px;
                }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #A367B2;">
    <a class="navbar-brand" href="#"  target="_blank">AC Pred Maintenance</a>  
    </nav>
""",
    unsafe_allow_html=True,
)


data = pd.read_excel(r'data.xlsx') 

high_temp_threshold = 28  
high_humidity_threshold = 80  
high_sound_threshold = 2800  


high_conditions = (data['Temp'] > int(high_temp_threshold)) & \
                  (data['Humid'] > int( high_humidity_threshold)) & \
                  (data['Sound'] > int(high_sound_threshold))

high_conditions_data = data[high_conditions]


st.title('Feedback App based on Conditions')

st.write("Data with high temperature, humidity, and sound:")
st.write(high_conditions_data)


fig = px.scatter(high_conditions_data, x='Time', y='Temp', color='Humid', size='Sound', title='High Conditions Visualization')
st.plotly_chart(fig)

st.write("Number of instances meeting the conditions:", len(high_conditions_data))

st.write("Feedback:")
if len(high_conditions_data) > 0:
    st.markdown("<span class='card alert alert-warning'>Based on the provided data, it seems that there have been instances of high temperature, high humidity, and high sound levels. This might indicate a need for maintenance or attention to the machinery.</span>",unsafe_allow_html=True)
else:
    st.markdown("<span class='card alert alert-warning'>Based on the provided data, there are no instances that meet the conditions for high temperature, high humidity, and high sound levels.</span>",unsafe_allow_html=True)

# You can add more content or interactivity as needed
