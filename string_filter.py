def get_result_array_size(input_array):
    """
    Функция для определения размера результирующего массива.
    Подсчитывает количество строк, длина которых меньше или равна 3.
    """
    size = 0
    for string in input_array:
        if len(string) <= 3:
            size += 1
    return size

def create_filtered_array(input_array):
    """
    Основная функция для создания нового массива.
    Формирует массив из строк, длина которых меньше или равна 3 символам.
    """
    # Получаем размер нового массива
    result_size = get_result_array_size(input_array)
    
    # Создаем новый массив нужного размера
    result_array = [None] * result_size
    
    # Индекс для отслеживания позиции в новом массиве
    result_index = 0
    
    # Перебираем все строки исходного массива
    for string in input_array:
        # Если длина строки подходит под условие
        if len(string) <= 3:
            # Добавляем строку в новый массив
            result_array[result_index] = string
            result_index += 1
            
    return result_array

def print_array(array):
    """
    Функция для красивого вывода массива в консоль.
    Выводит массив в формате, указанном в задании.
    """
    print('[', end='')
    for i in range(len(array)):
        print(f'"{array[i]}"', end='')
        if i < len(array) - 1:
            print(', ', end='')
    print(']')

def main():
    # Тестовые примеры из задания
    test_arrays = [
        ["Hello", "2", "world", ":-)"],
        ["1234", "1567", "-2", "computer science"],
        ["Russia", "Denmark", "Kazan"]
    ]
    
    # Проверяем на всех тестовых примерах
    for array in test_arrays:
        print("\nИсходный массив:", end=' ')
        print_array(array)
        
        result = create_filtered_array(array)
        print("Новый массив:", end=' ')
        print_array(result)

if __name__ == "__main__":
    main()
