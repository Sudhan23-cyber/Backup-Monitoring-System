
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Backup Monitoring Log System", layout="centered")

st.title("Backup Monitoring Log System")
st.subheader("Backup & Recovery Management")

# Initialize session state
if "logs" not in st.session_state:
    st.session_state.logs = []

st.markdown("### Add Backup Record")

backup_date = st.date_input("Backup Date", date.today())
backup_status = st.selectbox("Backup Status", ["Success", "Failed", "In Progress"])

if st.button("Add Record"):
    st.session_state.logs.append({
        "Backup Date": backup_date,
        "Backup Status": backup_status
    })
    st.success("Backup record added successfully!")

st.markdown("### Backup Logs")

if st.session_state.logs:
    df = pd.DataFrame(st.session_state.logs)
    st.dataframe(df)
else:
    st.info("No backup records available.")
