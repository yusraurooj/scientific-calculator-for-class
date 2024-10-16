# Import necessary libraries
import streamlit as st
import math

# Function to perform the calculations
def scientific_calculator(operation, num1=None, num2=None, angle=None):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    elif operation == 'Exponentiation':
        return num1 ** num2
    elif operation == 'Square Root':
        if num1 >= 0:
            return math.sqrt(num1)
        else:
            return "Error! Square root of negative number."
    elif operation == 'Logarithm':
        if num1 > 0:
            return math.log(num1)
        else:
            return "Error! Logarithm of non-positive number."
    elif operation == 'Sine':
        return math.sin(math.radians(angle))
    elif operation == 'Cosine':
        return math.cos(math.radians(angle))
    elif operation == 'Tangent':
        return math.tan(math.radians(angle))

# Streamlit interface
st.title("Scientific Calculator")

# Select operation from the sidebar
operation = st.selectbox("Select operation", 
                         ['Addition', 'Subtraction', 'Multiplication', 
                          'Division', 'Exponentiation', 'Square Root', 
                          'Logarithm', 'Sine', 'Cosine', 'Tangent'])

# Take inputs based on operation
if operation in ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation']:
    num1 = st.number_input("Enter first number", value=0.0, step=1.0, format="%.2f")
    num2 = st.number_input("Enter second number", value=0.0, step=1.0, format="%.2f")
    if st.button("Calculate"):
        result = scientific_calculator(operation, num1=num1, num2=num2)
        st.write(f"Result: {result}")

elif operation == 'Square Root':
    num1 = st.number_input("Enter number", value=0.0, step=1.0, format="%.2f")
    if st.button("Calculate"):
        result = scientific_calculator(operation, num1=num1)
        st.write(f"Result: {result}")

elif operation == 'Logarithm':
    num1 = st.number_input("Enter number", value=1.0, step=1.0, format="%.2f")
    if st.button("Calculate"):
        result = scientific_calculator(operation, num1=num1)
        st.write(f"Result: {result}")

elif operation in ['Sine', 'Cosine', 'Tangent']:
    angle = st.number_input("Enter angle in degrees", value=0.0, step=1.0, format="%.2f")
    if st.button("Calculate"):
        result = scientific_calculator(operation, angle=angle)
        st.write(f"Result: {result}")

