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
    .michigan-box {
        background-color: #FFF8E1;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #00274C;
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
    .developer-credit {
        text-align: center;
        color: #666;
        font-size: 0.9em;
        margin-top: -1rem;
        margin-bottom: 2rem;
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
if 'xp_points' not in st.session_state:
    st.session_state.xp_points = 0
if 'achievements' not in st.session_state:
    st.session_state.achievements = []
if 'completed_checks' not in st.session_state:
    st.session_state.completed_checks = set()

# XP Award Function
def award_xp(points, check_id, achievement_name=None):
    """Award XP points and track completed checks to prevent double-counting"""
    if check_id not in st.session_state.completed_checks:
        st.session_state.xp_points += points
        st.session_state.completed_checks.add(check_id)
        if achievement_name and achievement_name not in st.session_state.achievements:
            st.session_state.achievements.append(achievement_name)
        return True
    return False

# Achievement definitions
ACHIEVEMENTS = {
    "first_correct": {"name": "🌟 First Steps", "desc": "Answer your first question correctly", "xp": 10},
    "atmosphere_master": {"name": "🌤️ Atmosphere Expert", "desc": "Complete all Atmosphere questions", "xp": 25},
    "ocean_master": {"name": "🌊 Ocean Expert", "desc": "Complete all Ocean & Great Lakes questions", "xp": 25},
    "land_master": {"name": "🌲 Land Expert", "desc": "Complete all Land questions", "xp": 25},
    "ice_master": {"name": "🧊 Ice Expert", "desc": "Complete all Ice & Snow questions", "xp": 25},
    "satellite_scholar": {"name": "🛰️ Satellite Scholar", "desc": "Complete all satellite section questions", "xp": 50},
    "engineer": {"name": "🔧 Space Engineer", "desc": "Complete the Design Challenge", "xp": 50},
    "quiz_complete": {"name": "📝 Quiz Champion", "desc": "Complete the final assessment", "xp": 75},
    "perfect_quiz": {"name": "🏆 Perfect Score", "desc": "Get 100% on the final quiz", "xp": 100},
}

# Sidebar navigation
with st.sidebar:
    # XP Progress Display
    st.markdown("### 🏆 Your Progress")
    st.metric("XP Points", st.session_state.xp_points, help="Earn XP by answering questions correctly!")
    
    # Progress bar (max 500 XP for completing everything)
    progress = min(st.session_state.xp_points / 500, 1.0)
    st.progress(progress)
    
    # Level calculation
    if st.session_state.xp_points >= 400:
        level = "🌟 Earth Science Master"
    elif st.session_state.xp_points >= 250:
        level = "🛰️ Satellite Expert"
    elif st.session_state.xp_points >= 100:
        level = "🔬 Science Explorer"
    elif st.session_state.xp_points >= 25:
        level = "📚 Learner"
    else:
        level = "🌱 Beginner"
    
    st.caption(f"Level: {level}")
    
    # Show achievements
    if st.session_state.achievements:
        with st.expander(f"🎖️ Achievements ({len(st.session_state.achievements)})"):
            for achievement in st.session_state.achievements:
                st.write(f"✅ {achievement}")
    
    st.markdown("---")
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
    st.info("**Grade Level:** 9-12\n\n**Duration:** 50-60 minutes\n\n**Subject:** Earth Science\n\n**State:** Michigan")
    
    st.markdown("---")
    st.markdown("**Teacher Mode**")
    teacher_mode = st.checkbox("Enable teacher notes")

# Main content area
def show_home():
    st.markdown('<div class="main-header">🛰️ Space Technology & Earth Observation</div>', unsafe_allow_html=True)
    st.markdown('<p class="developer-credit">Developed by Xavier Honablue, M.Ed. for Grosse Pointe South High School</p>', unsafe_allow_html=True)
    
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
        
        # Michigan Connection
        st.markdown("""
        <div class="michigan-box">
        <h4>🌊 Michigan Connection</h4>
        <p>The Great Lakes contain 20% of the world's fresh surface water. Satellites help us monitor 
        lake temperatures, ice coverage, algal blooms, and water levels—critical for Michigan's 
        environment and economy!</p>
        </div>
        """, unsafe_allow_html=True)
        
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
        
        # Michigan Science Standards Dropdown
        st.markdown("---")
        st.markdown("### 📋 Michigan Science Standards (MSS) Covered")
        
        with st.expander("🎓 Click to view all Michigan Science Standards addressed in this lesson", expanded=False):
            st.markdown("""
            <div class="michigan-box">
            <p>This lesson is aligned with the <strong>Michigan Science Standards (MSS)</strong>, which are based on 
            the Next Generation Science Standards (NGSS) with emphasis on Michigan-specific contexts.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### 🌍 Earth's Systems Standards")
            
            st.markdown("""
            **HS-ESS2-2: Earth Systems Feedback**
            > *Analyze geoscience data to make the claim that one change to Earth's surface can create 
            > feedbacks that cause changes to other Earth systems.*
            
            - **Lesson Connection:** Ice-albedo feedback, Great Lakes ice coverage effects on regional climate
            - **Activities:** Ice & Snow tab, Quiz questions on feedback loops
            """)
            
            st.markdown("""
            **HS-ESS2-4: Water Cycling**
            > *Develop a model to describe the cycling of water through Earth's systems driven by energy 
            > from the sun and the force of gravity.*
            
            - **Lesson Connection:** Great Lakes water cycle, lake-effect weather patterns, atmospheric monitoring
            - **Activities:** Atmosphere tab, Oceans & Great Lakes tab
            """)
            
            st.markdown("""
            **HS-ESS2-5: Water Properties**
            > *Plan and conduct an investigation of the properties of water and its effects on Earth 
            > materials and surface processes.*
            
            - **Lesson Connection:** Great Lakes erosion, water quality monitoring, algal bloom detection
            - **Activities:** Oceans & Great Lakes tab, Design Challenge
            """)
            
            st.markdown("#### 🏭 Earth and Human Activity Standards")
            
            st.markdown("""
            **HS-ESS3-1: Resources, Hazards, and Human Activity**
            > *Construct an explanation based on evidence for how the availability of natural resources, 
            > occurrence of natural hazards, and changes in climate have influenced human activity.*
            
            - **Lesson Connection:** Lake levels affecting shipping, coastal erosion impacts, agriculture monitoring
            - **Activities:** Land tab, Oceans & Great Lakes tab, Design Challenge
            """)
            
            st.markdown("""
            **HS-ESS3-5: Climate Data Analysis**
            > *Analyze geoscience data and the results from global climate models to make an evidence-based 
            > forecast of the current rate of global or regional climate change and associated future impacts.*
            
            - **Lesson Connection:** Satellite climate monitoring, Great Lakes temperature trends, ice coverage data
            - **Activities:** All satellite monitoring tabs, Quiz assessment
            """)
            
            st.markdown("#### 🔧 Engineering Design Standards")
            
            st.markdown("""
            **HS-ETS1-3: Evaluating Engineering Solutions**
            > *Evaluate a solution to a complex real-world problem based on prioritized criteria and 
            > trade-offs that account for a range of constraints, including cost, safety, reliability, 
            > and aesthetics, as well as possible social, cultural, and environmental impacts.*
            
            - **Lesson Connection:** 3D printing trade-offs, satellite mission design constraints, cost-benefit analysis
            - **Activities:** 3D Printing Innovation section, Design Challenge, Cost Calculator
            """)
            
            st.markdown("---")
            
            st.markdown("#### 📊 Standards Summary Table")
            
            standards_data = {
                "Standard": ["HS-ESS2-2", "HS-ESS2-4", "HS-ESS2-5", "HS-ESS3-1", "HS-ESS3-5", "HS-ETS1-3"],
                "Topic": ["Earth Systems Feedback", "Water Cycling", "Water Properties", 
                         "Resources & Hazards", "Climate Data", "Engineering Design"],
                "Lesson Sections": ["Ice & Snow, Quiz", "Atmosphere, Oceans", "Oceans & Great Lakes", 
                                   "Land, Oceans, Design", "All Tabs, Quiz", "3D Printing, Design Challenge"]
            }
            
            standards_df = pd.DataFrame(standards_data)
            st.table(standards_df)
        
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
    st.markdown('<p class="developer-credit">Developed by Xavier Honablue, M.Ed. for Grosse Pointe South High School</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Momentus shares spike after advancing 3D-printed fuel tank for spaceflight
        
        **By Fiona Craig • Published 10 hours ago**
        
        📰 **[Read the full article on Yahoo Finance](https://finance.yahoo.com/news/momentus-develops-additive-manufactured-fuel-133000052.html)**
        
        ---
        """)
        
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
    st.markdown('<p class="developer-credit">Developed by Xavier Honablue, M.Ed. for Grosse Pointe South High School</p>', unsafe_allow_html=True)
    
    st.markdown("## By the end of this lesson, you will be able to:")
    
    objectives = [
        {
            "icon": "🛰️",
            "title": "Explain Satellite Contributions",
            "description": "Understand how satellites contribute to Earth Science research and environmental monitoring",
            "examples": ["Hurricane tracking", "Climate monitoring", "Deforestation detection", "Great Lakes observation"]
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
    st.markdown("## 📊 Michigan Science Standards (MSS) Alignment")
    
    st.markdown("""
    <div class="michigan-box">
    <p><strong>Note:</strong> Michigan Science Standards are based on the Next Generation Science Standards (NGSS) 
    with emphasis on Michigan-specific contexts including the Great Lakes ecosystem.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **MS-ESS2-4 / HS-ESS2-4**
        
        *Earth's Systems*
        
        Develop a model to describe the cycling of water through Earth's 
        systems driven by energy from the sun and the force of gravity.
        
        **Michigan Context:** Great Lakes water cycle, lake-effect weather patterns
        """)
        
        st.markdown("---")
        
        st.markdown("""
        **HS-ESS2-2**
        
        *Earth's Systems*
        
        Analyze geoscience data to make the claim that one change to 
        Earth's surface can create feedbacks that cause changes to 
        other Earth systems.
        
        **Michigan Context:** Ice-albedo feedback in the Great Lakes region
        """)
    
    with col2:
        st.markdown("""
        **HS-ESS3-5**
        
        *Earth and Human Activity*
        
        Analyze geoscience data and the results from global climate 
        models to make an evidence-based forecast of the current rate 
        of global or regional climate change and associated future impacts.
        
        **Michigan Context:** Climate impacts on Michigan agriculture and ecosystems
        """)
        
        st.markdown("---")
        
        st.markdown("""
        **HS-ETS1-3**
        
        *Engineering Design*
        
        Evaluate a solution to a complex real-world problem based on 
        prioritized criteria and trade-offs that account for a range 
        of constraints.
        
        **Michigan Context:** Engineering solutions for Great Lakes monitoring
        """)
    
    st.markdown("---")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        **HS-ESS3-1**
        
        *Earth and Human Activity*
        
        Construct an explanation based on evidence for how the availability 
        of natural resources, occurrence of natural hazards, and changes in 
        climate have influenced human activity.
        
        **Michigan Context:** Lake levels, shipping, and coastal erosion impacts
        """)
    
    with col4:
        st.markdown("""
        **HS-ESS2-5**
        
        *Earth's Systems*
        
        Plan and conduct an investigation of the properties of water and 
        its effects on Earth materials and surface processes.
        
        **Michigan Context:** Great Lakes erosion, water quality monitoring
        """)

def show_satellites():
    st.markdown('<div class="main-header">🌍 Satellites & Earth Science</div>', unsafe_allow_html=True)
    st.markdown('<p class="developer-credit">Developed by Xavier Honablue, M.Ed. for Grosse Pointe South High School</p>', unsafe_allow_html=True)
    
    st.markdown("## Why Satellites Matter")
    
    st.info("""
    Satellites give us the **only way** to see our entire planet at once. They provide a "bird's eye view" 
    that helps us understand Earth's complex systems and how they're changing.
    """)
    
    # Michigan Connection Box
    st.markdown("""
    <div class="michigan-box">
    <h4>🌊 Michigan Connection</h4>
    <p>NOAA's Great Lakes Environmental Research Laboratory (GLERL) uses satellite data to monitor 
    the Great Lakes—tracking ice coverage, harmful algal blooms, water temperature, and lake levels 
    that directly impact Michigan communities.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive tabs for different satellite types
    tab1, tab2, tab3, tab4 = st.tabs(["🌤️ Atmosphere", "🌊 Oceans & Great Lakes", "🌲 Land", "🧊 Ice & Snow"])
    
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
            
            st.markdown("#### Michigan Application:")
            st.info("🌨️ **Lake-Effect Snow:** Satellites help meteorologists predict lake-effect snowstorms by tracking cold air masses moving over the warmer Great Lakes waters.")
        
        with col2:
            st.metric("Active Weather Satellites", "~400", "globally")
        
        # Tab-Specific Quick Check for Atmosphere
        st.markdown("---")
        st.markdown("### 🧠 Atmosphere Quick Check")
        
        atmo_q1 = st.radio(
            "**Question 1:** How do satellites measure atmospheric temperature at different altitudes?",
            ["A) By dropping thermometers from space",
             "B) By measuring infrared radiation emitted at different wavelengths",
             "C) By sending weather balloons",
             "D) By taking photographs of clouds"],
            key="atmo_q1"
        )
        
        if st.button("Check Answer", key="check_atmo_q1"):
            if atmo_q1 == "B) By measuring infrared radiation emitted at different wavelengths":
                if award_xp(15, "atmo_q1", "🌟 First Steps" if not st.session_state.achievements else None):
                    st.balloons()
                    st.success("✅ Correct! +15 XP! Different atmospheric layers emit infrared radiation at characteristic wavelengths. Satellites measure these wavelengths to determine temperature at various altitudes without physical contact. (MSS HS-ESS2-4)")
                else:
                    st.success("✅ Correct! Different atmospheric layers emit infrared radiation at characteristic wavelengths. Satellites measure these wavelengths to determine temperature at various altitudes without physical contact. (MSS HS-ESS2-4)")
            else:
                st.error("❌ Not quite. Satellites use remote sensing—they measure infrared radiation emitted by the atmosphere at different wavelengths to determine temperature profiles.")
        
        st.markdown("---")
        
        atmo_q2 = st.radio(
            "**Question 2:** Why is continuous satellite monitoring essential for tracking severe weather in Michigan?",
            ["A) Because Michigan weather never changes",
             "B) Because lake-effect storms can develop rapidly when cold air crosses the Great Lakes",
             "C) Because satellites are cheaper than thermometers",
             "D) Because Michigan has no weather stations"],
            key="atmo_q2"
        )
        
        if st.button("Check Answer", key="check_atmo_q2"):
            if atmo_q2 == "B) Because lake-effect storms can develop rapidly when cold air crosses the Great Lakes":
                newly_awarded = award_xp(15, "atmo_q2")
                # Check for Atmosphere Master achievement
                if "atmo_q1" in st.session_state.completed_checks and "atmo_q2" in st.session_state.completed_checks:
                    if "🌤️ Atmosphere Expert" not in st.session_state.achievements:
                        st.session_state.achievements.append("🌤️ Atmosphere Expert")
                        st.balloons()
                        st.success("✅ Correct! +15 XP! 🎖️ Achievement Unlocked: Atmosphere Expert! Lake-effect snow can develop within hours when cold Arctic air moves over the relatively warm Great Lakes. Satellites track these air masses and lake surface temperatures to predict where and when heavy snow will occur. (MSS HS-ESS3-5)")
                    else:
                        st.success("✅ Correct! Lake-effect snow can develop within hours when cold Arctic air moves over the relatively warm Great Lakes. (MSS HS-ESS3-5)")
                elif newly_awarded:
                    st.success("✅ Correct! +15 XP! Lake-effect snow can develop within hours when cold Arctic air moves over the relatively warm Great Lakes. Satellites track these air masses and lake surface temperatures to predict where and when heavy snow will occur. (MSS HS-ESS3-5)")
                else:
                    st.success("✅ Correct! Lake-effect snow can develop within hours when cold Arctic air moves over the relatively warm Great Lakes. (MSS HS-ESS3-5)")
            else:
                st.error("❌ Not quite. Think about how quickly weather can change in Michigan, especially near the Great Lakes during winter.")
    
    with tab2:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### Ocean & Great Lakes Observation")
            st.write("""
            Satellites help us understand water systems by measuring:
            - **Sea/lake surface temperature**
            - **Water level height** (tracking changes over time)
            - **Currents** and circulation patterns
            - **Water color** (indicates algae/phytoplankton health)
            - **Ice coverage** and thickness
            """)
            
            st.markdown("#### Real-World Applications:")
            st.success("✅ Tracking sea level rise\n\n✅ Monitoring water quality\n\n✅ Predicting El Niño events\n\n✅ Protecting aquatic ecosystems")
            
            st.markdown("#### Michigan Application:")
            st.info("🌊 **Harmful Algal Blooms:** Satellites detect algal blooms in Lake Erie and other Great Lakes by measuring water color changes, helping protect drinking water for millions of Michiganders.")
        
        with col2:
            st.metric("Great Lakes Surface Area", "94,250 mi²", "largest freshwater system")
        
        # Tab-Specific Quick Check for Oceans/Great Lakes
        st.markdown("---")
        st.markdown("### 🧠 Oceans & Great Lakes Quick Check")
        
        ocean_q1 = st.radio(
            "**Question 1:** How do satellites detect harmful algal blooms in the Great Lakes?",
            ["A) By counting individual algae cells from space",
             "B) By measuring changes in water color caused by chlorophyll in algae",
             "C) By tasting the water remotely",
             "D) By measuring water salinity"],
            key="ocean_q1"
        )
        
        if st.button("Check Answer", key="check_ocean_q1"):
            if ocean_q1 == "B) By measuring changes in water color caused by chlorophyll in algae":
                if award_xp(15, "ocean_q1", "🌟 First Steps" if not st.session_state.achievements else None):
                    st.balloons()
                    st.success("✅ Correct! +15 XP! Algae contain chlorophyll, which reflects green light. Satellites measure subtle color changes in water to detect and map algal blooms. This helps Michigan communities protect drinking water sources. (MSS HS-ESS2-5)")
                else:
                    st.success("✅ Correct! Algae contain chlorophyll, which reflects green light. Satellites measure subtle color changes in water to detect and map algal blooms. (MSS HS-ESS2-5)")
            else:
                st.error("❌ Not quite. Think about what makes algae visible—it's related to the pigments they contain and how those affect water color.")
        
        st.markdown("---")
        
        ocean_q2 = st.radio(
            "**Question 2:** Why is monitoring Great Lakes water levels important for Michigan?",
            ["A) It affects shipping, coastal erosion, property values, and ecosystem health",
             "B) Water levels never change",
             "C) Only fishermen care about water levels",
             "D) Satellites cannot measure water levels"],
            key="ocean_q2"
        )
        
        if st.button("Check Answer", key="check_ocean_q2"):
            if ocean_q2 == "A) It affects shipping, coastal erosion, property values, and ecosystem health":
                newly_awarded = award_xp(15, "ocean_q2")
                # Check for Ocean Master achievement
                if "ocean_q1" in st.session_state.completed_checks and "ocean_q2" in st.session_state.completed_checks:
                    if "🌊 Ocean Expert" not in st.session_state.achievements:
                        st.session_state.achievements.append("🌊 Ocean Expert")
                        st.balloons()
                        st.success("✅ Correct! +15 XP! 🎖️ Achievement Unlocked: Ocean Expert! Great Lakes water levels impact shipping, coastal erosion, wetland habitats, and municipal water intakes. Satellites track these levels continuously. (MSS HS-ESS3-1)")
                    else:
                        st.success("✅ Correct! Great Lakes water levels impact shipping, coastal erosion, wetland habitats, and municipal water intakes. (MSS HS-ESS3-1)")
                elif newly_awarded:
                    st.success("✅ Correct! +15 XP! Great Lakes water levels impact shipping (low levels restrict cargo), coastal erosion (high levels damage property), wetland habitats, and municipal water intakes. (MSS HS-ESS3-1)")
                else:
                    st.success("✅ Correct! Great Lakes water levels impact shipping, coastal erosion, wetland habitats, and municipal water intakes. (MSS HS-ESS3-1)")
            else:
                st.error("❌ Not quite. Consider all the ways that lake levels affect communities, businesses, and ecosystems around the Great Lakes.")
    
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
            
            st.markdown("#### Michigan Application:")
            st.info("🌾 **Agriculture:** Satellites monitor Michigan's $104.7 billion agriculture industry, tracking crop health, soil moisture, and drought conditions across cherry orchards, apple farms, and corn/soybean fields.")
        
        with col2:
            st.metric("Michigan Farmland", "9.8 million", "acres monitored")
        
        # Tab-Specific Quick Check for Land
        st.markdown("---")
        st.markdown("### 🧠 Land Surface Quick Check")
        
        land_q1 = st.radio(
            "**Question 1:** How do satellites determine if crops are healthy or stressed?",
            ["A) By asking farmers",
             "B) By measuring how plants reflect near-infrared light (healthy plants reflect more)",
             "C) By counting individual leaves",
             "D) By measuring soil temperature only"],
            key="land_q1"
        )
        
        if st.button("Check Answer", key="check_land_q1"):
            if land_q1 == "B) By measuring how plants reflect near-infrared light (healthy plants reflect more)":
                if award_xp(15, "land_q1", "🌟 First Steps" if not st.session_state.achievements else None):
                    st.balloons()
                    st.success("✅ Correct! +15 XP! Healthy plants with lots of chlorophyll strongly reflect near-infrared light while absorbing visible red light. Stressed or dying plants reflect less near-infrared. Satellites measure this ratio (called NDVI) to assess vegetation health. (MSS HS-ESS3-1)")
                else:
                    st.success("✅ Correct! Healthy plants with lots of chlorophyll strongly reflect near-infrared light while absorbing visible red light. Satellites measure this ratio (called NDVI) to assess vegetation health. (MSS HS-ESS3-1)")
            else:
                st.error("❌ Not quite. Think about how healthy vs. unhealthy plants might interact differently with light that we can't see with our eyes.")
        
        st.markdown("---")
        
        land_q2 = st.radio(
            "**Question 2:** Why is satellite monitoring valuable for tracking urban growth in Michigan?",
            ["A) It provides consistent, repeatable measurements showing how cities expand over time",
             "B) Cities don't grow",
             "C) Satellites can see through buildings",
             "D) Urban areas are too small to see from space"],
            key="land_q2"
        )
        
        if st.button("Check Answer", key="check_land_q2"):
            if land_q2 == "A) It provides consistent, repeatable measurements showing how cities expand over time":
                newly_awarded = award_xp(15, "land_q2")
                # Check for Land Master achievement
                if "land_q1" in st.session_state.completed_checks and "land_q2" in st.session_state.completed_checks:
                    if "🌲 Land Expert" not in st.session_state.achievements:
                        st.session_state.achievements.append("🌲 Land Expert")
                        st.balloons()
                        st.success("✅ Correct! +15 XP! 🎖️ Achievement Unlocked: Land Expert! Satellites take images of the same areas repeatedly, allowing scientists to track how urban areas expand into farmland or forests. (MSS HS-ESS3-1)")
                    else:
                        st.success("✅ Correct! Satellites take images of the same areas repeatedly, allowing scientists to track how urban areas expand into farmland or forests. (MSS HS-ESS3-1)")
                elif newly_awarded:
                    st.success("✅ Correct! +15 XP! Satellites take images of the same areas repeatedly (daily, weekly, yearly), allowing scientists to track how urban areas expand into farmland or forests. (MSS HS-ESS3-1)")
                else:
                    st.success("✅ Correct! Satellites take images of the same areas repeatedly, allowing scientists to track how urban areas expand. (MSS HS-ESS3-1)")
            else:
                st.error("❌ Not quite. Consider how comparing images from the same location over months or years can reveal patterns of change.")
    
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
            - **Lake ice** formation and breakup
            """)
            
            st.markdown("#### Real-World Applications:")
            st.success("✅ Tracking polar ice melt\n\n✅ Predicting sea level rise\n\n✅ Understanding climate feedback\n\n✅ Water resource planning")
            
            st.markdown("#### Michigan Application:")
            st.info("🧊 **Great Lakes Ice:** Satellites track ice coverage on all five Great Lakes. The 2013-2014 winter saw 92.5% ice coverage—the most since 1979. Ice coverage affects shipping, lake-effect snow, and spring water temperatures.")
        
        with col2:
            st.metric("2023-24 Great Lakes Ice", "~25%", "maximum coverage")
        
        # Tab-Specific Quick Check for Ice & Snow
        st.markdown("---")
        st.markdown("### 🧠 Ice & Snow Quick Check")
        
        ice_q1 = st.radio(
            "**Question 1:** What is the ice-albedo feedback, and why does it matter for climate?",
            ["A) Ice reflects sunlight; when it melts, darker water absorbs more heat, accelerating warming",
             "B) Ice makes the planet colder, so less ice is good",
             "C) Albedo is a type of ice cream",
             "D) Ice and albedo are unrelated"],
            key="ice_q1"
        )
        
        if st.button("Check Answer", key="check_ice_q1"):
            if ice_q1 == "A) Ice reflects sunlight; when it melts, darker water absorbs more heat, accelerating warming":
                if award_xp(15, "ice_q1", "🌟 First Steps" if not st.session_state.achievements else None):
                    st.balloons()
                    st.success("✅ Correct! +15 XP! White ice has high albedo (reflects ~80% of sunlight), while dark ocean water has low albedo (absorbs ~90% of sunlight). As ice melts, more dark surface is exposed, absorbing more heat, causing more melting—a positive feedback loop. (MSS HS-ESS2-2)")
                else:
                    st.success("✅ Correct! White ice has high albedo (reflects ~80% of sunlight), while dark ocean water absorbs ~90% of sunlight. This creates a feedback loop that amplifies warming. (MSS HS-ESS2-2)")
            else:
                st.error("❌ Not quite. Think about the difference between wearing a white shirt vs. a black shirt on a sunny day, and apply that to ice vs. water.")
        
        st.markdown("---")
        
        ice_q2 = st.radio(
            "**Question 2:** How does Great Lakes ice coverage affect Michigan's winter weather?",
            ["A) More ice coverage = less lake-effect snow because ice prevents water evaporation",
             "B) Ice coverage has no effect on weather",
             "C) More ice always means more snow",
             "D) Ice makes the lakes warmer"],
            key="ice_q2"
        )
        
        if st.button("Check Answer", key="check_ice_q2"):
            if ice_q2 == "A) More ice coverage = less lake-effect snow because ice prevents water evaporation":
                newly_awarded = award_xp(15, "ice_q2")
                # Check for Ice Master achievement
                if "ice_q1" in st.session_state.completed_checks and "ice_q2" in st.session_state.completed_checks:
                    if "🧊 Ice Expert" not in st.session_state.achievements:
                        st.session_state.achievements.append("🧊 Ice Expert")
                        st.balloons()
                        st.success("✅ Correct! +15 XP! 🎖️ Achievement Unlocked: Ice Expert! Lake-effect snow requires open water so moisture can evaporate into cold air. When lakes freeze over, this moisture source is cut off. (MSS HS-ESS2-4)")
                    else:
                        st.success("✅ Correct! Lake-effect snow requires open water so moisture can evaporate into cold air. When lakes freeze over, this moisture source is cut off. (MSS HS-ESS2-4)")
                elif newly_awarded:
                    st.success("✅ Correct! +15 XP! Lake-effect snow requires open water so moisture can evaporate into cold air. When lakes freeze over, this moisture source is cut off, reducing lake-effect snow. (MSS HS-ESS2-4)")
                else:
                    st.success("✅ Correct! Lake-effect snow requires open water so moisture can evaporate into cold air. When lakes freeze, lake-effect snow decreases. (MSS HS-ESS2-4)")
            else:
                st.error("❌ Not quite. Think about where the moisture for lake-effect snow comes from and what happens when that source gets covered by ice.")
        
        # Check for Satellite Scholar achievement (all 8 satellite questions)
        satellite_checks = {"atmo_q1", "atmo_q2", "ocean_q1", "ocean_q2", "land_q1", "land_q2", "ice_q1", "ice_q2"}
        if satellite_checks.issubset(st.session_state.completed_checks):
            if "🛰️ Satellite Scholar" not in st.session_state.achievements:
                st.session_state.achievements.append("🛰️ Satellite Scholar")
                award_xp(50, "satellite_scholar_bonus")
                st.balloons()
                st.success("🎖️ MAJOR ACHIEVEMENT UNLOCKED: Satellite Scholar! +50 Bonus XP! You've mastered all satellite monitoring concepts!")
    


def show_3d_printing():
    st.markdown('<div class="main-header">🖨️ 3D Printing Innovation</div>', unsafe_allow_html=True)
    st.markdown('<p class="developer-credit">Developed by Xavier Honablue, M.Ed. for Grosse Pointe South High School</p>', unsafe_allow_html=True)
    
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
    
    # Michigan Connection
    st.markdown("""
    <div class="michigan-box">
    <h4>🚗 Michigan Connection</h4>
    <p>Michigan's automotive industry is a leader in additive manufacturing! Companies in Detroit and 
    across the state use 3D printing for prototyping car parts, creating custom tooling, and even 
    manufacturing end-use components. The same technology advancing space satellites is driving 
    innovation in Michigan's economy.</p>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    # Quick Check for 3D Printing
    st.markdown("---")
    st.markdown("## 🧠 3D Printing Quick Check")
    
    printing_q = st.radio(
        "How does 3D printing technology relate to the MSS Engineering Design standard (HS-ETS1-3)?",
        ["A) 3D printing allows engineers to rapidly test and iterate designs, evaluating trade-offs between cost, weight, and performance",
         "B) 3D printing has nothing to do with engineering",
         "C) Engineers don't use 3D printing",
         "D) 3D printing only works for plastic toys"],
        key="printing_quiz"
    )
    
    if st.button("Check Answer", key="check_printing"):
        if printing_q == "A) 3D printing allows engineers to rapidly test and iterate designs, evaluating trade-offs between cost, weight, and performance":
            if award_xp(20, "printing_q1", "🌟 First Steps" if not st.session_state.achievements else None):
                st.balloons()
                st.success("✅ Correct! +20 XP! HS-ETS1-3 emphasizes evaluating solutions based on prioritized criteria and trade-offs. 3D printing enables engineers to quickly produce prototypes, test different designs, and optimize for multiple constraints. (MSS HS-ETS1-3)")
            else:
                st.success("✅ Correct! HS-ETS1-3 emphasizes evaluating solutions based on prioritized criteria and trade-offs. 3D printing enables rapid prototyping and optimization. (MSS HS-ETS1-3)")
        else:
            st.error("❌ Not quite. Think about how being able to quickly and cheaply produce prototypes helps engineers make better decisions.")

def show_design_challenge():
    st.markdown('<div class="main-header">🎨 Design Challenge</div>', unsafe_allow_html=True)
    st.markdown('<p class="developer-credit">Developed by Xavier Honablue, M.Ed. for Grosse Pointe South High School</p>', unsafe_allow_html=True)
    
    st.markdown("## 🚀 Design Your Own Satellite Mission!")
    
    st.info("""
    **Your Task:** You are a satellite engineer! Design a satellite mission to solve an Earth Science problem. 
    Consider what you'll measure, how many satellites you need, and how 3D printing technology will help.
    
    **Michigan Science Standard Alignment:** This activity addresses HS-ETS1-3 (Engineering Design) by having 
    you evaluate trade-offs and constraints in designing a real-world solution.
    """)
    
    # Select scenario
    st.markdown("### Step 1: Choose Your Mission Type")
    
    scenarios = {
        "🌊 Great Lakes Monitoring": {
            "description": "Monitor water quality, ice coverage, and ecosystem health across all five Great Lakes",
            "measures": ["Water temperature", "Algal bloom detection", "Ice extent", "Water levels", "Sediment plumes"],
            "challenges": "Great Lakes cover 94,250 square miles and conditions change rapidly with seasons",
            "michigan_relevance": "Direct impact on Michigan's drinking water, fishing industry, shipping, and tourism"
        },
        "🌀 Hurricane & Storm Tracking": {
            "description": "Track and predict severe storms in the Atlantic Ocean and Great Lakes region",
            "measures": ["Wind speed", "Air pressure", "Sea surface temperature", "Cloud patterns"],
            "challenges": "Storms move fast and need constant monitoring; lake-effect events develop quickly",
            "michigan_relevance": "Lake-effect snow events can dump several feet of snow in hours on Michigan communities"
        },
        "🌾 Michigan Agriculture Monitoring": {
            "description": "Monitor crop health, soil moisture, and drought conditions across Michigan farmland",
            "measures": ["Vegetation health (NDVI)", "Soil moisture", "Surface temperature", "Precipitation"],
            "challenges": "Michigan's 9.8 million acres of farmland span diverse climate zones",
            "michigan_relevance": "Michigan's $104.7 billion agriculture industry depends on accurate monitoring"
        },
        "🧊 Arctic & Great Lakes Ice Monitoring": {
            "description": "Monitor polar ice and Great Lakes ice coverage to understand climate change",
            "measures": ["Ice thickness", "Ice extent", "Surface temperature", "Melt rates"],
            "challenges": "Polar regions are remote; Great Lakes ice affects regional climate",
            "michigan_relevance": "Great Lakes ice coverage directly affects Michigan's winter weather and spring temperatures"
        }
    }
    
    mission_type = st.selectbox("Select your mission:", list(scenarios.keys()))
    
    with st.expander("📋 Mission Details"):
        st.write(f"**Goal:** {scenarios[mission_type]['description']}")
        st.write(f"**Challenge:** {scenarios[mission_type]['challenges']}")
        st.write(f"**Michigan Relevance:** {scenarios[mission_type]['michigan_relevance']}")
        st.write("**Suggested Measurements:**")
        for measure in scenarios[mission_type]['measures']:
            st.write(f"- {measure}")
    
    st.markdown("---")
    st.markdown("### Step 2: Design Your Mission")
    
    with st.form("mission_design"):
        col1, col2 = st.columns(2)
        
        with col1:
            mission_name = st.text_input("Mission Name:", placeholder="e.g., GreatLakes-Watch-1")
            
            num_sats = st.slider("Number of Satellites:", 1, 20, 4)
            
            orbit_type = st.selectbox("Orbit Type:", 
                ["Low Earth Orbit (LEO) - 200-2000 km - Best for detailed imaging",
                 "Medium Earth Orbit (MEO) - 2000-35000 km - Balance of coverage and detail",
                 "Geostationary (GEO) - 35,786 km - Fixed position over one location",
                 "Polar Orbit - Passes over poles - Full Earth coverage"])
        
        with col2:
            mission_goal = st.text_area("Mission Goal (What problem will you solve?):", 
                placeholder="Describe the Earth science problem your mission will address...")
            
            instruments = st.multiselect("Select Instruments:",
                ["Multispectral Imager (visible/IR light)",
                 "Radar Altimeter (measures surface height)",
                 "Thermal Sensor (temperature)",
                 "Microwave Radiometer (through clouds)",
                 "SAR (Synthetic Aperture Radar - all weather)",
                 "Spectrometer (atmospheric composition)"])
        
        st.markdown("### Step 3: Consider Engineering Trade-offs")
        
        col3, col4 = st.columns(2)
        
        with col3:
            use_3d_printing = st.checkbox("Use 3D-printed fuel tanks?")
            if use_3d_printing:
                st.success("✅ Cost savings: ~$120,000 per satellite")
            
            data_priority = st.select_slider("Data Priority:",
                options=["Coverage (more area)", "Balanced", "Resolution (more detail)"])
        
        with col4:
            budget = st.select_slider("Budget Level:",
                options=["Low ($10M)", "Medium ($50M)", "High ($200M)"])
            
            timeline = st.select_slider("Development Timeline:",
                options=["Fast (1 year)", "Standard (3 years)", "Extended (5 years)"])
        
        st.markdown("### Step 4: Michigan Impact Statement")
        
        michigan_impact = st.text_area("How will your mission benefit Michigan specifically?",
            placeholder="Explain how your satellite mission will help Michigan communities, industries, or ecosystems...")
        
        submitted = st.form_submit_button("Submit Mission Design")
        
        if submitted:
            # Award XP for completing the design challenge
            if award_xp(50, "design_challenge"):
                if "🔧 Space Engineer" not in st.session_state.achievements:
                    st.session_state.achievements.append("🔧 Space Engineer")
                st.balloons()
                st.success("🎉 Mission Design Submitted! +50 XP! 🎖️ Achievement Unlocked: Space Engineer!")
            else:
                st.success("🎉 Mission Design Submitted!")
            
            # Calculate estimated cost
            base_cost = num_sats * 5000000  # $5M per satellite base
            if use_3d_printing:
                base_cost -= num_sats * 120000  # Savings from 3D printing
            
            st.markdown("### 📊 Mission Summary")
            
            summary_col1, summary_col2, summary_col3 = st.columns(3)
            
            with summary_col1:
                st.metric("Satellites", num_sats)
            with summary_col2:
                st.metric("Estimated Cost", f"${base_cost/1000000:.1f}M")
            with summary_col3:
                st.metric("Instruments", len(instruments))
            
            st.markdown(f"""
            **Mission:** {mission_name if mission_name else 'Unnamed Mission'}
            
            **Orbit:** {orbit_type.split(' - ')[0]}
            
            **Goal:** {mission_goal if mission_goal else 'Not specified'}
            
            **Michigan Impact:** {michigan_impact if michigan_impact else 'Not specified'}
            
            **3D Printing:** {'Yes - Cost optimized!' if use_3d_printing else 'No - Traditional manufacturing'}
            """)
            
            if use_3d_printing:
                st.info(f"💰 By using 3D-printed fuel tanks, you saved **${num_sats * 120000:,}** on this mission!")

def show_quiz():
    st.markdown('<div class="main-header">❓ Quiz & Assessment</div>', unsafe_allow_html=True)
    st.markdown('<p class="developer-credit">Developed by Xavier Honablue, M.Ed. for Grosse Pointe South High School</p>', unsafe_allow_html=True)
    
    st.markdown("## 📝 Lesson Assessment")
    st.info("Complete this quiz to check your understanding of satellites, 3D printing, and Earth observation. This assessment aligns with Michigan Science Standards.")
    
    with st.form("final_quiz"):
        st.markdown("### Part 1: Satellite Technology")
        
        q1 = st.radio(
            "**1.** What is the primary advantage of using satellites for Earth observation compared to ground-based measurements? (MSS HS-ESS3-5)",
            ["A) Satellites are cheaper than all ground stations",
             "B) Satellites provide global, consistent coverage that's impossible from the ground",
             "C) Satellites can predict the future",
             "D) Satellites don't need any power to operate"],
            key="quiz_q1"
        )
        
        q2 = st.radio(
            "**2.** How do satellites help scientists understand climate change in the Great Lakes region? (MSS HS-ESS2-2)",
            ["A) They only take photographs for tourism",
             "B) They measure ice coverage, water temperature, and levels over time to detect trends",
             "C) They control the weather",
             "D) They have no role in climate science"],
            key="quiz_q2"
        )
        
        st.markdown("### Part 2: 3D Printing Innovation")
        
        q3 = st.radio(
            "**3.** Why is 3D printing (additive manufacturing) considered revolutionary for spacecraft construction? (MSS HS-ETS1-3)",
            ["A) It only works for small toys",
             "B) It enables complex designs, reduces costs, and speeds up production",
             "C) Traditional manufacturing is always better",
             "D) 3D printing uses more material than traditional methods"],
            key="quiz_q3"
        )
        
        q4 = st.radio(
            "**4.** How does the innovation chain from 3D printing ultimately benefit Earth science research?",
            ["A) It doesn't - they're unrelated fields",
             "B) Lower satellite costs → more satellites → better data → improved understanding of Earth",
             "C) 3D printers can predict earthquakes",
             "D) Scientists prefer expensive satellites"],
            key="quiz_q4"
        )
        
        st.markdown("### Part 3: Michigan Connections")
        
        q5 = st.radio(
            "**5.** Why is satellite monitoring particularly important for the Great Lakes? (MSS HS-ESS2-5)",
            ["A) The Great Lakes are too small to study from space",
             "B) The Great Lakes cover a vast area affecting millions of people, making satellite data essential for monitoring water quality, ice, and levels",
             "C) Ground stations can monitor everything about the Great Lakes",
             "D) The Great Lakes never change"],
            key="quiz_q5"
        )
        
        q6 = st.radio(
            "**6.** What is the ice-albedo feedback effect, and how does it relate to Great Lakes monitoring? (MSS HS-ESS2-2)",
            ["A) Ice has nothing to do with climate",
             "B) When ice melts, darker water absorbs more heat, causing more warming - satellites track this feedback",
             "C) More ice always cools the planet permanently",
             "D) Albedo refers to the saltiness of water"],
            key="quiz_q6"
        )
        
        st.markdown("### Part 4: Short Answer")
        
        q7 = st.text_area(
            "**7.** Explain how a single technological advancement (like 3D-printed fuel tanks) can lead to improvements in our understanding of Earth's systems. Use the innovation chain concept in your answer. (MSS HS-ETS1-3, HS-ESS3-5)",
            key="quiz_q7"
        )
        
        q8 = st.text_area(
            "**8.** Describe one way that satellite data is used to protect Michigan's environment or economy. Be specific about what is measured and why it matters. (MSS HS-ESS3-1)",
            key="quiz_q8"
        )
        
        submitted = st.form_submit_button("Submit Quiz")
        
        if submitted:
            score = 0
            total = 6  # Multiple choice questions
            
            # Check answers
            if q1 == "B) Satellites provide global, consistent coverage that's impossible from the ground":
                score += 1
            if q2 == "B) They measure ice coverage, water temperature, and levels over time to detect trends":
                score += 1
            if q3 == "B) It enables complex designs, reduces costs, and speeds up production":
                score += 1
            if q4 == "B) Lower satellite costs → more satellites → better data → improved understanding of Earth":
                score += 1
            if q5 == "B) The Great Lakes cover a vast area affecting millions of people, making satellite data essential for monitoring water quality, ice, and levels":
                score += 1
            if q6 == "B) When ice melts, darker water absorbs more heat, causing more warming - satellites track this feedback":
                score += 1
            
            # Award XP based on score
            xp_earned = score * 10  # 10 XP per correct answer
            
            # Award quiz completion achievement
            if "quiz_complete" not in st.session_state.completed_checks:
                st.session_state.completed_checks.add("quiz_complete")
                if "📝 Quiz Champion" not in st.session_state.achievements:
                    st.session_state.achievements.append("📝 Quiz Champion")
                st.session_state.xp_points += xp_earned + 25  # Bonus 25 XP for completing
                
                # Check for perfect score
                if score == total:
                    if "🏆 Perfect Score" not in st.session_state.achievements:
                        st.session_state.achievements.append("🏆 Perfect Score")
                        st.session_state.xp_points += 50  # Bonus for perfect score
            
            st.markdown("---")
            st.markdown("### 📊 Results")
            
            percentage = (score / total) * 100
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Score", f"{score}/{total}")
            with col2:
                st.metric("Percentage", f"{percentage:.0f}%")
            with col3:
                st.metric("XP Earned", f"+{xp_earned + 25}")
            with col4:
                if percentage >= 80:
                    st.metric("Status", "Excellent! 🌟")
                elif percentage >= 60:
                    st.metric("Status", "Good Work! 👍")
                else:
                    st.metric("Status", "Keep Studying 📚")
            
            if percentage == 100:
                st.balloons()
                st.success("🎉 PERFECT SCORE! +50 Bonus XP! 🏆 Achievement Unlocked: Perfect Score! You have mastered satellites, 3D printing, and their applications to Earth science!")
            elif percentage >= 80:
                st.balloons()
                st.success("🎉 Great job! 🎖️ Achievement Unlocked: Quiz Champion! You have a strong understanding of the material!")
            elif percentage >= 60:
                st.info("👍 Good work! 🎖️ Achievement Unlocked: Quiz Champion! Review the sections where you missed questions to strengthen your understanding.")
            else:
                st.warning("📚 🎖️ Achievement Unlocked: Quiz Champion! Consider reviewing the lesson materials and trying the quick checks again to improve your score.")
            
            st.markdown("### Short Answer Feedback")
            st.info("Your short answer responses have been recorded. Your teacher will review questions 7 and 8.")

def show_resources():
    st.markdown('<div class="main-header">📚 Resources</div>', unsafe_allow_html=True)
    st.markdown('<p class="developer-credit">Developed by Xavier Honablue, M.Ed. for Grosse Pointe South High School</p>', unsafe_allow_html=True)
    
    st.markdown("## 🔗 Additional Learning Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🛰️ Satellite & Earth Science")
        
        st.markdown("""
        **NASA Earth Science**
        - [NASA Earth Observatory](https://earthobservatory.nasa.gov/)
        - [NASA Worldview](https://worldview.earthdata.nasa.gov/) - Real-time satellite imagery
        - [NASA Climate Kids](https://climatekids.nasa.gov/)
        
        **NOAA Resources**
        - [NOAA Satellites](https://www.nesdis.noaa.gov/)
        - [Great Lakes Environmental Research Lab](https://www.glerl.noaa.gov/)
        - [CoastWatch Great Lakes](https://coastwatch.glerl.noaa.gov/)
        
        **Michigan-Specific**
        - [Michigan Sea Grant](https://www.michiganseagrant.org/)
        - [EGLE - Environment, Great Lakes & Energy](https://www.michigan.gov/egle)
        """)
        
        st.markdown("### 🖨️ 3D Printing & Manufacturing")
        
        st.markdown("""
        **Learn About Additive Manufacturing**
        - [NASA 3D Printing in Space](https://www.nasa.gov/mission_pages/station/research/experiments/explorer/Investigation.html?#id=982)
        - [How 3D Printing Works](https://www.youtube.com/watch?v=Vx0Z6LplaMU) (Video)
        - [Velo3D Technology](https://www.velo3d.com/)
        """)
    
    with col2:
        st.markdown("### 📖 Michigan Science Standards")
        
        st.markdown("""
        **Standards Resources**
        - [Michigan Science Standards](https://www.michigan.gov/mde/services/academic-standards/science)
        - [NGSS Hub](https://www.nextgenscience.org/)
        
        **Standards Covered in This Lesson:**
        - HS-ESS2-2: Earth systems feedback
        - HS-ESS2-4: Water cycling
        - HS-ESS2-5: Water properties
        - HS-ESS3-1: Resources and hazards
        - HS-ESS3-5: Climate data analysis
        - HS-ETS1-3: Engineering design
        """)
        
        st.markdown("### 🎓 Career Connections")
        
        st.markdown("""
        **STEM Careers in This Field**
        - Satellite Engineer
        - Remote Sensing Scientist
        - Climate Data Analyst
        - Additive Manufacturing Engineer
        - Earth System Scientist
        - GIS Specialist
        - Aerospace Engineer
        
        **Michigan Employers**
        - Ford Motor Company (3D printing)
        - GM (additive manufacturing)
        - University of Michigan
        - Michigan State University
        - NOAA GLERL (Ann Arbor)
        """)
    
    st.markdown("---")
    st.markdown("### 📺 Recommended Videos")
    
    vid_col1, vid_col2, vid_col3 = st.columns(3)
    
    with vid_col1:
        st.markdown("""
        **🎬 How Satellites See Earth**
        
        NASA Earth Observation Overview
        """)
    
    with vid_col2:
        st.markdown("""
        **🎬 3D Printing Metal Parts**
        
        Metal Additive Manufacturing
        """)
    
    with vid_col3:
        st.markdown("""
        **🎬 Great Lakes from Space**
        
        Satellite View of the Great Lakes
        """)

def show_downloads():
    st.markdown('<div class="main-header">📥 Downloads</div>', unsafe_allow_html=True)
    st.markdown('<p class="developer-credit">Developed by Xavier Honablue, M.Ed. for Grosse Pointe South High School</p>', unsafe_allow_html=True)
    
    st.markdown("## 📄 Downloadable Materials")
    
    st.info("Download these materials for offline use or classroom distribution.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📝 Student Materials")
        
        st.markdown("""
        **Worksheets**
        - 📄 Satellite Observation Worksheet
        - 📄 3D Printing Comparison Chart
        - 📄 Design Challenge Template
        - 📄 Vocabulary Review Sheet
        
        **Graphic Organizers**
        - 📄 Innovation Chain Diagram
        - 📄 Earth Systems Connection Map
        - 📄 Michigan Great Lakes Data Sheet
        """)
        
        st.button("Download Student Packet (PDF)", key="download_student")
    
    with col2:
        st.markdown("### 👩‍🏫 Teacher Materials")
        
        st.markdown("""
        **Lesson Plans**
        - 📄 Full Lesson Plan (50-60 min)
        - 📄 Michigan Standards Alignment
        - 📄 Assessment Rubrics
        - 📄 Answer Keys
        
        **Extensions**
        - 📄 Advanced Activities
        - 📄 Cross-curricular Connections
        - 📄 Differentiation Strategies
        """)
        
        st.button("Download Teacher Packet (PDF)", key="download_teacher")
    
    st.markdown("---")
    st.markdown("### 🖼️ Presentation Materials")
    
    st.markdown("""
    - 📊 PowerPoint Presentation (editable)
    - 🖼️ High-resolution satellite images
    - 📹 Video clip collection links
    - 🗺️ Great Lakes maps and data
    """)
    
    st.button("Download Presentation Materials (ZIP)", key="download_presentation")

# Page routing
if st.session_state.page == 'home':
    show_home()
elif st.session_state.page == 'article':
    show_article()
elif st.session_state.page == 'objectives':
    show_objectives()
elif st.session_state.page == 'satellites':
    show_satellites()
elif st.session_state.page == '3d_printing':
    show_3d_printing()
elif st.session_state.page == 'design_challenge':
    show_design_challenge()
elif st.session_state.page == 'quiz':
    show_quiz()
elif st.session_state.page == 'resources':
    show_resources()
elif st.session_state.page == 'downloads':
    show_downloads()
else:
    show_home()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.8em;">
<p>Developed by Xavier Honablue, M.Ed. for Grosse Pointe South High School</p>
<p>Aligned with Michigan Science Standards (MSS) | Earth Science Grades 9-12</p>
<p>© 2026 | For educational use only</p>
</div>
""", unsafe_allow_html=True)
