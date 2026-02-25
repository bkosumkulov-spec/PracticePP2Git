import datetime
x = datetime.datetime.now()
print(x)

#Creating Data objects
x = datetime.datetime(2015, 5,7)
print(x)

#Date Formatting
x = datetime.datetime(2015, 5,7)
print(x.strftime("%B"))

#Calculating Time Differences 
x = datetime.datetime(2015, 5,7)
y = datetime.datetime(2015, 2,10)
print(x - y)
