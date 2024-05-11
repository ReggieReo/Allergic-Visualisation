from pandas import DataFrame
import streamlit as st
from streamlit.connections import SQLConnection

class DatabaseUtil:

    def __init__(self):
        self.conn:SQLConnection = st.connection("mydb", type="sql", max_entries=1)

    def get_meta_aqi(self):
        df_aqi = self.conn.query(
            """
            SELECT date(ts), aqi, pm10, pm25
            FROM aqi
            """
        )
        return df_aqi

    def get_meta_temp(self):
        df_temp_hum = self.conn.query(
            """
            SELECT date(ts), temperature, humidity
            FROM temp_humid
            """
        )
        return df_temp_hum

    def get_meta_rhinitis(self):
        df_rhinitis = self.conn.query(
            """
            SELECT date, flare_up
            FROM flare_up
            """
        )
        return df_rhinitis
    
    
    def get_meta_average(self):
        df_average_mete = self.conn.query(
            """
            SELECT uqi_fare_up.date `date`, avg(avg_aqi) `avg_aqi`, avg(avg_pm10) `avg_pm10`, avg(avg_pm25) `avg_pm25`, avg(avg_temp) `avg_temp`, avg(avg_humid) `avg_humid`, sum(flare_up) `flare_up`
            FROM (SELECT date, flare_up
                FROM flare_up
                ) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi, AVG(pm10) as avg_pm10, AVG(pm25) as avg_pm25
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(temperature) as avg_temp, AVG(humidity) as avg_humid
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_temp ON date_avg_temp.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.date
            """
        )
        return df_average_mete

