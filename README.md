# data_test_streamlit

# 🧠 LendingClub Loan Risk Analysis (Module 1)

This project analyzes peer-to-peer loan performance using LendingClub’s historical data from 2007 to 2018. It is **Module 1** of a larger multi-source loan risk dashboard built with **Python, pandas, and Streamlit**.

> ✅ Includes full data pipeline: ingestion, cleaning, target labeling, and export
> ✅ Final data is used in a shared Streamlit dashboard (`app.py`) for visualization

---

## 🔍 What This Project Does

* Cleans LendingClub loan data (\~2.2M records)
* Selects relevant financial and credit risk fields
* Creates a binary loan outcome (`Fully Paid` = 0, `Charged Off/Default` = 1)
* Outputs a cleaned dataset ready for modeling or visualization

---

## 📁 Folder Structure

```
project_root/
├── data/
│   ├── accepted_2007_to_2018Q4.csv       # Raw Kaggle dataset
│   └── lendingclub_processed.csv         # Cleaned output
├── lendingclub_clean.py                  # Cleaning script
├── app.py                                # Streamlit dashboard (shared)
├── README.md                             # You're reading it
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install pandas numpy streamlit
```

### 2. Download and unzip the dataset

From Kaggle:
[LendingClub Loan Data (2007–2018)](https://www.kaggle.com/datasets/wordsforthewise/lending-club)

Place the file in the `data/` folder as:

```
data/accepted_2007_to_2018Q4.csv
```

### 3. Run the cleaning script

```bash
python lendingclub_clean.py
```

This will create:

```
data/lendingclub_processed.csv
```

### 4. (Optional) Launch the Streamlit dashboard

```bash
streamlit run app.py
```

---

## 📦 Requirements

* Python 3.8+
* pandas
* numpy
* streamlit (optional for dashboard)

---

## ✅ Outputs

* Cleaned CSV for modeling or analysis
* Ready-to-use input for `app.py` dashboard
* Modular structure supports expansion with other loan datasets (Fannie Mae, SBA, etc.)

---

## 📙 Part of a Multi-Module Risk Analytics Platform

| Module | Dataset Source       | Script                 | Notes         |
| ------ | -------------------- | ---------------------- | ------------- |
| 1      | LendingClub (Kaggle) | `lendingclub_clean.py` | Done          |
| 2      | Fannie Mae CRT       | `fanniemae_clean.py`   | Coming soon   |
| 3      | SBA 7(a)/504 Loans   | `sba_clean.py`         | Coming soon   |
| 4      | PPP & Disaster Loans | `ppp_clean.py`         | Coming soon   |
| 5      | Synthetic/NLP Loans  | `synthetic_clean.py`   | Coming soon   |

---

## 🧠 Author

**Chris Goodpaster**
📧 \[LinkedIn]\[https://www.linkedin.com/in/christopher-goodpaster-79320542/]
