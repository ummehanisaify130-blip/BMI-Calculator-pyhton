def BMI_calculator(wght,h_m):
    return wght/(h_m**2)

def get_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi >=18.5 and bmi <=24.9:
        return "normal weight"
    elif bmi >= 25 and bmi <= 29.9:
        return "overweight"
    else :
        return "obese"

#----main program-----
#1. weight input for cleaning
weight = input("enter weight (for eg: 70kg or 70):")
weight = weight.lower().strip()
weight = weight.replace("kg","").strip()
wght = float(weight)

#2. height input for cleaning
height = input("enter height (for eg: 170cm or 5.8ft or 1.75m):")
height = height.lower().strip()
if "cm" in height:
    clean = height.replace("cm","").strip()
    h_cm = float(clean)
    h_m = h_cm/100
elif "ft" in height or "feet" in height or "" in height:
    clean = height.replace("ft","").replace("feet","").replace("","").strip()
    h_ft = float(clean)
    h_m = h_ft*0.3048
else :
    clean = height.replace("m","").strip()
    h_m = float(clean)

#calculate bmi using functions 
bmi = BMI_calculator(wght,h_m)
#get category
category = get_category(bmi)

#final output
print("\n Your BMI value is", bmi)
print("Category :", category)
