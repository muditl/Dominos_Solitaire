import time
import matplotlib.pyplot as plt
from tqdm import tqdm
from algorithm import *


def analyse_algorithm(algorithm):
    sizes = np.array([])
    times = np.array([])
    for i in np.linspace(2, 7500, num=100):
        n = int(np.floor(i))
        grid_ = generate_random_grid(n, 0, 100)
        time_sort_start = time.perf_counter()
        algorithm(grid_)
        time_sort_end = time.perf_counter()
        sizes = np.append(sizes, i)
        times = np.append(times, (time_sort_end - time_sort_start) * 1000)
    return sizes, times


def plot_times():
    x, y = analyse_algorithm(dynamic_programming_algorithm)
    for i in tqdm(range(20), desc="Analysing algorithm"):
        x1, y1 = analyse_algorithm(dynamic_programming_algorithm)
        x = x + x1
        y = y + y1
    x = x / 100
    y = y / 100
    return x, y


anal_x, anal_y = plot_times()
plt.plot(anal_x, anal_y)
plt.title("Running time analysis of algorithm")
plt.ylabel("Time (milliseconds)")
plt.xlabel("Size of input")
plt.show()
# plt.savefig("pls")
plt.close()
