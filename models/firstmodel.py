import pandas as pd
import matplotlib.pyplot as plt
import subproces

data = pd.read_csv("sp500.csv", index_col="Date", parse_dates=["Date"])
data["SMA"] = data["SP500"].rolling(50).mean()

data.plot()
plt.savefig("plot_data/output_plot.png")
plt.close()

subprocess.run(["open", "plot_data/output_plot.png"])
