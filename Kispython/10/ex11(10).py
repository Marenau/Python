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


def read_f(reader):
    f1 = reader.read(Types.int32)
    f2 = [reader.read(Types.uint32) for _ in range(2)]
    return dict(F1=f1, F2=f2)


def read_e(reader):
    e1 = reader.read(Types.float)
    e2 = reader.read(Types.uint32)
    return dict(E1=e1, E2=e2)


def read_d(reader):
    d1 = reader.read(Types.uint16)
    d2 = reader.read(Types.int16)
    d3 = reader.read(Types.int16)
    d4 = reader.read(Types.int8)
    d5 = reader.read(Types.float)
    d6 = read_e(reader)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6)


def read_c(reader):
    c1 = reader.read(Types.uint8)
    c2 = reader.read(Types.uint32)
    c3 = reader.read(Types.int64)
    c4 = reader.read(Types.float)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4)


def read_b(reader):
    b1 = reader.read(Types.int32)
    b2 = reader.read(Types.double)
    b3 = reader.read(Types.int16)
    b4 = reader.read(Types.int32)
    b5 = b''.join([reader.read(Types.char) for _ in range(2)]).decode()
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5)


def read_a(reader):
    a1 = read_b(reader.jump_to(reader.read(Types.uint32)))
    a2 = b''.join([reader.read(Types.char) for _ in range(7)]).decode()
    a3 = read_c(reader)
    a4 = read_d(reader)
    a5 = reader.read(Types.uint16)
    a6_size = reader.read(Types.uint32)
    a6_address = reader.read(Types.uint32)
    a6_reader = reader.jump_to(a6_address)
    a6 = [read_f(a6_reader) for _ in range(a6_size)]
    a7_size = reader.read(Types.uint16)
    a7_address = reader.read(Types.uint32)
    a7_reader = reader.jump_to(a7_address)
    a7 = [a7_reader.read(Types.float) for _ in range(a7_size)]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)


def main(data):
    return read_a(BinaryReader(data, 5))


data = (b'\xc0NTFF\x00\x00\x00Drwllkbr6\x00\x07\xdeeW\x8aUj\xeb\x17\xdd\xaa\xbe\xca.'
 b'\xa5\xdb&\xecg$\x08j>\xdfB\xf4=x\x15\x03g\xb9\x0f5-o\x00\x00\x00\x03\x00\x00'
 b'\x00X\x00\x02\x00\x00\x00|\xfd\xdd\nV\xbf\xed\x944\x0e=\x0bJ]\xbfL).\xc9hq'
 b'T_\x8b\x9e\xe8\xb7Tn\xc1\xb3p\xe9\x19\xe8\xd0\x05\xfec\xfc71\xa0"\xec'
 b'\x81I\xb8\xd2\x1dFN\x88\x81JLw\xbfc7\x05>\x0b\x14^')

print(main(data))

data = (b'\xc0NTFF\x00\x00\x00Dwvxtuyr\\.\xce9\xaa\x1f\xa5#\x81QZ9\x13\xbf\x05\xc5'
 b'\x0bPRu\x8c\x8fU\xf5\xbd\xfa\xc60\xbd=\xf7\x87\xd6\xad\x90\xd9eu\x00\x00'
 b'\x00\x02\x00\x00\x00X\x00\x04\x00\x00\x00p\xc9\xfe\xb2\x7f\xbf\xe6\xbeQ'
 b'\xbd\xbc\xbaJZ\x90\n\xd9\xe2\xb2pp\x14eNz:\x1f\x15\xb5"\x05\xcfm'
 b'\xf1\x7f\xe0n\x96\xa07\xbf\xe4\x94\x80\xde\xbe\xbe\x08c>i\xab\xc8'
 b'\xbf.\xca\xe7\xbe\xf6\x81?')

print(main(data))
