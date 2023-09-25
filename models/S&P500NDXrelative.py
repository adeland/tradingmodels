import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess

def get_data(file):
    data = pd.read_csv(file + ".csv", index_col="Date", parse_dates=["Date"])
    return data

def calc_corr(ser1, ser2, window):
    ret1 = ser1.pct_change()
    ret2 = ser2.pct_change()
    corr = ret1.rolling(window).corr(ret2)
    return corr

points_to_plot = 300

data = get_data("indexes")

for ind in data:
    data[ind + "_rebased"] = (data[-points_to_plot:][ind].pct_change() + 1).cumprod()

data["rel_str"] = data["NDX"] / data["SP500"]
data["corr"] = calc_corr(data["NDX"], data["SP500"], 100)
plot_data = data[-points_to_plot:]
fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(311)
ax.set_title("Index Comparison")
ax.semilogy(plot_data["SP500_rebased"], linestyle="-", label="S&P 500", linewidth=3.0)
ax.semilogy(plot_data["NDX_rebased"], linestyle="--", label="Nasdaq", linewidth=3.0)
ax.legend()
ax.grid(False)

ax = fig.add_subplot(312)
ax.plot(plot_data["rel_str"], label="Relative Strength, Nasdaq to S&P 500", linestyle=":", linewidth=3.0)
ax.legend()
ax.grid(True)

ax = fig.add_subplot(313)
ax.plot(plot_data["corr"], label="Correlation between Nasdaq and S&P 500", linestyle="-", linewidth=3.0)
ax.legend()
ax.grid(True)

plt.savefig("plot_data/ndxsp500corr.png")
plt.close()

subprocess.run(["open", "plot_data/ndxsp500corr.png"])
