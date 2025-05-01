import streamlit as st
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="My Simple Site",
    page_icon="🌐",
    layout="centered"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .main {
        max-width: 800px;
        padding: 2rem;
    }
    .title {
        color: #2c3e50;
        text-align: center;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact", "Blog"])

# Home Page
if page == "Home":
    st.title("Welcome to My Simple Site")
    st.write("""
    This is a simple website built with Python and Streamlit.
    Use the sidebar to navigate between different pages.
    """)

# About Page
elif page == "About":
    st.title("About Us")
    st.write("""
    ## Our Story
    We're a small team passionate about making websites with Python!
    
    ## Our Mission
    To demonstrate how easy it can be to create web applications using Streamlit.
    """)

# Contact Page
elif page == "Contact":
    st.title("Get in Touch")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.success(f"Thank you {name}! We'll contact you at {email} soon.")

# Blog Page
elif page == "Blog":
    st.title("Our Blog")
    
    # Sample blog posts
    posts = [
        {
            "title": "Getting Started with Streamlit",
            "content": "Streamlit makes it easy to create web apps with Python...",
            "date": "2023-05-15"
        },
        {
            "title": "Why Python is Great for Web Development",
            "content": "Python offers many advantages for web development...",
            "date": "2023-04-10"
        }
    ]
    
    for post in posts:
        with st.expander(f"{post['title']} - {post['date']}"):
            st.write(post["content"])
            if st.button("Read more", key=post["title"]):
                st.write("Full article would go here...")

# Run the app
if __name__ == "__main__":
    st.write(f"© {datetime.now().year} My Simple Site")