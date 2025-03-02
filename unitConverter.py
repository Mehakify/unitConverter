import streamlit as st

# Custom CSS for Green & Mint Theme
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(45deg, #e8f6ef, #a8e6cf);
        color: #000000;
    }
    .stApp {
        background: linear-gradient(45deg, #dcedc1, #a8e6cf);
        color: black;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0, 128, 128, 0.4);
    }
    h1 {
        color: #379683;
        text-align: center;
        font-size: 36px;
        text-shadow: 2px 2px 10px #5cdb95;
    }
    .stButton>button {
        background: linear-gradient(45deg, #379683, #5cdb95);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: background 0.3s ease, transform 0.2s ease;
        box-shadow: 0 5px 15px rgba(0, 128, 128, 0.3);
        border: none;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #8ee4af, #5cdb95);
        color: black;
    }
    .result-box {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.2);
        padding: 15px;
        border-radius: 10px;
        margin: 20px;
        box-shadow: 0 5px 15px rgba(0, 128, 128, 0.3);
        color: #379683;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #379683;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Unit Converter")
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert units from one type to another with our user-friendly unit converter.")

# Input Fields
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", min_value=0.0, format="%.4f")

# Unit Selection
if conversion_type == "Length":
    units = ["meters", "centimeters", "kilometers", "feet", "yards", "miles", "inches"]
elif conversion_type == "Weight":
    units = ["grams", "kilograms", "pounds", "ounces", "milligrams"]
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]

from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)

# Conversion Functions
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "meters": 1.0,
        "centimeters": 100,
        "kilometers": 0.001,
        "feet": 3.28084,
        "yards": 1.09361,
        "miles": 0.000621371,
        "inches": 39.3701,
    }
    return value * length_units[from_unit] / length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "grams": 1.0,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274,
        "milligrams": 1000,
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    else:
        return "Invalid conversion"

# Button for Conversion
if st.button("Convert"):
    if from_unit == to_unit:
        result = value  # Same unit conversion
    elif conversion_type == "Length":
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_conversion(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_conversion(value, from_unit, to_unit)
    else:
        result = "Invalid conversion"

    st.markdown(
        f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>",
        unsafe_allow_html=True
    )

# Footer
st.markdown("<div class='footer'>Developed by Mehak</div>", unsafe_allow_html=True)
