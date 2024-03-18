'''
Напишите программу, которая считывает целое число n и вычисляет значение
выражения: n + nn + nnn

Sample Input 1:
5

Sample Output 1:
615
'''
n = int(input("введите число:"))
s = n + n*n + n*n*n
print(s)