import numpy as np
import matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


file_path = 'C:\\Users\\w18029876\\Downloads\\6000-report-2\\Data\\Demo\\Sensor_4_1.txt'
df = pd.read_csv(file_path, delimiter = '\t', index_col = False)
df = df[0:79500]
df = df.drop(columns=[df.columns[0]])
#fig, axes = plt.subplots(3, 2, figsize = (14, 30), dpi = 100)
#ax_index = [0, 1, 2] * 2
#for i in range(2, 8):
#    df[df.columns[i]].plot(ax = axes[ax_index[i-2]][int(i>=5)],alpha=0.8, color='tab:blue')
#    axes[ax_index[i-2]][int(i>=5)].set_title(df.columns[i], fontsize = 13)
#    plt.subplots_adjust(hspace = 0.45)

df_1 = df.copy()
Temp_df = []
i_node = 0
for i in range(0, len(df_1)-1):
    if df_1['Milisecond [ms]'][i] - df_1['Milisecond [ms]'][i+1] != -2:
        Temp_df.append([i_node, i])
        i_node = i+1

df_1['Milisecond [ms]'] = df_1['Milisecond [ms]']- df_1['Milisecond [ms]'][0]

Temp_df_Shard = []
for ii in Temp_df:
    Temp_df_Shard.append(df_1[ii[0]:ii[1]+1])

New_df = pd.DataFrame(columns = df.columns)

last_element = Temp_df_Shard[len(Temp_df_Shard)-1]
#del Temp_df_Shard[-1]
del Temp_df_Shard[-1]
count = 0
for i in range(len(Temp_df)-2):
    New_df = New_df.reset_index(drop = True)
    start_i = Temp_df_Shard[i]['Milisecond [ms]'].iloc[-1]
    end_i = Temp_df_Shard[i+1]['Milisecond [ms]'].iloc[0]
    TEMP_new_df = pd.DataFrame(columns = df.columns)
    TEMP_new_df['Milisecond [ms]'] =  np.linspace(start_i+2, end_i-2, int((end_i-start_i)/2)).astype('int')
    New_df = pd.concat([New_df, Temp_df_Shard[i],TEMP_new_df], ignore_index=True)
    count += 1
    print(count)


New_df.to_csv(r'C:\\Users\\w18029876\\Downloads\\6000-report-2\\Data\\Demo\\Cleaned.csv')

