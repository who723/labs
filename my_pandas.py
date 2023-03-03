import pandas as pd
import io

# JSON
DATA_JSON_LINES = '''
{"hello":"world"}
{"hello":"new-world"}
'''

df = pd.read_json(DATA_JSON_LINES, lines=True)
assert "world" in list(df.hello)
assert "new-world" in list(df.hello)