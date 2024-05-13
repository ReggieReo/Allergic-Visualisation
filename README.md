# Allergic Rhinitis and Environmental Factors
Github repository:<br>
[API server](https://github.com/ReggieReo/Allergic-Rhinitis-and-Environmental-Factors)<br>
[Visualization](https://github.com/ReggieReo/Allergic-Visualisation)

## Members
| Student ID | Name|
| -------- | ------- |
| 6510545764| Setthapon Thadisakun|
| 6510545420 |Tantikon Phasanphaengsi|

## Overview
Allergic Rhinitis and Environmetal Factors investigates how environmental factors influence allergy symptoms. We focus collecting on environmental factors such as data on dust levels, temperature, and humidity, as these elements could affect allergic rhinitis. We will also survey individuals with allergic rhinitis to determine whether they experience symptoms in the morning.<br>
All data were collected between 15-04-2024 to 10-05-2024<br>
This directory is for visualization web application.


## Required libraries and tools
Python version >= 3.8
pandas<br>
sqlalchemy<br>
mysqlclient<br>
streamlit<br>
watchdog<br>
seaborn<br>
plotly<br>

## Building and running
1. Change directory to the visusalization directory.
```
cd visualization
```
2. Create virtual environment.
```
python -m venv venv
```
3. Activate virtual environment.
Macos/Linux
```
./venv/bin/activate
```
Windows
```
.\venv\Scripts\activate
```
5. Install the required packages.
```
pip install -r requirements.txt
```
* If install requirements package fail might be because of mysqlclient package check out its requirement [mysqlclient requirement](https://github.com/PyMySQL/mysqlclient/blob/main/README.md#install)
6. Edit config file.
```
nvim ./.streamlit/secrets.toml\ example or use your prefered text editor
```
7. Run visualization web application.
```
streamlit run main.py
```
8. Open visualization web application.
```
http://127.0.0.1:8501 or http://localhost:8501
```

