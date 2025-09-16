# 🚀 Data Engineering Pipelines (Portfolio)

This repository contains hands-on **data engineering projects** demonstrating ETL, orchestration, and streaming pipelines using modern big data tools.  
It is an evolving portfolio where I will keep adding projects step by step.  

---

## 📂 Projects

### 1️⃣ Spark ETL Pipeline (CSV → Parquet)
- **Tech**: Python, Apache Spark  
- **Steps**:
  - Extract: Reads data from `input_data.csv`
  - Transform: Filters records where `age > 30`
  - Load: Stores results in `Parquet` format (`output_parquet/`)  
- **How to Run**:
  ```bash
  python spark_pipeline.py
