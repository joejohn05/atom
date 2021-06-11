import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

my_date = datetime.date.today() # if date is 01/01/2018
year, week_num, day_of_week = my_date.isocalendar()
print("Week #" + str(week_num) + " of year " + str(year))
x="Week #" + str(week_num)
print(x)

x1=106
y1=53

data = {'Ticket Status': [x1,y1]}
df = pd.DataFrame(data,columns=['Ticket Status'],index = ['Pending','Open_New'])

df.plot.pie(y='Ticket Status',figsize=(5, 5),autopct='%1.1f%%', startangle=90)
#plt.show()
plt.xlabel(x)
plt.savefig('/Users/jomon.john/Desktop/chart.pdf') '''


print("hi")

print("hi again")
