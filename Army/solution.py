def get_years_for_rank(n):
    d = list(map(int, input().split()))
    if len(d) != n - 1:
        print('error')
        return None
    return d

def num_total_years(a, b, d):
    if 1 <= a < b <= len(d) + 1:
        return sum(d[a-1:b-1])
    else:
        print('error')
        return None

def main():
    n = int(input())
    if not (2 <= n <= 100):
        print('error')
        return

    d = get_years_for_rank(n)
    if d is None:
        return

    a, b = map(int, input().split())
    
    years_needed = num_total_years(a, b, d)
    if years_needed is not None:
        print(years_needed)

if __name__ == "__main__":
    main()





