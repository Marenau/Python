def main(x):
    int_x = int(x)
    W2 = (int_x >> 1) & 0b111
    W3 = (int_x >> 4) & 0b111
    W4 = int_x >> 7
    return [('W2', str(W2)),
            ('W3', str(W3)),
            ('W4', str(W4))]
    
print(main('724'))
print(main('888'))
print(main('295'))
print(main('168'))