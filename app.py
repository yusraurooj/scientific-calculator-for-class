

# Import necessary libraries
import streamlit as st
import math

# Set page configuration
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# Styling
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #ff6347;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# App title and introduction
st.title("🧮 Scientific Calculator")
st.write("A sleek and interactive scientific calculator built with Streamlit!")

# Sidebar layout for operation selection
operation = st.sidebar.selectbox("Choose an Operation", 
                                 ['Addition', 'Subtraction', 'Multiplication', 
                                  'Division', 'Exponentiation', 'Square Root', 
                                  'Logarithm', 'Sine', 'Cosine', 'Tangent'])

st.sidebar.write("🧠 **Math is Fun!**")

# Function to perform calculations
def scientific_calculator(operation, num1=None, num2=None, angle=None):
    try:
        if operation == 'Addition':
            return num1 + num2
        elif operation == 'Subtraction':
            return num1 - num2
        elif operation == 'Multiplication':
            return num1 * num2
        elif operation == 'Division':
            return num1 / num2 if num2 != 0 else "Error! Division by zero."
        elif operation == 'Exponentiation':
            return num1 ** num2
        elif operation == 'Square Root':
            return math.sqrt(num1) if num1 >= 0 else "Error! Negative number."
        elif operation == 'Logarithm':
            return math.log(num1) if num1 > 0 else "Error! Non-positive number."
        elif operation == 'Sine':
            return math.sin(math.radians(angle))
        elif operation == 'Cosine':
            return math.cos(math.radians(angle))
        elif operation == 'Tangent':
            return math.tan(math.radians(angle))
    except:
        return "Invalid input!"

# Main input section based on selected operation
st.header(f"Performing: **{operation}**")

# Inputs and results for binary operations (Addition, Subtraction, etc.)
if operation in ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation']:
    num1 = st.number_input(f"Enter first number for {operation}", value=0.0, step=1.0, format="%.2f")
    num2 = st.number_input(f"Enter second number for {operation}", value=0.0, step=1.0, format="%.2f")
    if st.button(f"Calculate {operation}"):
        result = scientific_calculator(operation, num1=num1, num2=num2)
        st.success(f"Result: {result}")

# Inputs and results for square root
elif operation == 'Square Root':
    num1 = st.number_input("Enter number for Square Root", value=0.0, step=1.0, format="%.2f")
    if st.button(f"Calculate {operation}"):
        result = scientific_calculator(operation, num1=num1)
        st.success(f"Result: {result}")

# Inputs and results for logarithm
elif operation == 'Logarithm':
    num1 = st.number_input("Enter number for Logarithm (base e)", value=1.0, step=1.0, format="%.2f")
    if st.button(f"Calculate {operation}"):
        result = scientific_calculator(operation, num1=num1)
        st.success(f"Result: {result}")

# Inputs and results for trigonometric functions (Sine, Cosine, Tangent)
elif operation in ['Sine', 'Cosine', 'Tangent']:
    angle = st.number_input(f"Enter angle in degrees for {operation}", value=0.0, step=1.0, format="%.2f")
    if st.button(f"Calculate {operation}"):
        result = scientific_calculator(operation, angle=angle)
        st.success(f"Result: {result}")

# Footer for calculator
st.markdown("***")
st.write("🔢 **Developed using Python & Streamlit** | 📅 2024")
