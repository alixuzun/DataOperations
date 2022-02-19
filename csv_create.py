
"""
Created on Fri Feb 11 22:27:36 2022
"""

import pandas as pd
import json


my_json = [
    {"name":"AAA","surname":"BBBB","age":13},
    {"name":"VVV","surname":"BBBB","age":25},
    {"name":"ZZZ","surname":"BBBB","age":65},
    {"name":"YYY","surname":"BBBB","age":76},
    ]


df = pd.DataFrame(my_json)


# df.to_csv("my_personal_data.csv",index=False)

with open("my_data.json","w",encoding='utf-8') as file:
    file.write(json.dumps(my_json))