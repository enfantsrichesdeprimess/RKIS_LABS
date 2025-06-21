class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

sessions = [
    FitnessCenter("C001", 2023, 1, 60),
    FitnessCenter("C002", 2023, 2, 45),
    FitnessCenter("C003", 2023, 3, 90),
    FitnessCenter("C004", 2023, 4, 30),
    FitnessCenter("C005", 2023, 5, 120)
]

longest_session = max(sessions, key=lambda x: x.duration)
shortest_session = min(sessions, key=lambda x: x.duration)

print(f"Самое длинное занятие: Клиент {longest_session.client_code}, {longest_session.duration} мин")
print(f"Самое короткое занятие: Клиент {shortest_session.client_code}, {shortest_session.duration} мин")