import datetime

def format_date(input_date):
    try:
        parts = input_date.split('.')
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        current_year = datetime.datetime.now().year
        if year != current_year:
            return "Error: Date must be in current year"

        date_obj = datetime.datetime(year, month, day)

        months = {
            1: "Января",
            2: "Февраля",
            3: "Марта",
            4: "Апреля",
            5: "Мая",
            6: "Июня",
            7: "Июля",
            8: "Августа",
            9: "Сентября",
            10: "Октября",
            11: "Ноября",
            12: "Декабря"
        }

        weekdays = {
            0: "Понедельник",
            1: "Вторник",
            2: "Среда",
            3: "Четверг",
            4: "Пятница",
            5: "Суббота",
            6: "Воскресенье"
        }

        weekday_name = weekdays[date_obj.weekday()]
        month_name = months[month]

        return f"{weekday_name}, {day} {month_name}, {year} год"

    except:
        return "Invalid date format"


user_date = "02.06.2025"
print(format_date(user_date))
print()
