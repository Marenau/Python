# Ничего не работает

import struct


def main(data):
    signature = struct.unpack('<5B', data[:5])
    if signature != (0x4e, 0x50, 0x50, 0x4a, 0x14):
        raise ValueError("Invalid signature")

    A = {}
    A['A1'] = struct.unpack('B', data[5:6])[0]
    A['A2'] = struct.unpack('q', data[6:14])[0]
    
    A['A3'] = []
    for i in range(7):
        B = {}
        B['B1'] = struct.unpack('2s', data[14+i*6:16+i*6])[0]
        B['B1'] = B['B1'].decode()
        B['B2'] = struct.unpack('f', data[16+i*6:20+i*6])[0]
        A['A3'].append(B)
    
    A['A4'] = {}
    A['A4']['C1'] = struct.unpack('B', data[56:57])[0]
    C_size = struct.unpack('H', data[57:59])[0]
    C_addr = struct.unpack('H', data[59:61])[0]
    C_D_addr = struct.unpack('I', data[61:65])[0]
    A['A4']['C2'] = []
    for i in range(C_size):
        A['A4']['C2'].append(struct.unpack('H', data[C_addr+i*2:C_addr+(i+1)*2])[0])
    
    D = {}
    D1, D2 = struct.unpack('iQ', data[C_D_addr+1:C_D_addr+13])
    D['D1'], D['D2'] = D1, D2
    D['D3'] = []
    for i in range(4):
        D['D3'].append(struct.unpack('d', data[C_D_addr+13+i*8:C_D_addr+13*(i+1)*8])[0])
    D['D4'] = struct.unpack('b', data[C_D_addr+45:C_D_addr+46])[0]
    D['D5'] = struct.unpack('h', data[C_D_addr+46:C_D_addr+48])[0]
    
    A['A5'], A['A6'] = struct.unpack('>fH', data[65:71])

    return А


data = (b'NPPJ\x14\x13p\xf3b\x18~oqSek<\xb1?8yj?\r \x80ff?J\xba%nc>)\x896fm'
        b'=\x03\xe1\x90tc>p \x10rk\xbfQ&H\xd6\x00\x04\x00G\x00\x00\x00O\xbe\xe9\xeb'
        b'\xa8\xf1(\xf6\xc6\xb4\xf4]\\\xae\xee\xe6\x9aMp0\x00\xbf\x03\xb0\xee\x95E?'
        b'\xe6<\xaa?j_\x94?\xee\x00\xde\x9b\x8a\xfd\x82?\xeap*\x99\x05\xd4R?'
        b'\xad\x04i\xa1\x04\x90\x80\xdf-&')

print(main(data))

# data = (b'NPPJ\x14\x12\x13\xb7\x82]\x10\x8b\xea.ie\xbe\xda\xb7mbq\xbe\x08\xfc-en'
#         b'\xbf\rp\x87rf\xbeEU\xf9zw?\x19l_oj\xbd\xd5}\x9bfs\xbf/G\xbfs\x00\x07\x00'
#         b'G\x00\x00\x00U\xbfu\x94\x95\x12\xeb`\x1a\t"\xf6V,\xeb\xb8\x85J\xd9\x06'
#         b'|\xfa\\\xebp\x0e%\x7f\xd3(\x12\xd7\x17\xbf|\x0c\x96\xf2\xe7=\x00\xbf\xec\xb3'
#         b'\r*\xb5\xd54?\xe2%[\xb4\x1f%\xca\xbf\xe7\xa9\x1f1\x1a\xdcv\x9b\xf7x')

# print(main(data))
