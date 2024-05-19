# Internal
from utils import show_html_graph, show_download_button, display_csv_preview

# External
import streamlit as st

st.set_page_config(layout="wide")

display_csv_preview(file_path='assets/facebook_sample.csv', file_name='Facebook sample')

show_download_button(file_path='assets/facebook_sample.csv',
                     label='Download FB sample',
                     file_name='FB_sample_data.csv',
                     help='Click to download FB sample data')

st.markdown('<hr style="border:1px solid black">', unsafe_allow_html=True)

display_csv_preview(file_path='assets/twitter_sample.csv', file_name='X sample')

show_download_button(file_path='assets/twitter_sample.csv',
                     label='Download X sample',
                     file_name='X_sample_data.csv',
                     help='Click to download X sample data')

st.markdown('<hr style="border:1px solid black">', unsafe_allow_html=True)

display_csv_preview(file_path='assets/telegram_sample.csv', file_name='Telegram sample')

show_download_button(file_path='assets/telegram_sample.csv',
                     label='Download TG sample',
                     file_name='TG_sample_data.csv',
                     help='Click to download TG sample data')

st.markdown('<hr style="border:1px solid black">', unsafe_allow_html=True)

st.markdown(r'''
Betweenness centrality quantifies the number of times a node acts as a bridge along the shortest path between two other nodes.
''')

show_html_graph('assets/recovery_win_betweenness_centrality_size_viz.html')

st.markdown('<hr style="border:2px solid gray">', unsafe_allow_html=True)

