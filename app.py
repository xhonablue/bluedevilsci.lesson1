import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Space Technology & Earth Science",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #1E88E5 0%, #0D47A1 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #1E88E5;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #4CAF50;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #FFF3E0;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #FF9800;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        border-radius: 5px;
        padding: 0.5rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #0D47A1;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'quiz_answers' not in st.session_state:
    st.session_state.quiz_answers = {}
if 'activity_submitted' not in st.session_state:
    st.session_state.activity_submitted = False

# Sidebar navigation
with st.sidebar:
    st.image("https://via.placeholder.com/400x300/1E88E5/FFFFFF?text=Earth+From+Space", 
             use_container_width=True, caption="Earth from Space")
    
    st.markdown("### 🛰️ Navigation")
    
    pages = {
        "🏠 Home": "home",
        "📰 News Article": "article",
        "🎯 Learning Objectives": "objectives",
        "🌍 Satellites & Earth Science": "satellites",
        "🖨️ 3D Printing Innovation": "3d_printing",
        "🎨 Design Challenge": "design_challenge",
        "❓ Quiz & Assessment": "quiz",
        "📚 Resources": "resources",
        "📥 Downloads": "downloads"
    }
    
    for page_name, page_key in pages.items():
        if st.button(page_name):
            st.session_state.page = page_key
    
    st.markdown("---")
    st.markdown("### 👥 About")
    st.info("**Grade Level:** 9-12\n\n**Duration:** 50-60 minutes\n\n**Subject:** Earth Science")
    
    st.markdown("---")
    st.markdown("**Teacher Mode**")
    teacher_mode = st.checkbox("Enable teacher notes")

# Main content area
def show_home():
    st.markdown('<div class="main-header">🛰️ Space Technology & Earth Observation</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666; font-size: 0.9em; margin-top: -1rem; margin-bottom: 2rem;">Developed by Xavier Honablue, M.Ed. for Grosse Pointe South High School</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="info-box">
        <h3 style="text-align: center;">Welcome to the Interactive Lesson!</h3>
        <p style="text-align: center;">Explore how cutting-edge 3D printing technology is revolutionizing 
        satellite launches and helping us understand Earth better.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎯 Today's Big Question:")
        st.success("**How do we know what's happening to Earth's climate, oceans, and atmosphere when we can't see the whole planet at once?**")
        
        st.markdown("### 📋 What You'll Learn:")
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("""
            ✅ How satellites help study Earth
            
            ✅ What 3D printing technology is
            
            ✅ Why innovation matters for science
            """)
        
        with col_b:
            st.markdown("""
            ✅ Real-world applications
            
            ✅ Design your own satellite mission
            
            ✅ Career connections
            """)
        
        st.markdown("### 🚀 Ready to Begin?")
        st.info("👈 Use the sidebar navigation to explore different sections of this lesson!")
        
        # Quick stats
        st.markdown("---")
        st.markdown("### 📊 Fun Facts About Satellites")
        
        stat1, stat2, stat3, stat4 = st.columns(4)
        
        with stat1:
            st.metric("Active Satellites", "~8,000", "orbiting Earth")
        with stat2:
            st.metric("Weather Satellites", "~400", "monitoring climate")
        with stat3:
            st.metric("Orbit Speed", "17,000 mph", "to stay in
