

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
age = int(input("Enter your age in years: "))
sex = input("Enter your sex (male or female): ").strip().lower()
print("Activity Levels are grouped in 5 categories: \nSedentary: Little or no exercise (1) \nLightly active: Light exercise 1-3 days/week (2) \nModerately active: Moderate exercise 3-5 days/week (3) \nVery active: Hard exercise 6-7 days/week (4)\nExtra active: Very hard exercise daily or physical job (5)")
activity_level = int(input("Enter your activity level (1 - 5): "))

# calculate BMI
def calculate_bmi(weight, height) :
    bmi = weight / ((height / 100) ** 2)
    return bmi

# Calculate BMR
def calculate_bmr(sex, age, weight, height):
    if sex == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else :
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 16
    return bmr

# Find Daily Caloric Intake
def calculate_daily_calories(bmr, activity_level) :
    if activity_level == 1 :
        calories = bmr * 1.2
    if activity_level == 2 :
        calories = bmr * 1.375
    if activity_level == 3 :
        calories = bmr * 1.55
    if activity_level == 4 :
        calories == bmr * 1.725
    if activity_level == 5 :
        calories == bmr * 1.9
    return calories

bmr = calculate_bmr(sex, age, weight, height)
daily_calories = calculate_daily_calories(bmr, activity_level)

print("Your daily calories are: ", daily_calories)