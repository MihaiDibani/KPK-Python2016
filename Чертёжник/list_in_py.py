A = [1,2,3]
B = [4,5]
C = A + B
D = B + A
print('C =',C)

# ГЕНЕРАТОРЫ СПИСКОВ

A = list(range(1,11))

print('A =',A)
B = [x*x for x in A]  # for x in A:
                      #     B.append(x*x)
print('B =',B)
# A.append(5) - добавили в конце списка А элемент 5
# A.pop() - удалить последний элемент списка А
# x = A.pop() - удалить последний элемент списка А и этот элемент записать в х

C = [x for x in B if x % 10 == 6]
# выбрать из списка B элементы оканчивающихся на 6 и создать из них новый список С
# % - остаток от деления
# // - целая часть от деления
print('C =',C)


# СРЕЗЫ СПИСКОВ  A[start:stop:step]

#     0   1   2   3   4
A = [ 0,  1,  2,  3,  4]
#    -5  -4  -3  -2  -1

print(A[-4])    # 1
print(A[5])     # IndexError: list index out of range

print(A[1:3])   # [1, 2]
print(A[1:-1])  # [1, 2, 3]
print(A[3:2])   # []
print(A[2:1000])# [2, 3, 4]
print(A[30:200])# []

print(A[1:5:2]) # [1, 3]

A[1:3] = [10,20]
print(A)        # [0, 10, 20, 3, 4]
A[1:3] = [6,7,8]
print(A)        # [0, 6, 7, 8, 3, 4]
A[1:3] = []
print(A)        # [0, 3, 4]

B = list(range(100))
print(B[::-2])
B = B[::-1]      # обращение списка, то же что и B.reverse() при этом удаляется старый объект сборщиком мусора
B[:] = B[::-1]   # в старом объекте меняются элементы с помощью создания нового объекта, сборщик съедает новый объект
