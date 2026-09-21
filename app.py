import streamlit as st
import pandas as pd
import joblib


# Load trained model
MODEL_FILE = "crop_health_random_forest_model.joblib"

model = joblib.load(MODEL_FILE)


# Page configuration
st.set_page_config(
    page_title="Crop Disease Prediction",
    page_icon="🌱",
    layout="wide"
)


# Title
st.title("🌱 Crop Disease Prediction")
st.write("Enter the crop and environmental information below to predict whether disease is present.")


# Input section
st.header("Enter Crop Information")


col1, col2 = st.columns(2)


with col1:
    crop_type = st.selectbox(
        "Crop Type",
        [
            "Tomato",
            "Soybean",
            "Maize",
            "Cotton",
            "Wheat",
            "Groundnut",
            "Rice"
        ]
    )

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=25.0
    )

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=500.0,
        value=100.0
    )

    soil_moisture = st.number_input(
        "Soil Moisture (%)",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

    soil_ph = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5
    )

    nitrogen = st.number_input(
        "Nitrogen (ppm)",
        min_value=0.0,
        max_value=200.0,
        value=50.0
    )


with col2:
    phosphorus = st.number_input(
        "Phosphorus (ppm)",
        min_value=0.0,
        max_value=200.0,
        value=50.0
    )

    potassium = st.number_input(
        "Potassium (ppm)",
        min_value=0.0,
        max_value=200.0,
        value=50.0
    )

    sunlight = st.number_input(
        "Sunlight Hours",
        min_value=0.0,
        max_value=24.0,
        value=7.0
    )

    wind_speed = st.number_input(
        "Wind Speed (km/h)",
        min_value=0.0,
        max_value=100.0,
        value=15.0
    )

    pest_pressure = st.number_input(
        "Pest Pressure",
        min_value=0.0,
        max_value=100.0,
        value=30.0
    )

    irrigation = st.number_input(
        "Irrigation Frequency (per Week)",
        min_value=0.0,
        max_value=20.0,
        value=3.0
    )

    fertilizer = st.number_input(
        "Fertilizer Usage (kg/ha)",
        min_value=0.0,
        max_value=500.0,
        value=100.0
    )


# Feature engineering
temperature_humidity_interaction = temperature * humidity

rainfall_soil_moisture_interaction = rainfall * soil_moisture

nutrient_total = nitrogen + phosphorus + potassium

nutrient_balance = nitrogen / (phosphorus + potassium + 1)

weather_stress_index = (
    temperature
    + humidity / 10
    + wind_speed / 5
)

irrigation_fertilizer_interaction = irrigation * fertilizer


# Create input dataframe
input_data = pd.DataFrame({
    "Crop_Type": [crop_type],
    "Temperature_C": [temperature],
    "Humidity_pct": [humidity],
    "Rainfall_mm": [rainfall],
    "Soil_Moisture_pct": [soil_moisture],
    "Soil_pH": [soil_ph],
    "Nitrogen_ppm": [nitrogen],
    "Phosphorus_ppm": [phosphorus],
    "Potassium_ppm": [potassium],
    "Sunlight_Hours": [sunlight],
    "Wind_Speed_kmh": [wind_speed],
    "Pest_Pressure": [pest_pressure],
    "Irrigation_Frequency_per_Week": [irrigation],
    "Fertilizer_Usage_kg_per_ha": [fertilizer],
    "Temperature_Humidity_Interaction": [
        temperature_humidity_interaction
    ],
    "Rainfall_SoilMoisture_Interaction": [
        rainfall_soil_moisture_interaction
    ],
    "Nutrient_Total": [nutrient_total],
    "Nutrient_Balance": [nutrient_balance],
    "Weather_Stress_Index": [weather_stress_index],
    "Irrigation_Fertilizer_Interaction": [
        irrigation_fertilizer_interaction
    ]
})


# Prediction button
if st.button("🔍 Predict Disease", use_container_width=True):

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Disease Present")
    else:
        st.success("✅ Disease Absent")

    st.write(
        f"Estimated probability of disease: **{probability * 100:.2f}%**"
    )

