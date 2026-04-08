# 🇳🇬 Nigeria Economic Timeline

An interactive data visualization app that explores Nigeria’s economic and social indicators over time using World Bank data. The project focuses on **clear, honest visualization** inspired by **Edward Tufte’s principles**, helping users identify **correlations and long-term trends** without distortion.

---

## 📊 Project Overview

The Nigeria Economic Timeline visualizes key indicators from **1960 to 2024**, including:

- GDP  
- GDP Growth Rate  
- Inflation  
- Exchange Rate (USD/NGN)  
- Unemployment Rate  
- Population  
- Life Expectancy  

Each indicator is displayed in its own synchronized time-series chart, allowing users to explore how different metrics move together across decades.

This project is a **correlation tracker**, not a causation model. It is designed to reveal patterns and relationships rather than prove cause-and-effect.

---

## 🎯 Goals

- Present Nigeria’s economic data clearly and proportionally  
- Avoid misleading visual distortion  
- Maintain historical and economic context  
- Enable intuitive exploration of trends and correlations  

---

## 🧠 Design Principles (Edward Tufte)

The visualization follows Tufte’s core principles:

- **Proportional Representation:** Visual elements scale directly with data values  
- **Clear and Detailed Labeling:** Titles, subtitles, and tooltips reduce ambiguity  
- **Show Data Variation, Not Design Variation:** Consistent layout and styling across charts  
- **Standardized Time-Series Units:** Ensures fair comparisons across years  
- **Matching Dimensions:** Simple 2D charts avoid unnecessary complexity  
- **Contextual Integrity:** Full timelines and key historical events prevent cherry-picking  

---

## ✨ Features

- 📈 Multiple synchronized time-series charts  
- 🧭 Hover-based crosshair for year-by-year comparison  
- 📍 User-added pins to annotate key events  
- 🔄 Responsive resizing  
- 💾 Persistent annotations using local storage  

---

## 🔍 Key Observations

- Inflation spikes often coincide with **currency devaluations and GDP decline**  
- **Post-independence GDP** remains relatively stagnant compared to modern growth  
- **Life expectancy and population** show steady upward trends, contrasting cyclical economic indicators  
- The app is especially effective at **highlighting correlations** between indicators across time  

---

## ⚠️ Challenges

- **Fragmented Data:** Indicators sourced from separate World Bank CSV files  
- **Different Scales:** Economic indicators vary greatly in magnitude  
- **Data Parsing:** Required custom CSV parsing and missing-value handling  

---

## 🚀 Future Work

- Add more indicators (oil prices, education, government spending)  
- Enable chart reordering for direct comparisons  
- Add zooming and finer time-range inspection  
- Introduce causal modeling overlays (DAGs or counterfactuals)  

---

## 🛠️ Tech Stack

- **JavaScript**  
- **D3.js**  
- **HTML / CSS**  
- **World Bank Development Indicators**  

---

## 📁 Data Source

All data is sourced from the **World Bank Development Indicators (WDI)**.

---

## 📌 Disclaimer

This project visualizes **correlations**, not causation. While trends and relationships are visible, no causal claims are made without further statistical modeling.
