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


# --- CONTACT SECTION ---

st.title("Contact Me")

st.markdown("---")

st.markdown(
        """
        <div style='
            border-radius: 10px;
            background-color: white;
            color: black;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 40px 0;
            width :600px;
            text-align: left;
        '>
            <div style='font-size: 20px; margin-bottom: 10px;'> 📧 Email : <a href="mailto:svs15324@gmail.com" style="color: blue;">svs15324@gmail.com</a></div>
            <div style='font-size: 20px; margin-bottom: 10px;'> 🔗 LinkedIn : <a href="https://www.linkedin.com/in/vishal-s-650a1928b/" style="color: blue;" target="_blank">https://www.linkedin.com/in/vishal-s-650a1928b/</a></div>
            <div style='font-size: 20px;'> 🌐 GitHub : <a href="https://github.com/vishals25" style="color: blue;" target="_blank">https://github.com/vishals25</a></div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
