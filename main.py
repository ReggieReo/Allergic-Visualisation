import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from database_util_st import DatabaseUtil


st.markdown("<h1 style='text-align: center;'>Visualisation on Allergic Rhinitis and Evironment Factors</h1>", unsafe_allow_html=True)

db = DatabaseUtil()

container2 = st.container(border=True)
container = st.container(border=True)
container4 = st.container(border=True)
container5 = st.container(border=True)
container3 = st.container(border=True)

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

    st.plotly_chart(fig_heatmap, use_container_width=True) 

with container2:
    df_avg = db.get_meta_average()
    st.markdown('<h2 style="text-align: center;">Environmental Factors Time Series</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">Click on variable to enable or dissable a line graph</p>', unsafe_allow_html=True)
    fig = px.line(df_avg, x='date', y=df_avg.drop(columns='flare_up').columns[1:])


    flare_up_dates = df_avg[df_avg['flare_up'] > 0]['date']
    flare_up_values = df_avg[df_avg['flare_up'] > 0]['avg_pm25']
    fig.add_trace(go.Scatter(x=flare_up_dates, y=flare_up_values, mode='markers', marker=dict(color='red', size=10), name='Flare Up'))

    fig.update_xaxes(tickmode='auto', nticks=10)
    st.plotly_chart(fig, use_container_width=True)

with container3:
    st.markdown("<h2 style='text-align: center;'>Allergic Rhinitis Reaction Count</h2>", unsafe_allow_html=True)
    df_rhinitis = db.get_meta_rhinitis()
    flare_up_count = df_rhinitis['flare_up'].count() 
    fig_pie = px.pie(df_rhinitis, names='flare_up', title=f'Allergic Rhinitis Reaction Count (Total: {flare_up_count})')
    fig_pie.update_traces(hoverinfo='label+percent', textinfo='value')
    st.plotly_chart(fig_pie, use_container_width=True)
    
with container4:
    df_avg = db.get_meta_average()
    st.markdown('<h2 style="text-align: center;">Scatter Plot</h2>', unsafe_allow_html=True)
    df_avg['flare_up'] = df_avg['flare_up']

    selected_attribute = st.selectbox("Select attribute for x axis", df_avg.drop(columns=["date", "flare_up"]).columns, key="first_attribute")

    fig_scatter = px.scatter(df_avg, x=selected_attribute, y='flare_up', 
                            title=f'Scatter Plot: {selected_attribute} vs {"Allergic Rhinitis Reaction"}')
    st.plotly_chart(fig_scatter, use_container_width=True)

with container5:
    st.markdown('<h2 style="text-align: center;">Box Plots</h2>', unsafe_allow_html=True)

    show_allergic_flare_up = st.checkbox("Show only when there's an allergic flare-up", value=True)
    if show_allergic_flare_up:
        df_avg_filtered = df_avg[df_avg['flare_up'] >= 1]
    else:
        df_avg_filtered = df_avg

    selected_attribute = st.selectbox("Select Attribute", df_avg_filtered.drop(columns=["date", "flare_up"]).columns)

    fig_boxplot = px.box(df_avg_filtered, y=selected_attribute, title=f'Box Plot of {selected_attribute}', template="plotly_white", 
                         color_discrete_sequence=['#636EFA'], points="all")
    fig_boxplot.update_layout(yaxis_title=selected_attribute, showlegend=False)
    st.plotly_chart(fig_boxplot, use_container_width=True)
