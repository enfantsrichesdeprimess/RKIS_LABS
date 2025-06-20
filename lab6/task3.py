class Task:
    def __init__(self, date_start, date_finish, description):
        self.DateStart = date_start
        self.DateFinish = date_finish
        self.Description = description

tasks = [
    Task("2023-01-01 09:00", "2023-01-01 10:00", "Утренняя встреча"),
    Task("2023-01-01 10:00", "2023-01-01 12:00", "Работа над проектом"),
    Task("2023-01-01 12:00", "2023-01-01 13:00", "Обеденный перерыв"),
    Task("2023-01-01 13:00", "2023-01-01 15:00", "Совещание"),
    Task("2023-01-01 15:00", "2023-01-01 17:00", "Анализ данных")
]

latest_task = max(tasks, key=lambda x: x.DateFinish)
print(f"Занятие, заканчивающееся позже всех: {latest_task.Description}, Время окончания: {latest_task.DateFinish}")