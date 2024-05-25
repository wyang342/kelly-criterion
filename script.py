import csv
import yfinance as yf
import pandas as pd

ticker = "MSTR"
start_date = "2020-08-01"
end_date = "2024-05-25"

stock_data = yf.download(ticker, start=start_date, end=end_date, interval="1d")

print(stock_data)

# Resample the data to yearly frequency
# Use 'Y' for year-end frequency
yearly_data = stock_data.resample("YE").agg(
    {"Open": "first", "High": "max", "Low": "min", "Close": "last", "Volume": "sum"}
)

# Display the yearly data
print(yearly_data)


# time_ranges = ["daily", "weekly", "monthly"]


# for time_range in time_ranges:
#     print("Time range:", time_range)
#     print("=====================================")
#     with open("./data/voo/" + time_range + ".csv", mode="r") as file:
#         csvFile = csv.DictReader(file)

#         wins = 0
#         losses = 0

#         sum_percent_wins = 0
#         sum_percent_losses = 0

#         for line in csvFile:
#             close_price = float(line["Close"])
#             open_price = float(line["Open"])
#             if close_price >= open_price:
#                 wins += 1
#                 percent_win = (close_price - open_price) / open_price * 100
#                 sum_percent_wins += percent_win
#             else:
#                 losses += 1
#                 percent_loss = (open_price - close_price) / open_price * 100
#                 sum_percent_losses += percent_loss

#         print("Sum percent wins:", sum_percent_wins)
#         print("Sum percent losses:", sum_percent_losses)
#         print("# wins:", wins)
#         print("# losses:", losses)
#         print()
