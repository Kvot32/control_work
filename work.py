def filter_strings(input_array):
    result_array = [s.strip() for s in input_array if len(s.strip()) <= 3]
    return result_array

if __name__ == "__main__":
    input_array = input("Введите строки через запятую: ").split(', ')
    result = filter_strings(input_array)
    print("Результат:", result)
