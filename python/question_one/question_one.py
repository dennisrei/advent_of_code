def get_highest_value() -> list[int]:
    input_file = open('input_question_one.txt').read()
    input_list = input_file.split('\n')

    lists_of_numbers_list = [[]]
    for var in input_list:
        if var == '':
            lists_of_numbers_list.append([])
        else:
            lists_of_numbers_list[-1].append(int(var))
    list_of_sums = [sum(number) for number in lists_of_numbers_list]

    return list_of_sums


def get_three_highest_values(list_of_ints: list[int]) -> list[int]:
    return sorted(list_of_ints)[-3:]
