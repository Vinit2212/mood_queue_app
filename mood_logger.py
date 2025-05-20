import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import json
from io import StringIO

SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
SHEET_NAME = 'MoodLog'

def connect_sheet():
    """Connect to Google Sheet using credentials stored in Streamlit Secrets"""
    creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1
    return sheet

def log_mood(mood, note):
    """Log a new mood entry with timestamp and add headers if missing"""
    sheet = connect_sheet()

    # To prevent error - If sheet is empty, add header row
    if not sheet.get_all_values():
        sheet.append_row(["Timestamp", "Mood", "Note"])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, mood, note])