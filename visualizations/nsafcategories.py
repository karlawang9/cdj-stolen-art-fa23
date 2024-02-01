import pandas as pd
import matplotlib.pyplot as plt

file_path = '../data/nsaf_data_new_timecleaned.csv'
df = pd.read_csv(file_path)
value_counts = df['New Category'].value_counts()

plt.bar(value_counts.index, value_counts.values)
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Categories by Count')
plt.xticks(rotation=45)
plt.show()