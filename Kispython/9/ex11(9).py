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


def read_d(reader):
    d1 = [reader.read(Types.uint32) for _ in range(4)]
    d2 = reader.read(Types.double)
    return dict(D1=d1, D2=d2)

def read_c(reader):
    c1 = reader.read(Types.uint64)
    c2 = reader.read(Types.uint64)
    c3 = [reader.read(Types.int8) for _ in range(2)]
    c4 = reader.read(Types.float)
    c5 = [reader.read(Types.uint16) for _ in range(8)]
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5)


def read_b(reader):
    b1 = read_c(reader.jump_to(reader.read(Types.uint16)))
    b2 = reader.read(Types.uint16)
    b3 = reader.read(Types.int16)
    b4 = reader.read(Types.uint16)
    b5 = read_d(reader.jump_to(reader.read(Types.uint32)))
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5)


def read_a(reader):
    a_size = reader.read(Types.uint32)
    a_address = reader.read(Types.uint32)
    a_reader = reader.jump_to(a_address)
    arr = [a_reader.read(Types.uint32) for _ in range(a_size)]
    a1 = [read_b(reader.jump_to(arr[i])) for i in range(len(arr))]
    a2 = reader.read(Types.uint8)
    a3 = reader.read(Types.int16)
    return dict(A1=a1, A2=a2, A3=a3)


def main(data):
    return read_a(BinaryReader(data, 5))


data = (b'CDBM\xff\x02\x00\x00\x00\xa4\x00\x00\x00x\x02\x9d\x16\xbfy\x8c<+\xb42'
 b'\x14R\x0c\x06\x87\xb8N\x14\xab\x01\x07Q\x05\xbe\xc96\x14\x99\xf9/'
 b'\xc8\t\xce\xdbC6A\x83\xa8i|FY\xc7\xef5\xe6=-\xf8\xf7[h\xd2\xa0\x85\x0c)'
 b'\xfc:D4\xe3\xbf\x10\x003\r\xb7\x01\x1e\x886\x00\x00\x00\xdao>MaP'
 b'\x98\xfd\xc1fi\x03\x9c\xfc\xa0G\xf7l\xf7X[=\x81\x14\xb0\xacN\x03\xd4\xe7'
 b'\xfa\xc51\xfd}+\x96\x88\xdd\xa3\x1b\xc6\xcb\x80-\xa9\x90\t\x8e\x9fp\x02\xa2D'
 b'\x00\x0b\xcd%CH\x85?Z\x00=\xd1\x92\x84\xa2\x99\x80\x00\x00\x00N\x00\x00\x00'
 b'\x98\x00\x00\x00')

print(main(data))

data = (b'CDBM\xff\x02\x00\x00\x00\xa4\x00\x00\x00y\x10\x15\xc8\xab5p\xaf\x89\xe8W'
 b'g\x0f\x80\x90\x80].\xd5q\xbf\xfd\xbc\x85\xbb\xe3\xc4\xf0\x03\x98\xc7'
 b'{\xed\xe5)*\xad\xf4\xc5\xbb}.C*\xc2_\xc9-\xe6~\x87\x13d\x8ct\x84\x1e\x00L'
 b'Q=K\xf5\xc2?\x10\x00bx\xc1;\x1ev6\x00\x00\x00<xM\xc3X\x85\xe2Y*e'
 b'\x9f\xa8\xd3aa\x0f\x06\xc1\xed\xf8\x01\xbf\xeeP\xf9t\xbcY\xdbFD\x96dV'
 b'%\xf8\xd9\x95!`\xdb\xc5)\x8c\xad\xa3W\xd5\x19\xdfQ\x1b\xe7z\xa0<\xae\x7f'
 b'd\xd0\xd1?Z\x00\x99\x95\xc4\xd4c\xb5\x80\x00\x00\x00N\x00\x00\x00'
 b'\x98\x00\x00\x00')

print(main(data))
