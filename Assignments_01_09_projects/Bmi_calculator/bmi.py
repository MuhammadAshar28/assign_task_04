

import streamlit as st

# Title
st.title('BMI Calculator')
'''
    _Calculate your BMI Easily_
'''

# Take weight input
weight = st.number_input("Enter your weight (in kgs)")

# Take height input format
status = st.radio('Select your height format:', ('cms', 'meters', 'feet'))

# Initialize BMI variable
bmi = None

# Check selected height format
if status == 'cms':
    height = st.number_input('Enter height in centimeters')

    try:
        bmi = weight / ((height / 100) ** 2)  # Convert cm to meters and calculate BMI
    except:
        st.text("Please enter a valid height in centimeters")

elif status == 'meters':
    height = st.number_input('Enter height in meters')

    try:
        bmi = weight / (height ** 2)  # Direct BMI calculation in meters
    except:
        st.text("Please enter a valid height in meters")

else:  # If 'feet' is selected
    height = st.number_input('Enter height in feet')

    try:
        bmi = weight / (((height / 3.28)) ** 2)  # Convert feet to meters and calculate BMI
    except:
        st.text("Please enter a valid height in feet")
if(st.button('Calculate BMI')):
 
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
 
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
         st.error("Extremely Overweight")

st.header(
'''_Developed By Muhammad Ashar_''')