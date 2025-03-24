import streamlit as st

st.title("Welcome to BMI Calculator")

weight=st.number_input("Enter your weight(in kgs):")

format=st.radio("Select your height format:",("CMS","Meter","Feet"))

if(format=="CMS"):
    height=st.number_input("Centimeters(cms):")
    try:
        bmi=weight/(height*height)
    except:
        st.write("Enter some value for height")

elif(format=="Meter"):
    height=st.number_input("Meters(m):")

    try:
        bmi=weight/(height*height)
    except:
        st.write("Enter some value for height")

elif(format=="Feet"):
    height=st.number_input("Feet(F):")

    try:
        bmi=weight/(height*height)
    except:
        st.write("Enter some value for height")


if st.button("Calculate BMI!!"):
    st.text("Your BMI Index is {}".format(bmi))

    if(bmi<16):
        st.error("Extremely Underweight")
    elif(bmi>=16 and bmi<18.5):
        st.warning("Underweight")
    elif(bmi>=18.5 and bmi<25):
        st.success("Healthy")
    elif(bmi>=25 and bmi<30):
        st.warning("Overweight")
    elif(bmi>=30):
        st.error("Extremely Overweight")