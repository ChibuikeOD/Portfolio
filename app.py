import os

import streamlit as st
from projects import car_analysis, network_analysis, contour_analysis, nigeria_timeline

st.set_page_config(page_title="Chib Odibeli - Portfolio", layout="centered", initial_sidebar_state="collapsed")

_APP_DIR = os.path.dirname(os.path.abspath(__file__))


def _resolve_profile_pic_path():
    for name in (
        "ProfilePic.jpeg",
        "ProfilePic.jpg",
        "ProfilePic.png",
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
        position: relative;
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
        font-size: 1.55rem !important; 
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

    .header-btn-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        align-items: center;
        margin-top: 12px;
    }
    a.header-forma-btn {
        display: inline-block;
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

    a.header-genresense-btn {
        display: inline-block;
        padding: 10px 20px;
        background-color: #1DB954 !important;
        color: #ffffff !important;
        text-decoration: none !important;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.95rem;
    }
    a.header-genresense-btn:hover {
        opacity: 0.92;
        color: #ffffff !important;
        background-color: #1ed760 !important;
    }

    a.header-fist-btn {
        display: inline-block;
        padding: 10px 20px;
        background-color: #5f0914 !important;
        color: #ffccd3 !important;
        text-decoration: none !important;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.95rem;
    }
    a.header-fist-btn:hover {
        opacity: 0.92;
        color: #ffeaed !important;
    }

    a.header-gmcp-btn {
        display: inline-block;
        padding: 10px 20px;
        background-color: #004d40 !important;
        color: #b2dfdb !important;
        text-decoration: none !important;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.95rem;
    }
    a.header-gmcp-btn:hover {
        opacity: 0.92;
        color: #e0f2f1 !important;
    }

    a.header-deltabench-btn {
        display: inline-block;
        padding: 10px 20px;
        background-color: #1a237e !important;
        color: #c5cae9 !important;
        text-decoration: none !important;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.95rem;
    }
    a.header-deltabench-btn:hover {
        opacity: 0.92;
        color: #e8eaf6 !important;
    }

    /* Projects Badge Styles */
    .projects-badge-container {
        display: inline-flex;
        align-items: center;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    .projects-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: linear-gradient(135deg, #FFF5F5 0%, #FFF 100%);
        border: 1px solid #FFE3E3;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        color: #E53E3E;
        letter-spacing: 0.05em;
        box-shadow: 0 2px 4px rgba(229, 62, 62, 0.05);
        animation: bounce 2.2s infinite ease-in-out;
    }
    .pulse-dot {
        width: 6px;
        height: 6px;
        background-color: #E53E3E;
        border-radius: 50%;
        box-shadow: 0 0 0 0 rgba(229, 62, 62, 0.7);
        animation: pulse 1.2s infinite cubic-bezier(0.66, 0, 0, 1);
    }
    @keyframes pulse {
        to {
            box-shadow: 0 0 0 6px rgba(229, 62, 62, 0);
        }
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-3px); }
    }
    @keyframes floatArrow {
        0%, 100% { transform: translate(0, 0); }
        50% { transform: translate(2px, 2px); }
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

    /* Photography Sidebars and Polaroid Styles */
    .photo-sidebar-left {
        position: absolute;
        bottom: 80px;
        left: -220px;
        width: 190px;
        display: flex;
        flex-direction: column;
        gap: 30px;
        z-index: 99;
    }
    .photo-sidebar-right {
        position: absolute;
        bottom: 80px;
        right: -220px;
        width: 190px;
        display: flex;
        flex-direction: column;
        gap: 30px;
        z-index: 99;
    }
    .photo-sidebar-title {
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 0.72rem;
        font-weight: bold;
        font-style: italic;
        color: #6A1B9A;
        border-bottom: 1px solid #E2E8F0;
        padding-bottom: 8px;
        margin-bottom: 4px;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        user-select: none;
    }
    .polaroid-card {
        background-color: #ffffff;
        padding: 10px 10px 24px 10px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 6px 15px rgba(0,0,0,0.08);
        border-radius: 2px;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        cursor: pointer;
        user-select: none;
    }
    .polaroid-card:hover {
        transform: rotate(0deg) scale(1.08) !important;
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
        z-index: 100;
    }
    .polaroid-img-container {
        width: 100%;
        aspect-ratio: 1;
        overflow: hidden;
        background-color: #f7f5f2;
        margin-bottom: 8px;
    }
    .polaroid-img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }
    .polaroid-card:hover .polaroid-img-container img {
        transform: scale(1.05);
    }
    .polaroid-caption {
        font-family: 'Georgia', serif;
        font-size: 0.68rem;
        text-align: center;
        color: #718096;
        font-style: italic;
    }
    
    /* Inline Gallery (for smaller screens) */
    .inline-photo-gallery {
        margin-top: 1.5rem;
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
        user-select: none;
    }
    
    @media (min-width: 1101px) {
        .inline-photo-gallery {
            display: none !important;
        }
    }
    
    @media (max-width: 1100px) {
        .photo-sidebar-left, .photo-sidebar-right {
            display: none !important;
        }
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
            "<p style='color: #718096; font-size: 1rem; margin-top: 0;'>Solo Developer of Forma. Check it out below!</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
<div class="header-links">
    <a href="https://www.linkedin.com/in/chibuike-odibeli-862319220/" target="_blank">LinkedIn</a>
    <a href="mailto:chibuikeodibeli@gmail.com">Email</a>
</div>
<div class="projects-badge-container">
    <div class="projects-badge">
      <span class="pulse-dot"></span>
      <span class="badge-text">✨ CLICK TO EXPLORE MY LIVE APPS:</span>
    </div>
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FF0055" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 8px; animation: floatArrow 1.2s infinite ease-in-out;">
        <line x1="7" y1="7" x2="17" y2="17"></line>
        <polyline points="17 7 17 17 7 17"></polyline>
    </svg>
</div>
<div class="header-btn-row">
    <a class="header-forma-btn" href="https://forma-app.net" target="_blank" rel="noopener noreferrer">Forma</a>
    <a class="header-genresense-btn" href="https://genre-sense.vercel.app/" target="_blank" rel="noopener noreferrer">GenreSense</a>
    <a class="header-forma-btn" href="https://app.powerbi.com/view?r=eyJrIjoiYTJjZmYxNDQtODRmNC00YmZjLWI0ZDQtZTYwMGVmNzMzZTFhIiwidCI6IjA1YjVmMDhmLTdkZWQtNDNjNS1iZTNmLWFmMDQyMDcwNzQxNCJ9" target="_blank" rel="noopener noreferrer">Daily Stock Price Prediction</a>
    <a class="header-fist-btn" href="https://path-of-the-fist.com" target="_blank" rel="noopener noreferrer">Path of the Fist</a>
    <a class="header-gmcp-btn" href="https://github.com/ChibuikeOD/gesso-mcp-server" target="_blank" rel="noopener noreferrer">G-MCP</a>
    <a class="header-deltabench-btn" href="https://github.com/ChibuikeOD/DeltaBench2D" target="_blank" rel="noopener noreferrer">DeltaBench2D</a>
</div>
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
        "<p style='color: #718096; font-size: 1rem; margin-top: 0;'>Solo Developer of Forma. Check it out below!</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
<div class="header-links">
    <a href="https://www.linkedin.com/in/chibuike-odibeli-862319220/" target="_blank">LinkedIn</a>
    <a href="mailto:chibuikeodibeli@gmail.com">Email</a>
</div>
<div class="projects-badge-container">
    <div class="projects-badge">
      <span class="pulse-dot"></span>
      <span class="badge-text">✨ CLICK TO EXPLORE MY LIVE APPS:</span>
    </div>
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#FF0055" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 8px; animation: floatArrow 1.2s infinite ease-in-out;">
        <line x1="7" y1="7" x2="17" y2="17"></line>
        <polyline points="17 7 17 17 7 17"></polyline>
    </svg>
</div>
<div class="header-btn-row">
    <a class="header-forma-btn" href="https://forma-app.net" target="_blank" rel="noopener noreferrer">Forma</a>
    <a class="header-genresense-btn" href="https://genre-sense.vercel.app/" target="_blank" rel="noopener noreferrer">GenreSense</a>
    <a class="header-forma-btn" href="https://app.powerbi.com/view?r=eyJrIjoiYTJjZmYxNDQtODRmNC00YmZjLWI0ZDQtZTYwMGVmNzMzZTFhIiwidCI6IjA1YjVmMDhmLTdkZWQtNDNjNS1iZTNmLWFmMDQyMDcwNzQxNCJ9" target="_blank" rel="noopener noreferrer">Daily Stock Price Prediction</a>
    <a class="header-fist-btn" href="https://path-of-the-fist.com" target="_blank" rel="noopener noreferrer">Path of the Fist</a>
    <a class="header-gmcp-btn" href="https://github.com/ChibuikeOD/gesso-mcp-server" target="_blank" rel="noopener noreferrer">G-MCP</a>
    <a class="header-deltabench-btn" href="https://github.com/ChibuikeOD/DeltaBench2D" target="_blank" rel="noopener noreferrer">DeltaBench2D</a>
</div>
""",
        unsafe_allow_html=True,
    )

# --- About Myself ---
st.markdown("## About Myself")
st.markdown("""
<p>I am a Data Science Master's student at UMass Dartmouth and a Data-Driven Software Engineer. I am passionate about turning complex data into compelling stories, actionable insights, and robust software solutions.</p> 

<p>With a background in Software Engineering from Penn State, my work bridges the gap between machine learning research and full-stack application development. I've designed immersive VR AI chatbots, deployed quantized neural networks to edge devices, and modernized large-scale web applications.</p>
""", unsafe_allow_html=True)

# --- Projects ---
st.markdown("## Projects")

@st.dialog("Project Details")
def show_project_details(proj):
    st.markdown(f"### {proj['title']}")
    pages = proj.get("pages")
    if pages:
        tab_titles = [p["title"] for p in pages]
        tabs = st.tabs(tab_titles)
        for t, p in zip(tabs, pages):
            with t:
                st.markdown(p["content"], unsafe_allow_html=True)
    else:
        st.write(proj["details"])
    if proj['link']:
        st.link_button("View Live Project", proj['link'])

project_projects = [
    {
        "title": "GenreSense | ML-Powered Music Recommendation Engine",
        "subtitle": "Python (Flask), Scikit-Learn, Pandas, Spotify API, PostgreSQL.",
        "details": "Engineered a full-stack recommendation system that uses K-Means Clustering to discover 'Mathematical Genres' based on high-fidelity audio features (energy, valence, tempo).",
        "pages": [
            {
                "title": "Overview",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Project:</strong> GenreSense</p>
<p><strong>Core outcome:</strong> Engineered a full-stack recommendation system that uses K-Means Clustering to discover "Mathematical Genres" based on high-fidelity audio features (energy, valence, tempo).</p>
<p><strong>Tech Stack:</strong> Python (Flask), Scikit-Learn, Pandas, Spotify API, PostgreSQL.</p>
</div>
""",
            },
            {
                "title": "Clustering & Discovery",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p>Optimized cluster accuracy using Silhouette Scores and implemented a semantic labeling engine to translate abstract data into human-readable moods.</p>
</div>
""",
            },
            {
                "title": "Hybrid Recommendation",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p>Developed a Hybrid Playlist Generator using Cosine Similarity to create seamless transitions between distinct musical styles.</p>
</div>
""",
            },
        ],
        "link": "https://genre-sense.vercel.app/",
    },
    {
        "title": "Real Estate Pro Forma Investment Analyzer",
        "subtitle": "Solo Full-Stack Developer • Mobile-first underwriting engine for commercial real estate.",
        "details": "A dynamic, mobile-first underwriting engine that converts property walk-through inputs into a comprehensive 10-year IRR projection in seconds.",
        "pages": [
            {
                "title": "Overview",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Role:</strong> Solo Full-Stack Developer</p>
<p><strong>Project:</strong> Real Estate Pro Forma Investment Analyzer (Forma)</p>
<p><strong>Core outcome:</strong> A mobile-first underwriting engine that moves investors from a property walk-through to a full 10-year IRR projection in seconds.</p>
</div>
""",
            },
            {
                "title": "Problem",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p>Commercial real estate underwriting is still dominated by static, fragmented Excel models. These spreadsheets are hard to maintain, easy to break, and difficult to use in the field.</p>
<p><strong>What I solved:</strong> I designed a dynamic, mobile-first underwriting workflow that replaces error-prone spreadsheets with a structured, guided input experience and instant recalculation of key performance metrics.</p>
</div>
""",
            },
            {
                "title": "Architecture & Stack",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Frontend ecosystem:</strong> React Native + Expo for a single TypeScript/JavaScript codebase with consistent native performance across iOS and Android.</li>
  <li><strong>State & calculation engine:</strong> A <code>useProformaCalculator</code> custom hook acting as the “central nervous system,” coordinating dozens of interdependent inputs (purchase price, renovation budgets, debt tranches, exit cap rates) and recomputing KPIs in real time.</li>
  <li><strong>Data visualization:</strong> <code>react-native-chart-kit</code> for scalable, SVG-based analytics; interactive trendlines for DSCR and NOI vs. cash flow across a 10-year hold.</li>
  <li><strong>Backend & cloud sync:</strong> Centralized, cloud-synced storage as a single source of truth to prevent version drift across devices and collaborators.</li>
  <li><strong>Performance:</strong> UI optimized with React Native’s <code>ScrollView</code> and <code>FlatList</code> to sustain smooth rendering when working with dense, month-by-month matrices.</li>
</ul>
</div>
""",
            },
            {
                "title": "Financial Logic",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Tiered analytical workflow:</strong> Year 1 waterfall calculations cascade from GPR → EGI → NOI → cash flow, providing an intuitive hierarchy that matches how professionals underwrite deals.</li>
  <li><strong>Advanced capital structuring:</strong> Support for multi-tier debt tranches, mezzanine debt, seller financing, and interest-only periods—modeled to reflect real-world financing structures.</li>
  <li><strong>Institutional-grade returns:</strong> Implemented <strong>XIRR</strong> and <strong>XNPV</strong> algorithms to correctly handle irregular cash flow dates (critical for professional underwriting).</li>
</ul>
</div>
""",
            },
            {
                "title": "Deployment & Monetization",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>CI/CD & OTA updates:</strong> Expo Application Services (EAS) pipeline for streamlined releases and rapid over-the-air updates.</li>
  <li><strong>Subscription architecture:</strong> RevenueCat integration powering a freemium model—free tier for Year 1 analytics and a gated premium tier for the full 10-year projections and advanced visual suite.</li>
  <li><strong>ASO:</strong> Data-driven keyword strategy targeting high-intent long-tail searches (e.g., “DSCR calculator,” “multifamily proforma”) to drive organic acquisition.</li>
</ul>
</div>
""",
            },
        ],
        "link": "https://forma-app.net",
    },
    {
        "title": "Stock Market Forecasting",
        "subtitle": "Python, Prophet, Azure, Power BI • End-to-end pipeline predicting OHLCV data with automated cloud storage.",
        "details": "A comprehensive data engineering and predictive modeling pipeline designed for equity markets. The automated system reliably scrapes daily Open, High, Low, Close, and Volume (OHLCV) data, staging it in Azure Blob Storage. Meta's Prophet algorithm analyzes the time-series trends to forecast future price movements. Finally, this data flows into a dynamic Power BI report, providing stakeholders with intuitive visualizations of historical trends and short-term projections.",
        "pages": [
            {
                "title": "Overview",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Project:</strong> Stock Market Forecasting</p>
<p><strong>Focus:</strong> End-to-end data engineering and time-series forecasting for equity markets, from automated ingestion through cloud storage to interactive reporting.</p>
<p><strong>Stack:</strong> Python, Meta Prophet, Microsoft Azure (Blob Storage), Power BI.</p>
</div>
""",
            },
            {
                "title": "Problem & Goals",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p>Market analysis workflows often depend on manually refreshed spreadsheets and disconnected tools. That fragmentation increases operational risk, slows iteration, and makes it difficult to communicate forecasts consistently to stakeholders.</p>
<p><strong>Objectives:</strong> Automate reliable collection of daily OHLCV data, centralize historical series in the cloud, produce repeatable forecasts, and deliver a governed, shareable analytics surface in Power BI.</p>
</div>
""",
            },
            {
                "title": "Data Pipeline & Azure",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Ingestion:</strong> Automated scraping of daily Open, High, Low, Close, and Volume (OHLCV) fields with validation and structured staging suitable for downstream modeling.</li>
  <li><strong>Cloud storage:</strong> Persisted curated datasets in <strong>Azure Blob Storage</strong> as a durable, cost-effective landing zone and historical archive.</li>
  <li><strong>Operational design:</strong> Emphasized idempotent writes, clear partitioning by symbol/date where applicable, and a pipeline that can run on a schedule without manual file shuffling.</li>
</ul>
</div>
""",
            },
            {
                "title": "Modeling & Analytics",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Time-series engine:</strong> Applied Meta’s <strong>Prophet</strong> to model trend and seasonality components and generate forward-looking projections from historical price series.</li>
  <li><strong>Feature discipline:</strong> Treated missing dates, regime shifts, and volatility spikes as first-class concerns when fitting and evaluating forecasts.</li>
  <li><strong>Interpretability:</strong> Structured outputs so analysts can compare historical behavior to projected ranges rather than treating the model as a black box.</li>
</ul>
</div>
""",
            },
            {
                "title": "Reporting & Delivery",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Power BI:</strong> Built a dynamic report layer that connects stakeholders to historical trends and short-term projections in a single governed experience.</li>
  <li><strong>Publication:</strong> Published the report for consumption via Power BI’s web experience so reviewers can access insights without local spreadsheet dependencies.</li>
  <li><strong>Outcome:</strong> A repeatable pipeline from raw daily inputs to cloud-backed storage, modeled forecasts, and executive-ready visuals.</li>
</ul>
</div>
""",
            },
        ],
        "link": "https://app.powerbi.com/view?r=eyJrIjoiYTJjZmYxNDQtODRmNC00YmZjLWI0ZDQtZTYwMGVmNzMzZTFhIiwidCI6IjA1YjVmMDhmLTdkZWQtNDNjNS1iZTNmLWFmMDQyMDcwNzQxNCJ9"
    },
    {
        "title": "Automated PDF Remediation",
        "subtitle": "LayoutLMv3, FastAPI, pikepdf, React • AI-assisted PDF/UA accessibility at scale.",
        "details": "An automation workflow that remediates untagged PDFs by inferring document structure, restoring reading order, remediating tables, and artifacting decorative content—then materializing fixes into the PDF structure tree for assistive technology.",
        "pages": [
            {
                "title": "Overview & Problem",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p>Most PDFs on the web are effectively <strong>untagged</strong>: they look fine visually but lack the logical structure assistive technologies require. For the hundreds of millions of people who rely on screen readers, that gap makes documents incoherent or unusable.</p>
<p><strong>Manual remediation</strong> is slow, expensive, and depends on specialized accessibility expertise—so organizations accumulate inaccessible PDFs faster than teams can fix them.</p>
<p><strong>This project:</strong> An automated pipeline that turns visual layout into accessible digital logic, writes structure into the PDF, and pairs engineering with WCAG-oriented outcomes.</p>
</div>
""",
            },
            {
                "title": "Structure & Semantics",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p>Screen readers do not infer meaning from bold type or large fonts; they consume the PDF <strong>structure tree</strong> (tags).</p>
<p><strong>AI approach:</strong> A <strong>LayoutLM</strong>-style document vision model acts as the “eyes” of the system—identifying that a large, centered string is a <code>&lt;H1&gt;</code> (Heading 1), not arbitrary body text.</p>
<p><strong>Accessibility impact:</strong> Supports <strong>WCAG 1.3.1 (Info and Relationships)</strong> by generating meaningful tags so users can navigate by headings (for example, the common “next heading” gesture), similar to how sighted readers skim titles.</p>
</div>
""",
            },
            {
                "title": "Meaningful Sequence",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p>PDF content streams are often ordered for print mechanics, not human reading order—footnotes, sidebars, and multi-column layouts can appear in code in a sequence that does not match visual flow.</p>
<p><strong>AI + geometry:</strong> Because the model reasons over the page spatially, <code>fix_reading_order()</code> re-sorts elements in a top-to-bottom, column-aware order aligned with how a human reads.</p>
<p><strong>Accessibility impact:</strong> Addresses <strong>WCAG 1.3.2 (Meaningful Sequence)</strong>, preventing the “jumble effect” where assistive technology reads a second column before the first or jumps unexpectedly between regions.</p>
</div>
""",
            },
            {
                "title": "Table Remediation",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p>Untagged tables frequently degrade into disconnected strings of numbers and labels—little usable context for non-visual navigation.</p>
<p><strong>AI approach:</strong> Detect table boundaries and header rows (<code>&lt;TH&gt;</code>), then programmatically assign <strong>scope</strong> so headers bind to the correct rows or columns.</p>
<p><strong>Accessibility impact:</strong> Users hear coherent table announcements (for example, dimension + header + cell) instead of isolated values with no relationship.</p>
</div>
""",
            },
            {
                "title": "Artifacts & Non-text",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p>Decorative graphics, rules, and repeated “visual noise” are a major pain point when assistive technology announces <strong>“Graphic”</strong> for every line or flourish.</p>
<p><strong>AI approach:</strong> Classify content vs. decoration and automatically <strong>artifact</strong> non-informative elements so they do not participate in the reading experience.</p>
<p><strong>Accessibility impact:</strong> Aligns with <strong>WCAG 1.1.1 (Non-text Content)</strong> by reducing cognitive load and keeping focus on meaningful information.</p>
</div>
""",
            },
            {
                "title": "Technical Highlights",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<table style="width:100%; border-collapse:collapse; font-size:0.9rem;">
  <thead>
    <tr style="border-bottom:1px solid #E2E8F0;">
      <th style="text-align:left; padding:6px 8px;">Feature</th>
      <th style="text-align:left; padding:6px 8px;">Technology</th>
      <th style="text-align:left; padding:6px 8px;">Innovation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid #F1F5F9;">
      <td style="padding:6px 8px; vertical-align:top;"><strong>Document vision</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">LayoutLMv3</td>
      <td style="padding:6px 8px; vertical-align:top;">Fine-tuned on library-specific and archival layouts to recognize complex academic structures.</td>
    </tr>
    <tr style="border-bottom:1px solid #F1F5F9;">
      <td style="padding:6px 8px; vertical-align:top;"><strong>Structure injection</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">FastAPI + pikepdf</td>
      <td style="padding:6px 8px; vertical-align:top;">Bridges model predictions into the physical PDF <code>/StructTreeRoot</code> and tag graph.</td>
    </tr>
    <tr>
      <td style="padding:6px 8px; vertical-align:top;"><strong>Remediation UI</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">React</td>
      <td style="padding:6px 8px; vertical-align:top;">Before/after dashboard showing accessibility score improvements as automated fixes land.</td>
    </tr>
  </tbody>
</table>
</div>
""",
            },
        ],
        "link": None,
    },
    {
        "title": "Voice-Automated AI Chatbot (VR)",
        "subtitle": "Llama 2 (QLoRA), Unity, AWS • Low-latency voice tutor for clinical training in VR.",
        "details": "A hands-free, voice-driven VR tutor that simulates clinical scenarios and provides responsive conversational guidance through a cloud-hosted LLM pipeline.",
        "pages": [
            {
                "title": "Overview",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Project:</strong> Voice-Automated AI Chatbot (VR)</p>
<p><strong>Goal:</strong> Deliver a hands-free, low-latency conversational tutor inside VR to support realistic clinical training workflows.</p>
<p><strong>Outcome:</strong> A distributed architecture bridging Speech-to-Text (STT), an LLM reasoning layer, and Text-to-Speech (TTS) back into Unity—creating a natural, voice-first experience.</p>
</div>
""",
            },
            {
                "title": "Use Case & UX",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Hands-free interaction:</strong> Designed for scenarios where users cannot rely on typing or menus while immersed in VR.</li>
  <li><strong>Clinical realism:</strong> Conversational flow tailored to simulated patient encounters and guided decision-making.</li>
  <li><strong>Low friction:</strong> Voice-first design reduces cognitive overhead and keeps attention on the scenario rather than UI mechanics.</li>
</ul>
</div>
""",
            },
            {
                "title": "Architecture & Stack",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>VR runtime:</strong> Built in <strong>Unity</strong> for immersive interaction and scenario simulation.</li>
  <li><strong>LLM core:</strong> Parameter-efficient fine-tuning of <strong>Llama 2</strong> using <strong>QLoRA</strong> to improve domain relevance while keeping training practical.</li>
  <li><strong>Cloud infrastructure:</strong> Deployed services on <strong>AWS</strong> to host the model and coordinate STT/TTS routing.</li>
  <li><strong>Speech pipeline:</strong> Real-time STT → LLM → TTS loop to enable continuous conversational turns.</li>
</ul>
</div>
""",
            },
            {
                "title": "Latency & Reliability",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Pipeline orchestration:</strong> Designed the system as a distributed set of services so each stage (STT, LLM, TTS) can be optimized independently.</li>
  <li><strong>Streaming mindset:</strong> Focused on minimizing end-to-end response time to keep the VR experience conversational rather than “turn-based.”</li>
  <li><strong>Resilience:</strong> Guardrails for partial failures (e.g., speech service hiccups) to preserve usability during sessions.</li>
</ul>
</div>
""",
            },
            {
                "title": "Technical Highlights",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<table style="width:100%; border-collapse:collapse; font-size:0.9rem;">
  <thead>
    <tr style="border-bottom:1px solid #E2E8F0;">
      <th style="text-align:left; padding:6px 8px;">Capability</th>
      <th style="text-align:left; padding:6px 8px;">Technology</th>
      <th style="text-align:left; padding:6px 8px;">Implementation detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid #F1F5F9;">
      <td style="padding:6px 8px; vertical-align:top;"><strong>VR experience</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">Unity</td>
      <td style="padding:6px 8px; vertical-align:top;">Immersive scenario simulation with voice-driven interaction loop.</td>
    </tr>
    <tr style="border-bottom:1px solid #F1F5F9;">
      <td style="padding:6px 8px; vertical-align:top;"><strong>LLM adaptation</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">Llama 2 + QLoRA</td>
      <td style="padding:6px 8px; vertical-align:top;">Parameter-efficient fine-tuning to align responses to clinical tutoring needs.</td>
    </tr>
    <tr>
      <td style="padding:6px 8px; vertical-align:top;"><strong>Cloud orchestration</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">AWS + STT/TTS</td>
      <td style="padding:6px 8px; vertical-align:top;">Distributed speech + inference pipeline optimized for low-latency turn-taking.</td>
    </tr>
  </tbody>
</table>
</div>
""",
            },
        ],
        "link": None,
    },
    {
        "title": "Path Of The Fist | AI-Powered Esports Commentator",
        "subtitle": "FastAPI, Neo4j, GraphRAG, React, start.gg API, TailwindCSS.",
        "details": "Designed an AI esports commentator and bracket analytics assistant that models competitive tournament data into a Neo4j graph database. The system uses a GraphRAG analytics engine to construct high-fidelity game contexts, translating abstract tournament logs (Combo Breaker 2022 - 2026 Street Fighter 6) into natural, high-energy commentary and real-time player ELO statistics.",
        "pages": [
            {
                "title": "Overview",
                "content": """
<style>
  .fist-container {
    background-color: #030303;
    border-radius: 12px;
    padding: 24px;
    font-family: 'Outfit', 'Inter', -apple-system, sans-serif;
    color: #ffffff;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    margin-bottom: 20px;
    border: 1px solid #1a1e24;
    overflow: hidden;
  }
  .fist-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #00ffcc;
    padding-bottom: 12px;
    margin-bottom: 24px;
  }
  .fist-header-title-group {
    display: flex;
    align-items: baseline;
    gap: 16px;
  }
  .fist-header-title {
    font-size: 1.6rem;
    font-weight: 900;
    font-style: italic;
    color: #00ffcc;
    letter-spacing: -0.05em;
    text-transform: uppercase;
    text-shadow: 0 0 10px rgba(0, 255, 204, 0.3);
  }
  .fist-header-subtitle {
    font-size: 0.7rem;
    color: #00ffcc;
    opacity: 0.8;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
  }
  .fist-header-icons {
    display: flex;
    gap: 16px;
    color: #00ffcc;
    font-size: 1.1rem;
    cursor: pointer;
  }
  .fist-header-icons span:hover {
    text-shadow: 0 0 8px rgba(0, 255, 204, 0.8);
    transform: scale(1.1);
    transition: all 0.2s;
  }
  .fist-body-layout {
    display: flex;
    gap: 30px;
    align-items: flex-start;
    margin-bottom: 24px;
  }
  /* Advertisement Box */
  .fist-ad-box {
    transform: skewX(-8deg);
    background-color: #ffffff;
    border: 1px solid #ddd;
    padding: 20px 15px;
    width: 150px;
    height: 170px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
    flex-shrink: 0;
  }
  .fist-ad-indicator {
    transform: skewX(8deg);
    position: absolute;
    top: 6px;
    right: 6px;
    font-size: 0.55rem;
    color: #999;
    border: 1.2px solid #ccc;
    border-radius: 50%;
    width: 14px;
    height: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
  }
  .fist-ad-content {
    transform: skewX(8deg);
    text-align: center;
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .fist-ad-title-link {
    color: #0066cc;
    font-size: 0.8rem;
    font-weight: bold;
    text-decoration: none;
    line-height: 1.2;
  }
  .fist-ad-title-link:hover {
    text-decoration: underline;
  }
  .fist-ad-text {
    color: #333333;
    font-size: 0.65rem;
    line-height: 1.3;
  }
  .fist-ad-domain-link {
    color: #0066cc;
    font-size: 0.75rem;
    text-decoration: underline;
    font-weight: 500;
  }
  
  /* Arena Card */
  .fist-arena-card {
    flex: 1;
    background-color: #16181c;
    border: 2px dashed rgba(0, 255, 204, 0.25);
    border-radius: 8px;
    padding: 30px;
    text-align: center;
    transform: skewX(-8deg);
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    position: relative;
    max-width: 500px;
  }
  .fist-arena-inner {
    transform: skewX(8deg);
  }
  .fist-arena-icon {
    margin-bottom: 12px;
  }
  .fist-arena-title {
    font-size: 1.8rem;
    font-weight: 900;
    font-style: italic;
    color: #00ffcc;
    margin: 0 0 10px 0;
    text-transform: uppercase;
    letter-spacing: -0.01em;
    text-shadow: 0 0 8px rgba(0, 255, 204, 0.2);
  }
  .fist-arena-desc {
    font-size: 0.8rem;
    color: #a0aec0;
    line-height: 1.5;
    margin: 0 0 24px 0;
  }
  
  /* Suggestion Buttons Grid */
  .fist-suggestions-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }
  .fist-suggestion-btn {
    transform: skewX(-8deg);
    border: 1.5px solid #00ffcc;
    background-color: transparent;
    color: #ffffff;
    font-size: 0.75rem;
    font-style: italic;
    font-weight: 700;
    padding: 10px 12px;
    cursor: pointer;
    text-align: center;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  }
  .fist-suggestion-btn-text {
    transform: skewX(8deg);
    display: inline-block;
  }
  .fist-suggestion-btn:hover {
    background-color: #00ffcc;
    color: #000000;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.5);
  }
  
  /* Bottom Controls Column */
  .fist-controls-col {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    margin-top: 10px;
  }
  
  /* Chat Bar */
  .fist-chat-bar {
    transform: skewX(-8deg);
    display: flex;
    border: 2px solid #e5b323; /* gold/yellow */
    background-color: #111317;
    width: 100%;
    max-width: 500px;
    align-items: center;
    box-shadow: 0 6px 15px rgba(0,0,0,0.4);
    height: 48px;
    margin-bottom: 10px;
  }
  .fist-chat-input-placeholder {
    transform: skewX(8deg);
    flex: 1;
    font-size: 0.8rem;
    color: #718096;
    font-weight: 700;
    text-transform: uppercase;
    padding-left: 16px;
    text-align: left;
    user-select: none;
  }
  .fist-chat-send-btn {
    height: 100%;
    background-color: #0f7e8a;
    color: #ffffff;
    font-size: 0.8rem;
    font-weight: 900;
    padding: 0 24px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
    border-left: 2px solid #e5b323;
  }
  .fist-chat-send-btn-text {
    transform: skewX(8deg);
    color: #000000;
  }
  .fist-chat-send-btn:hover {
    background-color: #00ffcc;
    box-shadow: -5px 0 15px rgba(0, 255, 204, 0.4);
  }
  .fist-chat-send-btn:hover .fist-chat-send-btn-text {
    font-weight: 900;
  }
  
  .fist-footer-text {
    font-size: 0.65rem;
    color: #555e6b;
    margin-top: 6px;
    text-align: center;
    letter-spacing: 0.02em;
  }

  @media (max-width: 600px) {
    .fist-body-layout {
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }
    .fist-ad-box {
      width: 100%;
      max-width: 280px;
      height: auto;
      padding: 15px;
    }
    .fist-suggestions-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<div class="fist-container">
  <!-- Header -->
  <div class="fist-header">
    <div class="fist-header-title-group">
      <span class="fist-header-title">PATH OF THE FIST</span>
      <span class="fist-header-subtitle">YOUR COMBO BREAKER ANALYTICS ASSISTANT</span>
    </div>
    <div class="fist-header-icons">
      <span>🔔</span>
      <span>👤</span>
    </div>
  </div>
  
  <!-- Body Layout -->
  <div class="fist-body-layout">
    <!-- Ad Box (Left) -->
    <div class="fist-ad-box">
      <div class="fist-ad-indicator">A</div>
      <div class="fist-ad-content">
        <a href="https://aads.com" target="_blank" class="fist-ad-title-link">Advertise in this ad space</a>
        <span class="fist-ad-text">Create a campaign in just 5 minutes</span>
        <a href="https://aads.com" target="_blank" class="fist-ad-domain-link">aads.com</a>
      </div>
    </div>
    
    <!-- Center Column -->
    <div style="flex: 1; display: flex; flex-direction: column; align-items: center; width: 100%;">
      <!-- Arena Card -->
      <div class="fist-arena-card">
        <div class="fist-arena-inner">
          <div class="fist-arena-icon">
            <svg viewBox="0 0 100 100" style="width: 54px; height: 54px; fill: #00ffcc; margin: 0 auto;">
              <!-- Two clashing fighters -->
              <circle cx="34" cy="30" r="5" />
              <path d="M34 37h-3.5l-6.5 9v14h4v-11l3.5-5v16h4V45l3.5 7h3.5L34 37z" />
              <circle cx="66" cy="30" r="5" />
              <path d="M66 37h3.5l6.5 9v14h-4v-11l-3.5-5v16h-4V45l-3.5 7h-3.5L66 37z" />
              <path d="M50 25l2.5 7.5 7.5 2.5-7.5 2.5-2.5 7.5-2.5-7.5-7.5-2.5 7.5-2.5z" fill="#00ffcc" />
            </svg>
          </div>
          <h3 class="fist-arena-title">ENTER THE ARENA</h3>
          <p class="fist-arena-desc">
            Ask me anything about Combo Breaker from 2022 through 2026, including brackets, matchups, player runs, and standout performances.
          </p>
          
          <!-- Suggestions Grid -->
          <div class="fist-suggestions-grid">
            <button class="fist-suggestion-btn"><span class="fist-suggestion-btn-text">Who won the Street Fighter 6 bracket?</span></button>
            <button class="fist-suggestion-btn"><span class="fist-suggestion-btn-text">Were there any upsets?</span></button>
            <button class="fist-suggestion-btn"><span class="fist-suggestion-btn-text">Who had the most wins?</span></button>
            <button class="fist-suggestion-btn"><span class="fist-suggestion-btn-text">Who performed best in each game?</span></button>
          </div>
        </div>
      </div>
      
      <!-- Controls Column (Input & Footer) -->
      <div class="fist-controls-col">
        <!-- Chat Bar -->
        <div class="fist-chat-bar">
          <div class="fist-chat-input-placeholder">ENTER THE ARENA...</div>
          <div class="fist-chat-send-btn">
            <span class="fist-chat-send-btn-text">SEND</span>
          </div>
        </div>
        
        <!-- Footer -->
        <div class="fist-footer-text">
          Powered by DeepSeek via GraphRAG - Answers stream live with full tournament context
        </div>
      </div>
    </div>
  </div>
</div>

<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6; margin-top: 15px;">
<p><strong>Project Overview:</strong> Designed an AI-powered Esports commentator and bracket analytics assistant that models competitive gaming data from start.gg into a Neo4j graph database. The system uses a GraphRAG analytics engine to construct high-fidelity game contexts, translating abstract tournament logs (Combo Breaker 2022 - 2026 Street Fighter 6) into natural, high-energy commentary and real-time player ELO statistics.</p>
</div>
""",
            },
            {
                "title": "GraphRAG & Context",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Neo4j Graph Database:</strong> Models complex relationships between players, sets, tournaments, and events. Programmatically ingest and sync tournament brackets from the start.gg API across multiple years (2022 - 2026).</p>
<p><strong>GraphRAG Engine:</strong> Resolves global and local tournament context dynamically to generate highly accurate ELO ratings, player progression summaries, and match details, preventing LLM hallucinations about complex bracket layouts.</p>
</div>
""",
            },
            {
                "title": "Esports Commentary",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Voice of Combo Breaker:</strong> Fine-tuned and prompted LLM models to adopt a high-energy, elite esports commentator persona. Generates engaging narratives of specific match run sequences and historical tournament stories using punchy, action-oriented verbs.</p>
</div>
""",
            },
        ],
        "link": "https://path-of-the-fist.com",
    },
    {
        "title": "G-MCP | Model Context Protocol Server for Godot",
        "subtitle": "TypeScript, Node.js, Godot 4 (GDScript), WebSockets, Mermaid, Vitest.",
        "details": "Engineered a custom Model Context Protocol (MCP) server for the Godot 4.x game engine, empowering AI agents with runtime debugging, dynamic GDScript execution, automated playtesting via simulated inputs, base64 visual screenshot capturing, and web asset integration (Kenney.nl, OpenGameArt). Implemented dual-execution modes (Live WebSocket and Headless fallback) to bridge the gap between AI code generation and game state verification.",
        "pages": [
            {
                "title": "Overview",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Project:</strong> G-MCP (Gesso Model Context Protocol Server)</p>
<p><strong>Core outcome:</strong> A bridge enabling AI agents to debug, inspect, and interact with running Godot 4.x game sessions and editor spaces in real-time.</p>
<p><strong>Tech Stack:</strong> TypeScript, Node.js, Godot 4.x (GDScript/WebSocket), Vitest, MCP SDK.</p>
</div>
""",
            },
            {
                "title": "Core Features",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Runtime Debugging & Introspection:</strong> Inspect live node trees, read/modify node properties, query signals, and monitor execution states.</li>
  <li><strong>Input Emulation & Playtesting:</strong> Programmatically dispatch simulated keyboard, mouse, gamepad, and touch input sequences.</li>
  <li><strong>Dynamic Code Execution (eval):</strong> Run arbitrary GDScript snippets on active game instances and fetch results.</li>
  <li><strong>Visual Agent Vision:</strong> Take screenshots of the game window, Godot editor, or screen monitor, converting them directly to base64 images for LLM vision models.</li>
</ul>
</div>
""",
            },
            {
                "title": "Architecture & Dual-Execution",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Dual-Execution Modes:</strong> Supports both WebSocket Live Mode (connecting to Godot Editor plugins and autoloaded game scripts at port 6505) and Headless Fallback Mode (spawning standalone headless GDScript runtimes via the Godot CLI executable).</p>
</div>
""",
            },
        ],
        "link": "https://github.com/ChibuikeOD/gesso-mcp-server",
    },
]

research_projects = [
    {
        "title": "Audio Deepfake Detection",
        "subtitle": "PyTorch, Librosa, Spectral Analysis • Multimodal hybrid CNN-LSTM system addressing synthetic media threats (ROC-AUC 0.94).",
        "details": "A multimodal deep learning framework for synthetic speech detection that fuses CNN-based spectral representations with LSTM temporal modeling, trained and evaluated under realistic channel degradations (compression and background noise).",
        "pages": [
            {
                "title": "Overview & Motivation",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Project:</strong> Audio Deepfake Detection</p>
<p><strong>Motivation:</strong> Generative audio models make it increasingly easy to fabricate convincing speech. The goal was a detector that generalizes beyond a single generator or dataset and remains useful under real-world recording conditions.</p>
<p><strong>Outcome:</strong> A hybrid CNN–LSTM architecture achieving <strong>0.94 ROC-AUC</strong>, with emphasis on robustness to compression artifacts and ambient noise.</p>
</div>
""",
            },
            {
                "title": "Problem Framing",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Subtle manipulations:</strong> Synthetic speech can preserve prosody and bandwidth cues that fool naive spectral heuristics.</li>
  <li><strong>Distribution shift:</strong> Models trained on one synthesis family often fail when generators, codecs, or microphones change.</li>
  <li><strong>Operational realism:</strong> Deployed detectors must tolerate lossy compression, variable SNR, and background interference—conditions absent from “clean lab” datasets.</li>
</ul>
</div>
""",
            },
            {
                "title": "Data & Audio Representation",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Frontend DSP:</strong> Used <strong>Librosa</strong> for framing, windowing, and mel-scale feature extraction to stabilize inputs across sample rates and recording devices.</li>
  <li><strong>Mel-spectrograms:</strong> Treated time–frequency tiles as structured inputs so convolutional filters can capture fine-grained harmonic and noise-floor signatures.</li>
  <li><strong>Augmentation & hygiene:</strong> Applied noise, codec-like degradation, and gain variation during training to reduce overfitting to a single acoustic environment.</li>
</ul>
</div>
""",
            },
            {
                "title": "Model Architecture",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>CNN branch:</strong> Convolutional layers extract local spatial patterns from mel-spectrogram patches (short-term spectral texture).</li>
  <li><strong>LSTM branch:</strong> Recurrent modeling captures long-range temporal dependencies across frames (prosody, coarticulation, and generator-specific temporal artifacts).</li>
  <li><strong>Hybrid fusion:</strong> Combined pathways into a unified classifier in <strong>PyTorch</strong> so the model jointly reasons about “what it looks like” and “how it evolves over time.”</li>
</ul>
</div>
""",
            },
            {
                "title": "Training & Evaluation",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Objective:</strong> Binary discrimination (authentic vs. synthetic) with threshold-independent reporting via ROC-AUC.</li>
  <li><strong>Generalization:</strong> Evaluated across authentic and generated sources to stress-test domain shift rather than memorizing a single generator fingerprint.</li>
  <li><strong>Robustness:</strong> Reported performance under compression and background noise to approximate real playback and capture pipelines.</li>
</ul>
</div>
""",
            },
            {
                "title": "Technical Highlights",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<table style="width:100%; border-collapse:collapse; font-size:0.9rem;">
  <thead>
    <tr style="border-bottom:1px solid #E2E8F0;">
      <th style="text-align:left; padding:6px 8px;">Capability</th>
      <th style="text-align:left; padding:6px 8px;">Technology</th>
      <th style="text-align:left; padding:6px 8px;">Innovation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid #F1F5F9;">
      <td style="padding:6px 8px; vertical-align:top;"><strong>Spectral modeling</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">CNN on mel-spectrograms</td>
      <td style="padding:6px 8px; vertical-align:top;">Localized time–frequency cues that separate subtle synthesis artifacts from natural speech texture.</td>
    </tr>
    <tr style="border-bottom:1px solid #F1F5F9;">
      <td style="padding:6px 8px; vertical-align:top;"><strong>Temporal modeling</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">LSTM / sequence head</td>
      <td style="padding:6px 8px; vertical-align:top;">Captures frame-to-frame dynamics that CNNs alone can miss across longer utterances.</td>
    </tr>
    <tr>
      <td style="padding:6px 8px; vertical-align:top;"><strong>Training stack</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">PyTorch + Librosa</td>
      <td style="padding:6px 8px; vertical-align:top;">End-to-end pipeline from raw waveform to calibrated probabilities with degradation-aware augmentation.</td>
    </tr>
  </tbody>
</table>
</div>
""",
            },
        ],
        "link": None,
    },
    {
        "title": "Edge-Deployed Neural Networks",
        "subtitle": "hls4ml, Vivado HLS, Keras/TensorFlow • Hardware-aware quantization and FPGA inference.",
        "details": "End-to-end path from a Keras deep learning model to a quantized, HLS-simulated FPGA inference engine—optimizing fixed-point arithmetic for throughput and resource use while tracking numerical fidelity against the floating-point baseline.",
        "pages": [
            {
                "title": "Overview",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Project focus:</strong> Hardware-aware quantization for FPGA inference.</p>
<p>I built an end-to-end workflow to deploy a <strong>Keras</strong>-trained model to an <strong>FPGA</strong>. The central challenge was translating floating-point mathematics into <strong>hardware-efficient fixed-point</strong> arithmetic without unacceptable accuracy loss.</p>
<p>Using <strong>hls4ml</strong>, I targeted a high-throughput inference implementation suitable for <strong>resource-constrained</strong> edge environments, with validation through HLS simulation.</p>
</div>
""",
            },
            {
                "title": "Quantization Strategy",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Model compression:</strong> Moved from standard 32-bit floating-point weights and activations toward <strong>custom fixed-point</strong> representations sized for FPGA datapaths.</li>
  <li><strong>Per-layer precision:</strong> Manually tuned bit-widths (for example, <code>ap_fixed&lt;16,6&gt;</code>) layer by layer to balance <strong>numerical fidelity</strong> against <strong>LUT and DSP</strong> budget.</li>
  <li><strong>Hardware–software tradeoff:</strong> Each reduction in bit-width directly affects area and power; the workflow treated quantization as a co-design problem, not a post-hoc afterthought.</li>
</ul>
</div>
""",
            },
            {
                "title": "Profiling & Bounds",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Static and dynamic analysis:</strong> Profiled activation ranges and weight distributions to choose the minimum integer and fractional bits needed at each layer.</li>
  <li><strong>Overflow prevention:</strong> Bounded tensors so fixed-point operators remained stable across representative inputs—avoiding silent saturation that would invalidate downstream layers.</li>
  <li><strong>Traceability:</strong> Quantization decisions were tied back to measurable signal statistics rather than generic defaults.</li>
</ul>
</div>
""",
            },
            {
                "title": "HLS & Validation",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Xilinx Vivado HLS:</strong> Simulated the generated hardware-oriented C++ to verify timing structure and functional behavior before full RTL closure.</li>
  <li><strong>Equivalence checking:</strong> Compared quantized fixed-point behavior against the original floating-point model to confirm acceptable error margins on held-out data.</li>
  <li><strong>Outcome:</strong> A validated path from trained network → fixed-point specification → HLS-friendly implementation suitable for FPGA deployment.</li>
</ul>
</div>
""",
            },
            {
                "title": "Results & Stack",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<table style="width:100%; border-collapse:collapse; font-size:0.9rem;">
  <thead>
    <tr style="border-bottom:1px solid #E2E8F0;">
      <th style="text-align:left; padding:6px 8px;">Dimension</th>
      <th style="text-align:left; padding:6px 8px;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid #F1F5F9;">
      <td style="padding:6px 8px; vertical-align:top;"><strong>Optimization tooling</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">hls4ml, Xilinx Vivado (HLS toolchain)</td>
    </tr>
    <tr style="border-bottom:1px solid #F1F5F9;">
      <td style="padding:6px 8px; vertical-align:top;"><strong>Frameworks</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">Keras / TensorFlow, Python</td>
    </tr>
    <tr style="border-bottom:1px solid #F1F5F9;">
      <td style="padding:6px 8px; vertical-align:top;"><strong>Hardware concepts</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">High-level synthesis (HLS), fixed-point arithmetic, RTL-oriented simulation</td>
    </tr>
    <tr>
      <td style="padding:6px 8px; vertical-align:top;"><strong>Impact</strong></td>
      <td style="padding:6px 8px; vertical-align:top;">Substantially reduced memory footprint and logic utilization through disciplined per-layer quantization—aligned with prior portfolio estimates of large inference speedup and power reduction vs. baseline ARM execution on comparable workloads.</td>
    </tr>
  </tbody>
</table>
</div>
""",
            },
        ],
        "link": None,
    },
    {
        "title": "DeltaBench2D | 2D Game Development Benchmark Suite",
        "subtitle": "TypeScript, Node.js, Godot 4.x (GDScript), Git LFS, Python.",
        "details": "Contributed to and rebranded a multimodal benchmarking suite containing 132 automated tasks to evaluate agentic software development capabilities in the Godot 4.x game engine. Configured a unified test runner, managed large asset files using Git LFS, and developed verification modules to test agent performance on Gameplay, 2D Graphics, and UI tasks.",
        "pages": [
            {
                "title": "Overview",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Project:</strong> DeltaBench2D (formerly GameDevBench / Gesso-2D)</p>
<p><strong>Core outcome:</strong> A rigorous multimodal evaluation benchmark consisting of 132 game development tasks in the Godot 4 game engine.</p>
<p><strong>Tech Stack:</strong> TypeScript, Node.js, Godot 4.x (GDScript/websocket client), Python, Git LFS.</p>
</div>
""",
            },
            {
                "title": "Task Taxonomy",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<p><strong>Multi-Category Evaluation:</strong> Tasks span four categories—3D Graphics, 2D Graphics, Gameplay, and UI—requiring agents to manipulate and reason about multimodal assets (shaders, sprites, animations, and visual scenes).</p>
<p><strong>Complexity:</strong> Average solutions require 3x more lines of code and file changes compared to typical software engineering benchmarks (like SWE-bench), highlighting the complexity of real-world game development.</p>
</div>
""",
            },
            {
                "title": "Engineering Details",
                "content": """
<div style="color:#4A4A4A; font-size:0.95rem; line-height:1.6;">
<ul>
  <li><strong>Unified Test Runner:</strong> Configured a testing suite where agents execute solutions and run automated assertion checks inside the Godot runtime.</li>
  <li><strong>Asset Management:</strong> Set up Git LFS tracking for heavy zip packages (e.g. game project templates exceeding 100MB) to optimize repository size and resolve GitHub upload limitations.</li>
</ul>
</div>
""",
            },
        ],
        "link": "https://github.com/ChibuikeOD/DeltaBench2D",
    },
]

for i, proj in enumerate(project_projects):
    st.markdown(f"""
    <div class="project-item" style="margin-bottom: 0.3rem;">
        <div class="item-title">{proj['title']}</div>
        <div class="item-subtitle">{proj['subtitle']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("View Project", key=f"view_proj_{i}"):
        show_project_details(proj)
    
    st.markdown("<div style='margin-bottom: 1.2rem;'></div>", unsafe_allow_html=True)

# --- Research ---
st.markdown("## Research")
for j, proj in enumerate(research_projects):
    st.markdown(f"""
    <div class="project-item" style="margin-bottom: 0.3rem;">
        <div class="item-title">{proj['title']}</div>
        <div class="item-subtitle">{proj['subtitle']}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("View Project", key=f"view_research_{j}"):
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
import base64
import os

def get_img_base64(filename):
    for folder in [".", "vercel/public"]:
        full_path = os.path.join(folder, filename)
        if os.path.exists(full_path):
            with open(full_path, "rb") as f:
                return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

img1 = get_img_base64("street_photo_1.png")
img2 = get_img_base64("street_photo_2.png")
img3 = get_img_base64("street_photo_3.png")
img4 = get_img_base64("street_photo_4.png")

# Sidebar markup for desktop
st.markdown(f"""
<div class="photo-sidebar-left">
    <div class="photo-sidebar-title">📷 chibuiketakespictures</div>
    <div class="polaroid-card" style="transform: rotate(-3deg);">
        <div class="polaroid-img-container">
            <img src="{img1}" alt="Golden Hour">
        </div>
        <div class="polaroid-caption">"Golden Hour"</div>
    </div>
    <div class="polaroid-card" style="transform: rotate(2deg);">
        <div class="polaroid-img-container">
            <img src="{img2}" alt="Concrete Geometry">
        </div>
        <div class="polaroid-caption">"Concrete Geometry"</div>
    </div>
</div>

<div class="photo-sidebar-right">
    <div class="photo-sidebar-title">📷 chibuiketakespictures</div>
    <div class="polaroid-card" style="transform: rotate(3deg);">
        <div class="polaroid-img-container">
            <img src="{img3}" alt="Misty Ridges">
        </div>
        <div class="polaroid-caption">"Misty Ridges"</div>
    </div>
    <div class="polaroid-card" style="transform: rotate(-2deg);">
        <div class="polaroid-img-container">
            <img src="{img4}" alt="Neon Night">
        </div>
        <div class="polaroid-caption">"Neon Night"</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Certifications ---
st.markdown("## Certifications")
st.markdown("""
<div style="background-color: rgba(255,255,255,0.7); border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); margin-top: 15px; margin-bottom: 25px;">
    <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 15px;">
        <div style="display: flex; align-items: flex-start; gap: 15px; flex: 1; min-width: 250px;">
            <!-- Microsoft Logo Grid -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2px; width: 40px; height: 40px; margin-top: 4px; flex-shrink: 0;">
                <div style="background-color: #F25022;"></div>
                <div style="background-color: #7FBA00;"></div>
                <div style="background-color: #00A4EF;"></div>
                <div style="background-color: #FFB900;"></div>
            </div>
            <div>
                <h4 style="margin: 0 0 4px 0; font-size: 1.05rem; font-weight: 700; color: #1A1A1A;">Microsoft Certified: Azure AI Engineer Associate</h4>
                <p style="margin: 0 0 6px 0; font-size: 0.85rem; color: #718096; font-weight: 500;">Microsoft</p>
                <div style="display: flex; flex-wrap: wrap; gap: 15px; font-size: 0.75rem; color: #718096;">
                  <span><strong>Credential ID:</strong> 8FDC769C0A0CD6EB</span>
                  <span><strong>Issued:</strong> March 16, 2026</span>
                  <span><strong>Expires:</strong> March 17, 2027</span>
                </div>
            </div>
        </div>
        <a href="https://learn.microsoft.com/en-us/users/chibuikeodibeli-9487/credentials/8fdc769c0a0cd6eb?ref=https%3A%2F%2Fwww.linkedin.com%2F" target="_blank" style="display: inline-block; text-align: center; border: 1px solid #E2E8F0; background-color: #ffffff; color: #1A1A1A; font-size: 0.75rem; font-weight: 600; padding: 8px 16px; border-radius: 6px; text-decoration: none; transition: background-color 0.2s;" onmouseover="this.style.backgroundColor='#f7f2ee'" onmouseout="this.style.backgroundColor='#ffffff'">Verify Credential</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("## Interests / Readings")
st.markdown(f"""
<ul class="interests-list">
    <li>Machine Learning Architecture</li>
    <li>Distributed Systems</li>
    <li>Science Fiction</li>
    <li>Community Technology Education</li>
    <li>Photography (Instagram: <a href="https://instagram.com/chibuiketakespictures" target="_blank" style="color: #6A1B9A; font-weight: bold; text-decoration: underline;">@chibuiketakespictures</a>)</li>
</ul>

<div class="inline-photo-gallery">
    <div class="polaroid-card" style="transform: rotate(1deg);">
        <div class="polaroid-img-container">
            <img src="{img1}" alt="Golden Hour">
        </div>
        <div class="polaroid-caption">"Golden Hour"</div>
    </div>
    <div class="polaroid-card" style="transform: rotate(-1deg);">
        <div class="polaroid-img-container">
            <img src="{img2}" alt="Concrete Geometry">
        </div>
        <div class="polaroid-caption">"Concrete Geometry"</div>
    </div>
    <div class="polaroid-card" style="transform: rotate(2deg);">
        <div class="polaroid-img-container">
            <img src="{img3}" alt="Misty Ridges">
        </div>
        <div class="polaroid-caption">"Misty Ridges"</div>
    </div>
    <div class="polaroid-card" style="transform: rotate(-2deg);">
        <div class="polaroid-img-container">
            <img src="{img4}" alt="Neon Night">
        </div>
        <div class="polaroid-caption">"Neon Night"</div>
    </div>
</div>
<br>
""", unsafe_allow_html=True)

