import matplotlib
import matplotlib.pyplot as plt


cause = ['Chronic', 'heart attack','corona','drinking','accident', 'Others']
percentile = [62,5,4,2,1,26]

plt.figure(figsize=(10,10))
explode = (0.05,0,0,0,0,0)

plt.pie(percentile, labels=cause, explode= explode, autopct= "%1.1f%%", startangle = 70)
plt.axis('equal')
plt.title("India Death Rate-2013 : Leading Cuase of Death")
plt.show()