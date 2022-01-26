#importar blibliotecas
import streamlit as st
import pandas as pd
import numpy as np

DATA_COLUMN="date/time"
DATA_URL="https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"

@st.cache
def load_data(nrows):
    data =pd.read_csv(DATA_URL,nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data["date/time"] = pd.to_datetime(data["date/time"])

    return data


data_load_state = st.text("Loading ...")
data = load_data(10000)
data_load_state.text("Done!")


if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)

st.subheader("Number of Run per hour")
hist_values = np.histogram(data["date/time"].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

#Interatividade
hour_to_filter = st.slider('hour',0 ,23 , 17)
filtered_data = data[data[DATA_COLUMN].dt.hour == hour_to_filter]

st.subheader("Map for hour {}:".format(hour_to_filter))
st.map(filtered_data)


