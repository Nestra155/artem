'''
Напишите программу, которая проверяет, является ли данный вход четным или нечетным числом.

Sample Input 1:
2

Sample Output 1:
четное

Sample Input 2:
3

Sample Output 2:
нечетное
'''
number = int(input("введите число:"))

if number % 2 == 0:
    print("число чётное")
else:
    print("число не чётное")    