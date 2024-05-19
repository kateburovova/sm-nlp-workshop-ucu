# Base
import os
import time

# Internal
from utils import show_html_graph, show_download_button
from authenticate import check_password


# External
import streamlit as st
import streamlit.components.v1 as components

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

show_download_button(file_path='assets/facebook_sample.csv',
                     label='Download FB sample',
                     file_name='FB_sample_data.csv',
                     help='Click to download FB sample data')

show_download_button(file_path='assets/twitter_sample.csv',
                     label='Download X sample',
                     file_name='X_sample_data.csv',
                     help='Click to download X sample data')

show_download_button(file_path='assets/telegram_sample.csv',
                     label='Download TG sample',
                     file_name='TG_sample_data.csv',
                     help='Click to download TG sample data')

# if not check_password():
#     st.stop()
