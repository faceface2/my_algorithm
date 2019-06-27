def main():
    with open('domain.txt', 'r') as f:
        domains = f.read().split('\n')[0:-1]
    while 1:
        input_domain = input()
        if not input_domain:
            break
        loc = find_str('.', input_domain)
        count = input_domain.count('.')
        start = 0
        while start < count:
            pattern = '*' + input_domain[loc[start]:]
            if pattern in domains:
                print(input_domain, '\t', pattern)
                break
            start += 1


def find_str(s, string):
    res = []
    for idx, i in enumerate(string):
        if s == i:
            res.append(idx)
    return res


main()
