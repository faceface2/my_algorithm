def main():
    with open('keyword.conf', 'r') as f1:
        keyword = f1.read().split('\n')[0:-1]
    if not keyword:
        return
    with open('input.txt', 'r') as f2:
        while 1:
            line = f2.readline()
            if line:
                content = line.split(' ')[0]
                for w in keyword:
                    if w in content:
                        print(line)
            else:
                break


main()
