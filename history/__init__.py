import os
import pandas as pd
from decimal import Decimal
from datetime import datetime
from typing import Callable, List
from calculator.calculation import Calculation

class History:
    hist: pd.DataFrame[Calculation] = pd.DataFrame(columns = ["Num 1", "Num 2", "Operation", "Result"])

    @classmethod
    def append_calc(cls, calc: Calculation):
        cls.hist.loc[len(cls.hist)] = [calc.get_a(), calc.get_b(), calc.get_oper(), calc.do()]

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.hist

    @classmethod
    def load_history(cls, hist, path: str): # going to be in same file as environment variable
        new_data = pd.read_csv(path)
        hist = pd.concat([hist, new_data], ignore_index = True)

    @classmethod
    def save_history(cls, hist):
        save_dir = "logs"
        os.makedirs(save_dir, exist_ok = True)
        save_file = os.path.join(save_dir, datetime.now().strftime("%m.%d.%H.%M.log"))
        
        
    @classmethod
    def clear_history(cls):
        cls.hist = pd.DataFrame(columns = ["Num 1", "Num 2", "Operation", "Result"])
