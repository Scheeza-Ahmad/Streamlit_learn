import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

st.title("🌤️ Weather App")
st.markdown("### Kisi bhi city ka current weather check karein")
st.markdown("---")

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Apni OpenWeatherMap API Key daalein", type="password").strip()
    unit = st.radio("Temperature Unit", ["Celsius", "Fahrenheit"])
    st.markdown("---")
    st.info("API key free milti hai openweathermap.org se")

# ---------- MAIN INPUT ----------
city = st.text_input("Shehar ka naam likhein", "Karachi")

units_param = "metric" if unit == "Celsius" else "imperial"
temp_symbol = "°C" if unit == "Celsius" else "°F"

if st.button("Weather Check Karo"):

    if not api_key:
        st.warning("Pehle sidebar mein apni API key daalein.")
    elif not city:
        st.warning("City ka naam likhein.")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units_param}"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                # ---------- MAIN INFO ----------
                st.success(f"Weather report for {data['name']}, {data['sys']['country']}")

                col1, col2 = st.columns([1, 2])

                with col1:
                    icon_code = data['weather'][0]['icon']
                    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
                    st.image(icon_url, width=100)

                with col2:
                    st.markdown(f"### {data['main']['temp']}{temp_symbol}")
                    st.markdown(f"**Condition:** {data['weather'][0]['description'].title()}")

                st.markdown("---")

                # ---------- DETAILS IN COLUMNS ----------
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.metric("Feels Like", f"{data['main']['feels_like']}{temp_symbol}")
                with c2:
                    st.metric("Humidity", f"{data['main']['humidity']}%")
                with c3:
                    st.metric("Wind Speed", f"{data['wind']['speed']} m/s")

                c4, c5 = st.columns(2)
                with c4:
                    st.metric("Min Temp", f"{data['main']['temp_min']}{temp_symbol}")
                with c5:
                    st.metric("Max Temp", f"{data['main']['temp_max']}{temp_symbol}")

                # ---------- EXPANDER FOR EXTRA INFO ----------
                with st.expander("Zyada Details Dekhein"):
                    st.write(f"**Pressure:** {data['main']['pressure']} hPa")
                    st.write(f"**Visibility:** {data['visibility']} meters")
                    st.write(f"**Cloudiness:** {data['clouds']['all']}%")

            else:
                st.error(f"Error: {data.get('message', 'City nahi mili, naam check karein')}")

        except Exception as e:
            st.error(f"Kuch ghalat hua: {e}")