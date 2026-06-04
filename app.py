import streamlit as st
import pickle
import pandas as pd
st.title("PLACEMENT SALARY PREDICTION")
with open('placement_salary_model.pkl','rb') as f:
    model=pickle.load(f)
    st.subheader("ENTER THE DETAILS")
    CGPA=st.number_input(
        "CGPA", 
        min_value=0, 
        max_value=10, 
        value=9)
    Internships=st.number_input(
        "Internships", 
        min_value=0, 
        max_value=5, 
        value=10)
    Projects=st.number_input(
        "Projects",
        min_value=0,
        max_value=9
        value=5)
    AptitudeScore=st.number_input(
        "AptitudeScore",
        min_value=0,
        max_value=99,
        value=70)
    CommunicationSkill=st.number_input(
        "CommunicationSkill",
        min_value=0,
        max_value=9,
        value=7)
    if st.button("Predict"):
        input_data=pd.DataFrame({
            'CGPA':[CGPA],
            'Internships':[Internships],
            'Projects':[Projects],
            'AptitudeScore':[AptitudeScore],
            'CommunicationSkill':[CommunicationSkill]
        })
        prediction=model.predict(input_data)
        st.subheader(f"Predicted Score: {prediction[0]:.2f}"
                    )
    