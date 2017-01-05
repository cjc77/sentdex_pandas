import pandas as pd
import datetime
# import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use("ggplot")

# "Bounce_Rate" is a percentage
web_stats = {"Day": [1, 2, 3, 4, 5, 6],
             "Visitors": [43, 53, 34, 45, 64, 34],
             "Bounce_Rate": [65, 72, 62, 64, 54, 66]}


web_stats_df = pd.DataFrame(web_stats)

#print(web_stats_df)
#
## first 2
#print(web_stats_df.head(2))
#
## last 2
#print(web_stats_df.tail(2))
#

# set "Day" as the index of a new dataframe
mod_df = web_stats_df.set_index("Day")
print(mod_df)

# add the 0-n indexing back in
mod_df.reset_index(inplace=True)
print(mod_df)

# set "Day" as the index
mod_df.set_index("Day", inplace=True)


# print visitors col
print(mod_df["Visitors"])

# print contents of each col
for i in mod_df:
    print(mod_df[i])


# print contents of specified cols
print(mod_df[["Bounce_Rate", "Visitors"]])


# make a list
visitors_list = mod_df.Visitors.tolist()
print("\n\n\nVisitors (list form): ", visitors_list, sep="")

# make a numpy array
np_array = np.array(mod_df[["Bounce_Rate", "Visitors"]])
print("\n\n\nPairs of [Bounce_Rate, Visitors]: \n", np_array, sep="")


# turn np array back into a dataframe
np_frame = pd.DataFrame(np_array)
print(np_frame)
