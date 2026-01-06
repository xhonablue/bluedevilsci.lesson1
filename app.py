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
    .sub-header {
        font-size: 1.5rem;
        color: #0D47A1;
        margin-top: 1rem;
        margin-bottom: 1rem;
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
    .hyliard-box {
        background-color: #FFF9C4;
        padding: 1.5rem;
        border-radius: 10px;
        border: 3px solid #FBC02D;
        margin: 1.5rem 0;
        font-family: 'Georgia', serif;
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
if 'met_hyliard' not in st.session_state:
    st.session_state.met_hyliard = False

# Dr. Hyliard helper function
def dr_hyliard_says(message, title="🔬 Dr. Hyliard's Insight"):
    st.markdown(f"""
    <div class="hyliard-box">
    <h4 style="color: #F57C00; margin-top: 0;">{title}</h4>
    <p style="font-size: 1.05rem; line-height: 1.6; margin-bottom: 0;">
    {message}
    </p>
    <p style="text-align: right; font-style: italic; color: #666; margin-bottom: 0;">
    — Dr. Marcus Hyliard, Satellite Engineer & Climate Scientist
    </p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.image("https://via.placeholder.com/400x300/1E88E5/FFFFFF?text=Dr.+Hyliard", 
             use_container_width=True, caption="Dr. Marcus Hyliard - Your Guide")
    
    st.markdown("### 🛰️ Navigation")
    
    pages = {
        "🏠 Home": "home",
        "👨‍🔬 Meet Dr. Hyliard": "hyliard",
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
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="info-box">
        <h3 style="text-align: center;">Welcome to the Interactive Lesson!</h3>
        <p style="text-align: center;">Join Dr. Marcus Hyliard as he explores how cutting-edge 3D printing technology 
        is revolutionizing satellite launches and helping us understand Earth better.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Dr. Hyliard introduction
        if not st.session_state.met_hyliard:
            dr_hyliard_says("""
            Hello! I'm Dr. Marcus Hyliard, and I've spent the last 15 years working with satellites and 
            climate data. Today, I'm going to share something incredible with you - a breakthrough in 3D printing 
            that's changing everything we know about launching satellites into space. Trust me, by the end of 
            this lesson, you'll see Earth in a whole new way! Let's get started by clicking 'Meet Dr. Hyliard' 
            in the sidebar.
            """, "👋 Welcome from Dr. Hyliard")
            
            if st.button("I'm ready to learn!"):
                st.session_state.met_hyliard = True
                st.session_state.page = 'hyliard'
                st.rerun()
        
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
            st.metric("Orbit Speed", "17,000 mph", "to stay in space")
        with stat4:
            st.metric("Daily Images", "Millions", "of Earth's surface")

def show_hyliard():
    st.markdown('<div class="main-header">👨‍🔬 Meet Dr. Marcus Hyliard</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://via.placeholder.com/400x500/1E88E5/FFFFFF?text=Dr.+Hyliard", 
                caption="Dr. Marcus Hyliard")
        
        st.markdown("""
        ### Quick Facts
        
        **Position:** Senior Satellite Engineer
        
        **Education:** PhD in Aerospace Engineering
        
        **Specialty:** Climate Monitoring Systems
        
        **Years of Experience:** 15
        
        **Satellites Helped Launch:** 23
        
        **Favorite Part of Job:** "Watching our planet from space never gets old!"
        """)
    
    with col2:
        st.markdown("## Dr. Hyliard's Story")
        
        dr_hyliard_says("""
        When I was your age, I looked up at the stars and wondered what was out there. But then something 
        changed my perspective completely - I realized the most interesting thing we can study from space 
        isn't "out there" at all. It's right here. It's Earth.
        
        I remember the first time I saw live satellite data showing a hurricane forming in the Atlantic. 
        We watched it develop in real-time, tracked its path, and because of that data, thousands of people 
        evacuated safely. That's when I knew this was my calling.
        
        Now, after 15 years working with satellites, I'm more excited than ever. Why? Because of 3D printing. 
        This technology is making satellites cheaper and faster to build, which means we can launch more of 
        them. More satellites means better data. Better data means we can better protect our planet and 
        everyone on it.
        """, "📖 My Journey to the Stars")
        
        st.markdown("---")
        st.markdown("### A Day in Dr. Hyliard's Life")
        
        with st.expander("🌅 Morning: Checking Overnight Data"):
            st.write("""
            Every morning, I review data from satellites that monitored Earth while I slept. 
            Did any wildfires start? Are ocean temperatures changing? How much ice melted in Antarctica overnight? 
            
            One morning last year, I noticed something unusual - ocean temperatures in the Pacific were rising 
            faster than expected. Within hours, we alerted climate scientists, and it turned out to be the 
            beginning of an El Niño event. Early warning meant farmers and fishermen could prepare.
            """)
        
        with st.expander("☀️ Afternoon: The 3D Printing Breakthrough"):
            st.write("""
            This is where today's lesson comes in! A few months ago, my colleague at Momentus showed me 
            something incredible - a fuel tank for a satellite, completely 3D printed. 
            
            I held it in my hands. It was lighter than traditional tanks, more complex in design, and cost 
            a fraction of the price. I immediately thought: "This changes everything."
            
            With cheaper satellites, we could finally create the global monitoring network we've always dreamed of!
            """)
        
        with st.expander("🌙 Evening: Planning Future Missions"):
            st.write("""
            I spend my evenings planning future satellite missions. With 3D printing technology, missions 
            that would have cost $50 million might now cost $10 million. That means we can do FIVE times 
            as many missions!
            
            Right now, I'm planning a constellation of micro-satellites to monitor Arctic ice. Ten years ago, 
            this would have been impossible to afford. Today, with 3D-printed components, we're making it happen.
            """)
        
        st.markdown("---")
        st.markdown("### 💭 Dr. Hyliard's Philosophy")
        
        st.info("""
        **"Technology and science are partners in discovery. Every technological breakthrough - whether it's 
        a better telescope, a faster computer, or now 3D printing - opens new doors for scientific understanding. 
        That's what makes this work so exciting. We're not just engineers or scientists. We're explorers, 
        and Earth is our frontier."**
        """)
        
        st.markdown("### 🎯 Why This Matters to You")
        
        dr_hyliard_says("""
        You might be thinking, "I'm not going to be a satellite engineer." And that's fine! But here's the thing - 
        the data we collect affects YOUR life every single day.
        
        - Weather forecast on your phone? That's satellite data.
        - News about climate change? Based on satellite measurements.
        - GPS navigation to your friend's house? Wouldn't work without satellites.
        - Warnings about natural disasters? Satellites spot them first.
        
        Whether you become a doctor, teacher, artist, or entrepreneur, you'll be using information gathered 
        by satellites. That's why I'm so passionate about making them better, cheaper, and more accessible. 
        Better satellites mean better information for EVERYONE.
        
        Now, let's dive into the technology that's making all this possible!
        """, "🌍 How This Connects to Your Life")

def show_article():
    st.markdown('<div class="main-header">📰 The News Article</div>', unsafe_allow_html=True)
    
    # Dr. Hyliard's introduction to the article
    dr_hyliard_says("""
    This is the news story that got me so excited! When I first read about Momentus's 3D-printed fuel tank, 
    I immediately called my colleague to congratulate them. This is the breakthrough we've been waiting for. 
    As you read, think about how this technology could change space exploration and Earth observation.
    """, "📰 Dr. Hyliard Introduces the Story")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Momentus shares spike after advancing 3D-printed fuel tank for spaceflight
        
        **By Fiona Craig • Published 10 hours ago**
        
        📰 **[Read the full article on Yahoo Finance](https://finance.yahoo.com/news/momentus-develops-additive-manufactured-fuel-133000052.html)**
        
        ---
        """)
        
        st.image("https://via.placeholder.com/800x400/1E88E5/FFFFFF?text=Satellite+in+Space", 
                 caption="Space satellite in Earth orbit", use_container_width=True)
        
        st.markdown("""
        **Momentus Inc.** (NASDAQ:MNTS) shares jumped 44.1% in premarket trading on Monday after the company 
        disclosed progress on a newly developed 3D-printed fuel tank created in partnership with **Velo3D**.
        
        The U.S.-based commercial space company said the additively manufactured tank is slated for flight 
        testing on its upcoming **Vigoride-7 Orbital Service Vehicle** mission. The component was produced 
        using Velo3D's metal additive manufacturing technology, which enables highly complex designs that 
        are difficult or impractical to produce using conventional fabrication techniques.
        
        Momentus said the fuel tank was engineered to optimize performance while taking advantage of Velo3D's 
        end-to-end manufacturing solution. The company plans to leverage this capability to enter new markets 
        as a certified supplier of space-grade fuel tanks—components that are typically expensive and 
        associated with long production lead times.
        
        > "Testing an additively manufactured fuel tank on Vigoride-7 is a major achievement for Momentus 
        > and a testament to the strength of our partnership with Velo3D," said **John Rood**, Chief Executive 
        > Officer of Momentus. "Additive manufacturing opens new possibilities for spacecraft design and 
        > production, and this successful demonstration paves the way for broader adoption across our 
        > future missions."
        
        By incorporating additive manufacturing into its supply chain, Momentus aims to:
        - **Lower costs** for satellite production
        - **Accelerate development timelines**
        - **Improve robustness** of spacecraft platforms
        
        The company provides satellite buses and integration services, satellite components, as well as 
        in-space transportation and infrastructure solutions.
        """)
        
        # Dr. Hyliard's reaction
        st.markdown("---")
        dr_hyliard_says("""
        Here's what excites me most: "Lower costs" and "accelerate development timelines." 
        
        Remember when I told you about my Arctic ice monitoring project? With traditional manufacturing, 
        those fuel tanks would take 6 months to make and cost $150,000 each. With 3D printing, we're talking 
        3 weeks and $30,000. That's the difference between a mission that's possible and one that's not.
        
        And John Rood is right - this IS a major achievement. In 20 years, we'll look back at this moment 
        as the turning point when satellite technology became accessible to everyone.
        """, "🔬 Dr. Hyliard's Analysis")
    
    with col2:
        st.markdown("### 🔑 Key Terms")
        
        with st.expander("**Additive Manufacturing**"):
            st.write("Building objects layer by layer, also known as 3D printing. Uses materials like metal powder to create complex shapes.")
            dr_hyliard_says("Think of it like a super-advanced hot glue gun that uses metal instead of glue!", 
                           "💡 Dr. Hyliard Explains")
        
        with st.expander("**Fuel Tank**"):
            st.write("Container that holds propellant for spacecraft maneuvering in space. Essential for adjusting satellite position.")
            dr_hyliard_says("Without fuel tanks, satellites would be like cars without steering wheels - they'd drift wherever gravity takes them!", 
                           "💡 Dr. Hyliard Explains")
        
        with st.expander("**Orbital Service Vehicle**"):
            st.write("A spacecraft designed to provide services to other satellites while in orbit around Earth.")
        
        with st.expander("**Vigoride-7**"):
            st.write("The name of Momentus's upcoming mission that will test the 3D-printed fuel tank in actual space conditions.")
            dr_hyliard_says("This mission will prove the technology works in space. If successful (and I believe it will be), this opens the floodgates!", 
                           "💡 Dr. Hyliard Explains")
        
        st.markdown("---")
        st.markdown("### 💡 Discussion Prompt")
        st.info("Why do you think a 3D-printed fuel tank would be cheaper and faster to produce than a traditional fuel tank?")
        
        if st.button("Show Answer + Dr. Hyliard's Thoughts"):
            st.success("""
            3D printing builds the tank layer by layer from a digital design, which means:
            - No need for expensive molds or tools
            - Less material waste
            - Can create complex shapes in one piece
            - Automated process = faster production
            - Easy to modify designs
            """)
            dr_hyliard_says("""
            I'll add one more thing: with traditional manufacturing, if you discover a design flaw, you might have 
            to scrap weeks of work and start over. With 3D printing, you just update the computer file and print 
            a new one. I've seen this save missions that would have otherwise been delayed by months!
            """, "✏️ Dr. Hyliard Adds")

def show_objectives():
    st.markdown('<div class="main-header">🎯 Learning Objectives</div>', unsafe_allow_html=True)
    
    dr_hyliard_says("""
    Before we dive into the technical details, let me tell you what I hope you'll take away from this lesson. 
    These aren't just abstract learning goals - they're the building blocks of understanding how we study and 
    protect our planet from space.
    """, "🎯 Dr. Hyliard's Learning Goals")
    
    st.markdown("## By the end of this lesson, you will be able to:")
    
    objectives = [
        {
            "icon": "🛰️",
            "title": "Explain Satellite Contributions",
            "description": "Understand how satellites contribute to Earth Science research and environmental monitoring",
            "examples": ["Hurricane tracking", "Climate monitoring", "Deforestation detection"],
            "hyliard_note": "Last week, I used satellite data to track three different wildfires across the western US. Without satellites, we'd be flying planes over every fire - expensive, dangerous, and slow. Satellites do it better!"
        },
        {
            "icon": "🖨️",
            "title": "Describe 3D Printing Technology",
            "description": "Explain how additive manufacturing is advancing space technology",
            "examples": ["Faster production", "Complex designs", "Lower costs"],
            "hyliard_note": "I've held both traditional and 3D-printed fuel tanks. The 3D-printed one had internal structures that would be impossible to create any other way. It's not just about cost - it's about making better designs possible."
        },
        {
            "icon": "🔬",
            "title": "Analyze Technology-Science Connection",
            "description": "Understand how technological innovation drives scientific discovery",
            "examples": ["Better tools → Better data", "More satellites → Better coverage", "Innovation enables research"],
            "hyliard_note": "When Galileo invented the telescope, he didn't just improve astronomy - he revolutionized it. That's what 3D printing is doing for satellite technology right now. We're living through a revolution!"
        },
        {
            "icon": "🏢",
            "title": "Evaluate Commercial Space",
            "description": "Assess the role of commercial space companies in Earth observation",
            "examples": ["Competition drives innovation", "Reduces costs", "Increases accessibility"],
            "hyliard_note": "When I started my career, only governments could afford satellites. Now? Universities, research groups, even high schools are launching satellites. That's the power of commercial innovation."
        }
    ]
    
    for obj in objectives:
        with st.expander(f"{obj['icon']} {obj['title']}", expanded=True):
            st.write(f"**Learning Goal:** {obj['description']}")
            st.write("**Examples:**")
            for example in obj['examples']:
                st.write(f"- {example}")
            
            dr_hyliard_says(obj['hyliard_note'], "💭 Dr. Hyliard's Experience")
    
    st.markdown("---")
    st.markdown("## 📊 NGSS Standards Alignment")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **HS-ESS3-1**
        
        Construct explanations based on evidence for how natural resources, hazards, 
        and climate changes influence human activity
        """)
    
    with col2:
        st.markdown("""
        **HS-ETS1-3**
        
        Evaluate solutions to complex real-world problems based on prioritized 
        criteria and trade-offs
        """)
    
    with col3:
        st.markdown("""
        **HS-ESS2-4**
        
        Use models to describe variations in energy flow and their effects on 
        Earth's climate systems
        """)

def show_satellites():
    st.markdown('<div class="main-header">🌍 Satellites & Earth Science</div>', unsafe_allow_html=True)
    
    st.markdown("## Why Satellites Matter")
    
    dr_hyliard_says("""
    Let me show you what I see every day at work. These are the four main systems I monitor using satellites. 
    Each one tells us something crucial about our planet's health. Click through the tabs and I'll explain 
    what we're looking for and why it matters.
    """, "👁️ Through Dr. Hyliard's Eyes")
    
    st.info("""
    Satellites give us the **only way** to see our entire planet at once. They provide a "bird's eye view" 
    that helps us understand Earth's complex systems and how they're changing.
    """)
    
    # Interactive tabs for different satellite types
    tab1, tab2, tab3, tab4 = st.tabs(["🌤️ Atmosphere", "🌊 Oceans", "🌲 Land", "🧊 Ice & Snow"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### Atmospheric Monitoring")
            st.write("""
            Satellites constantly monitor Earth's atmosphere to track:
            - **Temperature** at different altitudes
            - **Humidity** and precipitation
            - **Air pressure** systems
            - **Atmospheric gases** (CO₂, methane, ozone)
            - **Cloud patterns** and movement
            """)
            
            st.markdown("#### Real-World Applications:")
            st.success("✅ Weather forecasting\n\n✅ Climate change tracking\n\n✅ Air quality monitoring\n\n✅ Hurricane prediction")
            
            dr_hyliard_says("""
            Three days ago, I watched Hurricane data come in live. We could see it strengthen from a tropical 
            storm to a Category 3 hurricane in just 18 hours. That early warning gave coastal communities 
            time to evacuate. In the 1900 Galveston hurricane, 8,000 people died because they had no warning. 
            Today, with satellites, that would never happen.
            """, "📖 Dr. Hyliard's Recent Example")
        
        with col2:
            st.image("https://via.placeholder.com/400x300/42A5F5/FFFFFF?text=Weather+Satellite", 
                     caption="Weather satellite monitoring hurricanes")
            
            st.metric("Active Weather Satellites", "~400", "globally")
    
    with tab2:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### Ocean Observation")
            st.write("""
            Satellites help us understand ocean systems by measuring:
            - **Sea surface temperature**
            - **Sea level height** (tracking rise over time)
            - **Ocean currents** and circulation
            - **Ocean color** (indicates phytoplankton/health)
            - **Ice coverage** and thickness
            """)
            
            st.markdown("#### Real-World Applications:")
            st.success("✅ Tracking sea level rise\n\n✅ Monitoring ocean health\n\n✅ Predicting El Niño events\n\n✅ Protecting marine ecosystems")
            
            dr_hyliard_says("""
            The ocean covers 70% of Earth's surface. Without satellites, we'd need thousands of ships taking 
            measurements 24/7. Even then, we'd miss most of it. Satellites let us see the ENTIRE ocean every day. 
            
            Last year, we detected an unusual warming pattern in the Pacific that predicted an El Niño event 
            three months before it happened. Farmers in Peru used that information to prepare for flooding. 
            That's the power of satellite data!
            """, "🌊 Dr. Hyliard's Ocean Story")
        
        with col2:
            st.image("https://via.placeholder.com/400x300/0277BD/FFFFFF?text=Ocean+Monitoring", 
                     caption="Satellite measuring ocean temperatures")
            
            st.metric("Sea Level Rise Since 1993", "+100mm", "≈4 inches")
    
    with tab3:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### Land Surface Monitoring")
            st.write("""
            Satellites track changes on Earth's land surface:
            - **Vegetation health** (forests, crops, grasslands)
            - **Deforestation** and logging
            - **Urban growth** and development
            - **Agricultural** productivity
            - **Wildfires** and burn scars
            """)
            
            st.markdown("#### Real-World Applications:")
            st.success("✅ Tracking deforestation\n\n✅ Monitoring crop health\n\n✅ Wildfire detection\n\n✅ Urban planning")
            
            dr_hyliard_says("""
            Here's something that breaks my heart but also shows why this work matters: I can pull up satellite 
            images of the Amazon rainforest from 2000 and compare them to today. The difference is staggering. 
            
            But here's the hopeful part - by tracking deforestation in real-time, we can alert authorities 
            immediately. In some cases, we've helped catch illegal logging operations within days of them starting. 
            Without satellites, it might take months to discover.
            """, "🌲 Dr. Hyliard's Forest Watch")
        
        with col2:
            st.image("https://via.placeholder.com/400x300/66BB6A/FFFFFF?text=Land+Monitoring", 
                     caption="Satellite tracking deforestation")
            
            st.metric("Forest Lost Since 2000", "10%", "of global forests")
    
    with tab4:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### Ice & Snow (Cryosphere)")
            st.write("""
            Satellites monitor frozen parts of Earth:
            - **Glacier movement** and retreat
            - **Ice sheet thickness** in Antarctica/Greenland
            - **Sea ice extent** in Arctic/Antarctic
            - **Snow cover** and depth
            - **Permafrost** changes
            """)
            
            st.markdown("#### Real-World Applications:")
            st.success("✅ Tracking polar ice melt\n\n✅ Predicting sea level rise\n\n✅ Understanding climate feedback\n\n✅ Water resource planning")
            
            dr_hyliard_says("""
            This is the part that keeps me up at night - and it's why I'm so passionate about getting MORE 
            satellites up there faster. 
            
            The Arctic is warming twice as fast as the rest of the planet. I compare satellite images from 
            when I started my career to today, and the ice loss is shocking. But we need MORE data, MORE 
            frequently, from MORE angles. That's why 3D-printed satellites are so important. We can finally 
            afford to build the comprehensive monitoring system the Arctic desperately needs.
            """, "🧊 Dr. Hyliard's Urgent Mission")
        
        with col2:
            st.image("https://via.placeholder.com/400x300/E1F5FE/000000?text=Ice+Monitoring", 
                     caption="Satellite measuring ice sheet thickness")
            
            st.metric("Arctic Ice Loss", "-13%", "per decade since 1979")
    
    # Interactive quiz
    st.markdown("---")
    st.markdown("## 🧠 Quick Check")
    
    question = st.radio(
        "Which of these can satellites NOT do?",
        ["Measure ocean temperature", "Predict earthquakes before they happen", 
         "Track deforestation", "Monitor air quality"]
    )
    
    if st.button("Check Answer"):
        if question == "Predict earthquakes before they happen":
            st.success("✅ Correct! Satellites cannot predict earthquakes before they happen. While they can measure ground movement AFTER earthquakes occur, we don't yet have technology to predict them in advance.")
            dr_hyliard_says("""
            Good catch! This is actually something I get asked about a lot. Satellites are amazing, but they're 
            not magic. We can measure ground deformation after earthquakes, which helps us understand them better. 
            But predicting WHEN and WHERE an earthquake will happen? That's still beyond our current technology - 
            satellite or otherwise. Maybe one of you students will figure it out someday!
            """, "👍 Dr. Hyliard Confirms")
        else:
            st.error("❌ Try again! Satellites CAN do this. Think about what requires advance knowledge we don't have yet.")
            dr_hyliard_says("Think about it this way: satellites are great at measuring things that are happening or have happened. But predicting the future? That's much harder!", "💡 Hint from Dr. Hyliard")

def show_3d_printing():
    st.markdown('<div class="main-header">🖨️ 3D Printing Innovation</div>', unsafe_allow_html=True)
    
    st.markdown("## The Momentus Innovation: 3D-Printed Fuel Tanks")
    
    dr_hyliard_says("""
    Okay, this is where it gets really exciting for me. Let me show you the difference between how we USED 
    to make fuel tanks and how we make them NOW. The contrast is mind-blowing!
    """, "🎉 Dr. Hyliard's Favorite Topic")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔧 Traditional Manufacturing")
        st.markdown("""
        <div class="warning-box">
        <h4>Old Way: Cut, Weld, Assemble</h4>
        
        ❌ **Expensive**: $100,000+ per tank
        
        ❌ **Slow**: Takes months to produce
        
        ❌ **Heavy**: More weight = higher launch costs
        
        ❌ **Limited**: Simple designs only
        
        ❌ **Wasteful**: Lots of material waste
        
        ❌ **Inflexible**: Hard to make changes
        </div>
        """, unsafe_allow_html=True)
        
        st.image("https://via.placeholder.com/400x300/FF9800/FFFFFF?text=Traditional+Manufacturing", 
                 caption="Traditional tank manufacturing process")
        
        dr_hyliard_says("""
        I've waited 6 months for a fuel tank before. SIX MONTHS. And if we found a design flaw during testing? 
        Start over. Another 6 months. It was incredibly frustrating. Every delay meant more time before we 
        could launch and start collecting crucial climate data.
        """, "😤 Dr. Hyliard's Frustration")
    
    with col2:
        st.markdown("### 🖨️ 3D Printing (Additive Manufacturing)")
        st.markdown("""
        <div class="success-box">
        <h4>New Way: Print Layer by Layer</h4>
        
        ✅ **Affordable**: Much lower cost
        
        ✅ **Fast**: Weeks instead of months
        
        ✅ **Lightweight**: Optimized designs
        
        ✅ **Complex**: Any design possible
        
        ✅ **Efficient**: Minimal waste
        
        ✅ **Flexible**: Easy design changes
        </div>
        """, unsafe_allow_html=True)
        
        st.image("https://via.placeholder.com/400x300/4CAF50/FFFFFF?text=3D+Printing", 
                 caption="3D printing metal fuel tank")
        
        dr_hyliard_says("""
        The first time I held a 3D-printed fuel tank, I couldn't believe it was real. It was lighter, 
        stronger, and more intricate than anything we could make before. And it took 3 weeks to make instead 
        of 6 months. I literally jumped up and down with excitement. My colleagues thought I was crazy!
        """, "🤩 Dr. Hyliard's First Impression")
    
    st.markdown("---")
    st.markdown("## 🔍 How Does 3D Printing Work?")
    
    st.info("""
    **Step-by-step process:**
    
    1. **Design** the tank on a computer using CAD software
    2. **Slice** the design into thousands of thin layers
    3. **Print** layer by layer using metal powder and lasers
    4. **Fuse** each layer to the one below it
    5. **Build** up the entire tank from bottom to top
    6. **Finish** with post-processing (cleaning, polishing)
    """)
    
    dr_hyliard_says("""
    Think of it like building with LEGO blocks, except each "block" is a layer of metal thinner than a human 
    hair, and instead of your hands stacking them, it's a laser melting metal powder. Layer by layer, hour 
    by hour, a fuel tank emerges from a bed of powder. It's honestly like watching magic happen.
    
    I've stood and watched the printer work. It's mesmerizing. You see nothing but powder, then slowly a 
    shape starts to emerge. After 20 hours, you've got a complete fuel tank that would have taken traditional 
    manufacturing 6 months to make!
    """, "🔬 Dr. Hyliard Explains the Process")
    
    # Interactive comparison
    st.markdown("---")
    st.markdown("## 💰 Cost Comparison Calculator")
    
    st.write("See how 3D printing saves money on a satellite mission:")
    
    dr_hyliard_says("""
    Okay, this is MY favorite part. Play around with the slider below and watch how the savings add up. 
    This is REAL data from actual satellite missions. This isn't theoretical - this is what we're experiencing 
    right now!
    """, "📊 Dr. Hyliard's Favorite Tool")
    
    num_satellites = st.slider("How many satellites in your mission?", 1, 50, 10)
    
    traditional_cost = num_satellites * 150000  # $150k per tank
    printing_cost = num_satellites * 30000  # $30k per tank
    savings = traditional_cost - printing_cost
    savings_percent = (savings / traditional_cost) * 100
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Traditional Cost", f"${traditional_cost:,}", 
                 help="Based on $150,000 per fuel tank")
    
    with col2:
        st.metric("3D Printing Cost", f"${printing_cost:,}", 
                 help="Based on $30,000 per fuel tank")
    
    with col3:
        st.metric("Savings", f"${savings:,}", f"-{savings_percent:.0f}%")
    
    st.success(f"💡 With 3D printing, you save **${savings:,}** on this mission! That's enough to launch {int(savings/printing_cost)} additional satellites!")
    
    dr_hyliard_says(f"""
    Look at that! ${savings:,} saved! Do you know what I could do with that money? 
    
    - Launch {int(savings/printing_cost)} more satellites
    - Hire {int(savings/80000)} more scientists for a year
    - Fund {int(savings/50000)} graduate students' research
    - Buy {int(savings/5000)} high-end computers for data analysis
    
    Every dollar saved is a dollar we can invest in better science. That's why I get so excited about this technology!
    """, "💵 What Dr. Hyliard Could Do With the Savings")
    
    # The connection to Earth Science
    st.markdown("---")
    st.markdown("## 🔗 Why This Matters for Earth Science")
    
    st.markdown("""
    ### The Innovation Chain Reaction:
    """)
    
    flow_col1, flow_col2, flow_col3, flow_col4, flow_col5 = st.columns(5)
    
    with flow_col1:
        st.markdown("""
        <div class="info-box" style="text-align: center;">
        <h3>🖨️</h3>
        <p><strong>3D Printing</strong></p>
        <p style="font-size: 0.9em;">New technology</p>
        </div>
        """, unsafe_allow_html=True)
    
    with flow_col2:
        st.markdown("""
        <div class="info-box" style="text-align: center;">
        <h3>💰</h3>
        <p><strong>Lower Costs</strong></p>
        <p style="font-size: 0.9em;">Cheaper satellites</p>
        </div>
        """, unsafe_allow_html=True)
    
    with flow_col3:
        st.markdown("""
        <div class="info-box" style="text-align: center;">
        <h3>🚀</h3>
        <p><strong>More Launches</strong></p>
        <p style="font-size: 0.9em;">More satellites</p>
        </div>
        """, unsafe_allow_html=True)
    
    with flow_col4:
        st.markdown("""
        <div class="info-box" style="text-align: center;">
        <h3>🌍</h3>
        <p><strong>Better Coverage</strong></p>
        <p style="font-size: 0.9em;">More data</p>
        </div>
        """, unsafe_allow_html=True)
    
    with flow_col5:
        st.markdown("""
        <div class="info-box" style="text-align: center;">
        <h3>🔬</h3>
        <p><strong>Better Science</strong></p>
        <p style="font-size: 0.9em;">Understanding Earth</p>
        </div>
        """, unsafe_allow_html=True)
    
    dr_hyliard_says("""
    This chain reaction is exactly why I'm so optimistic about the future. Each link in this chain makes 
    the next one possible. 
    
    Better technology → Lower costs → More satellites → Better data → Better science → Better decisions → 
    Better protection for our planet
    
    And it all starts with a 3D printer in a lab somewhere, printing metal layer by layer. Who would have 
    thought that a manufacturing technique could help us save the planet? But that's exactly what's happening!
    """, "🔗 Dr. Hyliard Connects the Dots")

def show_design_challenge():
    st.markdown('<div class="main-header">🎨 Design Challenge</div>', unsafe_allow_html=True)
    
    st.markdown("## 🚀 Design Your Own Satellite Mission!")
    
    dr_hyliard_says("""
    Alright, this is where YOU become the satellite engineer! I'm going to give you the same challenge I give 
    my graduate students: design a satellite mission to solve a real Earth Science problem.
    
    Think carefully about what you want to measure, why it matters, and how 3D printing makes your mission 
    possible. I'll be here to guide you through the process. Let's build something amazing together!
    """, "🎓 Dr. Hyliard's Challenge to You")
    
    st.info("""
    **Your Task:** You are a satellite engineer! Design a satellite mission to solve an Earth Science problem. 
    Consider what you'll measure, how many satellites you need, and how 3D printing technology will help.
    """)
    
    # Select scenario
    st.markdown("### Step 1: Choose Your Mission Type")
    
    scenarios = {
        "🌀 Hurricane Monitoring": {
            "description": "Track and predict hurricanes in the Atlantic Ocean",
            "measures": ["Wind speed", "Air pressure", "Sea surface temperature", "Cloud patterns"],
            "challenges": "Hurricanes move fast and need constant monitoring",
            "hyliard_story": """
            I worked on a hurricane monitoring mission in 2017. We tracked Hurricane Irma in real-time as it 
            strengthened to Category 5. Our data helped meteorologists predict its path with 95% accuracy 
            five days in advance. Millions of people evacuated safely because of that early warning. This kind 
            of mission saves lives!
            """
        },
        "🧊 Arctic Ice Monitoring": {
            "description": "Monitor polar ice cap melting and thickness",
            "measures": ["Ice thickness", "Ice extent", "Surface temperature", "Glacier movement"],
            "challenges": "Polar regions are remote and changing rapidly",
            "hyliard_story": """
            This is actually MY current project! The Arctic is warming faster than anywhere else on Earth. 
            I need a constellation of satellites providing continuous coverage because ice can change 
            dramatically in just days. With 3D-printed components, I can finally afford the 12 satellites 
            I need instead of just 3!
            """
        },
        "🔥 Wildfire Detection": {
            "description": "Detect and monitor wildfires worldwide",
            "measures": ["Heat signatures", "Smoke detection", "Vegetation dryness", "Fire spread"],
            "challenges": "Fires can start quickly and spread unpredictably",
            "hyliard_story": """
            Last summer, I used satellite data to track 17 different wildfires simultaneously across California, 
            Oregon, and Washington. We detected two of them within 15 minutes of ignition - before any 911 
            calls came in! Early detection means firefighters can respond faster and save more homes and lives.
            """
        },
        "🌊 Ocean Temperature": {
            "description": "Track ocean temperature changes globally",
            "measures": ["Sea surface temp", "Ocean currents", "Heat absorption", "El Niño patterns"],
            "challenges": "Oceans cover 70% of Earth and change slowly",
            "hyliard_story": """
            The ocean is Earth's climate regulator. It absorbs 90% of excess heat from climate change. I monitor 
            ocean temperatures daily because small changes can have huge impacts. A 2°C increase in Pacific 
            Ocean temperature can trigger droughts in Australia and floods in Peru. Understanding ocean 
            temperature helps us predict these events!
            """
        }
    }
    
    mission_type = st.selectbox("Select your mission:", list(scenarios.keys()))
    
    with st.expander("📋 Mission Details + Dr. Hyliard's Experience"):
        st.write(f"**Goal:** {scenarios[mission_type]['description']}")
        st.write(f"**Challenge:** {scenarios[mission_type]['challenges']}")
        st.write("**Suggested Measurements:**")
        for measure in scenarios[mission_type]['measures']:
            st.write(f"- {measure}")
        
        dr_hyliard_says(scenarios[mission_type]['hyliard_story'], "📖 Dr. Hyliard's Story")
    
    st.markdown("---")
    st.markdown("### Step 2: Design Your Mission")
    
    with st.form("mission_design"):
        col1, col2 = st.columns(2)
        
        with col1:
            mission_name = st.text_input("Mission Name:", placeholder="e.g., EarthWatch-1")
            
            mission_goal = st.text_area("Primary Goal:", 
                                       placeholder="What specific problem will your mission solve?",
                                       height=100)
            
            measurements = st.multiselect(
                "What will your satellites measure?",
                scenarios[mission_type]['measures'] + ["Other"],
                default=scenarios[mission_type]['measures'][:2]
            )
            
            if "Other" in measurements:
                other_measure = st.text_input("Specify other measurements:")
        
        with col2:
            num_satellites = st.number_input("How many satellites?", min_value=1, max_value=100, value=5,
                                            help="Consider global coverage needs")
            
            orbit_type = st.radio(
                "Orbit Type:",
                ["Low Earth Orbit (detailed images)", 
                 "Geostationary (stays over one spot)",
                 "Polar Orbit (covers whole Earth)"]
            )
            
            coverage_area = st.selectbox(
                "Coverage Area:",
                ["Global", "Northern Hemisphere", "Southern Hemisphere", 
                 "Tropical Regions", "Polar Regions", "Specific Region"]
            )
        
        st.markdown("### Step 3: 3D Printing Benefits")
        
        printing_benefits = st.multiselect(
            "How will 3D printing help your mission?",
            ["Reduce overall mission cost",
             "Launch more satellites with same budget",
             "Create custom tank designs for specific needs",
             "Faster deployment to respond to emerging issues",
             "Replace failed satellites quickly"],
            default=["Reduce overall mission cost"]
        )
        
        impact = st.text_area("How will your satellite data help Earth scientists?",
                             placeholder="Explain the scientific impact of your mission...",
                             height=100)
        
        submitted = st.form_submit_button("🚀 Submit Mission Design for Dr. Hyliard's Review")
    
    if submitted:
        st.session_state.activity_submitted = True
        
        st.balloons()
        
        st.success("## 🎉 Mission Design Complete!")
        
        # Dr. Hyliard reviews the mission
        dr_hyliard_says(f"""
        Excellent work! Let me review your mission design for **{mission_name}**...
        
        **Mission Type:** {mission_type} - Great choice! This is an area where we really need more data.
        
        **Number of Satellites:** {num_satellites} - {'Perfect! That should give you good coverage.' if num_satellites >= 5 else 'Good start, but you might want to consider a few more for better coverage.'}
        
        **Orbit:** {orbit_type} - {'Excellent choice for this mission type!' if 'Polar' in orbit_type and 'Arctic' in mission_type else 'Interesting choice! Make sure this orbit supports your goals.'}
        
        Overall, I'm impressed! {'With 3D-printed components, this mission is absolutely feasible.' if num_satellites <= 20 else 'This is ambitious, but with 3D printing making satellites cheaper, it might just work!'}
        
        I'd love to see this mission become reality. Want to join my research team someday? 😊
        """, "📋 Dr. Hyliard's Mission Review")
        
        # Display mission summary
        st.markdown("### 📊 Your Mission Summary")
        
        summary_col1, summary_col2 = st.columns(2)
        
        with summary_col1:
            st.markdown(f"""
            <div class="info-box">
            <h4>{mission_name}</h4>
            <p><strong>Type:</strong> {mission_type}</p>
            <p><strong>Goal:</strong> {mission_goal}</p>
            <p><strong>Satellites:</strong> {num_satellites}</p>
            <p><strong>Orbit:</strong> {orbit_type}</p>
            <p><strong>Coverage:</strong> {coverage_area}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with summary_col2:
            st.markdown("""
            <div class="success-box">
            <h4>Cost Analysis</h4>
            """, unsafe_allow_html=True)
            
            traditional_cost = num_satellites * 150000
            printing_cost = num_satellites * 30000
            savings = traditional_cost - printing_cost
            
            st.metric("Total Mission Cost (3D Printing)", f"${printing_cost:,}")
            st.metric("Savings vs Traditional", f"${savings:,}", f"-{((savings/traditional_cost)*100):.0f}%")
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown(f"""
        **Measurements:** {', '.join(measurements)}
        
        **3D Printing Benefits:** {', '.join(printing_benefits)}
        
        **Scientific Impact:** {impact}
        """)
        
        # Download option
        if st.button("📥 Download Mission Plan (Dr. Hyliard Approved!)"):
            mission_report = f"""
# SATELLITE MISSION PLAN: {mission_name}
## Reviewed and Approved by Dr. Marcus Hyliard

## Mission Overview
- **Type:** {mission_type}
- **Goal:** {mission_goal}
- **Coverage Area:** {coverage_area}

## Technical Specifications
- **Number of Satellites:** {num_satellites}
- **Orbit Type:** {orbit_type}
- **Measurements:** {', '.join(measurements)}

## Cost Analysis
- **Traditional Manufacturing Cost:** ${traditional_cost:,}
- **3D Printing Cost:** ${printing_cost:,}
- **Total Savings:** ${savings:,} ({((savings/traditional_cost)*100):.0f}%)

## 3D Printing Benefits
{chr(10).join(['- ' + benefit for benefit in printing_benefits])}

## Scientific Impact
{impact}

## Dr. Hyliard's Comments
"{'Excellent mission design! This addresses a critical need in Earth observation.' if num_satellites >= 5 else 'Good start! Consider expanding the satellite constellation for better coverage.'} 
The use of 3D-printed components makes this mission economically feasible. 
I would be proud to work on this mission!"

---
*Created using Space Technology & Earth Science Interactive Lesson*
*Date: {datetime.now().strftime('%Y-%m-%d')}*
*Reviewed by: Dr. Marcus Hyliard, Senior Satellite Engineer*
"""
            st.download_button(
                label="Download Mission Report",
                data=mission_report,
                file_name=f"{mission_name.replace(' ', '_')}_mission_plan.txt",
                mime="text/plain"
            )

def show_quiz():
    st.markdown('<div class="main-header">❓ Quiz & Assessment</div>', unsafe_allow_html=True)
    
    st.markdown("## 🧠 Test Your Knowledge")
    
    dr_hyliard_says("""
    Alright, let's see what you've learned! I'm not grading you on this - I just want to see if I explained 
    things clearly. If you get something wrong, that's on me as a teacher, not on you as a student. 
    Let's do this together!
    """, "📝 Dr. Hyliard's Quiz Introduction")
    
    st.info("Answer these questions to check your understanding of the lesson!")
    
    # Quiz questions
    questions = [
        {
            "q": "What is additive manufacturing?",
            "options": [
                "Adding chemicals to manufacturing processes",
                "Building objects layer by layer (3D printing)",
                "Adding more workers to a factory",
                "Manufacturing in addition to other activities"
            ],
            "correct": 1,
            "explanation": "Additive manufacturing is the process of building objects layer by layer, also known as 3D printing. It 'adds' material layer by layer instead of cutting it away.",
            "hyliard_comment": "Perfect! It's called 'additive' because we ADD material layer by layer, unlike traditional manufacturing where we START with a block and CUT AWAY material. Much less wasteful!"
        },
        {
            "q": "Why are fuel tanks important for satellites?",
            "options": [
                "They store electricity for the satellite",
                "They hold propellant for adjusting the satellite's position",
                "They protect the satellite from radiation",
                "They store data collected by the satellite"
            ],
            "correct": 1,
            "explanation": "Fuel tanks hold propellant that allows satellites to make small adjustments to their position and orientation in space. Without fuel, satellites would drift out of position.",
            "hyliard_comment": "Exactly right! Without fuel, a satellite would slowly drift out of its orbit due to tiny forces like solar radiation pressure and Earth's irregular gravity. I've seen satellites run out of fuel - they become useless space junk. That's why fuel tanks are SO critical!"
        },
        {
            "q": "What is a major advantage of 3D printing fuel tanks compared to traditional manufacturing?",
            "options": [
                "They work better in space",
                "They are prettier",
                "They are much faster and cheaper to produce",
                "They last longer"
            ],
            "correct": 2,
            "explanation": "3D printing can reduce production time from months to weeks and significantly lower costs, making satellite missions more affordable and accessible.",
            "hyliard_comment": "YES! Time and money - those are the game-changers. I used to wait 6 months for a fuel tank. Now? 3 weeks. That means I can launch satellites 5 times faster and with my budget, I can launch 5 times as many. Mathematics of innovation!"
        },
        {
            "q": "How do cheaper satellites help Earth Science?",
            "options": [
                "Scientists can buy more telescopes",
                "More satellites can be launched, providing better Earth coverage and data",
                "It makes satellites easier to control",
                "Cheaper satellites use less electricity"
            ],
            "correct": 1,
            "explanation": "When satellites are more affordable, more can be launched. More satellites means better coverage of Earth, more frequent measurements, and more accurate scientific data.",
            "hyliard_comment": "This is THE key insight! More satellites = more data = better science. It's that simple. When I started my career, we had gaps in our satellite coverage. Sometimes we'd miss important events because no satellite was watching that part of Earth. With cheaper satellites, we can eliminate those gaps!"
        },
        {
            "q": "Which of these do satellites help us monitor?",
            "options": [
                "Only weather patterns",
                "Only ocean temperatures",
                "Weather, climate, oceans, land use, and ice coverage",
                "Only natural disasters"
            ],
            "correct": 2,
            "explanation": "Satellites are versatile tools that help us monitor many Earth systems including atmosphere, oceans, land surface, ice and snow, and much more.",
            "hyliard_comment": "Satellites are the Swiss Army knives of Earth observation! I use the same satellite network to track hurricanes, monitor Arctic ice, detect wildfires, and measure ocean temperatures - sometimes all in the same day! That's the beauty of comprehensive satellite coverage."
        }
    ]
    
    score = 0
    total = len(questions)
    
    for i, q in enumerate(questions):
        st.markdown(f"### Question {i+1}")
        answer = st.radio(q["q"], q["options"], key=f"q{i}")
        
        if st.button(f"Check Answer {i+1}", key=f"check{i}"):
            selected_index = q["options"].index(answer)
            if selected_index == q["correct"]:
                st.success(f"✅ Correct! {q['explanation']}")
                st.session_state.quiz_answers[i] = True
                
                # Dr. Hyliard's comment
                dr_hyliard_says(q['hyliard_comment'], "👏 Dr. Hyliard Celebrates")
            else:
                st.error(f"❌ Not quite. {q['explanation']}")
                st.session_state.quiz_answers[i] = False
                
                # Dr. Hyliard's encouragement
                dr_hyliard_says("No worries! This is how we learn. I got SO many things wrong when I was learning this stuff. The important thing is you're thinking about it. Try the other options and see if one makes more sense!", "💪 Dr. Hyliard Encourages You")
        
        st.markdown("---")
    
    # Calculate score
    if len(st.session_state.quiz_answers) == total:
        score = sum(st.session_state.quiz_answers.values())
        percentage = (score / total) * 100
        
        st.markdown("## 📊 Your Score")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Correct Answers", f"{score}/{total}")
        with col2:
            st.metric("Percentage", f"{percentage:.0f}%")
        with col3:
            if percentage >= 80:
                st.metric("Grade", "🌟 Excellent!")
            elif percentage >= 60:
                st.metric("Grade", "✅ Good!")
            else:
                st.metric("Grade", "📚 Keep Learning!")
        
        # Dr. Hyliard's final assessment
        if percentage >= 80:
            st.success("🎉 Great job! You have a strong understanding of how space technology helps Earth Science!")
            dr_hyliard_says(f"""
            Outstanding! You got {score} out of {total} correct - that's {percentage:.0f}%! 
            
            I'm genuinely impressed. You've grasped the key concepts: how satellites work, why 3D printing matters, 
            and how technology drives scientific discovery. If you were in my graduate program, I'd be very proud!
            
            Keep this curiosity alive. Whether you become a scientist, engineer, teacher, or anything else, 
            understanding how we study our planet will serve you well. The future of Earth observation is bright, 
            and people like you - people who GET IT - are going to be part of that future.
            
            Thank you for learning with me today! 🚀
            """, "🌟 Dr. Hyliard's Final Thoughts")
        elif percentage >= 60:
            st.info("👍 Good work! Review the material to strengthen your understanding.")
            dr_hyliard_says(f"""
            Good job! You got {score} out of {total} - that's solid! 
            
            You've got the main ideas down. Go back and review the sections where you weren't sure. Science 
            is all about iteration - getting better with each attempt. I review papers and make mistakes all 
            the time. What matters is that you keep learning.
            
            Take another look at the lesson, maybe talk to your teacher about questions you have, and try again. 
            I believe in you!
            """, "👍 Dr. Hyliard Encourages You")
        else:
            st.warning("📖 Keep studying! Review the lesson sections and try again.")
            dr_hyliard_says(f"""
            You got {score} out of {total}. That's okay! This is complex stuff. 
            
            Here's what I recommend: Go back through the lesson at your own pace. Don't rush. Click on the 
            sections that confused you and really take your time understanding them. Maybe take notes. Draw 
            diagrams. Whatever helps YOU learn best.
            
            I've taught hundreds of students, and I can tell you this: The students who struggle at first 
            but keep trying often end up understanding the material BETTER than students who get it right away. 
            Why? Because they really think deeply about it.
            
            Don't give up! The fact that you're here learning means you care. That's the most important thing.
            """, "💪 Dr. Hyliard Won't Give Up On You")
    
    # Exit ticket
    st.markdown("---")
    st.markdown("## 📝 Exit Ticket")
    
    st.write("Choose ONE prompt and write your response:")
    
    exit_prompt = st.radio(
        "Select a prompt:",
        [
            "A) Explain how 3D-printed fuel tanks could lead to better climate change monitoring",
            "B) Describe an Earth Science problem and how improved satellite technology could help",
            "C) Compare traditional manufacturing to 3D printing for space applications"
        ]
    )
    
    exit_response = st.text_area("Your response (5-7 sentences):", height=200,
                                placeholder="Write your thoughtful response here...")
    
    if st.button("Submit Exit Ticket to Dr. Hyliard"):
        if len(exit_response) > 50:
            st.success("✅ Exit ticket submitted! Great work today!")
            st.balloons()
            
            dr_hyliard_says("""
            Thank you for submitting your exit ticket! I wish I could read every single one personally. 
            
            Your teacher will review your response, but I want you to know something: The fact that you took 
            the time to think deeply about these questions means you're already thinking like a scientist. 
            
            That's what science is - asking questions, thinking about problems, and proposing solutions. 
            You did that today, and I'm proud of you for it.
            
            Keep looking up at the stars, but remember to look down at Earth too. Our planet needs curious, 
            thoughtful people like you to help protect it.
            
            Until next time! 🚀🌍
            
            — Dr. Marcus Hyliard
            """, "👋 Dr. Hyliard's Goodbye Message")
        else:
            st.warning("Please write a more detailed response (at least 5 sentences).")
            dr_hyliard_says("Take your time! I want to hear your thoughts. Even if you're not sure you're right, write what you're thinking. There's no wrong answer here - I just want to know what YOU learned today!", "✏️ Dr. Hyliard Wants More")

def show_resources():
    st.markdown('<div class="main-header">📚 Additional Resources</div>', unsafe_allow_html=True)
    
    st.markdown("## 🔗 Learn More")
    
    dr_hyliard_says("""
    Want to keep learning? Here are my favorite resources. These are websites and tools I actually use in 
    my work. No boring textbooks - just the cool stuff that will blow your mind!
    """, "🌐 Dr. Hyliard's Favorite Resources")
    
    # Current Media & Story Links
    st.markdown("---")
    st.markdown("## 📰 Current Media & News")
    
    col_media1, col_media2 = st.columns(2)
    
    with col_media1:
        st.markdown("""
        ### 🗞️ The Original Story
        
        **Momentus Develops 3D-Printed Fuel Tank**
        
        [📖 Read on Yahoo Finance](https://finance.yahoo.com/news/momentus-develops-additive-manufactured-fuel-133000052.html)
        
        This is the actual news story we've been discussing throughout this lesson! 
        Read the full article to see all the details about this breakthrough technology.
        """)
        
        dr_hyliard_says("""
        This is THE article that got me so excited! When this news broke, I immediately shared it with 
        my entire team. Click through and read the full story - there are more technical details that 
        will fascinate you if you're really into this stuff!
        """, "📰 The Story That Started It All")
    
    with col_media2:
        st.markdown("""
        ### 🎥 Related Video Content
        
        **Search for:**
        - "Momentus Vigoride mission" on YouTube
        - "Velo3D 3D printing satellites"
        - "Additive manufacturing aerospace"
        - "3D printed rocket components"
        
        These videos show the actual technology in action!
        """)
        
        dr_hyliard_says("""
        I love watching behind-the-scenes videos of this technology. Seeing the 3D printer build a fuel 
        tank layer by layer is mesmerizing. Search for "metal 3D printing timelapse" - you won't regret it!
        """, "🎬 Must-Watch Videos")
    
    st.markdown("---")
    st.markdown("## 📚 IXL Science Lessons (Interactive Practice)")
    
    st.info("""
    **IXL offers interactive science lessons that reinforce concepts from this lesson!**
    
    Visit [IXL.com](https://www.ixl.com/science) to practice these skills:
    """)
    
    col_ixl1, col_ixl2 = st.columns(2)
    
    with col_ixl1:
        st.markdown("""
        ### 🌍 Earth Science Skills
        
        **Recommended IXL Lessons:**
        
        - **Climate & Weather**
          - Analyze satellite weather data
          - Interpret climate graphs
          - Compare climate zones
        
        - **Earth's Systems**
          - How satellites monitor Earth
          - Remote sensing technology
          - Earth observation systems
        
        - **Natural Disasters**
          - Hurricane tracking and prediction
          - Using technology to monitor hazards
          - Early warning systems
        
        [🔗 Browse IXL Earth Science](https://www.ixl.com/science/earth-science)
        """)
    
    with col_ixl2:
        st.markdown("""
        ### 🔬 Engineering & Technology Skills
        
        **Recommended IXL Lessons:**
        
        - **Engineering Design**
          - Evaluate technological solutions
          - Design processes and iterations
          - Cost-benefit analysis
        
        - **Space Technology**
          - Satellites and orbital mechanics
          - Space exploration technology
          - Engineering challenges in space
        
        - **Materials Science**
          - Properties of materials
          - Manufacturing processes
          - Material innovations
        
        [🔗 Browse IXL Physical Science](https://www.ixl.com/science/physical-science)
        """)
    
    dr_hyliard_says("""
    IXL is fantastic for practice! I wish I had something like this when I was learning. The interactive 
    nature means you get immediate feedback, just like in a real lab. 
    
    I especially recommend their lessons on "Interpreting data from graphs and charts" - that's a skill 
    I use EVERY SINGLE DAY analyzing satellite data. The more you practice reading data, the better 
    scientist you'll become!
    
    **Pro tip:** Start with the Earth Science lessons on climate and weather, then move to the engineering 
    design lessons. That progression mirrors how we actually work in satellite engineering!
    """, "📖 Dr. Hyliard's IXL Recommendations")
    
    st.markdown("---")
    st.markdown("## 🎓 Additional Educational Platforms")
    
    col_edu1, col_edu2, col_edu3 = st.columns(3)
    
    with col_edu1:
        st.markdown("""
        **Khan Academy**
        
        [Science Courses](https://www.khanacademy.org/science)
        
        - Physics (orbital mechanics)
        - Climate science
        - Engineering principles
        
        *Free video lessons & practice*
        """)
    
    with col_edu2:
        st.markdown("""
        **Crash Course**
        
        [YouTube Channel](https://www.youtube.com/user/crashcourse)
        
        - Engineering series
        - Physics series
        - Climate & energy
        
        *Engaging video content*
        """)
    
    with col_edu3:
        st.markdown("""
        **MIT OpenCourseWare**
        
        [Free Courses](https://ocw.mit.edu/)
        
        - Aerospace Engineering
        - Earth Science
        - Advanced topics
        
        *College-level content*
        """)
    
    # Organized resources by category
    st.markdown("---")
    st.markdown("## 🌐 Professional Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌍 Earth Observation")
        
        with st.expander("NASA Earth Observatory"):
            st.write("""
            **Website:** https://earthobservatory.nasa.gov/
            
            Features stunning satellite images and explanations of Earth science phenomena. 
            Perfect for exploring real examples of satellite data in action.
            
            **Best for:** Visual learners, current events, image galleries
            """)
            
            dr_hyliard_says("I check this website almost every day! The 'Image of the Day' feature is incredible. Last week they showed before/after images of a glacier in Alaska - you could see 30 years of melting in just two pictures. Powerful stuff!", "⭐ Dr. Hyliard's Pick")
        
        with st.expander("NOAA Satellites"):
            st.write("""
            **Website:** https://www.noaa.gov/satellites
            
            Information about weather and climate satellites operated by the National Oceanic 
            and Atmospheric Administration.
            
            **Best for:** Weather and ocean data, real-time satellite views
            """)
            
            dr_hyliard_says("NOAA's satellites are the workhorses of weather forecasting. Every weather report you see on TV uses NOAA data. Their website lets you see the same real-time satellite views that meteorologists use!", "⭐ Dr. Hyliard's Pick")
        
        with st.expander("ESA Earth Observation"):
            st.write("""
            **Website:** https://www.esa.int/Applications/Observing_the_Earth
            
            European Space Agency's Earth observation program with interactive tools and 
            educational resources.
            
            **Best for:** International perspective, educational activities
            """)
            
            dr_hyliard_says("ESA has some of the most advanced Earth observation satellites in space. Their Sentinel program is AMAZING. If you want to see how Europeans approach Earth monitoring, this is the place!", "⭐ Dr. Hyliard's Pick")
    
    with col2:
        st.markdown("### 🚀 Space Technology")
        
        with st.expander("How 3D Printing Works"):
            st.write("""
            Learn about additive manufacturing technology and how it's revolutionizing 
            aerospace engineering.
            
            **Key Topics:**
            - Layer-by-layer fabrication
            - Metal 3D printing
            - Applications in space
            - Future possibilities
            """)
            
            dr_hyliard_says("If you want to see 3D printing in action, search YouTube for 'metal 3D printing timelapse'. Watching a fuel tank emerge from a bed of metal powder is mesmerizing. I've watched these videos dozens of times!", "⭐ Dr. Hyliard's Pick")
        
        with st.expander("Satellite Tracking"):
            st.write("""
            **Website:** https://www.n2yo.com/
            
            Track satellites in real-time as they orbit Earth! See where satellites are 
            right now and when they'll pass over your location.
            
            **Best for:** Interactive learning, real-time data
            """)
            
            dr_hyliard_says("This is SO COOL. You can track the International Space Station, weather satellites, even spy satellites! I use this to know when my satellites are passing over interesting areas. Download their app - you can get notifications when the ISS is visible from your backyard!", "⭐ Dr. Hyliard's Favorite Tool")
        
        with st.expander("Career Exploration"):
            st.write("""
            **Careers Combining Space Technology & Earth Science:**
            
            - Aerospace Engineer
            - Satellite Data Analyst
            - Remote Sensing Specialist
            - Climate Scientist
            - GIS Specialist
            - Mission Operations Engineer
            - Environmental Consultant
            """)
            
            dr_hyliard_says("""
            Want to know the truth? We DESPERATELY need more people in these fields. There are more jobs 
            than qualified people to fill them. If you're interested in ANY of these careers, reach out to 
            universities, companies, or research labs. Many offer summer programs for high school students. 
            
            I mentor 5 high school students every summer. Could you be one of them someday?
            """, "💼 Dr. Hyliard on Careers")
    
    st.markdown("---")
    st.markdown("## 🎥 Recommended Videos")
    
    dr_hyliard_says("""
    These are videos I actually watch myself! Some are educational, some are just beautiful views of Earth. 
    All of them will give you a deeper appreciation for what satellites do.
    """, "🎬 Dr. Hyliard's Viewing List")
    
    video_col1, video_col2, video_col3 = st.columns(3)
    
    with video_col1:
        st.markdown("""
        <div class="info-box">
        <h4>How Satellites Track Climate</h4>
        <p>Understand how satellite data reveals climate change patterns</p>
        <p><em>Search YouTube: "NASA climate satellites"</em></p>
        </div>
        """, unsafe_allow_html=True)
        
        dr_hyliard_says("The NASA video 'A Year in the Life of Earth's CO2' is mind-blowing. You can literally SEE carbon dioxide moving around the planet. Watch it!", "🎥 Must-Watch")
    
    with video_col2:
        st.markdown("""
        <div class="info-box">
        <h4>3D Printing in Space</h4>
        <p>See how 3D printing technology works for aerospace applications</p>
        <p><em>Search YouTube: "metal 3D printing aerospace"</em></p>
        </div>
        """, unsafe_allow_html=True)
        
        dr_hyliard_says("Search for 'Velo3D Sapphire printer timelapse' - that's the exact printer that made the Momentus fuel tank we discussed today!", "🎥 Must-Watch")
    
    with video_col3:
        st.markdown("""
        <div class="info-box">
        <h4>A Day in Earth Orbit</h4>
        <p>Experience what satellites see as they orbit our planet</p>
        <p><em>Search YouTube: "ISS timelapse Earth"</em></p>
        </div>
        """, unsafe_allow_html=True)
        
        dr_hyliard_says("This is what I dream about at night. Seriously. The view of Earth from space never gets old. Watch this and you'll understand why I do what I do!", "🎥 Must-Watch")
    
    st.markdown("---")
    st.markdown("## 📖 Vocabulary Reference")
    
    vocab_df = pd.DataFrame({
        "Term": [
            "Additive Manufacturing",
            "Satellite",
            "Orbit",
            "Fuel Tank",
            "Orbital Service Vehicle",
            "Remote Sensing",
            "Commercial Space",
            "Payload"
        ],
        "Definition": [
            "Building objects layer by layer (3D printing)",
            "An object that orbits a planet",
            "The path an object takes around another object in space",
            "Container that holds propellant for spacecraft maneuvering",
            "A spacecraft designed to provide services to other satellites in orbit",
            "Gathering information about Earth from a distance",
            "Private companies involved in space activities",
            "The instruments and equipment a satellite carries"
        ]
    })
    
    st.dataframe(vocab_df, use_container_width=True, hide_index=True)
    
    dr_hyliard_says("""
    Pro tip: Don't just memorize these definitions. UNDERSTAND them. Ask yourself: "Why does this word exist? 
    What problem does this concept solve?" That's how you really learn science!
    """, "📚 Study Tip from Dr. Hyliard")
    
    st.markdown("---")
    st.markdown("## 🎙️ Podcasts & Audio Resources")
    
    col_pod1, col_pod2 = st.columns(2)
    
    with col_pod1:
        st.markdown("""
        ### Space & Technology Podcasts
        
        **Houston We Have a Podcast** (NASA)
        - Behind-the-scenes NASA stories
        - Interviews with engineers and scientists
        - Current space missions
        
        **Planetary Radio** (The Planetary Society)
        - Space exploration news
        - Interviews with planetary scientists
        - Weekly updates
        
        **SpacePod** (Various)
        - Commercial space industry news
        - Satellite technology updates
        - Launch schedules and analysis
        """)
    
    with col_pod2:
        st.markdown("""
        ### Climate & Earth Science Podcasts
        
        **Warm Regards** (Climate change)
        - Climate science explained
        - Expert interviews
        - Solutions and hope
        
        **Climate One** (Commonwealth Club)
        - Climate conversations
        - Policy and science
        - Solutions-focused
        
        **Science Friday** (NPR)
        - Weekly science news
        - Listener questions
        - Expert discussions
        """)
    
    dr_hyliard_says("""
    I listen to podcasts during my commute! "Houston We Have a Podcast" is fantastic - they once interviewed 
    the team that launched a satellite I worked on. Hearing the behind-the-scenes stories reminded me why 
    I love this work.
    
    And "Science Friday" is perfect for staying current. They covered the Momentus 3D-printing story we 
    discussed today within days of it happening!
    """, "🎧 Dr. Hyliard's Podcast Recommendations")
    
    st.markdown("---")
    st.markdown("## 📱 Follow Current Space News")
    
    col_news1, col_news2, col_news3 = st.columns(3)
    
    with col_news1:
        st.markdown("""
        **Space.com**
        [space.com](https://www.space.com)
        
        Daily space news, articles, and breaking stories about satellites, launches, and discoveries.
        """)
    
    with col_news2:
        st.markdown("""
        **SpaceNews**
        [spacenews.com](https://spacenews.com)
        
        Industry news, policy updates, commercial space developments.
        """)
    
    with col_news3:
        st.markdown("""
        **NASA News**
        [nasa.gov/news](https://www.nasa.gov/news)
        
        Official NASA updates, mission news, Earth science discoveries.
        """)
    
    dr_hyliard_says("""
    I check Space.com and SpaceNews almost every morning with my coffee. They're how I stay current on what 
    other teams are doing. The space industry moves FAST - new breakthroughs happen weekly!
    
    Sign up for their newsletters. You'll get the most important space news delivered to your inbox. That's 
    how I first learned about the Momentus 3D-printing announcement!
    """, "📰 Stay Updated Like Dr. Hyliard")
    
    st.markdown("---")
    st.markdown("## 🎮 Interactive Tools & Simulations")
    
    col_int1, col_int2 = st.columns(2)
    
    with col_int1:
        st.markdown("""
        ### Satellite & Orbit Simulations
        
        **NASA Eyes on the Earth**
        [eyes.nasa.gov](https://eyes.nasa.gov/apps/earth/)
        - Real-time 3D visualization
        - Track NASA satellites
        - See what they're observing
        - Interactive and beautiful!
        
        **Satellite Tracker (N2YO)**
        [n2yo.com](https://www.n2yo.com/)
        - Live satellite tracking
        - Predict passes over your location
        - ISS spotting
        - Mobile app available
        
        **Orbit Simulator**
        [orbitsimulator.com](https://www.orbitsimulator.com/)
        - Design your own orbits
        - Understand orbital mechanics
        - Physics visualization
        """)
    
    with col_int2:
        st.markdown("""
        ### Earth Observation Tools
        
        **NASA Worldview**
        [worldview.earthdata.nasa.gov](https://worldview.earthdata.nasa.gov/)
        - Real satellite imagery
        - Historical comparisons
        - Multiple data layers
        - Track events (fires, storms, etc.)
        
        **Google Earth Engine**
        [earthengine.google.com](https://earthengine.google.com/)
        - Analyze satellite data
        - Time-lapse features
        - Environmental monitoring
        - Advanced but powerful!
        
        **Climate Time Machine**
        [climate.nasa.gov/interactives/climate-time-machine](https://climate.nasa.gov/interactives/climate-time-machine)
        - Visualize climate change
        - See ice melt over time
        - Sea level changes
        - CO₂ concentrations
        """)
    
    dr_hyliard_says("""
    These tools are INCREDIBLE! NASA Eyes on the Earth is what I show people when they ask "what do you do?" 
    You can literally watch satellites orbiting in real-time and see what they're measuring at that exact moment.
    
    NASA Worldview is even better - it's the same tool WE use in our research! You can see the exact same 
    satellite imagery that scientists analyze. Want to track wildfires? See a hurricane from space? Watch 
    Arctic ice melt? It's all there, updated daily!
    
    And the Climate Time Machine... wow. It shows decades of change in seconds. It's powerful and, honestly, 
    a bit sobering. But it shows exactly WHY our work with satellites matters so much.
    
    **Challenge:** Download the N2YO app and set it to alert you when the ISS passes over your house. Then 
    go outside and WATCH IT. That bright dot moving across the sky? That's humans living in space, 270 miles 
    above you. It never gets old! 🌟
    """, "🎮 Dr. Hyliard's Favorite Interactive Tools")

def show_downloads():
    st.markdown('<div class="main-header">📥 Downloads</div>', unsafe_allow_html=True)
    
    st.markdown("## Download Lesson Materials")
    
    dr_hyliard_says("""
    Take these resources with you! I've put together everything you need to remember what we learned today. 
    Share them with your friends, your family, anyone who's curious about satellites and Earth science!
    """, "📦 Take This Home")
    
    st.info("Download these resources for offline use or printing!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📄 For Students")
        
        # Student handout
        student_handout = """# Student Handout: Space Technology & Earth Observation
## With Dr. Marcus Hyliard

**Name:** _________________________ **Date:** _____________ **Period:** _____

## The News Article

**Title:** Momentus shares spike after advancing 3D-printed fuel tank for spaceflight

**Read the full story:** https://finance.yahoo.com/news/momentus-develops-additive-manufactured-fuel-133000052.html

**Key Points:**
- Momentus Inc. created a 3D-printed fuel tank with Velo3D
- Will be tested on Vigoride-7 mission
- Uses metal additive manufacturing technology
- Could reduce costs and production time

## Dr. Hyliard Says:
"This breakthrough is what we've been waiting for. 3D printing is going to revolutionize how we study Earth from space!"

## Vocabulary

1. **Additive Manufacturing**: _______________________________
2. **Satellite**: _______________________________
3. **Orbit**: _______________________________
4. **Fuel Tank**: _______________________________

## Discussion Questions

1. How does 3D printing help make satellites more affordable?

_________________________________________________________________

2. Why are satellites important for studying Earth?

_________________________________________________________________

3. Give an example of how satellite data affects your daily life:

_________________________________________________________________

## Design Challenge Notes

**Mission Name:** _______________________________

**Goal:** _________________________________________________________________

**Measurements:** _________________________________________________________________

**Number of Satellites:** _______________________________

**How 3D printing helps:** _________________________________________________________________

## Dr. Hyliard's Challenge to You:
"Think about a problem on Earth you care about. How could satellites help solve it?"

_________________________________________________________________

_________________________________________________________________

## 📚 Continue Learning - Recommended Resources

### Interactive Practice:
**IXL Science Lessons** - www.ixl.com/science
- Earth Science: Climate & Weather lessons
- Engineering Design lessons  
- Space Technology lessons

### Watch:
- NASA Eyes on the Earth (eyes.nasa.gov)
- NASA Worldview satellite imagery (worldview.earthdata.nasa.gov)
- Track the ISS live (n2yo.com)

### Follow Current News:
- Space.com - Daily space news
- NASA News (nasa.gov/news)
- SpaceNews (spacenews.com)

### Listen:
- Houston We Have a Podcast (NASA)
- Science Friday (NPR)

## Dr. Hyliard's Pro Tips:
✅ Do the IXL Earth Science lessons - they're just like real lab work!
✅ Download N2YO app and watch the ISS pass over your house
✅ Check Space.com weekly for new satellite discoveries
✅ Ask questions - that's what scientists do!

---
*Interactive Lesson: Space Technology & Earth Science*
*Guided by Dr. Marcus Hyliard, Senior Satellite Engineer*
"""
        
        st.download_button(
            label="📥 Download Student Handout",
            data=student_handout,
            file_name="student_handout_with_dr_hyliard.txt",
            mime="text/plain"
        )
        
        # Vocabulary cards
        vocab_cards = """# Vocabulary Flashcards
## Dr. Hyliard's Study Guide

## Additive Manufacturing
**Definition:** Building objects layer by layer (3D printing)
**Example:** Using lasers to fuse metal powder layer by layer
**Dr. Hyliard says:** "Think of it like a hot glue gun, but with metal and lasers!"

## Satellite
**Definition:** An object that orbits a planet
**Example:** Weather satellites orbiting Earth
**Dr. Hyliard says:** "Earth has about 8,000 active satellites. That's a lot of eyes watching our planet!"

## Orbit
**Definition:** The path an object takes around another object in space
**Example:** The International Space Station orbits Earth every 90 minutes
**Dr. Hyliard says:** "Satellites move at 17,000 mph to stay in orbit. That's New York to Los Angeles in 10 minutes!"

## Fuel Tank
**Definition:** Container that holds propellant for spacecraft maneuvering
**Example:** Momentus's 3D-printed fuel tank
**Dr. Hyliard says:** "Without fuel, satellites drift like boats without rudders. Fuel tanks are CRITICAL!"

## Remote Sensing
**Definition:** Gathering information about Earth from a distance
**Example:** Satellites measuring ocean temperature from space
**Dr. Hyliard says:** "We can measure Earth without touching it. That's the magic of remote sensing!"

## Commercial Space
**Definition:** Private companies involved in space activities
**Example:** Momentus, SpaceX, Blue Origin
**Dr. Hyliard says:** "Competition drives innovation. Commercial space companies are making satellites accessible to everyone!"

---
*Study these well! - Dr. Hyliard*
"""
        
        st.download_button(
            label="📥 Download Vocabulary Cards",
            data=vocab_cards,
            file_name="vocabulary_cards_dr_hyliard.txt",
            mime="text/plain"
        )
    
    with col2:
        st.markdown("### 👨‍🏫 For Teachers")
        
        # Teacher guide
        teacher_guide = """# Teacher Guide: Space Technology & Earth Science
## Featuring Dr. Marcus Hyliard

## Lesson Overview
- **Duration:** 50-60 minutes
- **Grade Level:** 9-12
- **Subject:** Earth Science
- **Special Feature:** Fictional scientist Dr. Hyliard for student engagement

## About Dr. Hyliard
Dr. Marcus Hyliard is a fictional character created to make this lesson more engaging. He serves as:
- A relatable expert who explains complex concepts
- A storyteller who shares real-world applications
- A mentor who encourages students
- A bridge between abstract concepts and practical applications

## Using Dr. Hyliard in Your Classroom
- **Voice:** Dr. Hyliard speaks in an approachable, enthusiastic tone
- **Purpose:** Helps students connect emotionally with the material
- **Flexibility:** You can expand or minimize his presence as needed
- **Extension:** Consider having students write letters to "Dr. Hyliard" about their questions

## Learning Objectives
1. Explain how satellites contribute to Earth Science research
2. Describe how 3D printing is advancing space technology
3. Analyze the connection between technology and science
4. Evaluate the role of commercial space companies

## NGSS Standards
- HS-ESS3-1: Natural resources and climate impacts
- HS-ETS1-3: Evaluate solutions to complex problems
- HS-ESS2-4: Energy flow and climate systems

## Lesson Flow

### Introduction (10 min)
- Hook: "How do we know what's happening to Earth's climate?"
- Introduce Dr. Hyliard
- Show satellite images
- Present the Momentus article

### Direct Instruction (15 min)
- Satellites and Earth Science (with Dr. Hyliard's examples)
- 3D printing technology (with Dr. Hyliard's experiences)
- Innovation chain reaction

### Guided Practice (15 min)
- Design Challenge activity
- Students design missions "reviewed by Dr. Hyliard"
- Group work on satellite missions

### Discussion (10 min)
- Technology-science connection
- Real-world applications
- Career exploration

### Assessment (10 min)
- Quiz (with Dr. Hyliard's feedback)
- Exit ticket
- Dr. Hyliard's final message

## Common Misconceptions (and How Dr. Hyliard Addresses Them)
1. "Satellites are only for communication"
   - Dr. Hyliard shows the diversity of satellite applications
2. "3D printing is just for plastic"
   - Dr. Hyliard explains metal 3D printing with real examples
3. "Space technology doesn't affect daily life"
   - Dr. Hyliard provides concrete daily examples

## Dr. Hyliard's Best Moments
- His reaction to the first 3D-printed fuel tank
- His stories about tracking hurricanes
- His encouragement during the quiz
- His career advice to students

## Extension Activities
- Research specific satellite missions
- Calculate cost-benefit analysis  
- Write a letter to "Dr. Hyliard" with questions
- Create your own scientist character for other lessons

## Resources
- NASA Earth Observatory
- NOAA Satellites
- ESA Earth Observation
- Satellite tracking websites

## NEW: Current Media & Interactive Resources

### The Original Story:
- Yahoo Finance article: https://finance.yahoo.com/news/momentus-develops-additive-manufactured-fuel-133000052.html
- Use as primary source for lesson

### IXL Science Lessons:
- Recommended for homework/practice
- Earth Science: Climate & Weather
- Engineering Design lessons
- Aligns with NGSS standards
- Immediate feedback for students

### Interactive Tools Students Love:
- NASA Eyes on the Earth (3D visualization)
- NASA Worldview (real satellite imagery)
- N2YO Satellite Tracker (track ISS)
- Climate Time Machine (visualize change)

### Follow-Up Resources:
- Space.com for current news
- Houston We Have a Podcast
- Science Friday podcast
- Khan Academy science courses

### Using These Resources:
**For Homework:**
- Assign specific IXL lessons (listed in Resources page)
- Have students track ISS and report sightings
- Weekly current event from Space.com

**For Extension:**
- Research projects using NASA Worldview
- Podcast listening with reflection questions
- Create timeline using Climate Time Machine data

**For Engagement:**
- Start class with Space.com news update
- ISS spotting challenge (who can see it?)
- Compare real satellite data from NASA Worldview

---
*Remember: Dr. Hyliard is a teaching tool. Use him to make science personal and exciting!*
*All resources have been vetted and are free/accessible to students.*
"""
        
        st.download_button(
            label="📥 Download Teacher Guide",
            data=teacher_guide,
            file_name="teacher_guide_with_dr_hyliard.txt",
            mime="text/plain"
        )
        
        # Assessment rubric
        rubric = """# Assessment Rubric: Satellite Mission Design
## Dr. Hyliard's Evaluation Criteria

## Mission Design (40 points)

**Excellent (36-40):**
- Clear, specific mission goal
- Appropriate satellite configuration
- Well-justified design choices
- Comprehensive measurements
*Dr. Hyliard would say: "Outstanding! This mission is ready for funding!"*

**Proficient (30-35):**
- Clear mission goal
- Reasonable satellite configuration
- Some justification for choices
- Good measurement selection
*Dr. Hyliard would say: "Solid work! A few tweaks and this is mission-ready."*

**Developing (24-29):**
- General mission goal
- Basic satellite configuration
- Limited justification
- Basic measurements
*Dr. Hyliard would say: "Good start! Let's refine this together."*

**Beginning (0-23):**
- Unclear mission goal
- Inadequate configuration
- No justification
- Incomplete measurements
*Dr. Hyliard would say: "Don't worry, let's work through this step by step."*

## Scientific Understanding (30 points)

**Excellent (27-30):**
- Demonstrates deep understanding of satellite applications
- Makes clear connections to Earth Science
- Explains scientific value well
*Dr. Hyliard: "You think like a scientist!"*

**Proficient (21-26):**
- Shows good understanding
- Makes connections to Earth Science
- Explains scientific value
*Dr. Hyliard: "You've got the main concepts down!"*

**Developing (15-20):**
- Shows basic understanding
- Some connections made
- Limited explanation
*Dr. Hyliard: "Keep learning, you're on the right track!"*

**Beginning (0-14):**
- Limited understanding
- Few connections
- Weak explanation
*Dr. Hyliard: "Let's review together. Everyone starts somewhere!"*

## 3D Printing Application (20 points)

**Excellent (18-20):**
- Clearly explains cost/time benefits
- Multiple relevant advantages identified
- Strong connection to mission goals
*Dr. Hyliard: "You understand the innovation!"*

**Proficient (14-17):**
- Explains major benefits
- Several advantages identified
- Good connection to mission
*Dr. Hyliard: "Good grasp of the technology!"*

**Developing (10-13):**
- Mentions basic benefits
- Some advantages identified
- Basic connection
*Dr. Hyliard: "Getting there!"*

**Beginning (0-9):**
- Limited benefit discussion
- Few advantages
- Weak connection
*Dr. Hyliard: "Let's talk about why 3D printing matters."*

## Communication (10 points)

**Excellent (9-10):**
- Clear, organized presentation
- Professional quality
- Engaging delivery
*Dr. Hyliard: "Presentation ready!"*

**Proficient (7-8):**
- Clear presentation
- Good quality
- Adequate delivery
*Dr. Hyliard: "Well communicated!"*

**Developing (5-6):**
- Somewhat clear
- Acceptable quality
- Basic delivery
*Dr. Hyliard: "Work on clarity!"*

**Beginning (0-4):**
- Unclear
- Poor quality
- Weak delivery
*Dr. Hyliard: "Let's practice presenting together!"*

---
*Remember: Dr. Hyliard's feedback is constructive and encouraging, even for low scores.*
*Use his voice to motivate students rather than discourage them.*
"""
        
        st.download_button(
            label="📥 Download Assessment Rubric",
            data=rubric,
            file_name="assessment_rubric_dr_hyliard.txt",
            mime="text/plain"
        )
    
    st.markdown("---")
    st.markdown("### 📊 Data & Charts")
    
    # Create sample data visualization
    st.markdown("#### Satellite Launch Costs Over Time")
    
    import numpy as np
    years = list(range(2010, 2026))
    traditional_costs = [200 - (i * 5) for i in range(len(years))]
    printing_costs = [200 - (i * 12) for i in range(len(years))]
    
    chart_data = pd.DataFrame({
        'Year': years,
        'Traditional Manufacturing': traditional_costs,
        '3D Printing': printing_costs
    })
    
    st.line_chart(chart_data.set_index('Year'))
    
    st.caption("Sample data showing how 3D printing technology has reduced satellite component costs over time")
    
    dr_hyliard_says("""
    See that gap widening? That's innovation in action! Every year, 3D printing gets better and cheaper while 
    traditional manufacturing stays expensive. By 2030, I predict 3D printing will cost 90% less than traditional 
    methods. That's when space really becomes accessible to everyone!
    """, "📈 Dr. Hyliard Analyzes the Data")

# Main app logic
if teacher_mode:
    st.sidebar.info("👨‍🏫 **Teacher Mode Active**\n\nAdditional notes and guidance visible.")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### About Dr. Hyliard")
    st.sidebar.info("""
    Dr. Marcus Hyliard is a fictional character designed to increase student engagement. 
    
    **Purpose:**
    - Makes content relatable
    - Provides real-world context
    - Encourages students
    - Creates narrative continuity
    
    **Teaching Tip:** 
    Refer to Dr. Hyliard in discussions: "What would Dr. Hyliard say about this?"
    """)

# Route to appropriate page
page_functions = {
    'home': show_home,
    'hyliard': show_hyliard,
    'article': show_article,
    'objectives': show_objectives,
    'satellites': show_satellites,
    '3d_printing': show_3d_printing,
    'design_challenge': show_design_challenge,
    'quiz': show_quiz,
    'resources': show_resources,
    'downloads': show_downloads
}

page_functions[st.session_state.page]()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🛰️ Space Technology & Earth Science Interactive Lesson</p>
    <p>Guided by Dr. Marcus Hyliard</p>
    <p>Based on real news about Momentus's 3D-printed fuel tank innovation</p>
    <p><em>Exploring how technology drives scientific discovery</em></p>
</div>
""", unsafe_allow_html=True)
