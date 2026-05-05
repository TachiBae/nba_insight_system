from tabulate import tabulate

def print_table(rows, headers):
    if rows:
        print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))
    else: 
        print("No Results Found")

def print_header(title):
    print('\n' + '=' * 50)
    print(f'  {title}')
    print('=' * 50)