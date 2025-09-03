import argparse        
import json            
import pandas as pd    
from pathlib import Path
import logging

# ===== 로거 설정 =====
logging.basicConfig(
    level=logging.INFO,                         
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'                                 
)

logger = logging.getLogger(__name__)

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

    try:
        records = csv_to_records(args.csv, args.limit)
        logger.info(f"Loaded {len(records)} records from {args.csv}")
    except FileNotFoundError:
        logger.error(f"CSV 파일을 찾을 수 없습니다: {args.csv}")
        return
    except UnicodeDecodeError:
        logger.error(f"CSV 인코딩 오류: {args.csv}")
        return
    except pd.errors.ParserError as e:
        logger.error(f"CSV 파싱 오류: {e}")
        return

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(records, f, ensure_ascii=False, indent=2)
            logger.info(f"JSON 저장 완료 -> {out_path}")
        except PermissionError:
            logger.error(f"쓰기 권한이 없습니다: {out_path}")
    else:
        # 결과를 stdout으로 출력
        print(json.dumps(records, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
