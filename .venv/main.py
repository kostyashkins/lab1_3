def bubble_sort(arr, ascending=True):
    """
    Функция для сортировки массива пузырьком.
    :param arr: Массив чисел.
    :param ascending: Если True, сортировка по возрастанию, иначе по убыванию.
    :return: Отсортированный массив.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1] and ascending) or (arr[j] < arr[j + 1] and not ascending):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    # Ввод чисел от пользователя
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    # Запрос направления сортировки
    order = input("Введите направление сортировки (возрастание/убывание): ").strip().lower()
    ascending = order == "возрастание"

    # Сортировка
    sorted_numbers = bubble_sort(numbers.copy(), ascending=ascending)
    print("Отсортированный массив:", sorted_numbers)