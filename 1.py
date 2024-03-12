import matplotlib.pyplot as plt

def is_self_intersecting(polygon):
    def ccw(A, B, C):
        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

    def intersect(A, B, C, D):
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

    for i in range(len(polygon)):
        for j in range(i+1, len(polygon)-1):
            if i == 0 and j == len(polygon)-1:
                continue
            if intersect(polygon[i], polygon[i+1], polygon[j], polygon[j+1]):
                return "Самопересекающийся"
    
    return "Самонепересекающийся"

def plot_polygon(polygon):
    x = [point[0] for point in polygon]
    y = [point[1] for point in polygon]
    
    plt.figure()
    plt.fill(x, y)
    plt.plot(x + [x[0]], y + [y[0]], 'ro-')  # соединяем последнюю точку с первой для замыкания полигона
    plt.show()

polygon = [(3, -4), (-1, -5), (5, 3), (1, -2), (3, -1)]
result = is_self_intersecting(polygon)
print(f"Полигон {result}")

plot_polygon(polygon)
