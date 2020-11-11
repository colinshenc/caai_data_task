# %%
# Importing dependencies
"""Code taken from https://github.com/imdeepmind/processed-imdb-wiki-dataset"""
"""Cheng Shen Nov 10, 2020"""
import pandas as pd
import matplotlib.pyplot as plt

# %%
data = pd.read_csv('meta_wiki_imdb.csv')
# %%
# print(data.head())
# %%
print(data.columns)
# %%
print(data.shape)
# %%
gender = []
# for g in data['gender'].values:
#     if g == 'male':
#         gender.append(1)
#     else:
#         gender.append(0)
#
# plt.hist(gender, range(3))
# plt.title(
#     'There are total ' + str(len(gender) - sum(gender)) + ' female images and ' + str(sum(gender)) + ' male images')
# plt.show()
# # %%
# print(111)
# print(data.shape[0])
########Q3
ct_male=len(data[(data['age']==30) & (data['gender']=='male')])
ct_total=len(data[(data['age']==30)])
ct_female=len(data[(data['age']==30) & (data['gender']=='female')])
print('tot {}, female {}'.format(ct_total, ct_female))
percent = ct_male / data.shape[0]
print(ct_male)
# print(percent)
print('percent {}'.format(percent))
########Q2
ct_bucket = len(data[(data['age']>=15) & (data['age']<=25)])
print(ct_bucket)
plt.figure(figsize=(12,7))
plt.hist(data['age'], range(111),rwidth = 1, alpha=0.65)
plt.title('IMDB-WIKI Age Distribution')
plt.xlabel('age/year')
plt.ylabel('freq')
plt.xticks(range(0,111,10))

plt.savefig('./{}.png'.format('plot_q2'), dpi=300)

# plt.show()


