import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown('''How do I use it?
-
-
- ''')

col1,col2,col3 = st.columns(3)

if col2.button("I am ready to try it myself!"):
    switch_page("2")
