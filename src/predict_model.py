import pandas as pd
from train_model import get_model, load_dataset

df = load_dataset('data/machine_failure_predict.csv')
df = df[['maintenance_history', 'temperature', 'vibration','runtime_hours']]

model = get_model('data/machine_failure_train.csv')
df['failure'] = model.predict(df)

print(df.head())