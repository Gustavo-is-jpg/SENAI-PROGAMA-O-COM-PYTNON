import pandas as pd

anf = {
    'and' : [False, False],
    'and' : [False, True],
    'and' : [True, False],
    'and' : [True, True],
    'or' : [False, False],
    'or' : [False, True],   
    'or' : [True, False],
    'or' : [True, True],
}

anf = pd.DataFrame(anf)

print(anf)