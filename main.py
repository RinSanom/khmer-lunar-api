from fastapi import FastAPI
from datetime import datetime
import calendar

app = FastAPI()

# Khmer lunar month names (mocked)
khmer_lunar_months = [
    "មិគសិរ", "បុស្ស", "មាឃ", "ផល្គុន", "ចេត្រ", "ពិសាខ",
    "ជេស្ឋ", "អាសាឍ", "ស្រាពណ៍", "ភទ្របទ", "អស្សុជ", "កត្តិក"
]

# Mock holidays - You can customize this per month/day later
mock_holidays = {
    (1, 1): ["New Year's Day"],
    (1, 7): ["Victory over Genocide Day"],
    (4, 14): ["Khmer New Year Day 1"],
    (4, 15): ["Khmer New Year Day 2"],
    (4, 16): ["Khmer New Year Day 3"],
    (5, 1): ["International Labor Day"],
    (11, 9): ["Independence Day"],
    (12, 31): ["New Year's Eve"],
}

def convert_month_to_khmer_lunar(year: int, month: int):
    # Pick 15th as representative date for lunar info
    date = datetime(year, month, 15)
    lunar_day = date.day % 15 or 15
    lunar_month = khmer_lunar_months[(month - 1) % 12]
    lunar_year = f"ឆ្នាំ {2567 + (year - 2024)}"  # Buddhist year mock

    # Get number of days in the current month
    total_days = calendar.monthrange(year, month)[1]

    # Create a list of all days with holidays (if any)
    days_of_month = []
    for day in range(1, total_days + 1):
        holidays = mock_holidays.get((month, day), [])
        days_of_month.append({
            "day": day,
            "holiday": holidays
        })

    return {
        "gregorian_month": date.strftime("%B"),
        "gregorian_date": date.strftime("%Y-%m-%d"),
        "lunar_day": lunar_day,
        "lunar_month": lunar_month,
        "lunar_year": lunar_year,
        "days_of_month": days_of_month
    }

@app.get("/khmer-lunar/year/{year}")
def get_lunar_calendar_year(year: int):
    try:
        lunar_calendar = [
            convert_month_to_khmer_lunar(year, month) for month in range(1, 13)
        ]
        return {
            "year": year,
            "lunar_calendar": lunar_calendar
        }
    except Exception as e:
        return {"error": str(e)}
