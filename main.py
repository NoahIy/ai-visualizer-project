import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Interactive Data Visualization with Streamlit and Plotly")
st.write("This app allows you to visualize data interactively using Plotly.")
files=st.file_uploader("Upload a CSV file", type=None)
if files is not None:
    df=pd.read_csv(files)
    st.subheader("Data Preview")
    st.dataframe(df) 
    chart=go.Figure()
    chart.add_trace(go.Bar(x=df['model'], y=df['precision'], name='Precision'))
    chart.add_trace(go.Bar(x=df['model'], y=df['recall'], name='Recall'))
    chart.add_trace(go.Bar(x=df['model'], y=df['f1_score'], name='F1 Score'))
    chart.update_layout(
            title='Model Performance Metrics',
            xaxis_title='Model',
            yaxis_title='Score',
            barmode='group'  # Group bars side-by-side
        )
    st.plotly_chart(chart)
else:
    st.warning("Please upload a CSV file to visualize the data.")