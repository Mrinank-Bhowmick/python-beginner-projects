# This is the code for stock market dashboard, it features Bollinger Bands, MACD, RSI indicators plotted using closing prices of S&P 500 companies
# To run the project, follow these steps:
# 1. install the following libraries:
# pandas==1.3.2
# yfinance==0.1.63
# ta==0.7.0
# streamlit
# 2. In the terminal type the command: streamlit run stock_market_dashboard.py


import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator


@st.cache
def load_data(url: str):
    html = pd.read_html(url, header=0)
    df1 = html[0]
    return df1


df = load_data("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
sector = df.groupby("GICS Sector")

# Sidebar:
sorted_sector_unique = sorted(df["GICS Sector"].unique())
selected_sector = st.sidebar.multiselect("Sector", sorted_sector_unique)
today = datetime.date.today()

if len(selected_sector) == 0:
    st.title("Stock Market Dashboard")
    st.write(
        "This dashboard consists of stock market visualization of companies in the list S&P 500 given in "
        "Wikipedia. Click here to see the [list](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)."
    )
    st.write(
        "The companies are grouped by their sectors and identified by their tickers. Select the Sector from the"
        " sidebar. For each selected ticker Bollinger Bands, MACD and RSI is plotted taking closing prices as the"
        " reference."
    )


else:
    df_selected_sector = df[df["GICS Sector"].isin(selected_sector)]
    before = today - datetime.timedelta(days=700)
    start_date = st.sidebar.date_input("Start date", before)
    end_date = st.sidebar.date_input("End date", today)
    if start_date < end_date:
        st.sidebar.success("Start date: `%s`\n\nEnd date:`%s`" % (start_date, end_date))
    else:
        st.sidebar.error("Error: End date must fall after start date.")
    st.title("Display Companies in:")
    for sector in selected_sector:
        st.header(sector)
    option = st.selectbox("Select ticker:", df_selected_sector.Symbol)
    company = df[df["Symbol"].isin([option])].Security

    # Stock data:

    # Download data
    stock_data = yf.download(option, start=start_date, end=end_date, progress=False)
    ticker_data = yf.Ticker(option)
    string_logo = "<img src=%s>" % ticker_data.info["logo_url"]
    st.markdown(string_logo, unsafe_allow_html=True)
    string_name = ticker_data.info["longName"]
    st.header("**%s**" % string_name)

    # Bollinger Bands
    indicator_bb = BollingerBands(stock_data["Close"])
    bb = stock_data
    bb["bb_h"] = indicator_bb.bollinger_hband()
    bb["bb_l"] = indicator_bb.bollinger_lband()
    bb = bb[["Close", "bb_h", "bb_l"]]

    # Moving Average Convergence Divergence
    macd = MACD(stock_data["Close"]).macd()

    # Resistance Strength Indicator
    rsi = RSIIndicator(stock_data["Close"]).rsi()

    # Main app

    # Plot the prices and the bollinger bands
    st.write("Stock Bollinger Bands")
    st.line_chart(bb)

    progress_bar = st.progress(0)

    # Plot MACD
    st.write("Stock Moving Average Convergence Divergence (MACD)")
    st.area_chart(macd)

    # Plot RSI
    st.write("Stock RSI ")
    st.line_chart(rsi)

    # Data of recent days
    st.write("Recent data ")
    st.dataframe(stock_data.tail(10))
