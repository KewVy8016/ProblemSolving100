def find_multiples_three_and_four(start,end):
    num_list = []
    if start < 1 or end>1000:
        return print("Please enter 1 between 1000")
    elif start>=end:
        return print(f"input: start = {start}, end = {end}\noutput: {num_list}" )
    for i in range(start,end+1):
        if i%3 == 0 and i%4==0:
            num_list.append(i)
    return print(f"input: start = {start}, end = {end}\noutput: {num_list}" )

find_multiples_three_and_four(10,50)