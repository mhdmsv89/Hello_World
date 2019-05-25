print("Welcome to BMI calculator!")
print("please choose your preferred system unit: metric or imperial ?")
sys_unit = input()
if sys_unit == 'metric':
    he_m = float(input('Please Enter Your Height in Meters!'))
    wi_k = float(input('Please Enter Your Weight in Kilograms!'))
    bmi_m = wi_k / (he_m * he_m)
    if bmi_m <= 18.5:
        print("your BMI is", bmi_m, "! you are underweight...\n"
                                    "you need to put some meat on your bone :-|")
    elif bmi_m > 18.5 and bmi_m <= 25:
        print("your BMI is", bmi_m, ". Congratulation!!! you are normal\n"
                                    "keep doing what you do! stay healthy :-)")
    elif bmi_m > 25 and bmi_m <= 30:
        print("Your BMI is", bmi_m, "! you are Overweight...\n"
                                    "you need to hit the gym :-(")
    elif bmi_m > 30:
        print("Your BMI is", bmi_m, "wow, you are Obese !!! that means you have too much fat\n" \
                                    "you need to stop eating unhealthy and start heavy exercising! good luck :-/")
if sys_unit == 'imperial':
    he_i = float(input('Please Enter Your Height in Inches!'))
    wi_p = float(input('Please Enter Your Weight in Pounds!'))
    bmi_i = wi_p / (he_i * he_i) * 703
    if bmi_i <= 18.5:
        print("your BMI is", bmi_i, "! you are underweight...\n"
                                    "you need to put some meat on your bone :-|")
    elif bmi_i > 18.5 and bmi_i <= 25:
        print("your BMI is", bmi_i, ". Congratulation!!! you are normal\n"
                                    "keep doing what you do! stay healthy :-)")
    elif bmi_i > 25 and bmi_i <= 30:
        print("Your BMI is", bmi_i, "! you are Overweight...\n"
                                    "you need to hit the gym :-(")
    elif bmi_i > 30:
        print("Your BMI is", bmi_i, "wow, you are Obese !!! that means you have too much fat\n" \
                                    "you need to stop eating unhealthy and start heavy exercising! good luck :-/")