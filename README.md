# 🏋️ BMI Calculator

Welcome to the **BMI Calculator**, a Python project that helps users calculate their Body Mass Index (BMI) and provides personalized health advice based on their BMI category.

## 🌟 Features
- **Calculate BMI**: Enter your height and weight to compute your BMI.
- **Categorize BMI**: Classifies BMI into categories like "Healthy", "Overweight", etc.
- **Custom Recommendations**: Get actionable health advice tailored to your BMI category.

---

## 🛠️ How It Works
1. **Input**: Users provide their height (in centimeters) and weight (in kilograms).
2. **BMI Calculation**: BMI is calculated using the formula:  
   \[
   BMI = \frac{\text{Weight (kg)}}{\text{Height (m)}^2}
   \]
3. **Categorization**: The BMI is categorized as:
   - **Severely Underweight**: BMI < 16.0
   - **Underweight**: 16.0 ≤ BMI < 18.5
   - **Healthy**: 18.5 ≤ BMI < 25.0
   - **Overweight**: 25.0 ≤ BMI < 30.0
   - **Severely Overweight**: BMI ≥ 30.0
4. **Recommendations**: Personalized messages offer tips for improving or maintaining health.

---

## 📋 Installation
To get started, clone this repository and run the script:

```bash
# Clone the repository
git clone https://github.com/yourusername/bmi-calculator.git

# Navigate to the project directory
cd bmi-calculator

# Run the script
python bmi_calculator.py
```

---

## 🚀 Usage
Simply run the program and follow the prompts:

```bash
Enter your height in centimeters: 170
Enter your weight in kilograms: 70
Your BMI is: 24.22
Category: Healthy
Congratulations!! You have a healthy figure. Keep it up and inspire others to maintain their health!
```

---

## 📚 Example Output

### Scenario 1: Healthy
```
Enter your height in centimeters: 165
Enter your weight in kilograms: 60
Your BMI is: 22.04
Category: Healthy
Congratulations!! You have a healthy figure. Keep it up and inspire others to maintain their health!
```

### Scenario 2: Severely Overweight
```
Enter your height in centimeters: 160
Enter your weight in kilograms: 85
Your BMI is: 33.2
Category: Severely Overweight
You need a healthy diet plan... Here is a suggestion: consult a dietitian for a personalized plan and commit to gym sessions daily!
```

---

## 🧑‍⚕️ Categories and Recommendations
| **Category**            | **BMI Range**     | **Recommendation**                                                                 |
|--------------------------|-------------------|-----------------------------------------------------------------------------------|
| Severely Underweight     | BMI < 16.0        | Seek medical advice and focus on gaining weight with a nutritionist's help.      |
| Underweight              | 16.0 ≤ BMI < 18.5 | Add more calories, protein, and healthy fats to your diet.                       |
| Healthy                  | 18.5 ≤ BMI < 25.0 | Maintain your routine and inspire others to stay healthy!                        |
| Overweight               | 25.0 ≤ BMI < 30.0 | Avoid junk food, focus on exercise, and maintain a balanced diet.                |
| Severely Overweight      | BMI ≥ 30.0        | Consult a dietitian and commit to a regular exercise plan.                       |

---

## 🧑‍💻 Code Explanation
### `categorize_bmi(bmi)`
Categorizes the BMI into different health categories.

### `custom_message(category)`
Prints personalized health advice based on the BMI category.

### `bmi_calculator()`
The main function that:
- Takes user input
- Computes BMI
- Calls helper functions for categorization and messages.

---

## 💡 Future Enhancements
- Add a **GUI interface** for easier use.
- Incorporate **dietary suggestions** based on regional preferences.
- Include **tracking features** for BMI trends over time.

---

## 🤝 Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments
- Thanks to the Python community for inspiration.
- Built with ❤️ by [Joyeeta Majumdar](https://github.com/majumdarjoyeeta/Python_BMI_Calculator).
```

This README features structured sections, emojis for visual appeal, and Markdown syntax for readability. You can replace placeholders with real links or images to suit your project.
