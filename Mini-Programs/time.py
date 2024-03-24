from datetime import datetime
import timeit
s = '''
def f():
  myList = []
  for n in range(5):
      myList.append(n)
'''
t = timeit.timeit(stmt=s)
print (t, "seconds")

start_time = datetime.now()
print("input some words:")
x = input()

time_elapsed = datetime.now() - start_time
print(time_elapsed)
print("Time elapsed(hh:mm:ss.ms): {}" . format(time_elapsed))
print("Time elapsed(hh:mm:ss.ms):" , format(time_elapsed))





"""
related links:
1. https://www.guru99.com/timeit-python-examples.html
2. example from https://www.geeksforgeeks.org/timeit-python-examples/:

# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = '''
def example():
    mylist = []
    for x in range(100):
        mylist.append(sqrt(x))
'''

# timeit statement
print(timeit.timeit(setup=mysetup, stmt=mycode, number=10000))

"""