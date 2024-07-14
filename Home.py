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
    .main .block-container {
        background: rgba(50, 50, 50, 0.1); 
    }
    .stAlert p {
        color: white; /* Change text color to black */
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


col1, col2 = st.columns([1, 2])

with col1:
    image = Image.open('images/image1.jpg')  
    st.image(image, width=250)

with col2:
     st.markdown("""
    <div style='
    border-radius: 10px;
    background-color:rgba(50, 50, 50, 0);
    color:  #E0E0E0;
    padding: 20px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
    margin-bottom: 20px;
    text-align: Left;'> 
                         
    # Hi, I'm Vishal S
                 
    ###### Self-driven, quick starter, passionate programmer with a curious mind who enjoys solving a complex and challenging real-world problems.
    
    ###### Currently working with Python to upskill in the Field of Artificial Intelligence and Machine Learning (AI & ML).   
                              
    </div>

    """,
        unsafe_allow_html=True)


st.markdown("""
## About Me

- I am a Computer Science Grad Student at Coimbatore Institute of Technology(CIT). I enjoy problem-solving and coding. Always strive to bring 100% to the work I do. I am working on technologies like Python, Django, Flask, Oracle sql, sqlite3, HTML5, CSS, Java, and C++ .

## Skills

**Languages:** Python, Java, JavaScript, C, C++, HTML/CSS, Bash  
**Databases:** sqlite3,oracle  
**Libraries:** Pandas, plotly, Streamlit  
**Frameworks:** Django, Node.js, Bootstrap, Tailwind-css  
**Tools & Technologies:** Git

## Objective

- Looking for an opportunity to work in a challenging position combining my skills in Software Engineering, which provides professional development, interesting experiences, and personal growth.
""")
