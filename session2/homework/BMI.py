height = int(input("Enter your height (cm):"))

weight = int(input("Enter your weight (kg)"))

height_meter = height / 100

BMI = weight / (height_meter * height_meter)

if BMI < 16:
  print("you are severely underweight")
elif BMI < 18.5:
  print("you are underweight")
elif BMI < 25:
  print("you are normal")
elif BMI < 30:
  print("you are overweight")
else:
  print("you are obese")
