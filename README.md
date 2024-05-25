# kelly-criterion

This script calculates the optimal portfolio allocation percentage for a given asset and re-allocation frequency. This percentage is calculated according to the [Kelly Criterion](https://en.wikipedia.org/wiki/Kelly_criterion#Investment_formula).

## How to Run

```
pip install -r requirements.txt
python script.py
```

## Example

```
Enter ticker (Yahoo finance):
MSTR
Enter start date, inclusive (YYYY-MM-DD):
2020-08-01
Enter end date, inclusive (YYYY-MM-DD):
2024-05-24
How often will you re-allocate your portfolio? (1d, 1wk, 1mo, 3mo):
1mo
Include dividends and stock splits? (y/n):
y

Results:
=======================
# wins: 27
# losses: 19
Win rate: 58.7%
Loss rate: 41.3%
Average win: 31.62%
Average loss: 20.53%
Profit factor: 1.54
Optimal allocation: 31.87%
```
