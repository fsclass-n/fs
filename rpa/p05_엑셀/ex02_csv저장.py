import pandas as pd
from pathlib import Path

cur_dir=Path(__file__).parent

data = {
	"이름": ["김철수","이영희"],
	"나이": [20,25]
}

df=pd.DataFrame(data)

df.to_csv(cur_dir / "output.csv", index=False)