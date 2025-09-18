import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt

START = "2015-01-01"
END = dt.date.today().isoformat()
TICKERS = {"INTC": "Intel", "NVDA": "NVIDIA"}

data = yf.download(list(TICKERS.keys()), start=START, end=END, interval="1d")["Adj Close"]

plt.figure(figsize=(10,5.5))
for tk, name in TICKERS.items():
    plt.plot(data.index, data[tk], label=name, linewidth=2)

plt.ylabel("股价（美元）")
plt.xlabel(f"时间区间：{START} 至 {END}")
plt.title("英特尔 vs 英伟达 股价走势对比（2015至今）")
plt.grid(True, linestyle="--", alpha=0.3)
plt.axhline(0, linewidth=1)
plt.legend(title="")
plt.tight_layout()
plt.savefig("股价对比_2015至今.png", dpi=180)
print("完成：股价对比图已生成。")
