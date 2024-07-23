def get_num_test_cases():
    while True:
        num_test_cases = int(input())
        if 1 <= num_test_cases <= 1000:
            return num_test_cases
        else:
            print("Please enter a number between 1 and 1000.")

def get_two_integers():
    while True:
        a, b = map(int, input().split())
        if 2 <= a <= 50 and 0 <= b <= a-1:
            return a, b 
        else:
            print("Please enter correct values")

def correct_order(n, k):
    result = list(range(1, n + 1))
    x = result[:k]
    y = result[k:]
    y_reversed = y[::-1]
    final = x + y_reversed

    return final

def main():
    t = get_num_test_cases()
    test_cases = [get_two_integers() for _ in range(t)]
    
    for n, k in test_cases:
        final_output = correct_order(n, k)
        print(" ".join(map(str, final_output)))

if __name__ == "__main__":
    main()
