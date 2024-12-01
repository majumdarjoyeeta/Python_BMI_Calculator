def categorize_bmi(bmi):
    if bmi < 16.0:
        return "Severely Underweight"
    elif 16.0 <= bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Healthy"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Severely Overweight"

def custom_message(category):
    if category == "Severely Overweight":
        print("You need a healthy diet plan... Here is a suggestion: consult a dietitian for a personalized plan and commit to gym sessions daily!")
    elif category == "Overweight":
        print("You should avoid junk food and fast foods. Focus on regular exercise and maintain a balanced diet!")
    elif category == "Healthy":
        print("Congratulations!! You have a healthy figure. Keep it up and inspire others to maintain their health!")
    elif category == "Underweight":
        print("You need to eat more nutrient-rich foods. Add more calories, protein, and healthy fats to your diet!")
    elif category == "Severely Underweight":
        print("It’s important to seek medical advice to ensure there are no underlying health issues. Focus on gaining weight with the help of a nutritionist.")
    else:
        print("Error: Unable to determine BMI category. Please try again.")

def bmi_calculator():
    while True:
        try:
            # Input height in cm
            height_in_cm = float(input("Enter your height in centimeters: "))
            if height_in_cm <= 0:
                raise ValueError("Height must be a positive number.")
            height_in_m = height_in_cm / 100

            # Input weight in kg
            weight_in_kg = float(input("Enter your weight in kilograms: "))
            if weight_in_kg <= 0:
                raise ValueError("Weight must be a positive number.")

            # Calculate BMI
            BMI = weight_in_kg / (height_in_m ** 2)
            BMI = round(BMI, 2)

            # Determine category
            category = categorize_bmi(BMI)

            # Display results
            print(f"Your BMI is: {BMI}")
            print(f"Category: {category}")

            # Display custom message based on category
            custom_message(category)

            break  # Exit loop after successful calculation

        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid positive numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

# Run the BMI calculator
bmi_calculator()
