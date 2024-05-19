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

import streamlit as st

text_and_formula = """
Betweenness centrality quantifies the number of times a node acts as a bridge along the shortest path between two other nodes. Let \\( \sigma(V_j, V_k) \\) be the number of shortest paths from node \\( V_j \\) to node \\( V_k \\), and \\( \sigma(V_j, V_k \mid V_i) \\) the number of those paths that pass through node \\( V_i \\). The betweenness centrality of a node \\( V_i \\) is given by:

\\[
C_B(V_i) = \sum_{V_i \neq V_j \neq V_k \in V} \dfrac{\sigma(V_j, V_k \mid V_i)}{\sigma(V_j, V_k)} \times \dfrac{2}{(|V| - 1)(|V| - 2)}
\\]

where \\( |V| \\) is the number of nodes in the graph.
"""

st.markdown(text_and_formula)


show_html_graph('assets/recovery_win_betweenness_centrality_size_viz.html')


if not check_password():
    st.stop()
