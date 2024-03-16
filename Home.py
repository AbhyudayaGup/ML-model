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

st.markdown("<h1 style='text-align: center; color: white;'> This will ________</h1>" , unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'> Abhyudaya's Project</h1>", unsafe_allow_html=True)
#st.markdown("<h1 style='text-align: center; color: blue;'> Ready to get started?</h1>", unsafe_allow_html=True)

st.title(" ")
st.title(" ")
    
col1,col2,col3 = st.columns(3)

if col2.button("I am ready to begin"):
    switch_page("1")

#col1.image("Gojo1.jpeg")
#col2.image("frown1.jpeg")
