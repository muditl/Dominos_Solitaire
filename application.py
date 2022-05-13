import PySimpleGUI as sg
from algorithm import generate_random_grid, dynamic_programming_algorithm, print_grid_sol


def get_row(string, sep):
    str_arr = string.strip().split(sep)
    int_arr = []
    for s in str_arr:
        int_arr.append(int(s.replace(" ", "")))
    return int_arr


def do_everything(inputs):
    int_1 = get_row(inputs[1], inputs[0])
    int_2 = get_row(inputs[2], inputs[0])
    if len(int_1) != len(int_2):
        show_error_message()
        return
    grid = [int_1, int_2]
    b, s = run_algorithm(grid)
    print_grid_sol(grid, s)


def show_error_message():
    raise Exception("Inputs are not equal!!")


def run_algorithm(grid):
    return dynamic_programming_algorithm(grid)


sg.theme('DarkAmber')
# All the stuff inside your window.
layout = [[sg.Text('Separator:  '), sg.InputText()],
          [sg.Text('Input row 1:'), sg.InputText()],
          [sg.Text('Input row 2:'), sg.InputText()],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Dominos Solitaire Algorithm Runner', layout)
# Event Loop to process "events" and get the "values" of the inputs


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    do_everything(values)

window.close()
