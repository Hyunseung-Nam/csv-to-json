# CSV → JSON 변환기 (CLI)

CSV 데이터를 JSON 형식으로 변환하는 간단한 커맨드라인 도구입니다.  
데이터 분석/웹 API 개발 전에 데이터를 가볍게 변환하고 확인하는 용도로 사용할 수 있습니다.

## ✨ 기능

- CSV 파일을 JSON 형식으로 변환
- 출력 제한 옵션 (`--limit`)
- 파일 저장 또는 stdout 출력 지원
- 실행 과정 및 오류 메시지를 로깅 (logging 모듈 사용)

---

## ⚙️ 기술 스택

- Python 3.13
- pandas
- logging

---

## 🚀 설치 & 실행 방법

```bash
1. 레포지토리 복사
git clone https://github.com/Hyunseung-Nam/csv-to-json.git
cd csv-to-json

2. 가상환경 설정(선택사항이지만 권장)
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
.venv/Scripts/activate       # Windows

3. 라이브러리 설치
pip install -r requirements.txt

4. 실행
python main.py --csv data/sample.csv                         # 결과를 화면에 출력
python main.py --csv data/sample.csv --out data/sample.json  # 결과를 파일로 저장
python main.py --csv data/sample.csv --limit 10              # 앞에서 10행만 출력
```

---

#### 예시(CSV)

```csv
id,name,age
1,Kim,23
2,Lee,30
3,Park,28
```

#### 실행 결과(json)
```json
[
  {
    "id": 1,
    "name": "Kim",
    "age": 23
  },
  {
    "id": 2,
    "name": "Lee",
    "age": 30
  },
  {
    "id": 3,
    "name": "Park",
    "age": 28
  }
]
```