def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

print("Welcome to the BMI Calculator!")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
bmi=round(bmi,2)
bmi_category = classify_bmi(bmi)
print(f"Your BMI is: ",bmi)
print(f"Classification: ",bmi_category)
