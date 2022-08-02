"""
BMI is calculated using a persons weight and height. BMI is 'weight' divided by square of height.

The BMI should be classified as follows
Underweight - BMI under or equal to 18.5
Normal - BMI between 18.5 and 25 (not including 18.5 but including 25)
Overweight - BMI between- 25 and 30 (not including 25 but including 30)
Obese - BMI greater than 30
"""


weight = input("Input your weight in KG: ")
height = input("Input your height in m: ")

BMI = float(weight) / (float(height) ** 2)
#
# BMI = round(BMI, 1)
if BMI <= 18.5:
    print("Your BMI is {}. You are underweight".format(BMI))
elif 18.5 < BMI <= 25:
    print("Your BMI is {}. You are normal weight".format(BMI))
elif 25 < BMI <= 30:
    print("Your BMI is {}. You are overweight".format(BMI))
else:
    print("Your BMI is {}. You are Obese".format(BMI))