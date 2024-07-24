def get_num_test_cases():
    while True:
        num_test_cases = int(input())
        if 1 <= num_test_cases <= 100:
            return num_test_cases
        else:
            print("Please enter a number between 1 and 100.")

def get_two_words():
    while True:
        a, b = map(str, input().split())
        if len(a)==3 and len(b)==3:
            return a, b 
        else:
            print("Please enter correct values")

def output(a, b):

    x = a[0]
    y = b[0]

    l = a[1:]
    m = b [1:]

    p = y+l
    q = x+m

    return (p, q)

def main():
    t = get_num_test_cases()
    test_cases = [get_two_words() for _ in range(t)]
    
    for a, b in test_cases:
        final_output = output(a, b)
        print(" ".join(map(str, final_output)))

if __name__ == "__main__":
    main()