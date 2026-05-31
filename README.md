# 🌤️ Weather ETL Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![unittest](https://img.shields.io/badge/unittest-Testing-brightgreen?style=for-the-badge&logo=python&logoColor=white)

## 📖 Project Overview

The **Weather ETL Pipeline** is an end-to-end Data Engineering project designed to extract real-time weather data from the OpenWeather API, transform it into a structured format, and load it into a PostgreSQL database for downstream analytics. 

This project demonstrates core Data Engineering principles, including API integration, data modeling, automated testing, and modular architecture. It is built with a focus on clean code, maintainability, reliability, and readiness for production scale.

## ✨ Features

- **Real-Time Data Extraction:** Fetches live weather data seamlessly from the OpenWeather REST API.
- **Data Lake Simulation:** Saves raw, unprocessed data in JSON format for auditing and historical reference.
- **Robust Transformation:** Cleans, formats, and structures the raw data into a relational format suitable for analysis.
- **Database Loading:** Safely loads the processed data into a PostgreSQL relational database using best practices.
- **Automated Testing:** Ensures pipeline integrity with comprehensive `unittest` coverage.
- **Centralized Logging:** Tracks pipeline execution, tracks data lineage steps, and captures errors through a dedicated logging system.
- **Modular Architecture:** Strict separation of concerns (Extractor, Transformer, Loader) for easy scalability and maintenance.

## 🏗️ Architecture Diagram

```text
+-------------------+       +-----------------------+       +-------------------+
|                   |       |      Extractor        |       |                   |
|  OpenWeather API  | =====>|  (Fetch REST API &    | =====>|  Local Storage    |
|                   |       |   Save Raw JSON)      |       |  (data/raw/)      |
+-------------------+       +-----------------------+       +-------------------+
                                        |
                                        v
                            +-----------------------+       +-------------------+
                            |     Transformer       |       |                   |
                            | (Clean & Structure    | =====>|  Local Storage    |
                            |  Data)                |       | (data/processed/) |
                            +-----------------------+       +-------------------+
                                        |
                                        v
                            +-----------------------+       +-------------------+
                            |       Loader          |       |                   |
                            |  (Insert into DB)     | =====>| PostgreSQL DB     |
                            |                       |       |                   |
                            +-----------------------+       +-------------------+
```

## 📁 Folder Structure

```text
weather-etl/
│
├── config/
│   └── settings.py          # Configuration variables and env loading
│
├── data/
│   ├── raw/                 # Landing zone for raw JSON data
│   └── processed/           # Transformed data ready for loading
│
├── database/
│   ├── connection.py        # PostgreSQL connection manager
│   └── schema.sql           # Database schema definition (DDL)
│
├── etl/
│   ├── extractor.py         # API connection and data extraction logic
│   ├── transformer.py       # Data cleaning and transformation logic
│   └── loader.py            # Database insertion logic
│
├── logs/
│   └── app.log              # Application execution logs
│
├── tests/
│   └── test_pipeline.py     # Unit tests for ETL components
│
├── utils/
│   └── logger.py            # Custom logging configuration
│
├── main.py                  # Pipeline orchestrator
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## 🛠️ Tech Stack

- **Language:** Python 3.14.2
- **Database:** PostgreSQL
- **External API:** OpenWeather API (REST)
- **Testing:** Python `unittest`
- **Key Libraries:** `requests`, `psycopg2-binary`, `python-dotenv`, `logging`, `json`

## 🚀 Installation Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/weather-etl-pipeline.git
   cd weather-etl-pipeline
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Environment Setup (.env)

Create a `.env` file in the root directory and add your secret credentials. Do not commit this file to version control.

```env
# API Configuration
OPENWEATHER_API_KEY=your_api_key_here
LAT=-6.1754049
LON=106.827168

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=weather_db
DB_USER=postgres
DB_PASSWORD=your_password
```

## 🗄️ Database Setup

Before running the pipeline, initialize the PostgreSQL database schema.

1. Ensure your PostgreSQL server is running locally or remotely.
2. Create a database named `weather_db` (or matching your `.env`).
3. Run the schema creation script from the command line:
   ```bash
   psql -U postgres -d weather_db -f database/schema.sql
   ```

## ▶️ How to Run the Project

Execute the main orchestrator script to trigger the entire ETL process:

```bash
python main.py
```

*Check the `logs/app.log` file or the console output to monitor the pipeline's progress and debug if necessary.*

## 🧪 How to Run Tests

To ensure all components are functioning correctly and reliably, run the test suite:

```bash
python -m unittest discover -s tests -v
```

## 📊 Sample Output

**Console/Log Examples:**
```text
2026-05-31 14:26:58,970 | weather_etl | INFO | Starting ETL Pipeline...
2026-05-31 12:35:54,382 | weather_etl | WARNING | Missing optional field 'visibility' in API response, using default value.
2026-05-31 14:11:48,678 | weather_etl | ERROR | Loading failed: column "latitude" of relation "weather_data" does not exist
```

**Database Record Example (weather_data table):**
| id | latitude | longitude | location_name | country | temperature | feels_like | humidity | pressure | weather_main | weather_description | wind_speed | visibility | recorded_at | created_at |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | -6.1754 | 106.8272 | Pecenongan | ID | 30.91 | 37.91 | 77 | 1009 | Clouds | scattered clouds | 4.12 | 8000 | 2026-05-31 14:26:59 | 2026-05-31 14:26:59 |

## 🛡️ Testing Strategy

The project utilizes Python's built-in `unittest` framework to guarantee data reliability:
- **Unit Testing:** Tests individual functions and ETL stages in isolation.
- **Mocking:** Uses `unittest.mock` to simulate OpenWeather API responses, preventing unnecessary network calls, flakiness, and rate limit exhaustion during tests.
- **Database Testing:** Verifies connection handlers and ensures SQL transformations match expected schemas before insertion.

## 📈 Future Improvements

To scale this pipeline for production-grade environments, the following enhancements are planned:
- **Orchestration:** Integrate Apache Airflow or Prefect for robust scheduling, retries, and dependency management.
- **Cloud Migration:** Deploy the pipeline using AWS Lambda or GCP Cloud Functions, and transition the database to Amazon RDS or Cloud SQL.
- **Data Quality (DQ):** Implement Great Expectations for rigorous data validation and anomaly detection in the pipeline.
- **Containerization:** Wrap the application in Docker for consistent deployment and scalability across environments.
