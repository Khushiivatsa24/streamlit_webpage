import streamlit as st
import plotly.express as px
import pandas as pd

# Create a sample dataset for experimental results
data = {
    'Experiment': ['Experiment 10','Experiment 10','Experiment 10','Experiment 10','Experiment 10','Experiment 10','Experiment 10','Experiment 9', 'Experiment 9','Experiment 9','Experiment 9','Experiment 9','Experiment 9',],
    'Result': [25,0,22.5,0.5,17,2,13,3,10.5,4,8.4,7.6,6.6,4.5,3,1.75],
    'Category': [100,100,500,500,1000,1000,1500,1500,2000,2000.100,200,400,1000,2200,4700]
}

df = pd.DataFrame(data)

# Create a Streamlit app
st.title("Experimental Results")

# Create a dropdown menu to select experiments
experiments = ['Experiment 10', 'Experiment 9']
selected_experiment = st.selectbox("Select Experiment", experiments)

# Filter the data based on the selected experiment
filtered_df = df[df['Experiment'] == selected_experiment]

# Create a Plotly graph
fig = px.line(filtered_df, x='Category', y='Result',title=f'Results of {selected_experiment},)

# Display the graph
st.plotly_chart(fig)
