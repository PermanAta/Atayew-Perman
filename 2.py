import matplotlib.pyplot as plt

def point_inside_polygon(x, y, poly):
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(n+1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

def plot_polygon_with_point(polygon, point):
    x = [point[0] for point in polygon]
    y = [point[1] for point in polygon]

    plt.figure()
    plt.fill(x, y)
    plt.plot(x + [x[0]], y + [y[0]], 'ro-')  # соединяем последнюю точку с первой для замыкания полигона
    plt.plot(point[0], point[1], 'bo')  # отмечаем точку синим цветом
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})', fontsize=12, verticalalignment='bottom')
    plt.show()

polygon = [(3, 5), (5, 8), (4, 4), (4, 5), (3, 2)]
point = (4, 6)

is_inside = point_inside_polygon(point[0], point[1], polygon)
if is_inside:
    print(f"Точка {point} находится внутри полигона.")
else:
    print(f"Точка {point} находится снаружи полигона.")

plot_polygon_with_point(polygon, point)
