import streamlit as st 
import pandas as pd
import numpy as np
import joblib

model = joblib.load("models/house_price_model.pkl")

st.title("🏠 House Price Prediction")
st.subheader("Housing Crash Simulator")

st.write(
    "Enter the property details below to estimate its sale price "
    "and explore how increasing interest rates could affect the simulated value."
)

st.sidebar.header("Property Details")

overall_quality = st.sidebar.slider(
    "Overall Quality", 1, 10, 6
)

living_area = st.sidebar.number_input(
    "Living Area (sq ft)", 300, 6000, 1500
)

garage_cars = st.sidebar.slider(
    "Garage Capacity", 0, 4, 2
)

basement_area = st.sidebar.number_input(
    "Basement Area (sq ft)", 0, 6000, 1000
)

full_bath = st.sidebar.slider(
    "Full Bathrooms", 0, 4, 2
)

bedrooms = st.sidebar.slider(
    "Bedrooms", 0, 8, 3
)

year_built = st.sidebar.slider(
    "Year Built", 1870, 2010, 2000
)

house_data = pd.DataFrame([{
    "OverallQual": overall_quality,
    "GrLivArea": living_area,
    "GarageCars": garage_cars,
    "TotalBsmtSF": basement_area,
    "FullBath": full_bath,
    "BedroomAbvGr": bedrooms,
    "YearBuilt": year_built
}])

predicted_price = model.predict(house_data)[0]

st.metric(
    "Predicted House Price",
    f"${predicted_price:,.0f}"
)
st.divider()

st.header("📉 Interest Rate Simulator")

st.write(
    "Adjust the interest rate to simulate how increasing borrowing costs "
    "could affect the predicted house price."
)

interest_rate = st.slider(
    "Interest Rate (%)",
    min_value=3.0,
    max_value=8.0,
    value=3.0,
    step=0.5
)

price_reduction = (interest_rate - 3.0) * 0.05

simulated_price = predicted_price * (1 - price_reduction)

st.metric(
    "Simulated House Price",
    f"${simulated_price:,.0f}",
    delta=f"${simulated_price - predicted_price:,.0f}"
)

rates = np.arange(3.0, 8.5, 0.5)

simulated_prices = [
    predicted_price * (1 - ((rate - 3.0) * 0.05))
    for rate in rates
]

chart_data = pd.DataFrame({
    "Interest Rate (%)": rates,
    "Simulated House Price": simulated_prices
})

st.line_chart(
    chart_data,
    x="Interest Rate (%)",
    y="Simulated House Price"
)

st.caption(
    "Simulation assumption: each 1 percentage-point increase in the "
    "interest rate above 3% reduces the displayed predicted price by 5%. "
    "This effect is for demonstration purposes and was not learned from "
    "the House Prices dataset."
)