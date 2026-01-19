// === Configuration ===
const CONFIG = {
    datasets: [
        {
            file: 'Datasets/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_322200.csv',
            name: 'GDP',
            title: 'Gross Domestic Product',
            subtitle: 'Current US$',
            color: '#e91e63',
            format: d => formatLargeNumber(d),
            unit: ''
        },
        {
            file: 'Datasets/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_322193.csv',
            name: 'GDP Growth',
            title: 'GDP Growth Rate',
            subtitle: 'Annual %',
            color: '#f06292',
            format: d => d?.toFixed(2) + '%',
            unit: '%'
        },
        {
            file: 'Datasets/API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_322058.csv',
            name: 'Inflation',
            title: 'Inflation Rate',
            subtitle: 'Consumer prices, annual %',
            color: '#ec407a',
            format: d => d?.toFixed(2) + '%',
            unit: '%'
        },
        {
            file: 'Datasets/API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_322167.csv',
            name: 'Unemployment',
            title: 'Unemployment Rate',
            subtitle: '% of total labor force',
            color: '#d81b60',
            format: d => d?.toFixed(2) + '%',
            unit: '%'
        },
        {
            file: 'Datasets/API_SP.DYN.LE00.IN_DS2_en_csv_v2_321761.csv',
            name: 'Life Expectancy',
            title: 'Life Expectancy at Birth',
            subtitle: 'Years',
            color: '#ff4081',
            format: d => d?.toFixed(1) + ' years',
            unit: 'years'
        },
        {
            file: 'Datasets/API_SP.POP.TOTL_DS2_en_csv_v2_322199.csv',
            name: 'Population',
            title: 'Total Population',
            subtitle: 'Number of people',
            color: '#f48fb1',
            format: d => formatLargeNumber(d),
            unit: ''
        }
    ],
    margin: { top: 20, right: 30, bottom: 30, left: 70 },
    yearRange: { start: 1960, end: 2024 }
};

// === Global State ===
let allData = {};
let countries = [];
let selectedCountry = 'WLD';
let charts = [];

// === Utility Functions ===
function formatLargeNumber(num) {
    if (num === null || num === undefined || isNaN(num)) return '—';
    if (num >= 1e12) return (num / 1e12).toFixed(2) + 'T';
    if (num >= 1e9) return (num / 1e9).toFixed(2) + 'B';
    if (num >= 1e6) return (num / 1e6).toFixed(2) + 'M';
    if (num >= 1e3) return (num / 1e3).toFixed(2) + 'K';
    return num.toFixed(2);
}

function parseWorldBankCSV(text) {
    const lines = text.split('\n');
    // Skip metadata rows (first 4 lines), get header row (line 5, index 4)
    const headerLine = lines[4];
    if (!headerLine) return { headers: [], data: [] };
    
    // Parse CSV header properly
    const headers = parseCSVLine(headerLine);
    
    // Find year columns (they start after the first 4 columns)
    const yearIndices = {};
    headers.forEach((header, index) => {
        const year = parseInt(header);
        if (year >= 1960 && year <= 2024) {
            yearIndices[year] = index;
        }
    });
    
    const data = [];
    for (let i = 5; i < lines.length; i++) {
        const line = lines[i].trim();
        if (!line) continue;
        
        const values = parseCSVLine(line);
        if (values.length < 5) continue;
        
        const countryName = values[0];
        const countryCode = values[1];
        
        const yearData = {};
        for (const [year, index] of Object.entries(yearIndices)) {
            const value = parseFloat(values[index]);
            yearData[year] = isNaN(value) ? null : value;
        }
        
        data.push({
            countryName,
            countryCode,
            values: yearData
        });
    }
    
    return { headers, data };
}

function parseCSVLine(line) {
    const result = [];
    let current = '';
    let inQuotes = false;
    
    for (let i = 0; i < line.length; i++) {
        const char = line[i];
        
        if (char === '"') {
            inQuotes = !inQuotes;
        } else if (char === ',' && !inQuotes) {
            result.push(current.trim());
            current = '';
        } else {
            current += char;
        }
    }
    result.push(current.trim());
    
    return result;
}

function getCountryData(datasetData, countryCode) {
    const country = datasetData.find(d => d.countryCode === countryCode);
    if (!country) return [];
    
    return Object.entries(country.values)
        .map(([year, value]) => ({
            year: parseInt(year),
            value: value
        }))
        .filter(d => d.value !== null)
        .sort((a, b) => a.year - b.year);
}

// === Data Loading ===
async function loadAllData() {
    const container = document.getElementById('charts-container');
    
    try {
        const loadPromises = CONFIG.datasets.map(async (dataset) => {
            const response = await fetch(dataset.file);
            const text = await response.text();
            const parsed = parseWorldBankCSV(text);
            return { name: dataset.name, data: parsed.data };
        });
        
        const results = await Promise.all(loadPromises);
        
        results.forEach(result => {
            allData[result.name] = result.data;
        });
        
        // Extract unique countries from first dataset
        if (results[0]?.data) {
            countries = results[0].data
                .map(d => ({ code: d.countryCode, name: d.countryName }))
                .sort((a, b) => a.name.localeCompare(b.name));
            
            populateCountrySelect();
        }
        
        // Clear loading state
        container.innerHTML = '';
        
        // Create charts
        createAllCharts();
        
    } catch (error) {
        console.error('Error loading data:', error);
        container.innerHTML = `
            <div class="loading">
                <span style="color: #fb7185;">Error loading data. Please ensure the CSV files are in the Datasets folder.</span>
            </div>
        `;
    }
}

function populateCountrySelect() {
    const select = document.getElementById('country-select');
    select.innerHTML = '';
    
    // Add important aggregates first
    const importantCodes = ['WLD', 'USA', 'CHN', 'JPN', 'DEU', 'GBR', 'IND', 'FRA', 'BRA', 'CAN'];
    const importantCountries = countries.filter(c => importantCodes.includes(c.code));
    const otherCountries = countries.filter(c => !importantCodes.includes(c.code));
    
    // Add a separator-like option group for important ones
    const importantGroup = document.createElement('optgroup');
    importantGroup.label = 'Major Economies';
    importantCountries
        .sort((a, b) => importantCodes.indexOf(a.code) - importantCodes.indexOf(b.code))
        .forEach(country => {
            const option = document.createElement('option');
            option.value = country.code;
            option.textContent = country.name;
            if (country.code === 'WLD') option.selected = true;
            importantGroup.appendChild(option);
        });
    select.appendChild(importantGroup);
    
    // Add all other countries
    const otherGroup = document.createElement('optgroup');
    otherGroup.label = 'All Countries';
    otherCountries.forEach(country => {
        const option = document.createElement('option');
        option.value = country.code;
        option.textContent = country.name;
        otherGroup.appendChild(option);
    });
    select.appendChild(otherGroup);
    
    // Add change handler
    select.addEventListener('change', (e) => {
        selectedCountry = e.target.value;
        updateAllCharts();
    });
}

// === Chart Creation ===
function createAllCharts() {
    const container = document.getElementById('charts-container');
    charts = [];
    
    CONFIG.datasets.forEach((dataset, index) => {
        const chartCard = createChartCard(dataset, index);
        container.appendChild(chartCard);
        
        const chartData = getCountryData(allData[dataset.name], selectedCountry);
        const chart = createChart(dataset, chartData, index);
        charts.push(chart);
    });
    
    // Setup synchronized hover
    setupSynchronizedHover();
}

function createChartCard(dataset, index) {
    const card = document.createElement('div');
    card.className = 'chart-card';
    card.id = `chart-card-${index}`;
    
    card.innerHTML = `
        <div class="chart-header">
            <div class="chart-title-group">
                <div class="chart-indicator" style="background: ${dataset.color}"></div>
                <div>
                    <div class="chart-title">${dataset.title}</div>
                    <div class="chart-subtitle">${dataset.subtitle}</div>
                </div>
            </div>
            <div class="chart-value">
                <div class="current-value" id="value-${index}">—</div>
                <div class="value-year" id="value-year-${index}">Latest available</div>
            </div>
        </div>
        <div class="chart-body" id="chart-${index}"></div>
    `;
    
    return card;
}

function createChart(dataset, data, index) {
    const container = document.getElementById(`chart-${index}`);
    const width = container.clientWidth;
    const height = container.clientHeight;
    
    const svg = d3.select(`#chart-${index}`)
        .append('svg')
        .attr('class', 'chart-svg')
        .attr('viewBox', `0 0 ${width} ${height}`)
        .attr('preserveAspectRatio', 'xMidYMid meet');
    
    const margin = CONFIG.margin;
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;
    
    const g = svg.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);
    
    // Scales
    const xScale = d3.scaleLinear()
        .domain([CONFIG.yearRange.start, CONFIG.yearRange.end])
        .range([0, innerWidth]);
    
    const yExtent = d3.extent(data, d => d.value);
    const yPadding = (yExtent[1] - yExtent[0]) * 0.1 || 1;
    const yScale = d3.scaleLinear()
        .domain([yExtent[0] - yPadding, yExtent[1] + yPadding])
        .range([innerHeight, 0]);
    
    // Grid lines
    g.append('g')
        .attr('class', 'grid')
        .selectAll('line')
        .data(yScale.ticks(5))
        .enter()
        .append('line')
        .attr('class', 'grid-line')
        .attr('x1', 0)
        .attr('x2', innerWidth)
        .attr('y1', d => yScale(d))
        .attr('y2', d => yScale(d));
    
    // X Axis
    g.append('g')
        .attr('class', 'axis-x')
        .attr('transform', `translate(0,${innerHeight})`)
        .call(d3.axisBottom(xScale)
            .tickFormat(d3.format('d'))
            .ticks(10));
    
    // Y Axis
    g.append('g')
        .attr('class', 'axis-y')
        .call(d3.axisLeft(yScale)
            .ticks(5)
            .tickFormat(d => formatLargeNumber(d)));
    
    // Area gradient
    const gradientId = `gradient-${index}`;
    const defs = svg.append('defs');
    const gradient = defs.append('linearGradient')
        .attr('id', gradientId)
        .attr('x1', '0%')
        .attr('y1', '0%')
        .attr('x2', '0%')
        .attr('y2', '100%');
    
    gradient.append('stop')
        .attr('offset', '0%')
        .attr('stop-color', dataset.color)
        .attr('stop-opacity', 0.3);
    
    gradient.append('stop')
        .attr('offset', '100%')
        .attr('stop-color', dataset.color)
        .attr('stop-opacity', 0);
    
    // Area
    const area = d3.area()
        .x(d => xScale(d.year))
        .y0(innerHeight)
        .y1(d => yScale(d.value))
        .curve(d3.curveMonotoneX);
    
    g.append('path')
        .datum(data)
        .attr('class', 'area-gradient')
        .attr('fill', `url(#${gradientId})`)
        .attr('d', area);
    
    // Line
    const line = d3.line()
        .x(d => xScale(d.year))
        .y(d => yScale(d.value))
        .curve(d3.curveMonotoneX);
    
    g.append('path')
        .datum(data)
        .attr('class', 'data-line')
        .attr('stroke', dataset.color)
        .attr('d', line);
    
    // Crosshair
    const crosshair = g.append('line')
        .attr('class', 'crosshair-line')
        .attr('y1', 0)
        .attr('y2', innerHeight)
        .style('opacity', 0);
    
    // Data point indicator
    const dataPoint = g.append('circle')
        .attr('class', 'data-point')
        .attr('r', 6)
        .attr('stroke', dataset.color);
    
    // Hover area
    const hoverArea = g.append('rect')
        .attr('class', 'hover-area')
        .attr('width', innerWidth)
        .attr('height', innerHeight)
        .attr('fill', 'transparent')
        .attr('data-index', index);
    
    // Update latest value display
    if (data.length > 0) {
        const latestData = data.filter(d => d.value !== null).pop();
        if (latestData) {
            document.getElementById(`value-${index}`).textContent = dataset.format(latestData.value);
            document.getElementById(`value-year-${index}`).textContent = `Year ${latestData.year}`;
        }
    }
    
    return {
        svg,
        g,
        xScale,
        yScale,
        crosshair,
        dataPoint,
        hoverArea,
        data,
        dataset,
        innerWidth,
        innerHeight,
        line,
        area
    };
}

function updateAllCharts() {
    charts.forEach((chart, index) => {
        const newData = getCountryData(allData[chart.dataset.name], selectedCountry);
        chart.data = newData;
        
        // Update scales
        const yExtent = d3.extent(newData, d => d.value);
        const yPadding = (yExtent[1] - yExtent[0]) * 0.1 || 1;
        chart.yScale.domain([
            (yExtent[0] || 0) - yPadding,
            (yExtent[1] || 0) + yPadding
        ]);
        
        // Update Y axis
        chart.g.select('.axis-y')
            .transition()
            .duration(500)
            .call(d3.axisLeft(chart.yScale)
                .ticks(5)
                .tickFormat(d => formatLargeNumber(d)));
        
        // Update grid lines
        chart.g.select('.grid').selectAll('.grid-line')
            .data(chart.yScale.ticks(5))
            .transition()
            .duration(500)
            .attr('y1', d => chart.yScale(d))
            .attr('y2', d => chart.yScale(d));
        
        // Update area
        chart.g.select('.area-gradient')
            .datum(newData)
            .transition()
            .duration(500)
            .attr('d', chart.area);
        
        // Update line
        chart.g.select('.data-line')
            .datum(newData)
            .transition()
            .duration(500)
            .attr('d', chart.line);
        
        // Update displayed value
        if (newData.length > 0) {
            const latestData = newData.filter(d => d.value !== null).pop();
            if (latestData) {
                document.getElementById(`value-${index}`).textContent = chart.dataset.format(latestData.value);
                document.getElementById(`value-year-${index}`).textContent = `Year ${latestData.year}`;
            } else {
                document.getElementById(`value-${index}`).textContent = '—';
                document.getElementById(`value-year-${index}`).textContent = 'No data';
            }
        } else {
            document.getElementById(`value-${index}`).textContent = '—';
            document.getElementById(`value-year-${index}`).textContent = 'No data';
        }
    });
}

function setupSynchronizedHover() {
    const yearDisplay = document.getElementById('current-year');
    
    charts.forEach((chart, index) => {
        chart.hoverArea
            .on('mousemove', function(event) {
                const [mouseX] = d3.pointer(event);
                const year = Math.round(chart.xScale.invert(mouseX));
                
                // Update year display
                yearDisplay.textContent = year;
                
                // Highlight all charts at this year
                highlightAllCharts(year);
            })
            .on('mouseleave', function() {
                yearDisplay.textContent = '—';
                clearAllHighlights();
            });
    });
}

function highlightAllCharts(year) {
    charts.forEach((chart, index) => {
        const x = chart.xScale(year);
        
        // Show crosshair
        chart.crosshair
            .attr('x1', x)
            .attr('x2', x)
            .style('opacity', 1);
        
        // Find data point for this year
        const dataPoint = chart.data.find(d => d.year === year);
        
        if (dataPoint && dataPoint.value !== null) {
            const y = chart.yScale(dataPoint.value);
            
            // Show and position data point
            chart.dataPoint
                .attr('cx', x)
                .attr('cy', y)
                .attr('class', 'data-point active');
            
            // Update value display
            document.getElementById(`value-${index}`).textContent = chart.dataset.format(dataPoint.value);
            document.getElementById(`value-year-${index}`).textContent = `Year ${year}`;
        } else {
            chart.dataPoint.attr('class', 'data-point');
            document.getElementById(`value-${index}`).textContent = '—';
            document.getElementById(`value-year-${index}`).textContent = `No data for ${year}`;
        }
    });
}

function clearAllHighlights() {
    charts.forEach((chart, index) => {
        // Hide crosshair
        chart.crosshair.style('opacity', 0);
        
        // Hide data point
        chart.dataPoint.attr('class', 'data-point');
        
        // Reset to latest value
        const latestData = chart.data.filter(d => d.value !== null).pop();
        if (latestData) {
            document.getElementById(`value-${index}`).textContent = chart.dataset.format(latestData.value);
            document.getElementById(`value-year-${index}`).textContent = `Year ${latestData.year}`;
        } else {
            document.getElementById(`value-${index}`).textContent = '—';
            document.getElementById(`value-year-${index}`).textContent = 'No data';
        }
    });
}

// === Window Resize Handler ===
let resizeTimeout;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
        // Redraw all charts
        document.getElementById('charts-container').innerHTML = '';
        createAllCharts();
    }, 250);
});

// === Initialize ===
document.addEventListener('DOMContentLoaded', loadAllData);

