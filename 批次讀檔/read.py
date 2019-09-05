import numpy as np
import pandas as pd
col_names = ['temperature', 'dewpoint', 'speed', 'direction']
df = pd.read_fwf('46000-2018073100.txt',usecols=[0, 1, 2, 3], names=col_names)
t=np.array(df.temperature)
print(df)