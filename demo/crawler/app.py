# crawler/app.py
from flask import Flask
import json
import os

app = Flask(__name__)

@app.route('/load')
def load_to_tidb():
    # 현재 파일(app.py)의 위치는 /app/crawler/
    # movies.json의 위치는 /app/data/movies.json
    # 따라서 부모의 부모 폴더로 이동 후 data/movies.json을 찾습니다.
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    PATH = os.path.join(BASE_DIR, "data", "movies.json")
    
    if not os.path.exists(PATH):
        return {"error": f"File not found at {PATH}"}, 404
        
    with open(PATH, "r", encoding="utf-8") as f:
        movies = json.load(f)
    
    # TiDB 적재 로직 (기존 코드 유지)
    # ...
    print(f"{len(movies)}개의 데이터를 TiDB에 적재 완료")
    return {"status": "success", "count": len(movies)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)