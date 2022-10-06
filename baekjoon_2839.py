

if __name__ == "__main__":

    input_str = "12345"

    result_sum = 0
    for idx in range(len(input_str)):
        result_sum += int(input_str[idx])

    print(result_sum)