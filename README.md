# Data Science Portfolio

Welcome to my Data Science Portfolio! This repository includes a **Streamlit** app (`app.py`) and a **Next.js** site under [`vercel/`](vercel/) for deployment on Vercel.

It currently features the following projects:

### Data Visualization

- **Car Data Analysis**: An interactive dashboard exploring vehicle performance metrics (Altair in Streamlit; Vega-Lite on the Vercel site).
- **Co-Authorship Network**: A force-directed graph visualization of academic co-authorship using D3.js.
- **Contour Analysis**: A medical imaging tool for visualizing CT scan density contours.

### Machine Learning

- **Audio Deepfake Detection**: A multimodal system for detecting AI-generated audio artifacts.
- **Edge-Deployed Neural Networks**: Research on deploying quantized neural networks to FPGAs.
- **Voice-Automated AI Chatbot**: A VR-integrated AI assistant powered by fine-tuned LLMs.

## Deploying the portfolio on Vercel

The site in [`vercel/`](vercel/) is **standalone**: interactive demos load from `public/` (bundled CSV, D3 HTML/JSON, and Vega-Lite in React). It does **not** call Streamlit or require `NEXT_PUBLIC_STREAMLIT_URL`.

1. Push this repository to GitHub (or GitLab/Bitbucket).
2. In [Vercel](https://vercel.com), import the repo and set **Root Directory** to `vercel`.
3. Use the default Next.js **Build Command** (`next build`) and detected output.

You can still run the Streamlit hub locally or on [Streamlit Community Cloud](https://streamlit.io/cloud) with `streamlit run app.py` independently of Vercel.

### Profile photo

Place **`ProfilePic.png`**, **`ProfilePic.jpg`**, **`ProfilePic.jpeg`**, or **`ProfilePic.webp`** in the **repository root** (next to `app.py`) for Streamlit. For the Vercel site, copy the same file into [`vercel/public/`](vercel/public/) with the same filename so it is served at `/ProfilePic.*`.
