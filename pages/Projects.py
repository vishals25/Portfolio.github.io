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
    .main .block-container {
        background: rgba(50, 50, 50, 0.1); 
    }
    .stAlert p {
        color: black; /* Change text color to black */
    }
    .eczjsme18 {
        background-color: whites !important;
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

