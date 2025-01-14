import streamlit as st
import os

def app():
    st.title("Project garbAIge")

    st.subheader("Objective :")
    st.markdown("The main Objective of this project is to use `Machine Learning` and `Deep learning` to categorize the garbage image into 6 different classes namely :", True)
    
    st.subheader("Motivation :")
    st.markdown("This Project has been created as part of the <b>Hack'n'Code 5.0 Competition</b> presented by <b>IET, MPSTME</b>", True)
    st.markdown("Visit the IET Website [Hack'n'code](https://ietmpstme.in/hackncode)", True)

    st.markdown("<hr/>", True)

    st.subheader("Description :")
    st.markdown("This Project uses `Fine Tuned InceptionV3 Model` which is a Pre-Trained CNN Model from Keras.", True)
    st.markdown("It Gave the `Highest Accuracy of 96%` while classifying image from test set.", True)

    st.markdown("<hr/>", True)

    st.subheader("Code :")
    st.markdown("Full code and files for this project are hosted on my Github profile! [GitHub Repo](https://github.com/aryashah2k/project-garbAIge)", True)
    