lst = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200]
mid_lst = len(lst) // 2
lft = lst[mid_lst:]
lft_mirror = lst[:(mid_lst - 1): -1]
print(lft, lft_mirror)

my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res_1 = my_lst[:len(my_lst) // 2] + my_lst[len(my_lst) // 2::-1]
res_2 = my_lst[:len(my_lst) // 2], my_lst[len(my_lst) // 2::-1]
res_3 = my_lst[:len(my_lst) // 2], my_lst[len(my_lst) // 2 - 1::-1]
res_4 = my_lst[:len(my_lst) // 2], my_lst[:len(my_lst) // 2][::-1]
res_5 = my_lst[len(my_lst) // 2:][::-1] + my_lst[len(my_lst) // 2:]
print(my_lst)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
print(res_5)

left_lst = lambda lst_1: lst_1[:len(lst_1) // 2] + lst_1[:len(lst_1) // 2][::-1]
right_lst = lambda lst_1: lst_1[len(lst_1) // 2:][::-1] + lst_1[len(lst_1) // 2:]
imp = list(range(1,41))
print(left_lst(imp))
print(right_lst(imp))