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


for i in range(500):
    n2 = bin(i)[2:]
    n2 += n2[-1]
    n2_d = bin(i)[2:]
    n2_d += n2_d[-1]
    n2 += "0" if n2.count("1") % 2 == 0 else "1"
    n2 += "1" if n2.count("1") % 2 == 0 else "0"
    n2_d += "01" if n2_d.count("1") % 2 == 0 else "11"
    r = int(n2, 2)
    if r > 553:
        print(f"n2 = {n2} n = {i}")
        print(f"n2_d = {n2_d} n = {i}")
        break
