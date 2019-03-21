"""
The :mod:`algosignal.finance_model._mavg` module includes classes and
functions to output signal by moving average method.
"""

# Author: Masato Tonouchi <tonouchi27@gmail.com>,
#         ??? ??? <???@gmail.com>
# License: MIT

import pandas as pd
from .._algosignal import AlgoSignal

WEIGHT_PATH = ""


class MovingAvg(AlgoSignal):
    """Most basic model using moving average

    Implementations must define `get_signal` and `load_model`.
    """
    def __init__(self):
        self.load_model(WEIGHT_PATH)

    def get_signal(self, inputs: pd.DataFrame):

        shape = inputs.shape
        if shape[1] != 17:
            return

        m25 = inputs['25DMA']
        m75 = inputs['75DMA']
        r = m25[0] / m75[0]

        buy_sig = 1.0 if 1.02 < r < 1.05 else 0.0
        sell_sig = 1.0 if r < 0.95 else 0.0
        return dict(buy_sig=buy_sig, sell_sig=sell_sig)

    def load_model(self, model_path: str):
        pass

