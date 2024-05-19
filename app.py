import os
import streamlit as st
import time
from authenticate import check_password
from utils import show_html_graph
import streamlit.components.v1 as components

#
# import plotly.express as px
# import streamlit.components.v1 as components
#
# from langchain import hub
# from datetime import datetime
# from langchain import callbacks
# from elasticsearch import Elasticsearch
# from elasticsearch import BadRequestError
# from elasticsearch.exceptions import NotFoundError
# from angle_emb import AnglE, Prompts
# from langchain_openai import ChatOpenAI
# from authentificate import check_password
# from utils import (display_distribution_charts,populate_default_values, project_indexes,
#                    populate_terms,create_must_term, create_dataframe_from_response,flat_index_list,
#                    search_elastic_below_threshold)

#
# es_config = {
#     'host': st.secrets['ld_rag']['ELASTIC_HOST'],
#     'port': st.secrets['ld_rag']['ELASTIC_PORT'],
#     'api_key': st.secrets['ld_rag']['ELASTIC_API']
# }

st.set_page_config(layout="wide")


st.markdown(r'''
Betweenness centrality quantifies the number of times a node acts as a bridge along the shortest path between two other nodes.
''')

show_html_graph('assets/recovery_win_betweenness_centrality_size_viz.html')

file_path = 'assets/facebook_sample.csv'

with open(file_path, "rb") as file:
    btn = st.download_button(
        label="Download CSV",
        data=file,
        file_name='sample_data.csv',
        mime='text/csv',
        help="Click to download the CSV file."
    )


if not check_password():
    st.stop()
