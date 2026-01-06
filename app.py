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
        
        submitted = st.form_submit_button("🚀 Submit Mission Design")
    
    if submitted:
        st.session_state.activity_submitted = True
        
        st.balloons()
        
        st.success("## 🎉 Mission Design Complete!")
        
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
        if st.button("📥 Download Mission Plan"):
            mission_report = f"""
# SATELLITE MISSION PLAN: {mission_name}

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

---
*Created using Space Technology & Earth Science Interactive Lesson*
*Date: {datetime.now().strftime('%Y-%m-%d')}*
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
            "explanation": "Additive manufacturing is the process of building objects layer by layer, also known as 3D printing. It 'adds' material layer by layer instead of cutting it away."
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
            "explanation": "Fuel tanks hold propellant that allows satellites to make small adjustments to their position and orientation in space. Without fuel, satellites would drift out of position."
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
            "explanation": "3D printing can reduce production time from months to weeks and significantly lower costs, making satellite missions more affordable and accessible."
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
            "explanation": "When satellites are more affordable, more can be launched. More satellites means better coverage of Earth, more frequent measurements, and more accurate scientific data."
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
            "explanation": "Satellites are versatile tools that help us monitor many Earth systems including atmosphere, oceans, land surface, ice and snow, and much more."
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
            else:
                st.error(f"❌ Not quite. {q['explanation']}")
                st.session_state.quiz_answers[i] = False
        
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
        
        if percentage >= 80:
            st.success("🎉 Great job! You have a strong understanding of how space technology helps Earth Science!")
        elif percentage >= 60:
            st.info("👍 Good work! Review the material to strengthen your understanding.")
        else:
            st.warning("📖 Keep studying! Review the lesson sections and try again.")
    
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
    
    if st.button("Submit Exit Ticket"):
        if len(exit_response) > 50:
            st.success("✅ Exit ticket submitted! Great work today!")
            st.balloons()
        else:
            st.warning("Please write a more detailed response (at least 5 sentences).")

def show_resources():
    st.markdown('<div class="main-header">📚 Additional Resources</div>', unsafe_allow_html=True)
    
    st.markdown("## 🔗 Learn More")
    
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
        
        with st.expander("NOAA Satellites"):
            st.write("""
            **Website:** https://www.noaa.gov/satellites
            
            Information about weather and climate satellites operated by the National Oceanic 
            and Atmospheric Administration.
            
            **Best for:** Weather and ocean data, real-time satellite views
            """)
        
        with st.expander("ESA Earth Observation"):
            st.write("""
            **Website:** https://www.esa.int/Applications/Observing_the_Earth
            
            European Space Agency's Earth observation program with interactive tools and 
            educational resources.
            
            **Best for:** International perspective, educational activities
            """)
    
    with col2:
        st.markdown("### 🚀 Space Technology")
        
        with st.expander("Satellite Tracking"):
            st.write("""
            **Website:** https://www.n2yo.com/
            
            Track satellites in real-time as they orbit Earth! See where satellites are 
            right now and when they'll pass over your location.
            
            **Best for:** Interactive learning, real-time data
            """)
        
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
        
        **Satellite Tracker (N2YO)**
        [n2yo.com](https://www.n2yo.com/)
        - Live satellite tracking
        - Predict passes over your location
        - ISS spotting
        """)
    
    with col_int2:
        st.markdown("""
        ### Earth Observation Tools
        
        **NASA Worldview**
        [worldview.earthdata.nasa.gov](https://worldview.earthdata.nasa.gov/)
        - Real satellite imagery
        - Historical comparisons
        - Track events (fires, storms, etc.)
        
        **Climate Time Machine**
        [climate.nasa.gov/interactives/climate-time-machine](https://climate.nasa.gov/interactives/climate-time-machine)
        - Visualize climate change
        - See ice melt over time
        - Sea level changes
        """)
    
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

def show_downloads():
    st.markdown('<div class="main-header">📥 Downloads</div>', unsafe_allow_html=True)
    
    st.markdown("## Download Lesson Materials")
    
    st.info("Download these resources for offline use or printing!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📄 For Students")
        
        # Student handout
        student_handout = """# Student Handout: Space Technology & Earth Observation

**Name:** _________________________ **Date:** _____________ **Period:** _____

## The News Article

**Title:** Momentus shares spike after advancing 3D-printed fuel tank for spaceflight

**Read the full story:** https://finance.yahoo.com/news/momentus-develops-additive-manufactured-fuel-133000052.html

**Key Points:**
- Momentus Inc. created a 3D-printed fuel tank with Velo3D
- Will be tested on Vigoride-7 mission
- Uses metal additive manufacturing technology
- Could reduce costs and production time

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

## Continue Learning

### Interactive Practice:
- **IXL Science Lessons** - www.ixl.com/science
- NASA Eyes on the Earth (eyes.nasa.gov)
- NASA Worldview satellite imagery

---
*Interactive Lesson: Space Technology & Earth Science*
"""
        
        st.download_button(
            label="📥 Download Student Handout",
            data=student_handout,
            file_name="student_handout.txt",
            mime="text/plain"
        )
    
    with col2:
        st.markdown("### 👨‍🏫 For Teachers")
        
        # Teacher guide
        teacher_guide = """# Teacher Guide: Space Technology & Earth Science

## Lesson Overview
- **Duration:** 50-60 minutes
- **Grade Level:** 9-12
- **Subject:** Earth Science

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
- Show satellite images
- Present the Momentus article

### Direct Instruction (15 min)
- Satellites and Earth Science
- 3D printing technology
- Innovation chain reaction

### Guided Practice (15 min)
- Design Challenge activity
- Group work on satellite missions

### Discussion (10 min)
- Technology-science connection
- Real-world applications
- Career exploration

### Assessment (10 min)
- Quiz
- Exit ticket

## Resources
- Original article: https://finance.yahoo.com/news/momentus-develops-additive-manufactured-fuel-133000052.html
- IXL Science Lessons (homework)
- NASA Eyes on the Earth (demonstrations)
- NASA Worldview (real data)

---
*All resources are free and accessible to students*
"""
        
        st.download_button(
            label="📥 Download Teacher Guide",
            data=teacher_guide,
            file_name="teacher_guide.txt",
            mime="text/plain"
        )

# Main app logic
if teacher_mode:
    st.sidebar.info("👨‍🏫 **Teacher Mode Active**\n\nAdditional notes and guidance visible.")

# Route to appropriate page
page_functions = {
    'home': show_home,
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
    <p>Based on real news about Momentus's 3D-printed fuel tank innovation</p>
    <p><em>Exploring how technology drives scientific discovery</em></p>
</div>
""", unsafe_allow_html=True)
