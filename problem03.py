def calculate_sum_and_average():
    num_list = []
    for i in range(5):
        num_input = float(input(f"Enter input {i+1} :"))
        num_list.append(num_input)
    sum_list = sum(num_list)
    len_list = len(num_list)
    print (f"Sum: {sum_list:.2f}")
    print (f"Average: {sum_list / len_list}")

calculate_sum_and_average()
