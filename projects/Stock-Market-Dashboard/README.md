# Stock Market Dashboard

A Streamlit dashboard that visualizes S&P 500 stock data with Bollinger Bands, MACD, and RSI indicators computed from closing prices. Companies are grouped by sector and selected by ticker.

## How to run

```
pip install pandas yfinance ta streamlit
streamlit run dashboard.py
```

## Dependencies

pandas, yfinance, ta, streamlit

## Pyodide-runnable

No — it is a Streamlit web app that downloads stock data and the S&P 500 company list over the network.
