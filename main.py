import pandas as pd
import statistics
import scipy.stats as st
import numpy as np
from scipy.stats import norm
import math
from matplotlib import pyplot as plt


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

male_pop_dev = male_height.std()
female_pop_dev = female_height.std()
male_deviation = male_sample.std()
female_deviation = female_sample.std()

CI = (float(input("Enter the confidence interval in percentage :\n")))/100
alpha = (1-CI)/2
z_value = float("% 0.2f"%st.norm.ppf(CI + alpha))

male_LCI = male_mean - (z_value *(male_deviation/ math.sqrt(len(male_sample))))
male_UCI = male_mean + (z_value *(male_deviation/ math.sqrt(len(male_sample))))


female_LCI = female_mean - (z_value *(female_deviation/ math.sqrt(len(female_sample))))
female_UCI = female_mean + (z_value *(female_deviation/ math.sqrt(len(female_sample))))
print("*"*10+" HYPOTHESIS TESTING FOR SAMPLE MEAN(MALE) "+"*"*10)
print(f"The lower limit of confidence interval :{male_LCI}")
print(f"The upper limit of confidence interval :{male_UCI}")


if male_LCI < male_mean < male_UCI :

    print(f"Thus, null hypothesis is not rejected as male sample mean {male_mean} lies between the interval {male_LCI} - {male_UCI}")
else:
    print(f"The male sample mean does not lie in the interval {male_LCI} - {male_UCI}. Thus, we reject the null hypothesis")

# matplotlib code
pos = male_mean
scale = male_deviation
size = len(male_sample)
values = np.random.normal(pos, scale, size)
plt.hist(values, 100)
plt.axvline(male_mean, color='k', linestyle='dashed', linewidth=2)
plt.axvline(male_average, color='r', linestyle='dashed', linewidth=2)

plt.axvline(male_LCI, color='y', linestyle='-', linewidth=2)

plt.axvline(male_UCI, color='y', linestyle='-', linewidth=2)
plt.show()


# /////////////////////////////////
print()
print()
print("*"*10+" HYPOTHESIS TESTING FOR SAMPLE MEAN(FEMALE) "+"*"*10)
print(f"The lower limit of confidence interval :{female_LCI}")
print(f"The upper limit of confidence interval :{female_UCI}")


if female_LCI < female_mean < female_UCI :

    print(f"Thus, null hypothesis is not rejected as female sample mean {female_mean} lies between the interval {female_LCI} - {female_UCI}")
else:
    print(f"The female sample mean does not lie in the interval {female_LCI} - {female_UCI}. Thus, we reject the null hypothesis")

# matplotlib code
pos = female_mean
scale = female_deviation
size = len(female_sample)
values = np.random.normal(pos, scale, size)
plt.hist(values, 100)
plt.axvline(female_mean, color='k', linestyle='dashed', linewidth=2)
plt.axvline(female_average, color='r', linestyle='dashed', linewidth=2)

plt.axvline(female_LCI, color='y', linestyle='-', linewidth=2)

plt.axvline(female_UCI, color='y', linestyle='-', linewidth=2)
plt.show()




