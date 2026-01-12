import streamlit as st
from projects import car_analysis, network_analysis, contour_analysis, price_prediction

st.set_page_config(page_title="Chib Odibeli - Portfolio", layout="wide")

# --- CSS Styling ---
st.markdown("""
<style>
    .big-font {
        font-size:50px !important;
        font-weight: bold;
        background: linear-gradient(to right, #FF4B4B, #FF9068);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subheader-font {
        font-size:24px !important;
        font-weight: 500;
        color: #555;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f9fa;
        border: 1px solid #e0e0e0;
        margin-bottom: 20px;
        transition: transform 0.2s, box-shadow 0.2s; 
    }
    .card:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-color: #FF4B4B;
    }
    .skill-tag {
        display: inline-block;
        background-color: #FF4B4B;
        color: white;
        padding: 5px 10px;
        margin: 3px;
        border-radius: 15px;
        font-size: 14px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Contact"])

# --- HOME SECTION ---
if selection == "Home":
    st.markdown('<p class="big-font">Chibuike ‘Chib’ Odibeli</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader-font">Data Science Master\'s Student | Data-Driven Software Engineer</p>', unsafe_allow_html=True)
    st.markdown("Turning complex data into compelling stories, actionable insights, and robust software solutions.")
    
    st.markdown("---")
    
    st.header("🚀 Featured Highlights")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="card">
            <h3>🤖 Machine Learning</h3>
            <p>From predicting car prices to detecting audio deepfakes and deploying neural networks on edge devices.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
            <h3>📊 Data Visualization</h3>
            <p>Interactive dashboards using Altair and D3.js to explore complex datasets like academic networks and medical imaging.</p>
        </div>
        """, unsafe_allow_html=True)

# --- ABOUT ME SECTION ---
elif selection == "About Me":
    st.header("About Me")
    
    tab1, tab2, tab3 = st.tabs(["Education", "Experience", "Skills"])
    
    with tab1:
        st.subheader("🎓 Education")
        st.markdown("""
        **University of Massachusetts Dartmouth** | Dartmouth, MA  
        *Master of Science in Data Science* | **GPA: 4.0** | *Expected: June 2026*
        
        **The Pennsylvania State University** | Erie, PA  
        *Bachelor of Science in Software Engineering* | **GPA: 3.5** | *August 2024*  
        *Certifications: Entry Certificate in Business Analysis (ECBA) – IIBA, 2024*
        """)
        
    with tab2:
        st.subheader("💼 Work Experience")
        
        st.markdown("### Data-Driven Software Engineer | **Jordan Brooke Estates**")
        st.caption("05/2024 - 12/2025")
        st.markdown("""
        - **Automated Complaint Classification**: Built an ML model with **92% accuracy**, utilizing various classifiers to categorize feedback and reduce manual entry.
        - **Full-Stack Pipeline**: Designed a data pipeline using **Spring Boot** and **MySQL** to process organizational feedback.
        - **Actionable Insights**: Created visualization dashboards to track complaint resolution metrics for management.
        - **DevOps**: Streamlined deployment using **Docker** containers to improve CI/CD reliability.
        """)
        
        st.divider()
        
        st.markdown("### Software Engineer | **Erie Insurance**")
        st.caption("05/2023 - 01/2024")
        st.markdown("""
        - **Full Stack Development**: Developed web applications using HTML, CSS, JS, **Spring Framework**, and MySQL.
        - **Modernization**: Led the conversion of legacy **AngularJS** components to **React**, improving User Experience scores by **45%**.
        - **Collaboration**: Worked closely with tech leads and cross-functional stakeholders.
        """)
        
        st.divider()
        
        st.markdown("### Research Assistant | **Penn State Erie**")
        st.caption("08/2020 - 06/2023")
        st.markdown("""
        - **VR Development**: Built a Virtual Reality environment in **Unity** to teach industrial engineering concepts.
        - **Publication**: Co-authored a paper detailing the development process and educational impact.
        """)

    with tab3:
        st.subheader("🛠️ Technical Skills")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Languages**")
            st.markdown("`Python` `Java` `SQL` `R` `C#` `JavaScript` `HTML/CSS`")
            
            st.markdown("**Frameworks**")
            st.markdown("`Tensorflow` `Spring` `React` `MongoDB`")
            
        with col2:
            st.markdown("**Technologies & Tools**")
            st.markdown("`AWS` `Azure` `Docker` `Git` `Hadoop` `Spark`")
            
            st.markdown("**Visualization**")
            st.markdown("`Power BI` `Tableau` `Matplotlib` `Altair` `D3.js`")

# --- PROJECTS SECTION ---
elif selection == "Projects":
    cat_selection = st.sidebar.radio("Category", ["Data Visualization", "Machine Learning"])
    
    if cat_selection == "Data Visualization":
        viz_selection = st.sidebar.radio("Project", ["Car Analysis", "Co-Authorship Network", "Contour Analysis"])
        if viz_selection == "Car Analysis":
            car_analysis.app()
        elif viz_selection == "Co-Authorship Network":
            network_analysis.app()
        elif viz_selection == "Contour Analysis":
            contour_analysis.app()
            
    elif cat_selection == "Machine Learning":
        ml_selection = st.sidebar.radio("Project", [
            "Used Car Price Prediction", 
            "Audio Deepfake Detection", 
            "Edge-Deployed Neural Networks",
            "Voice-Automated AI Chatbot"
        ])
        
        if ml_selection == "Used Car Price Prediction":
            price_prediction.app()
            
        elif ml_selection == "Audio Deepfake Detection":
            st.header("Audio Deepfake Detection")
            st.image("https://placehold.co/800x300?text=Multimodal+Deepfake+Detection", caption="Project Concept Art")
            st.markdown("""
            ### 🕵️‍♂️ Project Overview
            **Period**: 08/2025 - 12/2025
            
            Developed a robust multimodal system to detect AI-generated audio deepfakes. The system combines acoustic features, spectral representations, and metadata signals to distinguish real human speech from synthesized audio.
            
            #### Key Achievements
            - **Multimodal Fusion**: Integrated various signal processing techniques to analyze audio artifacts that are imperceptible to the human ear.
            - **Robust Evaluation**: Trained and tested models using metrics like **ROC-AUC**, precision, and recall to ensure reliability across different deepfake generation methods.
            - **Research Impact**: Contributed to the growing field of media forensics and AI safety.
            
            **Tech Stack**: Python, TensorFlow/PyTorch, Librosa, Scikit-learn.
            """)
            
        elif ml_selection == "Edge-Deployed Neural Networks":
            st.header("Edge-Deployed Neural Networks")
            st.image("https://placehold.co/800x300?text=FPGA+Neural+Networks", caption="Hardware Acceleration")
            st.markdown("""
            ### ⚡ Project Overview
            **Period**: 08/2025 - 12/2025
            
            Focused on optimizing neural networks for deployment on resource-constrained edge devices (FPGAs).
            
            #### Key Achievements
            - **Quantization**: implemented low-bit and binary network quantization to reduce model size without significant accuracy loss.
            - **Hardware Synthesis**: Deployed models using **High-Level Synthesis (HLS)** to FPGAs, optimizing for latency, throughput, and memory usage.
            - **Trade-off Analysis**: Conducted extensive hardware-aware optimization to balance accuracy vs. resource/energy consumption.
            
            **Tech Stack**: C++, HLS, FPGA, Python.
            """)
            
        elif ml_selection == "Voice-Automated AI Chatbot":
            st.header("Voice-Automated AI Chatbot (VR)")
            st.image("https://placehold.co/800x300?text=AI+Voice+Chatbot", caption="VR Integration")
            st.markdown("""
            ### 🗣️ Project Overview
            **Period**: 08/2023 - 07/2024
            
            Built an immersive voice-automated AI assistant for a Virtual Reality learning application focused on anatomy (learning bones).
            
            #### Key Achievements
            - **LLM Fine-Tuning**: Fine-tuned a **LLAMA** model using **QLoRA** to specialize the bot in medical/anatomical queries.
            - **Cloud Infrastructure**: Hosted the application infrastructure on an **AWS EC2** instance.
            - **Serverless Architecture**: Implemented **AWS Lambda** functions and a REST API to handle voice requests and responses efficiently.
            
            **Tech Stack**: LLAMA, QLoRA, AWS (EC2, Lambda), Unity (VR), Python.
            """)

# --- CONTACT SECTION ---
elif selection == "Contact":
    st.header("📬 Get In Touch")
    
    st.markdown("""
    I am always open to discussing new opportunities, collaborations, or data science projects.
    
    <div class="card">
        <h4>📧 Email</h4>
        <a href="mailto:chibuikeodibeli@gmail.com" style="text-decoration: none; color: #FF4B4B; font-weight: bold;">chibuikeodibeli@gmail.com</a>
    </div>
    
    <div class="card">
        <h4>🔗 LinkedIn</h4>
        <a href="https://www.linkedin.com/in/chibuike-odibeli-862319220/" target="_blank" style="text-decoration: none; color: #FF4B4B; font-weight: bold;">Visit My Profile</a>
    </div>
    
    <div class="card">
        <h4>📍 Location</h4>
        <p>Harrisburg, PA</p>
    </div>
    
    <div class="card">
        <h4>📞 Phone</h4>
        <p>(646) 981-3285</p>
    </div>
    """, unsafe_allow_html=True)
