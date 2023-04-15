import streamlit as st

def largest_of_three(num1, num2, num3):
    """
    This function takes three numbers as input and returns the largest value.
    """
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest

st.title("Find the Largest Number")

num1 = st.number_input("Enter the first number:", value=0)
num2 = st.number_input("Enter the second number:", value=0)
num3 = st.number_input("Enter the third number:", value=0)

if st.button("Find the largest number"):
    result = largest_of_three(num1, num2, num3)
    st.write(f"The largest number is {result}.")
