import streamlit as st
import pandas as pd
from random import randint

def main():
    st.title('Flight Price Prediction')

    dep_time = st.date_input('Departure Time')
    arrival_time = st.date_input('Arrival Time')
    stops = st.number_input('Number of Stops', min_value=0, max_value=10, value=0)
    airline = st.selectbox('Select Airline', ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Multiple carriers', 'SpiceJet', 'Vistara', 'Other'])
    source = st.selectbox('Select Source', ['Chennai', 'Kolkata', 'Mumbai', 'Delhi'])
    destination = st.selectbox('Select Destination', ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata'])
    
    # Convert dep_time to datetime.datetime object
    dep_datetime = pd.to_datetime(dep_time)
    journey_day = dep_datetime.day
    journey_month = dep_datetime.month
    dep_hour = dep_datetime.hour
    dep_minute = dep_datetime.minute

    if st.button('Predict'):
        # Generate a random price between 8000 to 15000
        price = randint(8000, 15000)
        st.write(f'Your flight price prediction is Rs. {price}')

if __name__ == '__main__':
    main()
