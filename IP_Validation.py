'''
Нужно написать алгоритм для проверки IPv4 адреса в десятичном формате.
IP-адреса следует считать если она состоит из 4-х октетов со значениями от 0 до 255 включительно
'''
def is_valid_IP(strng):
    #Эта строка записывает вводные значения в список OCTETS с разделяющей строкой в виде точки
    octets = strng.split(".")
    # Если длина одного октета неравна 4 то выводим FALSE
    if len(octets) != 4: return False
    # цикл
    for octet in octets:
        #Если условие второй функции не соблюдается то результат False иначе True
        if not is_valid_octet(octet): return False
    return True

def is_valid_octet(octet):
    #Если в списке есть Буквы то возвращаем False
    if not octet.isdigit(): return False
    # Если длина больше одного и первое число равно 0 то возвращаем False
    if len(octet) > 1 and octet[0] == "0": return False
    # Переводим значение на целочисленное значение
    octet = int(octet)
    # Если значение больше или равно 0 и  значение меньше или равно 255 возвращаем True
    if octet >= 0 and octet <= 255: return True
    else: return False

print(is_valid_IP("192.2222.0.2"))