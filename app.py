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
            st.metric("Orbit Speed", "17,000 mph", "to stay in space")
        with stat4:
            st.metric("Daily Images", "Millions", "of Earth's surface")

def show_article():
    st.markdown('<div class="main-header">📰 The News Article</div>', unsafe_allow_html=True)
    
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
    
    with col2:
        st.markdown("### 🔑 Key Terms")
        
        with st.expander("**Additive Manufacturing**"):
            st.write("Building objects layer by layer, also known as 3D printing. Uses materials like metal powder to create complex shapes.")
        
        with st.expander("**Fuel Tank**"):
            st.write("Container that holds propellant for spacecraft maneuvering in space. Essential for adjusting satellite position.")
        
        with st.expander("**Orbital Service Vehicle**"):
            st.write("A spacecraft designed to provide services to other satellites while in orbit around Earth.")
        
        with st.expander("**Vigoride-7**"):
            st.write("The name of Momentus's upcoming mission that will test the 3D-printed fuel tank in actual space conditions.")
        
        st.markdown("---")
        st.markdown("### 💡 Discussion Prompt")
        st.info("Why do you think a 3D-printed fuel tank would be cheaper and faster to produce than a traditional fuel tank?")
        
        if st.button("Show Answer"):
            st.success("""
            3D printing builds the tank layer by layer from a digital design, which means:
            - No need for expensive molds or tools
            - Less material waste
            - Can create complex shapes in one piece
            - Automated process = faster production
            - Easy to modify designs
            """)

def show_objectives():
    st.markdown('<div class="main-header">🎯 Learning Objectives</div>', unsafe_allow_html=True)
    
    st.markdown("## By the end of this lesson, you will be able to:")
    
    objectives = [
        {
            "icon": "🛰️",
            "title": "Explain Satellite Contributions",
            "description": "Understand how satellites contribute to Earth Science research and environmental monitoring",
            "examples": ["Hurricane tracking", "Climate monitoring", "Deforestation detection"]
        },
        {
            "icon": "🖨️",
            "title": "Describe 3D Printing Technology",
            "description": "Explain how additive manufacturing is advancing space technology",
            "examples": ["Faster production", "Complex designs", "Lower costs"]
        },
        {
            "icon": "🔬",
            "title": "Analyze Technology-Science Connection",
            "description": "Understand how technological innovation drives scientific discovery",
            "examples": ["Better tools → Better data", "More satellites → Better coverage", "Innovation enables research"]
        },
        {
            "icon": "🏢",
            "title": "Evaluate Commercial Space",
            "description": "Assess the role of commercial space companies in Earth observation",
            "examples": ["Competition drives innovation", "Reduces costs", "Increases accessibility"]
        }
    ]
    
    for obj in objectives:
        with st.expander(f"{obj['icon']} {obj['title']}", expanded=True):
            st.write(f"**Learning Goal:** {obj['description']}")
            st.write("**Examples:**")
            for example in obj['examples']:
                st.write(f"- {example}")
    
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
        
        with col2:
            st.image("https://via.placeholder.com/400x300/42A5F5/FFFFFF?text=Weather+Satellite", 
                     caption="Weather satellite monitoring hurricanes")
            
            st.metric("Active Weather Satellites", "~400", "globally")
        
        # Quick Check for Atmosphere tab
        st.markdown("---")
        st.markdown("### 🧠 Quick Check")
        
        atmo_question = st.radio(
            "Why do weather satellites need to monitor the atmosphere continuously?",
            ["Because the atmosphere is always changing and weather patterns develop quickly",
             "Because satellites run out of battery",
             "Because clouds move too slowly to see",
             "Because the atmosphere never changes"],
            key="atmosphere_quiz"
        )
        
        if st.button("Check Answer", key="check_atmosphere"):
            if atmo_question == "Because the atmosphere is always changing and weather patterns develop quickly":
                st.success("✅ Correct! The atmosphere is dynamic and constantly changing. Storms can develop in hours, so continuous monitoring is essential for accurate weather prediction and tracking severe weather events.")
            else:
                st.error("❌ Try again! Think about how fast weather can change and why meteorologists need up-to-date information.")
    
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
        
        with col2:
            st.image("https://via.placeholder.com/400x300/0277BD/FFFFFF?text=Ocean+Monitoring", 
                     caption="Satellite measuring ocean temperatures")
            
            st.metric("Sea Level Rise Since 1993", "+100mm", "≈4 inches")
        
        # Quick Check for Oceans tab
        st.markdown("---")
        st.markdown("### 🧠 Quick Check")
        
        ocean_question = st.radio(
            "How can satellites measure sea level from space?",
            ["They use radar to measure the distance between the satellite and the ocean surface",
             "They take pictures and count the waves",
             "They measure the color of the water",
             "They cannot measure sea level from space"],
            key="ocean_quiz"
        )
        
        if st.button("Check Answer", key="check_ocean"):
            if ocean_question == "They use radar to measure the distance between the satellite and the ocean surface":
                st.success("✅ Correct! Satellites use radar altimeters that send radio waves down to the ocean surface and measure how long it takes for the signal to bounce back. By doing this repeatedly over years, scientists can detect even small changes in sea level.")
            else:
                st.error("❌ Try again! Think about how you could measure distance from far away using signals that travel at a known speed.")
    
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
        
        with col2:
            st.image("https://via.placeholder.com/400x300/66BB6A/FFFFFF?text=Land+Monitoring", 
                     caption="Satellite tracking deforestation")
            
            st.metric("Forest Lost Since 2000", "10%", "of global forests")
        
        # Quick Check for Land tab
        st.markdown("---")
        st.markdown("### 🧠 Quick Check")
        
        land_question = st.radio(
            "Why is satellite monitoring important for tracking deforestation?",
            ["Forests cover huge areas that are impossible to monitor from the ground alone",
             "Satellites can see through trees",
             "It's cheaper than planting new trees",
             "Satellites can stop illegal logging"],
            key="land_quiz"
        )
        
        if st.button("Check Answer", key="check_land"):
            if land_question == "Forests cover huge areas that are impossible to monitor from the ground alone":
                st.success("✅ Correct! The Amazon rainforest alone covers 2.1 million square miles. Satellites can survey vast areas quickly and repeatedly, detecting changes that would be impossible to catch with ground surveys. This helps identify illegal logging and monitor forest health globally.")
            else:
                st.error("❌ Try again! Think about the scale of Earth's forests and why we need a view from above to track changes.")
    
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
        
        with col2:
            st.image("https://via.placeholder.com/400x300/E1F5FE/000000?text=Ice+Monitoring", 
                     caption="Satellite measuring ice sheet thickness")
            
            st.metric("Arctic Ice Loss", "-13%", "per decade since 1979")
        
        # Quick Check for Ice & Snow tab
        st.markdown("---")
        st.markdown("### 🧠 Quick Check")
        
        ice_question = st.radio(
            "Why is monitoring ice and snow important for understanding global climate change?",
            ["Ice reflects sunlight back to space; when ice melts, Earth absorbs more heat, accelerating warming",
             "Ice is only important for polar bears",
             "Snow makes good drinking water",
             "Ice doesn't affect climate at all"],
            key="ice_quiz"
        )
        
        if st.button("Check Answer", key="check_ice"):
            if ice_question == "Ice reflects sunlight back to space; when ice melts, Earth absorbs more heat, accelerating warming":
                st.success("✅ Correct! This is called the 'ice-albedo feedback.' White ice reflects about 80% of sunlight back to space, while dark ocean water absorbs about 90% of sunlight. As ice melts, more dark water is exposed, which absorbs more heat, causing more melting - a dangerous feedback loop that satellites help us monitor.")
            else:
                st.error("❌ Try again! Think about the color of ice versus ocean water and how they interact with sunlight differently.")
    
    # General satellite quiz at the end
    st.markdown("---")
    st.markdown("## 🧠 Quick Check: General Satellite Knowledge")
    
    question = st.radio(
        "Which of these can satellites NOT do?",
        ["Measure ocean temperature", "Predict earthquakes before they happen", 
         "Track deforestation", "Monitor air quality"],
        key="general_satellite_quiz"
    )
    
    if st.button("Check Answer", key="check_general"):
        if question == "Predict earthquakes before they happen":
            st.success("✅ Correct! Satellites cannot predict earthquakes before they happen. While they can measure ground movement AFTER earthquakes occur, we don't yet have technology to predict them in advance.")
        else:
            st.error("❌ Try again! Satellites CAN do this. Think about what requires advance knowledge we don't have yet.")

def show_3d_printing():
    st.markdown('<div class="main-header">🖨️ 3D Printing Innovation</div>', unsafe_allow_html=True)
    
    st.markdown("## The Momentus Innovation: 3D-Printed Fuel Tanks")
    
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
    
    # Interactive comparison
    st.markdown("---")
    st.markdown("## 💰 Cost Comparison Calculator")
    
    st.write("See how 3D printing saves money on a satellite mission:")
    
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

def show_design_challenge():
    st.markdown('<div class="main-header">🎨 Design Challenge</div>', unsafe_allow_html=True)
    
    st.markdown("## 🚀 Design Your Own Satellite Mission!")
    
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
            "challenges": "Hurricanes move fast and need constant monitoring"
        },
        "🧊 Arctic Ice Monitoring": {
            "description": "Monitor polar ice cap melting and thickness",
            "measures": ["Ice thickness", "Ice extent", "Surface temperature", "Glacier movement"],
            "challenges": "Polar regions are remote and changing rapidly"
        },
        "🔥 Wildfire Detection": {
            "description": "Detect and monitor wildfires worldwide",
            "measures": ["Heat signatures", "Smoke detection", "Vegetation dryness", "Fire spread"],
            "challenges": "Fires can start quickly and spread unpredictably"
        },
        "🌊 Ocean Temperature": {
            "description": "Track ocean temperature changes globally",
            "measures": ["Sea surface temp", "Ocean currents", "Heat absorption", "El Niño patterns"],
            "challenges": "Oceans cover 70% of Earth and change slowly"
        }
    }
    
    mission_type = st.selectbox("Select your mission:", list(scenarios.keys()))
    
    with st.expander("📋 Mission Details"):
        st.write(f"**Goal:** {scenarios[mission_type]['description']}")
        st.write(f"**Challenge:** {scenarios[mission_type]['challenges']}")
        st.write("**Suggested Measurements:**")
        for measure in scenarios[mission_type]['measures']:
            st.write(f"- {measure}")
    
    st.markdown("---")
    st.markdown("### Step 2: Design Your Mission")
    
    with st.form("mission_design"):
        col1, col2 = st.columns(2)
        
        with col1:
            mission_name = st.text_input("Mission Name:", placeholder="e.g., EarthWatch-1")
            
            mission_goal = st.
