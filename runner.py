from algorithm import *

grid = generate_random_grid(12, -10, 10)
print("\n" + get_grid_string(grid))

best, solution = dynamic_programming_algorithm(grid)
print(Fore.MAGENTA, "\nBlue means vertical column, green means horizontal column")
print_grid_sol(grid, solution)
print(Fore.LIGHTYELLOW_EX)
print("Score: " + str(best[len(best) - 1]))

