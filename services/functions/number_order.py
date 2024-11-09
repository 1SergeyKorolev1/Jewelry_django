import pathlib
project_path = pathlib.Path(__file__).parent.parent.parent
p = pathlib.Path(project_path, 'order_numbers.txt')

def get_number_order_list():
    with open(p, 'r') as file:
        list_numbers = []
        for line in file:
            list_numbers.append(line.rstrip())
        return list_numbers

def set_number_order_list(number):
    with open(p, 'a') as f_:
        f_.write(number + '\n')
        f_.close()

def delete_number_in_order_list(number):
    with open(p, 'r+') as f:
        data = f.read().replace(f'{number}\n', '')
        f.seek(0)
        f.write(data)
        f.truncate()
