import time


def main():
    file = open('lyrics.txt', 'r')

    for a in file:
        print(a)
        time.sleep(1)
    file.close()


if __name__ == '__main__':
    main()
