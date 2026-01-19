import streamlit as st
from projects import car_analysis, network_analysis, contour_analysis, price_prediction

st.set_page_config(page_title="Chib Odibeli - Portfolio", layout="wide")

# --- CSS Styling ---
st.markdown("""
<style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #FFEFBA 0%, #FFFFFF 100%);
        background-attachment: fixed;
    }
    
    /* Header Styling */
    h1, h2, h3 {
        color: #5D2E2E !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    .big-font {
        font-size:50px !important;
        font-weight: bold;
        background: linear-gradient(to right, #D35400, #800000); 
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .subheader-font {
        font-size:24px !important;
        font-weight: 500;
        color: #8B4513; /* SaddleBrown */
    }
    
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.95); /* Slight transparency */
        border-left: 5px solid #D35400; /* Orange-Red accent border */
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        transition: transform 0.2s, box-shadow 0.2s; 
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        border-color: #800000; /* Darker maroon on hover */
    }
    
    .skill-tag {
        display: inline-block;
        background: linear-gradient(to right, #D35400, #E67E22);
        color: white;
        padding: 5px 12px;
        margin: 5px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
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
            st.markdown("""
            ### 🕵️‍♂️ Project Overview
            **Period**: 08/2025 - 12/2025
            
            This project addresses the critical security threat posed by synthetic media. I developed a comprehensive multimodal detection system designed to distinguish between authentic human speech and AI-generated audio (deepfakes) produced by state-of-the-art TTS and Voice Conversion models.
            
            #### 🔬 Technical Architecture & Methodology
            - **Feature Extraction**: moved beyond simple waveform analysis to extract high-dimensional acoustic features, including **Mel-Frequency Cepstral Coefficients (MFCCs)**, **Chromagrams**, and **Mel-spectrograms**.
            - **Spectral Analysis**: Implemented Fast Fourier Transform (FFT) based analysis to detect high-frequency artifacts and spectral inconsistencies often left behind by vocoders (e.g., WaveNet, HiFi-GAN).
            - **Deep Learning Model**: Designed a hybrid architecture combining **Convolutional Neural Networks (CNNs)** for spatial feature learning from spectrograms and **Recurrent Neural Networks (LSTMs)** to capture temporal dependencies in speech patterns.
            
            #### 🚀 Key Results
            - **Dataset Construction**: Curated a balanced dataset including samples from the ASVspoof challenge and real-world celebrity voice clips.
            - **Performance**: Achieved an **ROC-AUC score of 0.94** on the test set, demonstrating high sensitivity to subtle synthetic artifacts.
            - **Generalization**: Successfully detected deepfakes from unseen generators, proving the model learned generalized artifacts rather than source-specific noise.
            
            **Tech Stack**: Python, PyTorch, Librosa, Scikit-learn, Matplotlib (for spectral visualization).
            """)
            
        elif ml_selection == "Edge-Deployed Neural Networks":
            st.header("Edge-Deployed Neural Networks")
            st.markdown("""
            ### ⚡ Project Overview
            **Period**: 08/2025 - 12/2025
            
            This project focused on the challenge of bringing deep learning to resource-constrained environments. The goal was to deploy a functional neural network onto an **FPGA (Field-Programmable Gate Array)**, optimizing for low latency and high energy efficiency without sacrificing model accuracy.
            
            #### 🛠️ Engineering Challenges & Solutions
            - **Hardware-Software Co-Design**: Utilized **Xilinx Vivado HLS** (High-Level Synthesis) to convert a Python/C++ defined neural network into Register Transfer Level (RTL) logic.
            - **Quantization Strategy**: Transformed 32-bit floating-point weights into **8-bit fixed-point integers**. This reduced memory bandwidth requirements by **4x** and significantly decreased logic utilization (LUTs/Flip-Flops) with less than 1% drop in accuracy.
            - **Parallelization**: Implemented **Loop Unrolling** and **Pipelining** directives in the HLS code to maximize the parallel processing capabilities of the FPGA fabric, achieving massive throughput improvements over CPU inference.
            
            #### 📊 Performance Metrics
            - **Platform**: Deployed on a **PYNQ-Z2** development board.
            - **Speedup**: Achieved a **20x inference speedup** compared to running the same unoptimized model on the board's embedded ARM Cortex-A9 processor.
            - **Energy**: Reduced power consumption per inference by **60%**, making it suitable for battery-operated IoT edge devices.
            
            **Tech Stack**: C++, Xilinx Vivado HLS, PYNQ Framework, Python, Jupyter Notebooks (for on-board control).
            """)
            
        elif ml_selection == "Voice-Automated AI Chatbot":
            st.header("Voice-Automated AI Chatbot (VR)")
            st.markdown("""
            ### 🗣️ Project Overview
            **Period**: 08/2023 - 07/2024
            
            Designed and implemented an immersive, voice-activated AI tutor integrated into a Virtual Reality anatomy learning environment. This system allows medical students to ask questions about bone structures and receive instant, context-aware verbal responses while navigating a 3D space.
            
            #### ☁️ Cloud Architecture & Immersive Integration
            - **Speech-to-Text (STT)**: Integrated **OpenAI Whisper** models to transcribe user voice commands with high accuracy, handling medical terminology effectively.
            - **LLM Customization**: Fine-tuned a **Llama 2** foundation model using **QLoRA (Quantized Low-Rank Adaptation)** on a custom dataset of anatomical Q&A pairs. This ensured the bot acted as a knowledgeable tutor rather than a generic assistant.
            - **Serverless Backend**: Built a scalable API using **AWS Lambda** and **API Gateway**. The VR headset sends audio data to the cloud, where it is processed, queried against the LLM, and synthesized back to speech (TTS).
            - **Unity Integration**: Developed C# scripts within Unity to handle real-time audio recording, API communication, and lip-sync synchronization for the 3D avatar.
            
            #### 🎓 Impact
            - **User Experience**: Eliminated the need for hand controllers to type queries, maintaining immersion and "flow" in the VR simulation.
            - **Latency Optimization**: Optimized the cloud pipeline to achieve sub-2-second end-to-end response time using warm-start Lambda instances.
            
            **Tech Stack**: Llama 2 (LLM), QLoRA, AWS (Lambda, API Gateway, EC2), Unity (C#), OpenAI Whisper, Python.
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
