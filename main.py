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
container3 = st.container(border=True)
container4 = st.container(border=True)

with container:
    df_avg = db.get_meta_average()
    df_avg = df_avg.drop(columns=['date'])
    corr = df_avg.corr().round(2)
    
    st.markdown('<h2 style="text-align: center;">Correlation Heatmap</h2>', unsafe_allow_html=True)
    fig_heatmap = px.imshow(corr, labels=dict(x="Variables", y="Variables"), color_continuous_scale='RdBu_r')

    for i in range(len(corr)):
        for j in range(len(corr)):
            fig_heatmap.add_annotation(text=str(corr.values[i, j]),
                                       x=corr.columns[j],
                                       y=corr.index[i],
                                       showarrow=False,
                                       font=dict(color='black', size=12),
                                       xshift=0.5, yshift=0.5)

    st.plotly_chart(fig_heatmap)

with container2:
    df_avg = db.get_meta_average()
    st.markdown('<h2 style="text-align: center;">Environmental Factors Time Series</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">Click on variable to enable or dissable a line graph</p>', unsafe_allow_html=True)
    fig = px.line(df_avg, x='date', y=df_avg.drop(columns='flare_up').columns[1:])
    fig.update_xaxes(tickmode='auto', nticks=10)
    st.plotly_chart(fig, use_container_width=True)

with container3:
    st.markdown("<h2 style='text-align: center;'>Allergic Flare-up Count</h2>", unsafe_allow_html=True)
    df_rhinitis = db.get_meta_rhinitis()
    flare_up_count = df_rhinitis['flare_up'].sum()  #
    fig_pie = px.pie(df_rhinitis, names='flare_up', title=f'Allergic Flare-up Count (Total: {flare_up_count})')
    st.plotly_chart(fig_pie)
    
with container4:
    df_avg = db.get_meta_average()
    st.markdown('<h2 style="text-align: center;">Correlation Heatmap</h2>', unsafe_allow_html=True)
    df_avg['flare_up'] = df_avg['flare_up'].replace(2, 1)

    selected_attribute = st.selectbox("Select First Attribute", df_avg.columns, key="first_attribute")
    selected_attribute2 = st.selectbox("Select Second Attribute", df_avg.columns, key="second_attribute")

    st.markdown(f"<h2 style='text-align: center;'>Scatter Plot: {selected_attribute} vs {selected_attribute2}</h2>", unsafe_allow_html=True)

    fig_scatter = px.scatter(df_avg, x=selected_attribute, y=selected_attribute2, 
                             title=f'Scatter Plot: {selected_attribute} vs {selected_attribute2}')
    st.plotly_chart(fig_scatter)