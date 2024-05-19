import streamlit as st
import streamlit.components.v1 as components


def show_html_graph(file_path, height=600):

    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    components.html(html_content, height=height, scrolling=True)
