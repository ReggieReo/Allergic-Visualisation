import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from database_util_st import DatabaseUtil


st.set_page_config(layout="centered")
st.markdown("<h1 style='text-align: center;'>Visualisation on Allergic rhinitis and Evironment Factors</h1>", unsafe_allow_html=True)

db = DatabaseUtil()

container2 = st.container(border=True)
container = st.container(border=True)
with container:
    df_avg = db.get_meta_average()
    df_avg = df_avg.drop(columns=['date'])
    corr = df_avg.corr()
    fig = plt.figure(figsize=(8, 6))
    cmap = sns.diverging_palette(220, 20, as_cmap=True)
    ax = sns.heatmap(df_avg.corr(), annot=True, cmap=cmap)
    st.markdown('<h2 style="text-align: center;">Correlation Heatmap</h2>', unsafe_allow_html=True)
    plt.yticks(rotation=0)
    st.pyplot(fig)

with container2:
    df_avg = db.get_meta_average()
    st.markdown('<h2 style="text-align: center;">Environmental Factors Time Series</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: right;">Click on variable to enable or dissable a line graph</p>', unsafe_allow_html=True)
    fig = px.line(df_avg, x='date', y=df_avg.drop(columns='flare_up').columns[1:])
    fig.update_xaxes(tickmode='auto', nticks=10)
    st.plotly_chart(fig, use_container_width=True)
