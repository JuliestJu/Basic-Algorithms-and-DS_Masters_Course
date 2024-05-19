import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 3

a = 0 # Нижня межа
b = 2 # Верхня межа

# Обчислення аналітичного інтеграла для перевірки
analytical_result, _ = quad(f, a, b)

# Метод Монте-Карло для обчислення інтеграла
N = 100000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(min(f(x_random)), max(f(x_random)), N)
under_curve = y_random < f(x_random)
integral_monte_carlo = (b - a) * (max(f(x_random)) - min(f(x_random))) * np.mean(under_curve)

# Створення діапазону значень для x
x = np.linspace(-2.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([-2.5, 2.5])
ax.set_ylim([min(y) - 0.1, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання осей x=0 та y=0 для чотирьох квадрантів
ax.axhline(y=0, color='black', linewidth=1)
ax.axvline(x=0, color='black', linewidth=1)

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^3 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Виведення результатів
print(f"Аналітичне значення інтеграла: {analytical_result}")
print(f"Значення інтеграла методом Монте-Карло: {integral_monte_carlo}")
