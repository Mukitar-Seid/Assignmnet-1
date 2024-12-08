import streamlit as st
from utils import load_data
import matplotlib.pyplot as plt

def plot_ghi_over_time(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Timestamp'], data['GHI'], label='GHI', color='blue')
    plt.title('Global Horizontal Irradiance Over Time')
    plt.xlabel('Date')
    plt.ylabel('GHI (W/m²)')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.legend()
    
    return plt  # Return the plot object instead of displaying it here.

def main():
    st.title("Solar Radiation Analysis Dashboard")

    @st.cache_data()
    def load_data_cached():
        return load_data()

    data = load_data_cached()

    st.subheader("Global Horizontal Irradiance Over Time")
    
    if not data.empty:
        st.write(data.head(10))  # Display only first 10 rows for verification
        
        # Implementing interactive features for date selection
        start_date = st.date_input("Start Date", value=data['Timestamp'].min())
        end_date = st.date_input("End Date", value=data['Timestamp'].max())

        filtered_data = data[(data['Timestamp'] >= str(start_date)) & (data['Timestamp'] <= str(end_date))]
        
        if not filtered_data.empty:
            fig = plot_ghi_over_time(filtered_data)
            st.pyplot(fig)
        else:
            st.write("No data available for the selected date range.")
    else:
        st.write("No data available to display.")

if __name__ == "__main__":
    main()
