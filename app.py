import os

import streamlit as st
from projects import car_analysis, network_analysis, contour_analysis, nigeria_timeline

st.set_page_config(page_title="Chib Odibeli - Portfolio", layout="centered", initial_sidebar_state="collapsed")

_APP_DIR = os.path.dirname(os.path.abspath(__file__))


def _resolve_profile_pic_path():
    for name in (
        "ProfilePic.png",
        "ProfilePic.jpg",
        "ProfilePic.jpeg",
        "ProfilePic.webp",
    ):
        p = os.path.join(_APP_DIR, name)
        if os.path.isfile(p):
            return p
    return None


def _portfolio_view_param() -> str:
    """Read `view` from the URL for deep-linking (e.g. Vercel iframe embeds)."""
    raw = st.query_params.get("view")
    if raw is None:
        return ""
    if isinstance(raw, list):
        return (raw[0] or "").strip() if raw else ""
    return str(raw).strip()


VIEW = _portfolio_view_param()

# --- CSS Styling for nickzuber.com aesthetic ---
st.markdown("""
<style>
    /* Reset and Base Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #1A1A1A;
        background-color: #FDF9F6 !important; /* Gentle warm cream background */
    }

    /* Hide Streamlit Header, Footer, and MainMenu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="collapsedControl"] {display: none;}
    
    /* Center and constrain maximum width */
    .block-container {
        max-width: 650px;
        padding-top: 4rem;
        padding-bottom: 5rem;
        padding-left: 1rem;
        padding-right: 1rem;
        margin: 0 auto;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        color: #1A1A1A !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }
    
    h1 { 
        font-size: 2.5rem !important; 
        margin-bottom: 0 !important; 
        letter-spacing: -0.02em; 
        background: linear-gradient(90deg, #FF0055, #FFC107, #00FFCC); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        animation: hueShift 10s infinite linear;
    }
    
    @keyframes hueShift {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
    
    h2 { 
        font-size: 1.4rem !important; 
        margin-top: 2.5rem !important; 
        border-bottom: none !important; 
        color: #6A1B9A !important; 
    }
    h3 { font-size: 1.1rem !important; margin-top: 1.5rem !important; }
    
    p, li {
        color: #4A4A4A;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    /* Links */
    a {
        color: #1A1A1A !important;
        text-decoration: underline;
        text-decoration-color: #E2E8F0;
        text-underline-offset: 4px;
        transition: text-decoration-color 0.2s ease;
    }
    a:hover {
        text-decoration-color: #1A1A1A;
    }
    
    /* Header links */
    .header-links {
        display: flex;
        gap: 15px;
        margin-top: 10px;
        margin-bottom: 30px;
        font-size: 0.9rem;
    }
    
    .header-links a {
        color: #718096 !important;
        text-decoration: none;
    }
    .header-links a:hover {
        color: #1A1A1A !important;
    }

    .header-forma-line {
        color: #4A4A4A;
        font-size: 0.95rem;
        margin-top: 0.5rem;
        margin-bottom: 0;
        line-height: 1.5;
    }
    a.header-forma-btn {
        display: inline-block;
        margin-top: 12px;
        padding: 10px 20px;
        background-color: #0a2342 !important;
        color: #9ecfff !important;
        text-decoration: none !important;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.95rem;
    }
    a.header-forma-btn:hover {
        opacity: 0.92;
        color: #c5e5ff !important;
    }

    /* Profile photo (top-left with header); only st.image() uses this in the app */
    [data-testid="stImage"] img {
        border-radius: 50%;
        border: 1px solid #E2E8F0;
        object-fit: cover;
        width: 112px !important;
        height: 112px !important;
        max-width: 112px !important;
    }

    /* Timeline & Projects */
    .timeline-item, .project-item {
        margin-bottom: 1.2rem;
    }
    .timeline-date {
        font-size: 0.85rem;
        color: #A0AEC0;
        min-width: 80px;
        display: inline-block;
    }
    .separator {
        color: #FF007F;
        margin: 0 8px;
        font-size: 1.1rem;
        font-weight: bold;
    }
    .item-title {
        font-weight: 600;
        color: #1A1A1A;
        font-size: 0.95rem;
    }
    .item-subtitle {
        font-size: 0.85rem;
        color: #718096;
        margin-top: 2px;
    }
    .project-tags {
        font-size: 0.75rem;
        color: #A0AEC0;
        margin-top: 6px;
        display: flex;
        gap: 10px;
    }
    .project-tags a {
        color: #A0AEC0 !important;
        text-decoration: none;
    }
    .project-tags a:hover {
        color: #1A1A1A !important;
        text-decoration: underline;
    }
    
    /* Interests list */
    .interests-list {
        list-style-type: none;
        padding-left: 0;
        margin-top: 1rem;
    }
    .interests-list li::before {
        content: "•";
        color: #CBD5E0;
        display: inline-block;
        width: 1em;
        margin-left: -1em;
    }

    /* Moving background blobs */
    .bg-blob {
        position: fixed;
        top: -150px;
        right: -100px;
        width: 700px;
        height: 700px;
        background: radial-gradient(circle at 40% 40%, rgba(255, 0, 122, 0.4) 0%, rgba(0, 255, 209, 0.3) 35%, rgba(122, 0, 255, 0.2) 60%, rgba(255, 255, 255, 0) 80%);
        border-radius: 50%;
        z-index: -10;
        opacity: 0.22;
        filter: blur(90px);
        animation: float 20s infinite alternate ease-in-out;
        pointer-events: none;
    }

    .bg-blob2 {
        position: fixed;
        bottom: -200px;
        left: -150px;
        width: 650px;
        height: 650px;
        background: radial-gradient(circle at 50% 50%, rgba(255, 170, 0, 0.4) 0%, rgba(255, 0, 85, 0.3) 40%, rgba(255, 255, 255, 0) 70%);
        border-radius: 50%;
        z-index: -11;
        opacity: 0.18;
        filter: blur(85px);
        animation: float2 18s infinite alternate ease-in-out;
        pointer-events: none;
    }
    
    @keyframes float {
        0% { transform: translate(0, 0) scale(1) rotate(0deg); }
        33% { transform: translate(-50px, 100px) scale(1.1) rotate(45deg); }
        66% { transform: translate(40px, -50px) scale(0.9) rotate(90deg); }
        100% { transform: translate(-70px, -80px) scale(1.05) rotate(135deg); }
    }

    @keyframes float2 {
        0% { transform: translate(0, 0) scale(1) rotate(0deg); }
        33% { transform: translate(60px, -100px) scale(1.15) rotate(-45deg); }
        66% { transform: translate(-40px, 60px) scale(0.95) rotate(-90deg); }
        100% { transform: translate(80px, 40px) scale(1.1) rotate(-135deg); }
    }
    
    /* Expander styling to match minimalist design */
    .streamlit-expanderHeader {
        font-size: 0.9rem !important;
        color: #4A4A4A !important;
        background-color: transparent !important;
        border: none !important;
        padding-left: 0 !important;
        font-weight: 500 !important;
    }
</style>

<!-- Background blob HTML -->
<div class="bg-blob"></div>
<div class="bg-blob2"></div>
""", unsafe_allow_html=True)

# --- Header Section (profile top-left) ---
_profile_pic = _resolve_profile_pic_path()
if _profile_pic:
    _hc1, _hc2 = st.columns([0.22, 0.78], gap="medium")
    with _hc1:
        st.image(_profile_pic, width=112)
    with _hc2:
        st.markdown("<h1>Chibuike 'Chib' Odibeli</h1>", unsafe_allow_html=True)
        st.markdown(
            "<p style='color: #718096; font-size: 1rem; margin-top: 0;'>Data Science Master's Student & Software Engineer</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p class='header-forma-line'>Solo Developer of Forma. Check it out below!</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
<div class="header-links">
    <a href="https://www.linkedin.com/in/chibuike-odibeli-862319220/" target="_blank">LinkedIn</a>
    <a href="mailto:chibuikeodibeli@gmail.com">Email</a>
</div>
<a class="header-forma-btn" href="https://forma-app.net" target="_blank" rel="noopener noreferrer">Forma</a>
""",
            unsafe_allow_html=True,
        )
else:
    st.markdown("<h1>Chibuike 'Chib' Odibeli</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #718096; font-size: 1rem; margin-top: 0;'>Data Science Master's Student & Software Engineer</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p class='header-forma-line'>Solo Developer of Forma. Check it out below!</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
<div class="header-links">
    <a href="https://www.linkedin.com/in/chibuike-odibeli-862319220/" target="_blank">LinkedIn</a>
    <a href="mailto:chibuikeodibeli@gmail.com">Email</a>
</div>
<a class="header-forma-btn" href="https://forma-app.net" target="_blank" rel="noopener noreferrer">Forma</a>
""",
        unsafe_allow_html=True,
    )

# --- About Myself ---
st.markdown("## About Myself")
st.markdown("""
<p>I am a Data Science Master's student at UMass Dartmouth and a Data-Driven Software Engineer. I am passionate about turning complex data into compelling stories, actionable insights, and robust software solutions.</p> 

<p>With a background in Software Engineering from Penn State, my work bridges the gap between machine learning research and full-stack application development. I've designed immersive VR AI chatbots, deployed quantized neural networks to edge devices, and modernized large-scale web applications.</p>
""", unsafe_allow_html=True)

# --- What I've Been Up To ---
st.markdown("## What I've Been Up To")

timeline_items = [
    {"date": "Jun 2025", "title": "Linux Server Admin", "company": "UMass Dartmouth"},
    {"date": "May 2024", "title": "Data-Driven Software Engineer", "company": "Jordan Brooke Estates"},
    {"date": "May 2023", "title": "Software Engineer", "company": "Erie Insurance"},
    {"date": "Aug 2020", "title": "Research Assistant", "company": "Penn State Erie"},
]

for item in timeline_items:
    st.markdown(f"""
    <div class="timeline-item">
        <span class="timeline-date">{item['date']}</span>
        <span class="separator">⊇</span>
        <span class="item-title">{item['title']}</span> <span style="color: #A0AEC0;">@ {item['company']}</span>
    </div>
    """, unsafe_allow_html=True)

# --- What I've Built ---
st.markdown("## What I've Built")

@st.dialog("Project Details")
def show_project_details(proj):
    st.markdown(f"### {proj['title']}")
    st.write(proj['details'])
    if proj['link']:
        st.link_button("View Live Project", proj['link'])

projects = [
    {
        "title": "Audio Deepfake Detection",
        "subtitle": "PyTorch, Librosa, Spectral Analysis • Multimodal hybrid CNN-LSTM system addressing synthetic media threats (ROC-AUC 0.94).",
        "details": "This project addressed the growing threat of synthetic media by developing a robust detection framework for audio deepfakes. It combined Convolutional Neural Networks (CNNs) to extract fine-grained spatial features from mel-spectrograms, and Long Short-Term Memory (LSTMs) networks to model temporal dependencies. Trained on extensive datasets of authentic and generated audio, the hybrid architecture achieved a 0.94 ROC-AUC score, demonstrating resilience against compression algorithms and background noise.",
        "link": None
    },
    {
        "title": "Edge-Deployed Neural Networks",
        "subtitle": "C++, Xilinx Vivado HLS, PYNQ • Porting quantized ML models onto FPGA logic for 20x speedup and 60% power reduction.",
        "details": "Focused on optimizing deep learning models for resource-constrained edge devices. The workflow involved quantizing neural networks and translating their C++ implementations into hardware description via Xilinx Vivado HLS. Designed custom hardware accelerators targeting the Zynq-7000 SoC architecture, utilizing the PYNQ framework for high-level hardware-software abstraction.Validated designs via Vivado simulation, demonstrating a theoretical 20x speedup in inference latency and an estimated 60% reduction in power consumption compared to baseline ARM-based software execution",
        "link": None
    },
    {
        "title": "Voice-Automated AI Chatbot (VR)",
        "subtitle": "Llama 2 (QLoRA), Unity, AWS • Immersive voice-activated tutor for medical students in virtual reality.",
        "details": "An immersive educational tool built in Unity that simulates realistic clinical scenarios for medical practitioners. The core intelligence is powered by a parameter-efficient fine-tuned Llama 2 model (using QLoRA). The architecture is distributed, relying on AWS infrastructure to host the LLM and bridge real-time Speech-to-Text and Text-to-Speech services. This created a low-latency, hands-free conversational experience within VR.",
        "link": None
    },
    {
        "title": "Stock Market Forecasting",
        "subtitle": "Python, Prophet, Azure, Power BI • End-to-end pipeline predicting OHLCV data with automated cloud storage.",
        "details": "A comprehensive data engineering and predictive modeling pipeline designed for equity markets. The automated system reliably scrapes daily Open, High, Low, Close, and Volume (OHLCV) data, staging it in Azure Blob Storage. Meta's Prophet algorithm analyzes the time-series trends to forecast future price movements. Finally, this data flows into a dynamic Power BI report, providing stakeholders with intuitive visualizations of historical trends and short-term projections.",
        "link": "https://app.powerbi.com/links/DS54-3Zmjn?ctid=328d6c0d-0f2f-4b76-9310-9762ba1c3e2d&pbi_source=linkShare&bookmarkGuid=b7a06065-d696-442f-8e4f-52b489fc6a0d"
    }
]

for i, proj in enumerate(projects):
    st.markdown(f"""
    <div class="project-item" style="margin-bottom: 0.3rem;">
        <div class="item-title">{proj['title']}</div>
        <div class="item-subtitle">{proj['subtitle']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("View Project", key=f"view_proj_{i}"):
        show_project_details(proj)
    
    st.markdown("<div style='margin-bottom: 1.2rem;'></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Interactive Projects (Streamlit Apps)
st.markdown("<div class='item-title' style='margin-bottom: 0.8rem;'>Interactive Visualizations</div>", unsafe_allow_html=True)

@st.dialog("Car Data Analysis", width="large")
def show_car_analysis_dialog():
    car_analysis.app()

with st.expander(
    "Car Data Analysis ⊇ Altair interactive dashboard",
    expanded=(VIEW == "car_analysis"),
):
    st.markdown("This visualization is optimized for a larger view to prevent charts from spilling over.")
    if st.button("Open Dashboard", key="car_analysis_btn"):
        show_car_analysis_dialog()

with st.expander(
    "Co-Authorship Network ⊇ D3.js force-directed graph",
    expanded=(VIEW == "network_analysis"),
):
    network_analysis.app()

with st.expander(
    "Contour Analysis ⊇ Medical imaging density contours",
    expanded=(VIEW == "contour_analysis"),
):
    contour_analysis.app()

with st.expander(
    "Nigeria Economic Timeline ⊇ Historical data visualization",
    expanded=(VIEW == "nigeria_timeline"),
):
    nigeria_timeline.app()

if VIEW == "car_analysis" and not st.session_state.get(
    "_portfolio_auto_car_dialog_shown", False
):
    st.session_state._portfolio_auto_car_dialog_shown = True
    show_car_analysis_dialog()

# --- Interests / Readings ---
st.markdown("## Interests / Readings")
st.markdown("""
<ul class="interests-list">
    <li>Machine Learning Architecture</li>
    <li>Distributed Systems</li>
    <li>Science Fiction</li>
    <li>Community Technology Education</li>
</ul>
<br>
""", unsafe_allow_html=True)
