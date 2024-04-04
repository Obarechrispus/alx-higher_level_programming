#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Attempt to convert elements to float for division
            try:
                num1 = float(my_list_1[i])
            except (TypeError, ValueError):
                print("wrong type")
                num1 = 0  # Treat non-numeric types as 0
            try:
                num2 = float(my_list_2[i])
                if num2 == 0:
                    raise ZeroDivisionError  # Raise ZeroDivisionError for division by zero
            except (TypeError, ValueError):
                print("wrong type")
                num2 = 1  # Treat non-numeric types as 1
            except ZeroDivisionError:
                print("division by 0")
                num2 = 1  # Treat division by zero as 1
            result.append(num1 / num2)
        except IndexError:
            print("out of range")
            result.append(0)  # Append 0 if any list is shorter than list_length
        finally:
            pass  # No specific action in the finally block
    return result

if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
