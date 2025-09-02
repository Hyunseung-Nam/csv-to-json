import argparse        
import json            
import pandas as pd    
from pathlib import Path  

# ===== CSV → list 변환 함수 =====
def csv_to_records(csv_path: str, limit: int | None = None) -> list[dict]:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if limit:
        df = df.head(limit)
    # NaN → None (JSON 직렬화 안전)
    df = df.where(pd.notnull(df), None)

    return df.to_dict(orient="records")

# ===== 메인 함수 =====
def main():
    # CLI 옵션 정의
    parser = argparse.ArgumentParser(
        description="CSV 데이터를 JSON으로 변환하는 CLI 도구"
    )
    parser.add_argument("--csv", required=True, help="입력 CSV 경로")
    parser.add_argument("--out", default="", help="출력 JSON 경로(비우면 stdout)")
    parser.add_argument("--limit", type=int, default=None, help="최대 행 수 제한")
    args = parser.parse_args()

    records = csv_to_records(args.csv, args.limit)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        print(f"JSON saved -> {out_path}")
    else:
        # 결과를 stdout으로 출력
        print(json.dumps(records, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
