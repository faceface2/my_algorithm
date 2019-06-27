def main(string):
    result = []
    if not string:
        return result
    func(list(string), result, 0)
    return sorted(result)


def func(string, res, i):
    if i == len(string) - 1:
        s = ''.join(string)
        if s not in res:
            res.append(s)
            return
    else:
        for j in range(i, len(string)):
            string[i], string[j] = string[j], string[i]
            func(string, res, i + 1)
            string[i], string[j] = string[j], string[i]
print(main('abcd'))
