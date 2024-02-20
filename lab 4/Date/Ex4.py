import datetime

x=datetime.datetime.now()
print(x)
y=x+datetime.timedelta(hours=-5)
print(y)
z=(x-y).total_seconds()
print(f"Difference in seconds: {z}")