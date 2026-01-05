import streamlit as st
import pickle

model = pickle.load(open("knn_pass_fail.pkl", "rb"))

st.title("Student Pass / Fail Prediction (KNN)")

studytime = st.number_input("Enter Study Time (Hours)", min_value=0.0)

if st.button("Predict"):
    prediction = model.predict([[studytime]])
    if prediction[0] == 1:
        st.success("PASS ✅")
    else:
        st.error("FAIL ❌")
