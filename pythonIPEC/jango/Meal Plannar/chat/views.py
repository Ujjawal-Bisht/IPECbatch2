from django.shortcuts import render
from .forms import MealForm
from google import genai
import os

def MealView(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            meal_type = form.cleaned_data['meal_type']
            location = form.cleaned_data['location']
            purpose = form.cleaned_data['purpose']

            # Build a proper prompt
            prompt = f"""
            You are a nutritionist. Based on the following details, give me a weekly meal plan:
            - Age: {age}
            - Weight: {weight}
            - Height: {height}
            - Meal Type: {meal_type}
            - Location: {location}
            - Purpose: {purpose}
            - Output Structure: A table with 7 rows(Monday to Sunday) and 3 columns (Breakfast, Lunch, Dinner) + All the details of each meal outside the table.
            
            Format the response as an HTML table string.
            """

            # Use environment variable for API key
            client = genai.Client(api_key=os.environ.get("GENAI_API_KEY"))

            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=[prompt]
            )

            # Extract text safely
            meal_suggestions = response.text if hasattr(response, "text") else str(response)

            return render(request, 'meal_suggestions.html', {'meal_suggestions': meal_suggestions})
    else:
        form = MealForm()
    
    return render(request, 'meal_form.html', {'form': form})