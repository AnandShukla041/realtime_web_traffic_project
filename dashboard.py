import streamlit as st
import pandas as pd
import plotly.express as px
import time
from consumer import get_metrics

st.set_page_config(page_title="Real-Time Web Traffic Dashboard", layout="wide")
st.title("🌐 Real-Time Web Traffic Analytics")

placeholder = st.empty()

while True:
    metrics = get_metrics()
    pages_data = pd.DataFrame(list(metrics['pages'].items()), columns=['Page', 'Views'])

    with placeholder.container():
        st.subheader(f"Active Users: {metrics['active_users']}")
        if not pages_data.empty:
            fig = px.bar(pages_data, x='Page', y='Views', title="Page Views", color='Page')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("Waiting for events...")

    time.sleep(5)
