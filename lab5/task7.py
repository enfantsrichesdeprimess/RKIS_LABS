def is_inside_circle(x, y, radius):
    distance = (x ** 2 + y ** 2) ** 0.5
    if distance <= radius:
        return True
    else:
        return False

point_x = 3
point_y = 4
circle_radius = 5
inside = is_inside_circle(point_x, point_y, circle_radius)
print(f"Точка ({point_x}, {point_y}) в круге радиуса {circle_radius}: {'да' if inside else 'нет'}")