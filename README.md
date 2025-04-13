# 🇰🇭 Khmer Lunar Calendar API

A simple FastAPI-based web service that provides Khmer lunar calendar data for all 12 Gregorian months of a given year.

---

## 🌟 Features

- 🔁 Converts Gregorian year to 12 Khmer lunar months (mock logic)
- 🧘‍♂️ Buddhist year conversion included
- 📅 Each month returns representative lunar day & month
- 📦 FastAPI + Uvicorn for blazing-fast API performance

---

## 🚀 Live Demo

> Deployed on Render (Free Tier)

🌐 https://khmer-lunar-api-1.onrender.com/khmer-lunar/year/{year}

---

## 📌 API Endpoints

### `GET /khmer-lunar/year/{year}`  is dynamic u can replace the year that u want like [ 2024 , 2023, ......... ]
### example   
 🌐 https://khmer-lunar-api-1.onrender.com/khmer-lunar/year/2025
Returns Khmer lunar calendar data for the entire year.

#### Response:

```json
{
  "year": 2025,
  "lunar_calendar": [
    {
      "gregorian_month": "January",
      "gregorian_date": "2025-01-15",
      "lunar_day": 15,
      "lunar_month": "មិគសិរ",
      "lunar_year": "ឆ្នាំ 2568"
    },
    ...
  ]
}


