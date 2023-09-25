import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess

data = pd.read_csv("sp500.csv", index_col="Date", parse_dates=["Date"])
data["SMA50"] = data["SP500"].rolling(50).mean()
data["SMA100"] = data["SP500"].rolling(100).mean()
data["Position"] = np.where(data["SMA50"] > data["SMA100"], 1, 0)
data["Position"] = data["Position"].shift()
data["StrategyPct"] = data["SP500"].pct_change(1) * data["Position"]
data["Strategy"] = (data["StrategyPct"] + 1).cumprod()
data["BuyHold"] = (data["SP500"].pct_change(1) + 1).cumprod()

data[["Strategy", "BuyHold"]].plot()
plt.savefig("plot_data/output1.png")
plt.close()

subprocess.run(["open", "plot_data/output1.png"])
