def main(s):
    i = int(s, 16)
    o1 = 0b1 & i
    o3 = 0b11111 & (i >> 5)
    o4 = 0b111 & (i >> 10)
    result = [('O1', o1), ('O3', o3), ('O4', o4)]
    return result

print(main('0x194b'))
print(main('0x13d7'))
print(main('0x369'))
print(main('0x8de'))