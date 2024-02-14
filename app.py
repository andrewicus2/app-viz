import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


image_nyu = Image.open("New-York-University-Logo.png")
st.image(image_nyu, width = 100)


st.title("Wine Exploration")


df = pd.read_csv("winequality-red.csv")

st.write("Visualizations")

list_variables = df.columns
user_selection = st.multiselect("Select two variables",list_variables,["quality", "chlorides"])


# quality_min, quality_max = st.sidebar.slider('Select Quality Range', min_value=int(df['quality'].min()), max_value = int(df['quality'].max()))



tab1, tab2 = st.tabs(["Line Chart", "Bar Chart"])





tab1.title("Line Chart")
tab1.line_chart(data = df, x = user_selection[0], y = user_selection[1])

tab2.title("Bar Chart")
tab2.bar_chart(data = df, x = user_selection[0], y = user_selection[1])



if st.button("Generate Report"):
  import streamlit.components.v1 as components
  st.title("Sweetviz Report of the Data")
  report_path = "report.html"
  HtmlFile = open(report_path, 'r', encoding = 'utf-8')
  source_code = HtmlFile.read()
  components.html(source_code, height = 1000, width = 1000)
