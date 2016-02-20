from pandas import Series, DataFrame

try:
    import numpy as np
except ImportError:
    print("numpy is not installed")
    
import pandas as pd
import matplotlib.pyplot as plt

arr = np.arange(10)

obj = Series([4, 7, -5, 3])