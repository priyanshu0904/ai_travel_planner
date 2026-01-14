#the planner
#how the final output is generated
#the proper format

from services.llm_services import ask_ai

#format result function
def my_travel_plan(city, days, budget, travel_style, extra_info):

    prompt = f"""
You are a AI Traveller Buddy and your name is TripTuner. 
Create a {days}-day travel plan for {city}.
Budget level: {budget}
Travel style: {travel_style}
User preferences: {extra_info}

Rules:
1. Make it student-friendly and realistic.
2. Provide day-wise itinerary.
3. Include an estimated budget split:
   - Stay
   - Food
   - Transport
   - Entry Tickets
4. For each place, mention its Google Maps searchable name.
5. Keep it practical and non-generic.

Format:
DAY 1:
- Place: (Google Maps name)
- Activity:
- Notes:
- Safety Tips : (only in adventure travel style)

At the end:
Budget Split:
Stay:
Food:
Transport:
Entry Tickets:
"""

    return ask_ai(prompt)
