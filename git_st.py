import streamlit as st
import os
st.title('Hi :cat:')
os.system('git config --global user.name "napoles-uach"')
os.system('git config --global user.email "jnapoles@uach.mx"')
os.system('git config --global pull.rebase false')
os.system('git clone https://napoles-uach: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@github.com/napoles-uach/simple.git')
os.system('git fetch')
os.system('git merge FETCH_HEAD')
