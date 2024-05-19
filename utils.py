import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


def show_html_graph(file_path, height=600):
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    components.html(html_content, height=height, scrolling=True)


def show_download_button(file_path, label, file_name, help):
    with open(file_path, "rb") as file:
        btn = st.download_button(
            label=label,
            data=file,
            file_name=file_name,
            mime='text/csv',
            help=help
        )


def display_csv_preview(file_path, file_name):
    try:
        df = pd.read_csv(file_path)
        st.write(f"Preview of {file_name}:")
        st.dataframe(df.head(20))

    except Exception as e:
        st.error(f"Failed to read {file_name}: {str(e)}")
