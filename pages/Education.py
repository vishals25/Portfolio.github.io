
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

# --- EDUCATION SECTION ---
st.title("EDUCATION")


st.markdown("---")


col1, col2 = st.columns(2)


with col1:

    st.header("Bharathi Matriculation Higher Secondary School")

    st.markdown("""
    <div style='
    border-radius: 10px;
    background-color:white;
    color: black;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
    text-align: Left;
        '>

    **Location:** Perundurai,Tamilnadu,India-638056.

    **Degree:** HSLC ,SSLC
                
    **Percentage:** 
    -  SSLC : 99.20%
    -  HSLC : 95.67%
                
    </div>

    """,
        unsafe_allow_html=True)


with col2:

    st.header("Coimbatore Institute of Technology (CIT)")

    st.markdown("""
    <div style='
    border-radius: 10px;
    background-color:white;
    color: black;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
    text-align: Left;
        '>

    **Location:** Coimbatore, Tamilnadu, India -641 014
                
    **Degree:** Bachelor of Computer Science And Engineering(B.E)

    **CGPA:** 8.9 / 10 (4 th semester current)
                                
    </div>

    """,
        unsafe_allow_html=True)