import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = int(input('Enter x value: '))
y = int(input('Enter y value: '))

if x>= 32 and y<=32:
    print(x-y)
else:
    print(x+y)