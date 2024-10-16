

import streamlit as st
import math

# Page Configurations
st.set_page_config(page_title="Modern Scientific Calculator", page_icon="🧮", layout="centered")

# Custom CSS for calculator look and feel
st.markdown("""
    <style>
    .calculator {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        max-width: 400px;
        margin: auto;
    }
    .stButton>button {
        background-color: #1e3c72;
        color: white;
        font-size: 20px;
        padding: 15px 0;
        border-radius: 10px;
        width: 100%;
    }
    .stTextInput>div>input {
        font-size: 25px;
        text-align: right;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #1e3c72;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to handle calculations
def perform_operation(operation, num1, num2=None):
    try:
        if operation == "Addition":
            return num1 + num2
        elif operation == "Subtraction":
            return num1 - num2
        elif operation == "Multiplication":
            return num1 * num2
        elif operation == "Division":
            return num1 / num2 if num2 != 0 else "Error"
        elif operation == "Exponentiation":
            return num1 ** num2
        elif operation == "Square Root":
            return math.sqrt(num1)
        elif operation == "Logarithm":
            return math.log(num1)
        elif operation == "Sine":
            return math.sin(math.radians(num1))
        elif operation == "Cosine":
            return math.cos(math.radians(num1))
        elif operation == "Tangent":
            return math.tan(math.radians(num1))
        else:
            return "Invalid operation"
    except:
        return "Error"

# App title
st.title("🧮 Modern Scientific Calculator")

# Display input field (like a real calculator screen)
calc_input = st.text_input("", "0", key="display", disabled=True)

# Store current input values
st.session_state["current_input"] = ""

# Calculator buttons with a grid layout
buttons = [
    "7", "8", "9", "÷",
    "4", "5", "6", "×",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "√", "^", "log", "AC",
    "sin", "cos", "tan", "C"
]

# Helper variables
stored_number = None
stored_operator = None

# Calculator grid layout
col1, col2 = st.columns(2)
with col1:
    st.subheader("Operation Panel")

    def button_click(label):
        global stored_number, stored_operator

        if label in ['+', '-', '×', '÷', '^', 'log', 'sin', 'cos', 'tan', '√']:
            if st.session_state['current_input']:
                stored_number = float(st.session_state['current_input'])
                st.session_state['display'] = str(stored_number)
                stored_operator = label
                st.session_state['current_input'] = ""
        elif label == "=":
            if stored_operator and st.session_state['current_input']:
                second_number = float(st.session_state['current_input'])
                if stored_operator == '+':
                    result = perform_operation("Addition", stored_number, second_number)
                elif stored_operator == '-':
                    result = perform_operation("Subtraction", stored_number, second_number)
                elif stored_operator == '×':
                    result = perform_operation("Multiplication", stored_number, second_number)
                elif stored_operator == '÷':
                    result = perform_operation("Division", stored_number, second_number)
                elif stored_operator == '^':
                    result = perform_operation("Exponentiation", stored_number, second_number)
                elif stored_operator == "log":
                    result = perform_operation("Logarithm", stored_number)
                elif stored_operator == "sin":
                    result = perform_operation("Sine", stored_number)
                elif stored_operator == "cos":
                    result = perform_operation("Cosine", stored_number)
                elif stored_operator == "tan":
                    result = perform_operation("Tangent", stored_number)
                elif stored_operator == "√":
                    result = perform_operation("Square Root", stored_number)
                
                st.session_state['display'] = str(result)
                st.session_state['current_input'] = str(result)
                stored_number = None
                stored_operator = None
        elif label == "AC":
            st.session_state['display'] = "0"
            st.session_state['current_input'] = ""
            stored_number = None
            stored_operator = None
        elif label == "C":
            st.session_state['current_input'] = ""
            st.session_state['display'] = "0"
        else:
            st.session_state['current_input'] += label
            st.session_state['display'] = st.session_state['current_input']

    # Create buttons dynamically
    with st.container():
        for i, button in enumerate(buttons):
            if i % 4 == 0:
                st.markdown("<br>", unsafe_allow_html=True)
            if st.button(button):
                button_click(button)

# Footer
st.markdown("***")
st.write("🔢 **Developed using Python & Streamlit** | 2024")
