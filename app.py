import os
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine



# Database connection using SQLAlchemy
DB_CONFIG = {
    "dbname": "timeseriesdb",
    "user": "++++",
    "password": "+++",
    "host": "your_host",
    "port": ++++,
}

# Create database connection
engine = create_engine(f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}")

# Lake Mapping (ID, Name)
lakes = {
    214001072: "Lake Maggiore",
    232014511: "Bielersee",
    232014514: "Schwyz",
    232014562: "Klöntalersee",
    232014579: "Lungernsee",
    232014665: "Oberaaarsee",
    232014811: "Göscheneralpsee",
    232014812: "Lac de Schiffenen",
    232014823: "Brienzersee",
    232014884: "Lac de Schiffenen",
}

# Streamlit App Title
st.title(" DETECT_Swiss_Reservoir Dashboard")

# Select Lake Name (Dropdown)
selected_lake = st.selectbox("Choose a Lake", list(lakes.values()))

# Get Lake ID from Selected Name
selected_lake_id = [key for key, value in lakes.items() if value == selected_lake][0]

# Date selection
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# Variable selection
variable = st.selectbox("Choose a variable", ["wsh", "wlsd", "np", "area", "wsc"])

# Fetch and display data when the button is clicked
if st.button("Show Data"):
    query = f"""
        SELECT time, {variable} FROM time_series_data
        WHERE subgroup_id = {selected_lake_id} 
        AND time BETWEEN '{start_date}' AND '{end_date}'
        ORDER BY time;
    """
    df = pd.read_sql(query, engine)

    if not df.empty:
        # Create a Grafana-style plot with markers
        fig = px.line(
            df, x="time", y=variable,
            title=f"{variable} Time Series ({start_date} → {end_date}) - {selected_lake}",
            markers=True  # Adds points like Grafana
        )

        # Update X-axis to show years properly
        fig.update_xaxes(
            title_text="Time [years]",
            tickformat="%Y",  # Yearly format
            showgrid=True,
        )

        # Update Y-axis with units (modify if needed)
        fig.update_yaxes(
            title_text=f"{variable} [meter]",  # Change 'unit' to actual measurement
            showgrid=True,
        )

        # Improve overall layout (background, grid, font)
        fig.update_layout(
            template="plotly_dark",  # Dark mode like Grafana
            xaxis=dict(showline=True, showgrid=True),
            yaxis=dict(showline=True, showgrid=True),
            font=dict(size=14),
        )

        # Display the chart
        st.plotly_chart(fig)

        # Show Data Preview
        st.write("### Data Preview")
        st.write(df.head())

        # **Download CSV Button**
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label=" Download CSV",
            data=csv,
            file_name=f"{selected_lake}_{variable}_data.csv",
            mime="text/csv",
        )
    else:
        st.warning("No data available for this lake and time period.")

