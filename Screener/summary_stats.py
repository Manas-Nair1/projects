import pandas as pd 
import statistics


df = pd.read_csv("/workspaces/projects/Screener/NasdaqRatios.csv")

lst = []

for index, value in df.iterrows():
    if value["Industry"] != "Industry information not found" and value['Ratio'] != "Information not available":
        lst.append([value.Ticker, value.Industry, value.Ratio])
new_df = pd.DataFrame(lst, columns=['Ticker', 'Industry', 'Ratio'])
print(new_df.tail())

industry_ratios = {}
for index, value in new_df.iterrows():
    if value.Industry in industry_ratios.keys():
        industry_ratios[value.Industry].append(float(value.Ratio))
    else:
        industry_ratios[value.Industry] = [float(value.Ratio)]
# print(industry_ratios)
averages = []
for key in industry_ratios.keys():
    print(key, statistics.mean(industry_ratios[key]), statistics.stdev(industry_ratios[key]))
    averages.append([key, statistics.mean(industry_ratios[key]), statistics.stdev(industry_ratios[key])])
    
averages_df = pd.DataFrame(averages, columns=['Industry', 'Mean', 'Stdev'])
# averages_df.to_csv('IndustryAverages.csv')