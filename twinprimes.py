# -*-coding:utf-8-*-
import time


def prime(n):  # 筛选法求素数
    pt = [True] * n
    res = []
    twin_prime_list = []
    count = 0

    for p in range(2, n):
        if not pt[p]: continue
        res.append(p)
        for i in range(p * p, n, p):
            pt[i] = False

    for i in range(1, len(res)):  # 求孪生素数
        if res[i] - res[i - 1] == 2:
            twin_prime_list.append(res[i - 1])
            twin_prime_list.append(res[i])
            count += 1
    return (count, twin_prime_list)


if __name__ == "__main__":
    start = time.time()  # 程序开始时间

    n = 100000000
    print_count = 0
    Twin_prime_count = 0
    Twin_prime_list = []

    Twin_prime_count, Twin_prime_list = prime(n)

    with open(r'C:\Users\54941\Desktop\3115002455.txt', 'a') as prime_file:  # 以要求的格式将孪生素数写入文件

        for i in Twin_prime_list:
            print('%8d' % i, end=' ', file=prime_file)
            print_count += 1
            if (print_count % 8 == 0):
                print(end='\n', file=prime_file)

    prime_file.close()
    print("%d以内的孪生素数有%d对" % (n, Twin_prime_count))

    end = time.time()
    print("程序运行时间：%ss" % str(end - start))
