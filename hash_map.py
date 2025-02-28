storage = {}

hash_func = len

def put(key: str, value: int) -> None:
    hash_ = hash_func(key)
    storage.setdefault(hash_, []).append((key, value))

def get(key: str) -> tuple:
    for i in storage.get(hash_func(key)): # не знаю насколько корректно использовать тут функцию get... но это для благих целей и быстрого поиска
        if i[0] == key:                   # один цикл, который ищет по всем коллизиям ключа, так что сложность O(n), где n - глубина коллизии ключа
            return i
    
                
put('Nissan', 'Skyline R34')
put('Лаадаа', 'Калина')
put('BMW', 'E34')

nissan = get('Nissan')
toyota = get('Toyota')

print(f'Ищем ниссан: {nissan}')
print(f'Ищем не существующую тойоту: {toyota}')
