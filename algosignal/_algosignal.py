"""
The :mod:`algosignal._algosignal` module includes interfaces.
"""

# Author: Masato Tonouchi <tonouchi27@gmail.com>,
#         ??? ??? <???@gmail.com>
# License: MIT

import pandas as pd
from typing import Dict
from abc import ABCMeta, abstractmethod


class AlgoSignal(metaclass=ABCMeta):

    @abstractmethod
    def get_signal(self, inputs: pd.DataFrame)->Dict[float, float]:
        """Get a trading signal.

        :param inputs: Input data to model that has been fillna.
        :return: Sell and buy signal (0.0 ~ 1.0).
        """

        pass

    @abstractmethod
    def load_model(self, model_path: str):
        """Load init configuration for model(optional).

        :param model_path: model configuration path.
        :return: None
        """
        pass
