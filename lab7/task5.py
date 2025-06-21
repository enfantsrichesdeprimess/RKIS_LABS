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
    FitnessCenter("C005", 2023, 5, 120),
    FitnessCenter("C006", 2024, 1, 75),
    FitnessCenter("C007", 2024, 2, 80),
    FitnessCenter("C008", 2024, 3, 65),
    FitnessCenter("C009", 2024, 4, 100),
    FitnessCenter("C010", 2024, 5, 50)
]

yearly_duration = {}
for session in sessions:
    if session.year in yearly_duration:
        yearly_duration[session.year] += session.duration
    else:
        yearly_duration[session.year] = session.duration

max_year = min(yearly_duration, key=lambda k: (-yearly_duration[k], k))
max_duration = yearly_duration[max_year]

print(f"Год с наибольшей продолжительностью занятий: {max_year} ({max_duration} мин)")