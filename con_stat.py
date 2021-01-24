import pandas as pd
def concat(x,y):
    DATA = x
    k = pd.concat([x, y], axis = 1)
    return k