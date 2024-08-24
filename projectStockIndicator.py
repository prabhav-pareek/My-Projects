import yfinance as yf
import plotly.graph_objects as go

print("Welcome!! to Stock Market Indicator!!")
print()
stock_name = input("Enter the Stock Name (for eg. AAPL,MSFT): ")
start_date = input("Enter the Start Date (YYYY-MM-DD): ")
end_date = input("Enter the End Date (YYYY-MM-DD): ")

# Download stock data
data = yf.download(stock_name, start=start_date, end=end_date)

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'],
                increasing_line_width=2, decreasing_line_width=2)])

fig.update_layout(title='Basic Candlestick Chart')
fig.show()