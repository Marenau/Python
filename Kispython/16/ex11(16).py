import struct


def main(data):
    signature = struct.unpack('<5B', data[:5])
    if signature != (0x54, 0x57, 0x51, 0x52, 0xf2):
        raise ValueError("Invalid signature")

    a_b_address, a_2, e_1, e_2, a_f_address = struct.unpack('<H B b Q H',
                                                            data[5:19])

    b_1 = [{'C1': c[0], 'C2': c[1], 'C3': c[2]} for c in
           struct.iter_unpack('<q l d', data[a_b_address:a_b_address + 60])]
    b_size, b_address = struct.unpack('<L L',
                                      data[a_b_address + 60: a_b_address + 68])
    b_2 = data[b_address: b_address + b_size].decode()
    b_3, b_4, b_5, b_6, b_d_address = \
        struct.unpack('<Q Q B f H', data[a_b_address + 68: a_b_address + 91])

    d_size = struct.unpack('<L', data[b_d_address: b_d_address + 4])[0]
    d_address = struct.unpack('<H', data[b_d_address + 4: b_d_address + 6])[0]
    d_1 = [
        struct.unpack('<l', data[d_address + i * 4: d_address + (i + 1) * 4])[
            0] for i in range(d_size)]
    d_2 = list(struct.unpack('<7B', data[b_d_address + 6: b_d_address + 13]))
    b_d_address += 13
    d_3, d_4, d_5, d_6 = struct.unpack('<i H i b',
                                       data[b_d_address: b_d_address + 11])

    f_1, f_2 = struct.unpack('<b B', data[a_f_address: a_f_address + 9])

    d = {'D1': d_1, 'D2': d_2, 'D3': d_3, 'D4': d_4, 'D5': d_5, 'D6': d_6}
    b = {'B1': b_1, 'B2': b_2, 'B3': b_3, 'B4': b_4, 'B5': b_5, 'B6': b_6,
         'B7': d}
    f = {'F1': f_1, 'F2': f_2}

    return {'A1': b, 'A2': a_2, 'A3': {'E1': e_1, 'E2': e_2}, 'A4': f}


data = (b'TWQR\xf25\x00\xdfnr1\\F\x11<\xdb`\x90\x00yt\xd77g\x18\xf4\x0f\xbe'
        b'\x0c\x02\x00\x00\x00\x15\x00{\xc1\x16\x8a\xeb\xa2{\xc1\x98\xaed\xd4yd\x99E;'
        b'\xf6y\xcf\xae\xf0\x17g\xd1\rT\xe7@\xbb\xac\xe3\x90\xf6\xaeI\xdf\xbfY\x18\x17'
        b"\xf6H\xc0\x8d\x06\xc9|\xe2\xcfX'\x1c\xf3;N\xef\xbf\xac!I\xf2\xe7\x96~"
        b'\xeb\x9d\x11\x0c\xa6FO2\x0f\x85.\xec\xbf\x02\x00\x00\x00\x13\x00\x00'
        b'\x00(\xd0\x92\x90u\x9c[\xc6w\xf1CZs\xf2\x00\xc6\x86\xd5\x8c%\xbe\x1d\x00'
        b'\xd8\xa2')

print(main(data))

data = (b'TWQR\xf29\x00^=\xc51\xe1\x0e\xc38vr\x94\x00zo\xa0\x01\x11\xd9\x8ed7'
        b'W\x90\n\xf6\xbb\x03\x00\x00\x00\x15\x008_\x0e\x7f\x17>~t$\xfa\xab\xca\x9b'
        b'w\x0bgb\x82XD\x17S\xc68d\x7f=\x7f\xffJ\x86U\x0e\x7f\xe7\x87\xe1\xbf5\x91\x88'
        b'Ao\x1ez1q;\xa4\xbe"R`\x9a\x92\x0c\xeb?\\uo\x94#s\r\x0c\x8f\xbfQ]H\xcb\x19'
        b'j-+\xcd\xbf\x02\x00\x00\x00\x13\x00\x00\x00\x89IvU\xa2\x15\x92bp:\x87'
        b'\xea$\x8b+\xeb\xbf\xa0\x8eD?!\x00\x1e\x8f')

print(main(data))
