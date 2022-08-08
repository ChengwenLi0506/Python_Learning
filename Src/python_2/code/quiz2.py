

import warnings
warnings.filterwarnings("ignore")


import warnings
def mytest(a=1,b=2):
    print(a, b)
    warnings.warn("deprecated", DeprecationWarning)
    return a+b


print(mytest(3,4))


