from calculate_age import age_calculator


def main():
    input_name = input("input your name: ")

    while True:
        input_age = input("input your age: ")
        try:
            string_to_int_age = int(input_age)
            if string_to_int_age <= 0:
                print("Please input a positive number.")
            else:
                break
        except ValueError:
            print("Please input a valid age.")

    result = age_calculator(input_name, string_to_int_age)

    print(result)

if __name__ == "__main__":
    main()


