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
    d3 = [reader.read(Types.double) for _ in range(4)]
    d4 = reader.read(Types.int8)
    d5 = reader.read(Types.int16)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5)


def read_c(reader):
    c1 = reader.read(Types.uint8)
    c2_size = reader.read(Types.uint16)
    c2_address = reader.read(Types.uint16)
    c2_reader = reader.jump_to(c2_address)
    c2 = [c2_reader.read(Types.uint16) for _ in range(c2_size)]
    c3_address = reader.read(Types.uint32)
    c3 = read_d(reader.jump_to(c3_address))
    return dict(C1=c1, C2=c2, C3=c3)


def read_b(reader):
    b1 = b''.join([reader.read(Types.char) for _ in range(2)]).decode()
    b2 = reader.read(Types.float)
    return dict(B1=b1, B2=b2)


def read_a(reader):
    a1 = reader.read(Types.uint8)
    a2 = reader.read(Types.int64)
    a3 = [read_b(reader) for _ in range(7)]
    a4 = read_c(reader)
    a5 = reader.read(Types.float)
    a6 = reader.read(Types.uint16)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6)


def main(data):
    return read_a(BinaryReader(data, 5))



data = (b'NPPJ\x14\x13p\xf3b\x18~oqSek<\xb1?8yj?\r \x80ff?J\xba%nc>)\x896fm'
        b'=\x03\xe1\x90tc>p \x10rk\xbfQ&H\xd6\x00\x04\x00G\x00\x00\x00O\xbe\xe9\xeb'
        b'\xa8\xf1(\xf6\xc6\xb4\xf4]\\\xae\xee\xe6\x9aMp0\x00\xbf\x03\xb0\xee\x95E?'
        b'\xe6<\xaa?j_\x94?\xee\x00\xde\x9b\x8a\xfd\x82?\xeap*\x99\x05\xd4R?'
        b'\xad\x04i\xa1\x04\x90\x80\xdf-&')

print(main(data))

data = (b'NPPJ\x14\x12\x13\xb7\x82]\x10\x8b\xea.ie\xbe\xda\xb7mbq\xbe\x08\xfc-en'
        b'\xbf\rp\x87rf\xbeEU\xf9zw?\x19l_oj\xbd\xd5}\x9bfs\xbf/G\xbfs\x00\x07\x00'
        b'G\x00\x00\x00U\xbfu\x94\x95\x12\xeb`\x1a\t"\xf6V,\xeb\xb8\x85J\xd9\x06'
        b'|\xfa\\\xebp\x0e%\x7f\xd3(\x12\xd7\x17\xbf|\x0c\x96\xf2\xe7=\x00\xbf\xec\xb3'
        b'\r*\xb5\xd54?\xe2%[\xb4\x1f%\xca\xbf\xe7\xa9\x1f1\x1a\xdcv\x9b\xf7x')

print(main(data))
