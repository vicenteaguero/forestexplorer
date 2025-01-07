# streamlit/src/layout.py

import streamlit as st


from src.params import PATHS, GITHUB_URL, ABOUT_URL

def setup_layout(page_title: str, page_icon: str):
    st.set_page_config(
        layout='wide',
        page_title=page_title,
        initial_sidebar_state='expanded',
        menu_items={
            'Get help': GITHUB_URL,
            'Report a bug': GITHUB_URL+'/issues',
            'About': ABOUT_URL
        }
    )
    st.logo(image=PATHS['logo-dark'], link=GITHUB_URL, size='large')

def setup_pages():
    pages = {
        'Home': [
            st.Page(page=PATHS['pages']['home'], title='Home', icon='🏠'),
            st.Page(page=PATHS['pages']['docs'], title='Docs', icon='📚'),
        ],
        'Basics': [
            st.Page(page=PATHS['pages']['decision_tree'], title='Decision Tree', icon='🌿'),
            st.Page(page=PATHS['pages']['random_forest'], title='Random Forest', icon='🌲'),
        ],
        'Advanced': [
            st.Page(page=PATHS['pages']['explanaibility'], title='Explainability', icon='🔍'),
            st.Page(page=PATHS['pages']['fairness'], title='Fairness', icon='🎯'),
        ],
    }
    nav = st.navigation(pages)
    nav.run()

def setup_custom_css():
    styles = ['base']
    for style in styles:
        with open(PATHS[f'{style}_css']) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
