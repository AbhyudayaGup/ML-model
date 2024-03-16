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

st.title("Enter the picture here:")


from ultralytics import YOLO
from PIL import Image

@st.cache_resource

def mod():
    model = YOLO("best.pt")
    return model

st.title("Predictions")
img = st.file_uploader("Upload an image of an animal to check its class", type=["jpg", "jpeg", "png"])
if img is not None:
    img = Image.open(img)
    st.image(img)
    model = mod()
    res = model.predict(img)
    label = res[0].probs.top5
    conf = res[0].probs.top5conf
    
    conf = conf.tolist()
    col1,col2 = st.columns(2)
    col1.subheader(res[0].names[label[0]].title() +' with '+ str(conf[0])+' Confidence')
    col2.subheader(res[0].names[label[1]].title() +' with '+ str(conf[1])+' Confidence')





