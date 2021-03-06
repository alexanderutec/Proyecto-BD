import pandas as pd
from IPython.display import display
from faker import Faker
from collections import defaultdict
import random

fake = Faker()
fake_data = defaultdict(list)

i = 1
tuples = 100
for _ in range(tuples):
    fake_data['id'].append("PT" + "0"*(7 - len(str(i))) + str(i))
    fake_data['nombre'].append(fake.job()[0:49])
    i += 1
df_fake_data = pd.DataFrame(fake_data)
df_fake_data.drop_duplicates(keep='first', inplace=True)
df_fake_data.to_csv('puestoTrabajo.csv', index = False)
display(df_fake_data)