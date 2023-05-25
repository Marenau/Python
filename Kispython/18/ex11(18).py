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
    def __init__(self, data, offset, order='<'):
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


def read_e(reader):
    e1 = reader.read(Types.int16)
    e2 = reader.read(Types.float)
    return dict(E1=e1, E2=e2)


def read_d(reader):
    d1 = reader.read(Types.uint8)
    d2 = reader.read(Types.uint8)
    d3 = reader.read(Types.uint32)
    return dict(D1=d1, D2=d2, D3=d3)


def read_c(reader):
    c1_size = reader.read(Types.uint32)
    c1_address = reader.read(Types.uint16)
    c1_reader = reader.jump_to(c1_address)
    c1 = [read_d(c1_reader) for _ in range(c1_size)]
    c2_size = reader.read(Types.uint32)
    c2_address = reader.read(Types.uint32)
    c2_reader = reader.jump_to(c2_address)
    c2 = [c2_reader.read(Types.uint8) for _ in range(c2_size)]
    c3 = reader.read(Types.uint64)
    c4 = reader.read(Types.double)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4)


def read_b(reader):
    b1 = read_c(reader)
    b2_size = reader.read(Types.uint16)
    b2_address = reader.read(Types.uint32)
    b2_reader = reader.jump_to(b2_address)
    b2 = [b2_reader.read(Types.uint32) for _ in range(b2_size)]
    b3_size = reader.read(Types.uint16)
    b3_address = reader.read(Types.uint16)
    b3_reader = reader.jump_to(b3_address)
    b3 = [b3_reader.read(Types.uint64) for _ in range(b3_size)]
    b4_address = reader.read(Types.uint32)
    b4_reader = reader.jump_to(b4_address)
    b4 = read_e(b4_reader)
    b5 = reader.read(Types.uint8)
    b6 = reader.read(Types.int64)
    b7 = reader.read(Types.double)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7)


def read_a(reader):
    a1 = read_b(reader)
    a2 = reader.read(Types.uint64)
    a3 = reader.read(Types.int16)
    a4 = reader.read(Types.int16)
    a5 = [reader.read(Types.int16) for _ in range(2)]
    a6 = reader.read(Types.uint32)
    a7 = reader.read(Types.uint16)
    a8 = reader.read(Types.int8)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8)


def main(data):
    return read_a(BinaryReader(data, 3))



data = (b'UXC\x02\x00\x00\x00W\x00\x03\x00\x00\x00c\x00\x00\x00\xcb?\x94;\xf0\x93]'
 b'\xee\xa4\xc3\xb5F\xedE\xef\xbf\x02\x00f\x00\x00\x00\x02\x00n\x00~'
 b"\x00\x00\x00Ul'\xc7\x1c\xba\xfb<-\xbaMo_\x98\x02\xef\xbf\x1ez_\xf6p8\xfd>"
 b'L)\xa3\xb3\x81T\x81\xaf\xa6\x9c\x96\xbd\x1a7]a:A\xf1A\x99Y\x1d\x14'
 b'\xa4\x8a\xce\x83N\xe2\x11*\x0fG\x18%\x8b4\xd7\x102\xf3m\x8eV\xe8\x12\x93'
 b'l\xe5M\xe5\x13\xdd\x00_\xce|\xd8>')

print(main(data))

data = (b'UXC\x03\x00\x00\x00W\x00\x02\x00\x00\x00i\x00\x00\x00\xa6\x8c\xc1'
 b'\x1d\xf1\xbaY\xab\x14\xa6B4\xd2\xc5\xd2?\x02\x00k\x00\x00\x00\x02'
 b'\x00s\x00\x83\x00\x00\x00\x8cMS\xec/\xa6(\xd67\xdc\x08\xfb#Wt\xe6?1\xde_\xab'
 b'\x93[F\xc0\x0f\x81\x12\x86k\xe5\xb3\xcb\xc6\x02\xa0O\xb7D\xa8\xc1'
 b'\xbb\xf8\xbb\xdd\xa5\xa9:\x07y\xf2\xa8\xb1\xcbEJ@\x177\x8f\xd6\x1dQb\x1b'
 b'\xe9\xb8\xaeH\x8f\xe5\xcd\xbb=\xeag\xb2FW\xa5\xa2Sz~K\xcaj\xe0\x1b?')

print(main(data))