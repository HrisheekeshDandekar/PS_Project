import pandas as pd
import scipy.stats as st
import math
data = pd.read_csv("Statistical-Survey-Assessment-_Responses_.csv")
male = data[data["Gender"]=="M"]
female = data[data["Gender"]=="F"]
male_height = male["Height "]
male_average = male_height.mean()
female_height = female["Height "]
female_average = female_height.mean()

count = int(input("Enter the slicing number for the systematic selection from sample!!!!\n"))
male_sample = male_height.iloc[::count]
female_sample = female_height.iloc[::count]

male_mean = male_sample.mean()
female_mean = female_sample.mean()

male_deviation = male_sample.std()
female_deviation = female_sample.std()

CI = (float(input("Enter the confidence interval in percentage :\n")))/100
alpha = (1-CI)/2
z_value = float("% 0.2f"%st.norm.ppf(CI + alpha))

male_LCI = male_mean - (z_value *(male_deviation/ math.sqrt(len(male_sample))))
male_UCI = male_mean + (z_value *(male_deviation/ math.sqrt(len(male_sample))))

female_LCI = female_mean - (z_value *(female_deviation/ math.sqrt(len(female_sample))))
female_UCI = female_mean + (z_value *(female_deviation/ math.sqrt(len(female_sample))))
print("*"*10+" MALE POPULATION "+"*"*10)
print(f"The lower limit of confidence interval :{male_LCI}")
print(f"The lower limit of confidence interval :{male_UCI}")

if male_LCI < male_average < male_UCI :
    print(f"The mean testing holds true for male's population mean {male_average}")
else:
    print("There exists some problem in testing....!!!")

print()
print()
print("*"*10+" FEMALE POPULATION "+"*"*10)
print(f"The lower limit of confidence interval :{female_LCI}")
print(f"The lower limit of confidence interval :{female_UCI}")

if female_LCI < female_average < female_UCI :
    print(f"The mean testing holds true for female's population mean {female_average}")
else:
    print("There exists some problem in testing....!!!")





