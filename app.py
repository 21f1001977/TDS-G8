import streamlit as st


st.write("""
# Subtraction of 2 given numbers App

This app subtract two number entered by user
""")
#Get Input

st.header('Enter Number to be Subtracted")

first_number = st.number_input("First_Number")
second_number = st.number_input("Second_Number")
result = first_number - second_number
    
data = {'First_Number': first_number,
        'Second_Numbe': second_number,
        'Result': result
       }
st.write("The Result of Subtraction of given number is ",result)
st.write(" By Yogesh Kumar ")


