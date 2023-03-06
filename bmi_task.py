#Get user to input their weight and height 
#Calculate BMI
#Depending on the conditions, print BMI and either obese, overweight, normal or underweight 
weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in metres: "))

bmi = weight / (height * height)

if bmi >= 30:
    print(f"Your BMI is {bmi:.2f}, you are considered obese")
elif bmi >= 25:
    print(f"Your BMI is {bmi:.2f}, you are considered overweight")
elif bmi >= 18.5:
    print(f"Your BMI is {bmi:.2f}, you are considered normal")
else:
    print(f"Your BMI is {bmi:.2f}, you are considered underweight")