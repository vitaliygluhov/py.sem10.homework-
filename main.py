import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})


data['robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
data['human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)
data.drop('whoAmI', axis=1, inplace=True)


data.head()
print(data)
