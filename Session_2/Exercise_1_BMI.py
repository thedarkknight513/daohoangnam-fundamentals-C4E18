# 1.	Write a program that asks user their height (cm) and weight (kg), and then calculate their BMI (Body Mass Index):
height_in_cm = int(input("Input your height in cm"))
height_in_m = height_in_cm / 100
weight_in_kg = int(input("Input your weight in kg"))
BMI = int(weight_in_kg / (height_in_m * height_in_m))#
print("Your BMI is ", BMI)

if BMI < 16:
    print("Severely underweight")
elif 16 <= BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obese")

