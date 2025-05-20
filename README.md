## A lightweight internal tool for tracking the emotional tone of customer support tickets throughout the day.

---

## Purpose

A Streamlit Mood Queue app created for a take home assignment.

---

## Features

- **Log Moods** — Select a mood (😊 😠 😕 🎉) and add an optional note.
- **Visualize Trends** — View a bar chart of mood counts for any selected day.
- **Auto-updating Data** — Logs are stored in a shared Google Sheet in real time.
- **Error-handled UX** — Built to gracefully handle empty logs, bad dates, or missing data.

---

## How It Works

1. The app connects to a Google Sheet using a secure service account.
2. Each entry includes:
   - Timestamp
   - Mood (emoji + label)
   - Optional user note
3. The app aggregates moods by date and shows a Plotly bar chart.

---

## Try It Live

👉 [**Live App on Streamlit**](https://moodqueueapp-vajc73yynm3akyan3o2jmn.streamlit.app/)  

---

## Example Sheet

🔗 [View Google Sheet](https://docs.google.com/spreadsheets/d/1Joq4ESO3GNgaD2Jq4X8oZujGg_io7wMfA8iMAM7fgdg/edit?gid=0#gid=0)

---

## Tech Stack

- Python
- Streamlit
- Plotly
- Pandas
- Google Sheets API
- OAuth2Client + GSpread

---

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/mood-queue-app.git
cd mood-queue-app

