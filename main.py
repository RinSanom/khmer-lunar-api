from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

khmer_lunar_months = [
    "មិគសិរ", "បុស្ស", "មាឃ", "ផល្គុន", "ចេត្រ", "ពិសាខ",
    "ជេស្ឋ", "អាសាឍ", "ស្រាពណ៍", "ភទ្របទ", "អស្សុជ", "កត្តិក"
]
def convert_month_to_khmer_lunar(year: int, month: int):
    date = datetime(year, month, 15)
    lunar_day = date.day % 15 or 15
    lunar_month = khmer_lunar_months[(month - 1) % 12]
    lunar_year = f"ឆ្នាំ {2567 + (year - 2024)}"  
    return {
        "gregorian_month": date.strftime("%B"),
        "gregorian_date": date.strftime("%Y-%m-%d"),
        "lunar_day": lunar_day,
        "lunar_month": lunar_month,
        "lunar_year": lunar_year
    }

@app.get("/khmer-lunar/year/{year}")
def get_lunar_calendar_year(year: int):
    try:
        lunar_calendar = [convert_month_to_khmer_lunar(year, month) for month in range(1, 13)]
        return {
            "year": year,
            "lunar_calendar": lunar_calendar
        }
    except Exception as e:
        return {"error": str(e)}
