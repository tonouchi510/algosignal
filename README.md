# algosignal

algosignal is a Python package for algorithmic trading.

The models included in this package return trading signals, 
with the stock prices as input.


## Features
- input: stock_price_csv
- output: buy and sell signal (json)

## Latest Features
- Mar 2019: Project start.

## Usage

```python
import pandas as pd
from algosignal.finance_model import MovingAvg

df = pd.read_table('stock_data_path')
model = MovingAvg()
model.get_signal(df)
```
