# Stock Market Dashboard

A Streamlit dashboard that visualizes S&P 500 stock data with Bollinger Bands, MACD, and RSI indicators computed from closing prices. Companies are grouped by sector and selected by ticker.

## Example

1. Run `streamlit run dashboard.py`. The dashboard opens in your browser showing a title and description.
2. In the sidebar, select a sector from the "Sector" multiselect — for example "Information Technology".
3. Choose a start and end date, then pick a ticker such as `AAPL` from the dropdown.
4. The dashboard displays Apple's company logo and name, followed by three charts: Stock Bollinger Bands, MACD, and RSI, each computed from the closing price over the selected date range.
5. A table of the 10 most recent trading days of data appears at the bottom.

## How to run on localhost

```
pip install pandas yfinance ta streamlit
streamlit run dashboard.py
```

## Dependencies

pandas, yfinance, ta, streamlit
