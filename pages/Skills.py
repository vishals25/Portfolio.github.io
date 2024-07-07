
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Vishal S",
    page_icon=":wave:",
    layout="wide"
)

st.markdown(
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

# --- SKILLS SECTION ---
st.title("Skills")

st.markdown("---")

st.markdown("""## Languages and Databases""")

st.write("")

col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    image = Image.open("pages/image/python-logo.jpg")
    st.image(image, caption="Python",width=150)

    

with col2:

    image = Image.open("pages/image/html5.jpg")
    st.image(image, caption="HTML5",width=150)


with col3:

    image = Image.open("pages/image/css3.jpg")
    st.image(image, caption="CSS3",width=150)

with col4:

    image = Image.open("pages/image/JavaScript-logo.png")
    st.image(image, caption="JavaScript",width=150)

st.markdown("---")

st.markdown("""## Libraries """)

st.write("")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    image = Image.open("pages/image/pandas-logo.jpg")
    st.image(image, caption="Pandas",width=150)

with col2:

    image = Image.open("pages/image/sp.webp")
    st.image(image, caption="Streamlit",width=150)

st.markdown("---")

st.markdown("""## FrameWorks """)

st.write("")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    image = Image.open("pages/image/django-logo.webp")
    st.image(image, caption="Django",width=150)

with col2:

    image = Image.open("pages/image/tw.jpg")
    st.image(image, caption="TailWind-CSS",width=150)

st.markdown("---")

st.markdown("""## Others """)

st.write("")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    image = Image.open("pages/image/git.png")
    st.image(image, caption="Git",width=150)