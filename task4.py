'''
Напишите программу, которая вычисляет площадь круга с заданным пользователем 
радиусом.

Sample Input 1:
1.1

Sample Output 1:
3.8013271108436504
'''
radius = float(input("Введите радиус круга: "))

area = 3.14 * radius**2

print(area)