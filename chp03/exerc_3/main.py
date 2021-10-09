def print_junction():
    print('+', end=' ')

def print_4of(char : str):
    print(char, char, char, char, end=' ')

def print_line_2():
    print_junction()
    print_4of('-')
    print_junction()
    print_4of('-')
    print_junction()
    print()

def print_column_2():
    print('|', end=' ')
    print_4of(' ')
    print('|', end=' ')
    print_4of(' ')
    print('|', end=' ')
    print()

def print_cell_borders_2():
    print_column_2()
    print_column_2()
    print_column_2()
    print_column_2()

def print_grid_2x2():
    print_line_2()
    print_cell_borders_2()
    print_line_2()
    print_cell_borders_2()
    print_line_2()

def print_line_4():
    print_junction()
    print_4of('-')
    print_junction()
    print_4of('-')
    print_junction()
    print_4of('-')
    print_junction()
    print_4of('-')
    print_junction()
    print()

def print_column_4():
    print('|', end=' ')
    print_4of(' ')
    print('|', end=' ')
    print_4of(' ')
    print('|', end=' ')
    print_4of(' ')
    print('|', end=' ')
    print_4of(' ')
    print('|', end=' ')
    print()

def print_cell_borders_4():
    print_column_4()
    print_column_4()
    print_column_4()
    print_column_4()

def print_grid_4x4():
    print_line_4()
    print_cell_borders_4()
    print_line_4()
    print_cell_borders_4()
    print_line_4()
    print_cell_borders_4()
    print_line_4()
    print_cell_borders_4()
    print_line_4()

print_grid_2x2()
print_grid_4x4()