# Network Traceroute Visualisation

An interactive network visualisation tool that traces the path of data packets across the internet and displays each hop's geographic location on a world map.

---

## Overview

When you visit a website, your data doesn't travel directly — it hops through multiple routers across different countries before reaching its destination. This project makes that invisible journey visible.

The program runs `traceroute` for multiple destinations, extracts intermediate router IP addresses, maps them to real-world geographic coordinates using a GeoIP database, and renders the complete routing path on an interactive world map.

---

## Features

- Traces routes to multiple destinations in one run
- Extracts hop IP addresses using regex parsing
- Converts IP addresses to geographic coordinates via GeoLite2
- Renders an interactive world map with colored routing paths
- Clickable markers showing IP address and destination info
- Auto-opens the generated map in your browser

---

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| `traceroute` | Discovers network routing paths |
| `subprocess` | Executes traceroute commands from Python |
| `re` (regex) | Extracts IP addresses from traceroute output |
| GeoLite2-City | IP geolocation database |
| `geoip2` | Python API for GeoLite2 |
| `folium` | Interactive map visualisation |
| HTML | Displays final visualisation in browser |

---

## Project Structure

```
network-traceroute-visualisation/
├── 2403118_Assignment1.py     → Main program
├── destination_list.txt       → List of target websites
├── GeoLite2-City.mmdb         → GeoIP database (not included, see setup)
└── README.md                  → Project documentation
```

---

## Setup & Installation

### 1. Install dependencies
```bash
pip install geoip2 folium
```

### 2. Get the GeoLite2 database
- Sign up for a free account at [MaxMind](https://www.maxmind.com)
- Download `GeoLite2-City.mmdb`
- Place it in the project directory

### 3. Add destinations
Edit `destination_list.txt` and add one website per line:
```
google.com
github.com
bbc.co.uk
```

---

## How to Run

```bash
python 2403118_Assignment1.py
```

The program will:
1. Read destinations from `destination_list.txt`
2. Run traceroute for each destination
3. Extract and geolocate each hop IP
4. Generate an interactive HTML map
5. Automatically open the map in your browser

---

## How It Works

```
destination_list.txt
        ↓
Run traceroute for each destination
        ↓
Extract hop IP addresses using regex
        ↓
Convert IPs → coordinates using GeoLite2
        ↓
Plot markers and paths on folium map
        ↓
Save and open interactive HTML map
```

---

## Output

An interactive world map is generated showing:
- **Markers** — each representing a network hop
- **Colored lines** — showing the packet routing path per destination
- **Popups** — clicking a marker displays the IP address and destination

This visualisation clearly shows how internet traffic travels across different geographic regions before reaching its final destination.

---

## Learning Outcomes

- Practical understanding of `traceroute` and network routing
- Visualisation of real-world packet paths across the internet
- Exposure to network diagnostic tools
- Understanding the relationship between logical routing and physical geography
- Working with IP geolocation databases

---

## Platform Compatibility

| Platform | Command | Status |
|---|---|---|
| macOS | `traceroute` | ✅ Supported |
| Linux | `traceroute` | ✅ Supported |
| Windows | `tracert` | ⚠️ Minor code changes required |

---

## Note

The `GeoLite2-City.mmdb` database file is not included in this repository due to its size. Please download it directly from [MaxMind](https://www.maxmind.com) and place it in the project directory before running.
