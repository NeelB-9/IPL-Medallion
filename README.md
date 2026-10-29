# 🏏 IPL Medallion Data Pipeline

A Python-based data engineering project that processes IPL ball-by-ball match data using the **Medallion Architecture** — Bronze, Silver, and Gold — to generate batting statistics and identify top performers.

## 📌 Project Overview

This project transforms raw IPL match data into structured datasets for analysis. Using Python and Pandas, it processes delivery-level records and produces batting metrics such as total runs, balls faced, and strike rate.

## 🏗️ Pipeline Architecture

```text
Cricsheet IPL Match Data (JSON)
             |
             ▼
      🥉 Bronze Layer
       Raw match files
             |
             ▼
      🥈 Silver Layer
   Processed delivery-level data
             |
             ▼
       🥇 Gold Layer
  Aggregated batting statistics
             |
             ▼
       CSV Output Files
```

## 📂 Project Structure

```text
IPL-Medallion/
├── bronze/                 # Raw IPL match JSON files
├── silver/                 # Processed match and delivery data
├── gold/                   # Aggregated batting statistics
│   ├── run_table.csv
│   ├── sr_table.csv
│   └── stats.csv
├── main.py                 # Pipeline implementation
├── match.csv               # Match-level dataset
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Locked dependency versions
└── README.md
```

## ⚙️ Tech Stack

- **Python** — pipeline implementation
- **Pandas** — data processing and aggregation
- **JSON** — raw match data ingestion
- **CSV** — structured data storage
- **Git & GitHub** — version control

## 📊 Key Features

- Processes ball-by-ball IPL match data.
- Organizes data into Bronze, Silver, and Gold layers.
- Extracts delivery-level information, including batter, bowler, runs, and extras.
- Calculates batting statistics such as total runs, balls faced, and strike rate.
- Generates CSV outputs for further analysis.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/NeelB-9/IPL-Medallion.git
cd IPL-Medallion
```

### 2. Install dependencies

If you have `uv` installed:

```bash
uv sync
```

Alternatively, create a virtual environment and install the dependencies listed in `pyproject.toml`.

### 3. Run the pipeline

```bash
uv run python main.py
```

## 📁 Data Source

IPL match data is sourced from [Cricsheet](https://cricsheet.org/), which provides structured cricket match data in JSON format.

## 🔮 Future Improvements

- Automate raw data ingestion and extraction.
- Add validation for missing, malformed, or incomplete match data.
- Improve handling of innings where the target team bats second.
- Add more batting and bowling metrics.
- Develop visual dashboards for performance analysis.

## 👨‍💻 Author

**Neel Bharambe**

Electronics Engineering Student | Interested in Python, Data Engineering, and Analytics
