
array = list(map(int, input("Введите числа в любом порядке через пробел: ").split()))
#array = list(set(array)) #если нужно удаление дублей
element = int(input("Введите любое положительное число из списка: "))

for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
            return False
    middle = (right + left) // 2
    if element == array[middle]:
        if array[middle - 1] < element:  # если элемент в середине,
            return [middle - 1]
        elif element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
    elif element == array[middle - 1]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)

left = int(array[0])
right = (array[-1])
if element < left or element > right:
    print("Число вне диапазона")
elif element not in array:
    print("Элемент отсутствует в списке")
else:
    print(binary_search(array, element, 0, len(array) - 1))
print(array)


