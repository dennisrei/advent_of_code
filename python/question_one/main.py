from python.question_one import question_one


def main() -> None:
    list_of_ints = question_one.get_highest_value()
    print(max(list_of_ints))
    three_highest_values = question_one.get_three_highest_values(list_of_ints)
    print(sum(three_highest_values))


if __name__ == '__main__':
    main()
