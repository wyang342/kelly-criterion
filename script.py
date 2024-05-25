import yfinance as yf

ticker = "VOO"
start_date = "2020-08-01"
end_date = "2024-05-18"
interval = "1d"

ticker = yf.Ticker(ticker)

hist = ticker.history(interval=interval, start=start_date, end=end_date)
hist = hist.reset_index()  # make sure indexes pair with number of rows

wins = 0
losses = 0

sum_percent_wins = 0
sum_percent_losses = 0

for _, line in hist.iterrows():
    close_price = float(line["Close"])
    open_price = float(line["Open"])
    if close_price >= open_price:
        wins += 1
        percent_win = (close_price - open_price) / open_price * 100
        sum_percent_wins += percent_win
    else:
        losses += 1
        percent_loss = (open_price - close_price) / open_price * 100
        sum_percent_losses += percent_loss

print("Sum percent wins:", sum_percent_wins)
print("Sum percent losses:", sum_percent_losses)
print("# wins:", wins)
print("# losses:", losses)
print()
