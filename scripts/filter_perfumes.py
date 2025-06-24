#!/usr/bin/env python3
"""
filter_perfumes.py
------------------
CSV 데이터에서 특정 노트(키워드)가 포함된 향수를 골라서 출력합니다.
사용법:  python3 scripts/filter_perfumes.py vanilla
"""

import sys
import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "data" / "sample_perfumes.csv"

def load_data() -> pd.DataFrame:
    """CSV를 읽어와 DataFrame으로 반환."""
    return pd.read_csv(CSV_PATH)

def filter_perfumes(df: pd.DataFrame, keyword: str) -> pd.DataFrame:
    """main_accords 컬럼에서 keyword(대소문자 무시)를 포함한 행만 반환."""
    kw = keyword.lower().strip()
    mask = df["main_accords"].str.lower().str.contains(kw, na=False)
    return df[mask]

if __name__ == "__main__":
    # ❶ 키워드 받아오기
    if len(sys.argv) >= 2:
        query = " ".join(sys.argv[1:])
    else:
        query = input("검색할 노트를 입력하세요 (예: vanilla, woody): ").strip()

    # ❷ 데이터 로드 & 필터링
    data = load_data()
    results = filter_perfumes(data, query)

    # ❸ 결과 출력
    if results.empty:
        print(f"⚠️  '{query}' 가 포함된 향수를 찾지 못했습니다.")
    else:
        print("\n🔍  검색 결과:")
        print(
            results[["name", "brand", "main_accords", "fragrantica_url"]]
            .to_string(index=False)
        )
