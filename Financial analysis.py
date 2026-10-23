import pandas as pd
rawdata = pd.read_excel("FAD data.xlsx") #reads the excel file
print(rawdata.shape) #This tells you how many rows and columns you have
ratio_columns = [
    "Revenue growth(c3/c2-1)*100",
    "Net margin (d2/c2)*100",
    "ROA (D2/E2)*100",
    "ROE (D2/F2)*100",
    "Current ratio (j2/k2)",
    "debt to equity (i2/h2)",
    "Asset turnover (c2/e2)"
]

averages = rawdata.groupby("Company")[ratio_columns].mean() 
averages.to_excel("financial_analysis_results.xlsx") #to save the averages in excel
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None) #display all the rows/columns
print("\nBest performing company:")
print(averages.idxmax()) 
rankings = averages.rank(ascending=False) 
rankings.to_excel("company_rankings.xlsx") 

print(rankings) 
import matplotlib.pyplot as plt #for making charts

averages["Revenue growth(c3/c2-1)*100"].plot(kind="bar")

plt.title("Average Revenue Growth by Company")
plt.xlabel("Company")
plt.ylabel("Average Revenue Growth (%)")
plt.xticks(rotation=0)
plt.savefig("revenue_growth.png", dpi=300, bbox_inches="tight")

plt.show() 
averages["Net margin (d2/c2)*100"].plot(kind="bar")

plt.title("Average Net Profit Margin by Company")
plt.xlabel("Company")
plt.ylabel("Average Net Margin (%)")
plt.xticks(rotation=0) 
plt.savefig("net_margin.png", dpi=300, bbox_inches="tight")
plt.show() 
averages["ROA (D2/E2)*100"].plot(kind="bar")

plt.title("Average Return on Assets by Company")
plt.xlabel("Company")
plt.ylabel("Average ROA (%)")
plt.xticks(rotation=0)
plt.savefig("ROA.png", dpi=300, bbox_inches="tight")
plt.show()
averages["ROE (D2/F2)*100"].plot(kind="bar")

plt.title("Average Return on Equity by Company")
plt.xlabel("Company")
plt.ylabel("Average ROE (%)")
plt.xticks(rotation=0)
plt.savefig("ROE.png", dpi=300, bbox_inches="tight")
plt.show()
averages["debt to equity (h2/i2)"].plot(kind="bar")

plt.title("Average Debt-to-Equity Ratio by Company")
plt.xlabel("Company")
plt.ylabel("Average Debt-to-Equity Ratio")
plt.xticks(rotation=0)
plt.savefig("debt_to_equity.png", dpi=300, bbox_inches="tight")
plt.show()
averages["Asset turnover (c2/e2)"].plot(kind="bar")

plt.title("Average Asset Turnover by Company")
plt.xlabel("Company")
plt.ylabel("Average Asset Turnover")
plt.xticks(rotation=0)
plt.savefig("asset_turnover.png", dpi=300, bbox_inches="tight")
plt.show()
averages["Current ratio (j2/k2)"].plot(kind="bar")

plt.title("Average Current Ratio by Company")
plt.xlabel("Company")
plt.ylabel("Average Current Ratio")
plt.xticks(rotation=0)
plt.savefig("current_ratio.png", dpi=300, bbox_inches="tight")
plt.show() 

# Check only the Debt-to-Equity chart
import pandas as pd
import matplotlib.pyplot as plt

rawdata = pd.read_excel("FAD data.xlsx")

de_col = "debt to equity (i2/h2)"
de_averages = rawdata.groupby("Company")[de_col].mean()

print("\nAverage Debt-to-Equity Ratio:")
print(de_averages)

de_averages.plot(kind="bar")
plt.title("Average Debt-to-Equity Ratio by Company")
plt.xlabel("Company")
plt.ylabel("Average Debt-to-Equity Ratio")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()