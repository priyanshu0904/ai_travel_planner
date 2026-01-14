#importing all the important functions from other files
import streamlit as st
from services.planner import my_travel_plan
from assets.image_services import get_image

# Page Setup
st.set_page_config(page_title="🧳TripTuner", layout="wide")

st.title("🧳TripTuner : Travel Planner Agent")
st.markdown("Plan smart. Travel cheap. Explore beautifully.")

#session state
if "plan" not in st.session_state:
    st.session_state.plan = ""

if "user_note" not in st.session_state:
    st.session_state.user_note = ""

#navigation filters for the trip
st.sidebar.header("🗒️Modify Your Trip")

city = st.sidebar.text_input("🌍 City")
days = st.sidebar.slider("📅 Number of Days", 1, 10, 3)

#budget
budget_option = ["Low", "Medium", "High"]
budget = st.sidebar.selectbox("💰 Budget", budget_option)

#travel
travel_option = [
    "Adventure","Nature", "Luxury Travel", "Spiritual", "Culture & Heritage", "Nightlife", "Photography"
]
travel_style = st.sidebar.selectbox(
    "🎒 Travel Style", travel_option)

#intrest
intrest_option = [
    "Scenic Views & Sunrise",
    "Photography Spots",
    "Local Food & Street Food",
    "Historical Places",
    "Shopping & Local Markets",
    "Cafes & Chill Places",
    "Adventure Activities",
    "Beaches & Relaxation",
    "Camping & Bonfire",
    "Nightlife & Parties",
    "Yoga / Meditation",
    "Art, Museums & Culture",
    "Walking Tours",
    "Stargazing & Nature",
    "Music & Cultural Shows"
]
interests = st.sidebar.multiselect(
    "✨ Interests", intrest_option)

#travel option
travel_mode = st.sidebar.radio(
    "👥 Traveling As",
    ["Solo", "With Friends", "With Family"]
)

# text area for user input 
st.markdown("<h3><b>📝Let’s map your Adventure</b></h3>", unsafe_allow_html=True)
user_note = st.text_area(
    "",
    placeholder="E.g. peaceful places, sunrise points, less crowd...",
    value=st.session_state.get("user_note", "")
)

#generate button
if st.button("Cook My TRIP🧑‍🍳"):

    if not city:
        st.warning("Please enter a city name.")
    else:
        plan = my_travel_plan(
            city,
            days,
            budget,
            travel_style,
            ", ".join(interests) + f". Travel mode: {travel_mode}. User request: {user_note}"
        )

        # If API returned error
        if "❌" in plan:
            st.error("AI service is busy right now. Please try again later.")
        else:
            st.session_state.plan = plan

#after generation
if st.session_state.plan:

    st.success("✅ Your personalized travel plan is ready!")

   

    # itinerary section
    st.subheader("🗓️ Your Travel Itinerary")

    for line in st.session_state.plan.split("\n"):
        if line.startswith("DAY"):
            with st.expander(line):
                st.write(line)
        else:
            st.write(line)
        
    # image section
    st.subheader("📸📷📷")

    selected_images = get_image(travel_style, 3)

    if selected_images:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(selected_images[0], use_container_width=True)
        with col2:
             st.image(selected_images[1], use_container_width=True)
        with col3:
            st.image(selected_images[2], use_container_width=True)
    else:
        st.info("No images found for this travel style.")

    # clear button
    if st.button("🔁Plan Next Trip"):
        st.session_state["plan"] = ""
        st.session_state["user_note"] = ""   # value reset
        st.rerun()

# -------------------- ABOUT SECTION --------------------
with st.expander("ℹ️ About This Project"):
    st.write("""
    This is an AI-based Student Travel Planner.
    It uses a Large Language Model via HuggingFace API
    to generate personalized, budget-friendly travel plans
    based on user preferences.
    """)
