import os
import pandas as pd
from decimal import Decimal
from datetime import datetime
from typing import Callable, List
from calculator.calculation import Calculation

class History:
    hist = pd.DataFrame(columns = ["Num 1", "Num 2", "Operation", "Result"])

    @classmethod
    def append_calc(cls, calc: Calculation):
        cls.hist.loc[len(cls.hist)] = [calc.get_a(), calc.get_b(), calc.get_operation().__name__, calc.do()]

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.hist

    @classmethod
    def load_history(cls, path: str): # going to be in same file as environment variable
        new_data = pd.read_csv(path)
        cls.hist = pd.concat([cls.hist, new_data], ignore_index = True)

    @classmethod
    def save_history(cls):
        save_dir = "saves"
        os.makedirs(save_dir, exist_ok = True)
        save_file = os.path.join(save_dir, datetime.now().strftime("%m.%d.%H.%M.csv"))
        cls.hist.to_csv(save_file, index = False)
                
    @classmethod
    def clear_history(cls):
        cls.hist = pd.DataFrame(columns = ["Num 1", "Num 2", "Operation", "Result"])
    
    @classmethod
    def delete_index(cls, i: str):
        cls.hist = cls.hist.drop(index = i)
        cls.hist.reset_index(drop = True) #deletes a row and resets the index