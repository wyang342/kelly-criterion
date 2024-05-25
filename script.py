import yfinance as yf
import datetime

print("Enter ticker (Yahoo finance): ")
ticker = input()

print("Enter start date, inclusive (YYYY-MM-DD): ")
start_date = input()

print("Enter end date, inclusive (YYYY-MM-DD): ")
end_date = input()
end_date_inclusive = (
    datetime.datetime.strptime(end_date, "%Y-%m-%d") + datetime.timedelta(days=1)
).strftime("%Y-%m-%d")

print("How often will you re-allocate your portfolio? (1d, 1wk, 1mo, 3mo): ")
interval = input().lower()

print("Include dividends and stock splits? (y/n): ")
actions = True if input().lower() == "y" else False

ticker = yf.Ticker(ticker)
hist = ticker.history(
    interval=interval, start=start_date, end=end_date_inclusive, actions=actions
)
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

p = (float(wins) / (wins + losses)) * 100
q = 100 - p
w = float(sum_percent_wins) / wins
l = float(sum_percent_losses) / losses
b = w / l
f = p - (q / b)

print(
    f"""
Results:
=======================
# wins: {wins}
# losses: {losses}
Win rate: {round(p, 2)}%
Loss rate: {round(q, 2)}%
Average win: {round(w, 2)}%
Average loss: {round(l, 2)}%
Profit factor: {round(b, 2)}
\033[1mOptimal allocation: {round(f, 2)}%\033[0m
"""
)
