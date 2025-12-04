import streamlit as st
import os
from data_loader import download_data
from annotation import annotate_video

# Streamlit UI setup
st.title('Textile Sewing Operation Annotation')

st.write("This application annotates video footage of sewing operations with GSD codes.")

# Button to download dataset
if st.button('Download Dataset'):
    dataset_path = download_data("belkhirnacim/textiledefectdetection")
    st.success(f"Dataset downloaded and saved at: {dataset_path}")

# Upload video file for annotation
uploaded_video = st.file_uploader("Upload Sewing Video", type=["mp4", "avi"])

if uploaded_video is not None:
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_video.getbuffer())

    # Annotate the uploaded video
    if st.button('Annotate Video'):
        output_path = "annotations.txt"
        annotate_video("temp_video.mp4", output_path)
        st.success(f"Video annotated! Check the annotations in {output_path}")
        with open(output_path, 'r') as file:
            annotations = file.read()
            st.text(annotations)
