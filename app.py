import streamlit as st
from services.planner import my_travel_plan
from assets.image_services import get_image

# ------------------ Page Setup ------------------
st.set_page_config(page_title="AI Travel Planner", layout="wide")

st.title("✈️ AI Student Travel Planner")
st.markdown("Plan smart. Travel cheap. Explore beautifully.")

# ------------------ Sidebar Inputs ------------------
st.sidebar.header("🧭 Trip Preferences")

# City Input
city = st.sidebar.text_input("🌍 City")

# Days
days_option = [1, 2, 3, 4, 5, 7, 10, 15]
days = st.sidebar.selectbox("📅 Number of Days", days_option)

# Budget Options
budget_options = ["Low", "Medium", "High"]
budget = st.sidebar.selectbox("💰 Budget", budget_options)

# Travel Style Options
travel_style_options = [
    "Adventure",
    "Nature",
    "Luxury Travel",
    "Spiritual",
    "Culture & Heritage",
    "Nightlife",
    "Photography"
]
travel_style = st.sidebar.selectbox("🎒 Travel Style", travel_style_options)

# Interest Options
interest_options = [
    "Nature",
    "Nightlife",
    "Photography",
    "Spiritual",
    "Adventure",
    "Culture & Heritage"
]
interests = st.sidebar.multiselect("✨ Interests", interest_options)

# Extra User Instructions
st.subheader("📝 Extra Instructions")
user_note = st.text_area(
    "Tell us anything specific you want in your trip:",
    placeholder="E.g. I want peaceful places, sunrise points, less crowd, cheap hostels...", key="user_note"
)
def clear_result():
    st.session_state["user_note"] = ""
    

st.button("Clear Result:", on_click=clear_result)


# Travel Mode
travel_mode_options = ["Solo", "With Friends", "With Family"]
travel_mode = st.sidebar.radio("👥 Traveling As", travel_mode_options)

# ------------------ Generate Button ------------------
if st.button("🚀 Generate My Travel Plan"):

    if not city:
        st.warning("Please enter a city name.")
    else:
        plan = my_travel_plan(
            city=city,
            days=days,
            budget=budget,
            travel_style=travel_style,
            extra_info=", ".join(interests) + f". Travel mode: {travel_mode}. User request: {user_note}"
        )

        if "❌" in plan:
            st.error("AI service is busy right now. Please try again later.")
        else:
            st.success("✅ Your personalized travel plan is ready!")

           

            # ------------------ Itinerary Display ------------------
            st.subheader("🗓️ Your Travel Itinerary")

            for line in plan.split("\n"):
                if line.startswith("DAY"):
                    with st.expander(line):
                        st.write(line)
                else:
                    st.write(line)

             # ------------------ Image Section ------------------
            st.subheader("📸 Trip Gallery")

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


# ------------------ About Section ------------------
with st.expander("ℹ️ About This Project"):
    st.write("""
    This is an AI-based Student Travel Planner.
    It uses a Large Language Model via HuggingFace API
    to generate personalized, budget-friendly travel plans
    based on user preferences.
    """)
