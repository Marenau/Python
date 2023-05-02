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
    d1 = [reader.read(Types.int16) for _ in range(2)]
    d2 = reader.read(Types.uint8)
    d3 = reader.read(Types.int8)
    d4 = reader.read(Types.uint16)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4)


def read_c(reader):
    c1 = reader.read(Types.uint32)
    c2 = reader.read(Types.int8)
    c3_size = reader.read(Types.uint16)
    c3_address = reader.read(Types.uint16)
    c3_reader = reader.jump_to(c3_address)
    c3 = [c3_reader.read(Types.int64) for _ in range(c3_size)]
    c4 = reader.read(Types.uint32)
    c5 = reader.read(Types.uint32)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5)


def read_b(reader):
    b1 = reader.read(Types.uint8)
    b2 = reader.read(Types.uint8)
    b3_size = reader.read(Types.uint16)
    b3_address = reader.read(Types.uint32)
    b3_reader = reader.jump_to(b3_address)
    b3 = [b3_reader.read(Types.uint16) for _ in range(b3_size)]
    return dict(B1=b1, B2=b2, B3=b3)


def read_a(reader):
    a1 = reader.read(Types.uint64)
    a2 = reader.read(Types.uint64)
    a3 = b''.join([reader.read(Types.char) for _ in range(8)]).decode()
    a4_addresses = [reader.read(Types.uint16) for _ in range(2)]
    a4 = [read_b(reader.jump_to(a4_addresses[i])) for i in range(2)]
    a5 = read_c(reader.jump_to(reader.read(Types.uint32)))
    a6 = read_d(reader)
    a7 = reader.read(Types.uint32)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)


def main(data):
    return read_a(BinaryReader(data, 4))


data = (b'ROEQ\xe1\x1c\xef\xdct\x0c\x9d\x99>\xb0J`\xedw\x87\xc9uwnaquuh\x00:\x00H'
 b'\x00\x00\x00`\x0b\xc9\x1c/Q<\xc34\xa9\xf1\x8b\xba\xff|=\x0f9\xb8p\xcd'
 b'i\xc3^\xfc\x00\x05\x00\x00\x000\xd3\x83\xb9\x19\xdf\xffM6\x00\x03'
 b'\x00\x00\x00BYO\x84g\xfev\xc2i!\xf6\x9b=\x18\xc3\xb0\xeemRs\xbd|\x00\x02\x00'
 b'PmgQ\xe5\xa7\xf2\x9cC')

print(main(data))

data = (b'ROEQ\x89\xa4\xed\x11\x90mt[1W&\xd4uY\x16pegqnchyv\x00@\x00T\x00\x00\x00l'
 b'\xbb\xd7|W\xebx\xb8x\xb3g\xce\x8eR\xcc\xc4\x8d\x01\x03\x9cj\t\xe1\xb3\xae'
 b't;\xf7\x9e\xb6\xc8\x00\x08\x00\x00\x000\x98\xcf\xf1\xd5\xe6Nh\xb9'
 b'\x9a\xefh\x99\xae#\x00\x06\x00\x00\x00H7\xdf\xf1\xf1\x97\x9d+\xe0'
 b'\x1c\xcc\x93u\xb5\x08\xba\xecV1"\x8b\x87\x00\x02\x00\\\x1c\x13\xbd\'0\x08u'
 b'\xe0')

print(main(data))
