def get_num_test_cases():
    while True:
        num_test_cases = int(input())
        if 1 <= num_test_cases <= 1000:
            return num_test_cases
        else:
            print("Please enter a number between 1 and 1000.")

def get_three_integers():
    while True:
        a, b, c = map(int, input(f'').split())
        if 1 <= a <= 10 and 1 <= b <= 10 and 1 <= c <= 10:
            return a, b, c
        else:
            print("Please enter values between 1 and 10 for all three integers.")

def min_distance(x1, x2, x3):
    min_value = float('inf')
    for a in range(1, 11):  # Check all possible values from 1 to 10
        f_a = abs(a - x1) + abs(a - x2) + abs(a - x3)
        min_value = min(min_value, f_a)
    return min_value

def main():
    num_test_cases = get_num_test_cases()
    results = []

    for _ in range(num_test_cases):
        x1, x2, x3 = get_three_integers()
        result = min_distance(x1, x2, x3)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()