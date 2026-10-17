# def task5_1(n):
#     for i in range(1, n + 1):
#         n2 = bin(i)[2:]
#         if n % 2 == 0:
#             n2 += "10"
#         else:
#             n2 += "01"
#         d = int(n2, 2)
#         if d > 200:
#             print(f"Число: {i}, после if: {n2}, d = {d}")
#             # return d
#
# task5_1(300)
# # print(task5_1(300))

# for n in range(1, 10000):
#     s = bin(n)[2:]
#     s += "00" if s.count("1") % 2 == 0 else "10"
#     r = int(s,2)
#
#     if r > 123:
#         print(r)
#         break


# for i in range(500):
#     n2 = bin(i)[2:]
#     n2 += n2[-1]
#     n2_d = bin(i)[2:]
#     n2_d += n2_d[-1]
#     n2 += "0" if n2.count("1") % 2 == 0 else "1"
#     n2 += "1" if n2.count("1") % 2 == 0 else "0"
#     n2_d += "01" if n2_d.count("1") % 2 == 0 else "11"
#     r = int(n2, 2)
#     if r > 553:
#         print(f"n2 = {n2} n = {i}")
#         print(f"n2_d = {n2_d} n = {i}")
#         break


# for n in range(1000):
#     n_2 = bin(n)[2:]
#     if n % 2 != 0:
#         n_2 += '0'
#     else:
#         n_2 = '1' + n_2
#     n_2 += '1' if n_2.count('1') % 2 == 0 else '0'
#     r = int(n_2, 2)
#     if r > 300:
#         print(f"r = {r}, n_2 = {n_2}, n = {n}")
#         break


# for n in range(1000):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 = '1' + n2 + '10'
#     else:
#         n2 = '11' + n2 + '0'
#     r = int(n2, 2)
#     if r > 130:
#         print(r, n)
#         break










# for n in range(1, 100):
#     n2 = bin(n)[2:]
#     if n % 2 == 0:
#         n2 = n2 + bin(n2.count("1"))[2:]
#     else:
#         n2 = f"1{n2}00"
#     r = int(n2, 2)
#     if r > 401:
#         print(n)
#         break











# for i in range(1, 1000):
#     i2 = bin(i)[2:]
#     for _ in range(3):
#         i2 += "1" if sum(map(int, str(int(i2, 2)))) % 2 != 0 else "0"
#     r = int(i2, 2)
#     if r > 1234:
#         print(r, i2)
#         break

#
# for n in range(1, 300):
#     n2 = bin(n)[2:]
#     for _ in range(3):
#         a = str(int(n2, 2))
#         s = 0
#         for l in a:
#             s = s + int(l)
#         if s % 2 == 0:
#             n2 += "0"
#         else:
#             n2 += "1"
#
#     r = int(n2, 2)
#     if r > 1234:
#         print(r)
#         break

def to10(n, i = 3):
    temp = ""
    while n > 0:
        temp += str(n % i)
        n //= i
    return temp[::-1]


for n in range(1, 1000):
    n3 = to10(n)
    if n % 3 == 0:
        n3 += n3[-3:]
    else:
        n3 += to10((n % 3) * 3)
    r = int(n3, 3)
    if r > 150:
        print(n)
        break
