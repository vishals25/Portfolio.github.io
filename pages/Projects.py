import streamlit as s
from PIL import Image
import pandas

s.set_page_config(
    page_title="Vishal S",
    page_icon=":wave:",
    layout="wide"
)

s.markdown(
    """
    <style>
    .reportview-container {
        background: #B7E5F4CC; 
    }
    .main .block-container {
        background: #B7E5F466; 
    }
    .stAlert p {
        color: black; /* Change text color to black */
    }
    .eczjsme18 {
            background-color: #B7E5F4cc !important;
        }
    .ezrtsby2 {
    display: none !important;
    }
    </style>

    """,
    unsafe_allow_html=True
)

s.title("PROJECTS")


s.markdown("---")



col3,mar_col,col4 =s.columns([1.5,0.5,1.5])

df=pandas.read_csv("pages/data.csv",sep=",")


toggle = True

for index,row in df.iterrows():

    if toggle:

        with col3:
            
            s.header(row["title"])
            s.write(row["description"])
            s.image(f'pages/images/{row["image"]}',width=300)
            s.write(f"[Source code]({row['url']})")
            s.write('---')


    else:

        with col4:
            s.header(row["title"])
            s.write(row["description"])
            s.image(f'pages/images/{row["image"]}',width=300)
            s.write(f"[Source code](rows['url'])")
            s.write('---')

    toggle = not toggle

