def get_num_test_cases():
    while True:
        num_test_cases = int(input())
        if 1 <= num_test_cases <= 1000:
            return num_test_cases
        else:
            print("Please enter a number between 1 and 1000.")

def get_three_integers(test_case_num):
    while True:
        a, b, c = map(int, input(f'').split())
        if 1 <= a <= 10 and 1 <= b <= 10 and 1 <= c <= 10:
            return a, b, c
        else:
            print("Please enter values between 1 and 10 for all three integers.")

def maximize_product(a, b, c):
    nums = [a, b, c]

    for _ in range(5):
        nums.sort()
        nums[0] += 1

    result = nums[0] * nums[1] * nums[2]
    return result            

num_test_cases = get_num_test_cases()

for i in range(num_test_cases):
    a, b, c = get_three_integers(i)

    result = maximize_product(a, b, c)

    print(f'{result}')
