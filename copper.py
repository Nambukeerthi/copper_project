import streamlit as st
from streeamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import pickle

st. set_page_config(page_title='Indutrial Copper', initial_sidebar_state= 'expanded',
                   layout= 'wide')

with st.sidebar:
  selected = option_menu('Main Menu', options=['Home', 'Prediction'], icons=['house','lightbulb'], default_index=1,orientation='vertical')
class option():
  country_values = [28.,  25.,  30.,  32.,  38.,  78.,  27.,  77., 113.,  79.,  26., 39.,  40.,  84.,  80., 107.,  89.]
  status_values = ['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered', 'Offerable']
  status encoded = ['Won':0, 'Draft':1, 'To be approved':2, 'Lost':3, 'Not lost for AM':4, 'Wonderful':5, 'Revised':6, 'Offered':7, 'Offerable':8]
  item_type_values = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
  item_type_encoded = ['W':0.0, 'WI':1.0, 'S':2.0, 'Others':3.0, 'PL':4.0, 'IPL':5.0, 'SLAWR':6.0]
  application_values = [10.0, 41.0, 28.0, 59.0, 15.0, 4.0, 38.0, 56.0, 42.0, 26.0, 27.0, 19.0, 20.0, 66.0, 29.0, 22.0, 40.0, 25.0, 67.0, 79.0, 3.0, 99.0,  2.0,  5.0, 39.0, 69.0, 70.0, 65.0, 58.0, 68.0]
  product_ref_values = [1670798778, 1668701718,     628377,     640665,     611993, 
       1668701376,  164141591, 1671863738, 1332077137,     640405,
       1693867550, 1665572374, 1282007633, 1668701698,     628117,
       1690738206,     628112,     640400, 1671876026,  164336407,
        164337175, 1668701725, 1665572032,     611728, 1721130331,
       1693867563,     611733, 1690738219, 1722207579,  929423819,
       1665584320, 1665584662, 1665584642]


if selected == "Prediction":
  title_text ='''<h1 style='font_size: 32px; text-align: center; color: grey;' >Copper Selling Price and Status prediction</h1'''
  st.markdown(title_text, unsafe_allow_html=True)
  

