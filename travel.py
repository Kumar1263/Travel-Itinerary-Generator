import streamlit as st
from google import genai

# 🔑 Add your NEW Gemini API key here
client = genai.Client(api_key="put your API key")


# -------------------
# Backend (Gemini)
# -------------------

def generate_itinerary(destination, days, nights):

    prompt = f"""
    Create a detailed travel itinerary for {destination}
    for {days} days and {nights} nights.
    Include:
    - Daily plan
    - Tourist attractions
    - Local food suggestions
    - Travel tips
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


# -------------------
# Frontend (Streamlit)
# -------------------

def main():

    st.title("Travel Itinerary Generator")

    destination = st.text_input("Enter your desired destination")
    days = st.number_input("Enter the Number of Days", min_value=1)
    nights = st.number_input("Enter the Number of Nights", min_value=0)

    if st.button("Generate Itinerary"):

        if destination.strip() == "":
            st.error("Please enter a destination.")
        else:
            result = generate_itinerary(destination, days, nights)
            st.text_area("Your Travel Plan", result, height=400)


if __name__ == "__main__":

    main()
