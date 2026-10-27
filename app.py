import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")

def generate_itinerary(destination, days, budget, travel_type):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""
    You are an expert AI Travel Planner. Generate a highly personalized and detailed day-wise travel itinerary for a trip to {destination}.
    Duration: {days} days
    Budget Category: {budget}
    Traveler Profile/Vibe: {travel_type}
    Provide the response in structured markdown format.
    """
    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="AI Personalized Travel Planner", layout="centered")
st.title("🧭 AI Personalized Travel Itinerary Planner")
st.write("Plan your perfect custom trip using Generative AI!")

with st.form("itinerary_form"):
    destination = st.text_input("📍 Destination", placeholder="e.g., Goa, Manali")
    days = st.number_input("📅 Number of Days", min_value=1, max_value=30, value=3)
    budget = st.selectbox("💰 Budget", ["Budget-Friendly", "Moderate", "Luxury"])
    travel_type = st.selectbox("🎒 Vibe", ["Adventure", "Cultural", "Relaxation", "Family"])
    submit_button = st.form_submit_button("Generate My Plan")

if submit_button:
    if not destination.strip():
        st.error("Please enter a destination!")
    else:
        with st.spinner("✨ Crafting your custom AI itinerary..."):
            try:
                itinerary_result = generate_itinerary(destination, days, budget, travel_type)
                st.success("🎉 Your Itinerary is Ready!")
                st.markdown(itinerary_result)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")