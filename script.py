import csv

with open("./data/daily.csv", mode="r") as file:
    csvFile = csv.DictReader(file)

    wins = 0
    losses = 0

    sum_percent_wins = 0
    sum_percent_losses = 0

    for line in csvFile:
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
