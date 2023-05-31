from struct import unpack_from, calcsize


class Types:
    uint16 = 'H'
    int16 = 'h'
    char = 'c'
    float = 'f'
    int8 = 'b'
    int64 = 'q'
    uint64 = 'Q'
    uint32 = 'I'
    int32 = 'i'
    double = 'd'
    uint8 = 'B'


class BinaryReader:
    def __init__(self, data, offset, order='>'):
        self.data = data
        self.offset = offset
        self.order = order
    def jump_to(self, offset):
        reader = BinaryReader(self.data, offset, self.order)
        return reader
    def read(self, frmt):
        data = unpack_from(self.order + frmt, self.data, self.offset)
        self.offset += calcsize(frmt)
        return data[0]


def read_d(reader):
    d1 = reader.read(Types.int32)
    d2 = reader.read(Types.uint64)
    return dict(D1=d1, D2=d2)


def read_c(reader):
    c1 = reader.read(Types.double)
    c2_size = reader.read(Types.uint16)
    c2_address = reader.read(Types.uint16)
    c2_reader = reader.jump_to(c2_address)
    c2 = b''.join([c2_reader.read(Types.char) for _ in range(c2_size)]).decode()
    return dict(C1=c1, C2=c2)


def read_b(reader):
    b1 = reader.read(Types.uint16)
    b2 = reader.read(Types.int8)
    return dict(B1=b1, B2=b2)


def read_a(reader):
    a1 = reader.read(Types.double)
    a2 = reader.read(Types.int32)
    a3 = read_b(reader)
    a4 = reader.read(Types.uint8)
    a5_size = reader.read(Types.uint16)
    a5_address = reader.read(Types.uint16)
    a5_reader = reader.jump_to(a5_address)
    a5_adresses = [a5_reader.read(Types.uint16) for _ in range(a5_size)]
    a5 = []
    for i in a5_adresses:
        a5.append(read_c(reader.jump_to(i)))
    a6_size = 6
    a6_addresses = [reader.read(Types.uint16) for _ in range(a6_size)]
    a6 = []
    for i in a6_addresses:
        a6.append(read_d(reader.jump_to(i)))
    a7_size = reader.read(Types.uint32)
    a7_address = reader.read(Types.uint32)
    a7_reader = reader.jump_to(a7_address)
    a7 = [a7_reader.read(Types.uint8) for _ in range(a7_size)]
    a8 = reader.read(Types.uint32)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8)


def main(data):
    return read_a(BinaryReader(data, 4))



data = (b'WJJ?\xbf\xe5\x8b\x97,/\xb0\x8c\xa5\xb4\x93,\xc6\x0c\xc8w\x00\x05\x00y'
 b'\x00\x83\x00\x8f\x00\x9b\x00\xa7\x00\xb3\x00\xbf\x00\x00\x00\x03'
 b'\x00\x00\x00\xcb\x0c\x14\x9f3uww?\xc8\x12\xf5\x8a\xf5b\xb0\x00\x03\x000y'
 b'q?\xd9\x8d\x96\x1c!=\xb0\x00\x02\x00?wdy?\xcbp\xe9\xce\xfa\x02`\x00\x03\x00M'
 b"cgz\xbf\xe3\xdcC\xef\xa6+H\x00\x03\x00\\as?\xec\xac\xb0\x81\x0b'"
 b'\xe4\x00\x02\x00k\x003\x00A\x00P\x00_\x00m\xe5\x1b\xb83\xf2\xba\x08\r8'
 b'\xc8\xdd9j1q0!X\xa6\xf4p\xc40y\xe2\xec\xecZ\xf7\xd3\x07\xbd\x81'
 b'\x9e\xb4\x84\xb0w\x9e\x0f\x06#\x16\xdf\x18_(a\x99\x8f3[\xcc\x12+\xe3\xc4'
 b'\xcc\xb0\xff\x03\xde\xfa\xb2\x18f\x98j\xb5\x97\xf4\x81\xa6\x8b\xb1')

print(main(data))