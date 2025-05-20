import streamlit as st
import pandas as pd
import plotly.express as px
from mood_logger import log_mood, connect_sheet
from datetime import datetime

st.set_page_config(page_title="Mood of the Queue", page_icon="🎭")

st.title("🎭 Mood of the Queue")
st.write("Log how the ticket queue *feels* right now.")

# Recoding Mood
with st.form("log_form"):
    mood = st.selectbox("Choose Mood", ["😊 Happy", "😠 Angry", "😕 Confused", "🎉 Celebratory"])
    note = st.text_input("Optional Note")
    submitted = st.form_submit_button("Submit")
    if submitted:
        log_mood(mood, note)
        st.success("Mood Recorded Successfully!")

# Visualization
st.subheader("📊 Mood Trend by Day")

try:
    sheet = connect_sheet()
    data = pd.DataFrame(sheet.get_all_records())
    data.columns = [col.strip().capitalize() for col in data.columns]

    if not data.empty and "Timestamp" in data.columns:
        # Convert Timestamp to datetime and sort
        data["Timestamp"] = pd.to_datetime(data["Timestamp"], errors="coerce")
        data = data.dropna(subset=["Timestamp"])
        data = data.sort_values(by="Timestamp", ascending=False)

        # Extract available dates
        available_dates = sorted(data["Timestamp"].dt.date.unique())

        if available_dates:
            today = datetime.now().date()
            default_date = today if today in available_dates else available_dates[-1]

            selected_date = st.date_input(
                "Select a date to view mood trend",
                value=default_date,
                min_value=min(available_dates),
                max_value=max(available_dates)
            )

            data_selected = data[data["Timestamp"].dt.date == selected_date]

            if not data_selected.empty:
                mood_counts = data_selected["Mood"].value_counts().reset_index()
                mood_counts.columns = ["Mood", "Count"]
                fig = px.bar(
                    mood_counts, 
                    x="Mood", 
                    y="Count", 
                    color="Mood", 
                    title=f"Mood Trend for {selected_date}"
                )
                fig.update_yaxes(dtick=1)
                st.plotly_chart(fig)
            else:
                st.info("No moods logged for that date.")
        else:
            st.info("No mood data available yet. Please log one above to begin.")
    else:
        st.info("No mood data available yet. Please log one above to begin.")

except Exception as e:
    st.error(f"Something went wrong while loading mood data: {e}")