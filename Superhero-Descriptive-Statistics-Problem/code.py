# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot(kind='bar')


# --------------
#Code starts here
import matplotlib.pyplot as plt
alignment = data['Alignment'].value_counts()
labels = alignment.index
plt.pie(alignment,labels=labels)
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df=data[['Strength','Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
sc_pearson = sc_covariance/(sc_strength*sc_combat)

ic_df=data[['Intelligence','Combat']].copy()
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)





# --------------
#Code starts here
total_high = data.Total.quantile(.99)
super_best = data[data['Total']>=total_high]
super_best_names_t = super_best.Name.values
super_best_names = []
for i in super_best_names_t:
    super_best_names.append(i)
super_best_names


# --------------
#Code starts here
import matplotlib.pyplot as plt
fig = plt.figure()
ax_1 = fig.add_subplot(221)
ax_1.boxplot(data['Intelligence'])
ax_2 = fig.add_subplot(222, sharex=ax_1, sharey=ax_1)
ax_3 = fig.add_subplot(223, sharex=ax_1, sharey=ax_1)
ax_2.boxplot(data['Speed'])
ax_3.boxplot(data['Power'])
ax_1.set_title('Intelligence')
ax_2.set_title('Speed')
ax_3.set_title('Power')
plt.show()


