import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt

START = "2015-01-01"
END = dt.date.today().isoformat()
tickers = ["INTC", "NVDA"]

df = yf.download(tickers, start=START, end=END, interval="1wk")["Adj Close"].dropna()

plt.figure(figsize=(10,5.5))
for t in tickers:
    plt.plot(df.index, df[t], label=t, linewidth=2)

plt.title("INTC vs NVDA 股价走势（2015至今）")
plt.xlabel(f"时间区间：{START} 至 {END}")
plt.ylabel("股价（美元）")
plt.grid(True, linestyle="--", alpha=0.3)
plt.axhline(0, linewidth=1)
plt.legend()
plt.tight_layout()
plt.savefig("股价对比_2015至今.png", dpi=180)
print("完成：股价对比图已生成。")
