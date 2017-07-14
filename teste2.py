'''
Aprendizadospandas
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''Gera uma série de datas
'''
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()

ts.plot()

plt.savefig('/home/rony/Imagens/teste6.jpg', dpi=None, facecolor = 'w', edgecolor = 'w', orientation = 'portrait', papertype = None, format = None, transparent = False, bbox_inches = None, pad_inches = 0.1, frameon = None)
plt.show()

