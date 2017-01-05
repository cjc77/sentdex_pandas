import pandas as pd

prices_frame = pd.read_csv("housing_prices.csv")
prices_frame.set_index("Date", inplace=True)
print(prices_frame.head())

# Create a new csv file
prices_frame.to_csv("newcsv.csv")
prices_frame_v2 = pd.read_csv("newcsv.csv", index_col=0)
print(prices_frame_v2.head())

# Already set index to "Date"
prices_frame_v2.columns = ["Austin_HPI"]
print(prices_frame_v2.head())

# Create another new csv file (with new column title)
prices_frame_v2.to_csv("newcsv2.csv")

# Create another new csv (with no headings)
prices_frame_v2.to_csv("newcsv3.csv", header=False)

# New dataframe with a header
prices_frame_v3 = pd.read_csv("newcsv3.csv", names=["Date", "Austin_HPI"])
prices_frame_v3.set_index("Date", inplace=True)
print(prices_frame_v3.head())

prices_frame_v3.to_html("housing_prices.html")
