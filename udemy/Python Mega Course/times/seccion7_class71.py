import datetime
import time

"""
Testing using datetime only
"""
yesterday = datetime.datetime(2016,5,14,11,0,48)
now = datetime.datetime.now()

print(yesterday)
print(now)

delta = now-yesterday
dd = delta.days
ds = delta.total_seconds()
print(dd)
print(ds)

"""
Creates an empty .txt file with the date as name
"""
filename = datetime.datetime.now()

def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M"+".txt"),'w') as file:
        file.write("")

create_file()

"""
More aplications of datetime
"""

after = now + datetime.timedelta(days=2)
print("after = {}".format(after))
