import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

df = sns.load_dataset('titanic')
fdf = df.copy()
sidebar = st.sidebar

sidebar.title('Dashboard Filters')
gender = sidebar.multiselect("Genders", options=df['sex'].unique())

pclass = sidebar.multiselect("Passenger Class", options=df['class'].unique())

svcount = sidebar.multiselect("Survived", options=df['survived'].unique())

age = sidebar.slider('Age Range', min_value=int(df['age'].min()),
                     max_value=int(df['age'].max()),
                     value=(int(df['age'].min()),int(df['age'].max())))
if gender:
    fdf = fdf[fdf['sex'].isin(gender)]

if pclass:
    fdf = fdf[fdf['class'].isin(pclass)]

if age:
    fdf = fdf[(fdf['age']>=age[0])&
              (fdf['age']<=age[1])]

if svcount:
    fdf = fdf[fdf['survived'].isin(svcount)]


st.dataframe(fdf)

fig1 = px.histogram(fdf, x="age",nbins=30,title="Age Distribution")

fig2 = px.bar(fdf, x='survived', y='pclass', title='Survival count')

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""**Conclusion** : The age distibution of titanic passenger is 
            right-skewed, with a higher concentration of younger passengers.
            There is a noticable drop in the number of passengers above 60 
            years old """)



