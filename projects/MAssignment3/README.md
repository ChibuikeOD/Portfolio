# Author Network Visualization

An interactive D3.js force-directed graph visualization showing co-authorship relationships from Scopus publication data.

## Features

- **Force-Directed Layout**: Dynamic network visualization using D3.js force simulation
- **Color-Coded Countries**: Nodes colored by author affiliation country (top 10 countries with distinct colors, others in gray)
- **Interactive Controls**: Adjust force parameters (charge strength, collision radius, link strength, link distance)
- **Hover Effects**: Highlight authors from the same country
- **Click Tooltips**: View detailed author information including country, publications, and number of co-authors
- **Zoom & Pan**: Navigate large networks easily
- **Drag Nodes**: Reposition nodes interactively

## Top 10 Countries (by author count)

1. United States (451 authors)
2. Germany (141 authors)
3. United Kingdom (104 authors)
4. China (88 authors)
5. Brazil (61 authors)
6. Russia (53 authors)
7. Canada (50 authors)
8. South Korea (49 authors)
9. Japan (47 authors)
10. Spain (41 authors)

## Files

- `index.html` - Main visualization page
- `author_network.json` - Processed network data (nodes and links)
- `data_scopus.csv` - Source Scopus publication data
- `process_data.py` - Python script to convert CSV to JSON

## Data Structure

### Nodes
Each node represents an author with:
- `id`: Author name
- `country`: Affiliation country
- `publications`: Number of publications
- `degree`: Number of unique co-authors
- `isTopCountry`: Boolean indicating if country is in top 10

### Links
Each link represents a co-authorship relationship with:
- `source`: Author 1
- `target`: Author 2
- `value`: Number of shared publications

## Usage

### View Online (GitHub Pages)
Visit the GitHub Pages URL for this repository.

### Run Locally
Due to browser security restrictions, you need a local server to load the JSON file:

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js
npx serve
```

Then open `http://localhost:8000` in your browser.

## Interactions

- **Hover** over a node to highlight all authors from the same country
- **Click** on a node to view detailed author information
- **Drag** nodes to reposition them
- Use **scroll/pinch** to zoom in/out
- **Pan** by clicking and dragging the background
- Adjust **sliders** to modify force parameters:
  - **Charge Strength**: Controls repulsion between nodes
  - **Collision Radius**: Minimum distance between nodes
  - **Link Strength**: How strongly connected nodes pull together
  - **Link Distance**: Natural distance between connected nodes

## Technical Details

- Built with D3.js v7
- Responsive design using CSS Grid/Flexbox
- Modern dark theme with accent colors
- Node size scaled by degree using `d3.scaleSqrt()` with range [3, 12]

## Data Filtering

Records excluded from the visualization:
- Missing Year
- Missing Affiliation
- Missing Author information



