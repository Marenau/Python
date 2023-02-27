def main(x):
    match x[3]:
        case 'HYPHY':
            match x[2]:
                case 1989:
                    match x[1]:
                        case 'MUF':
                            return 0
                        case 'VUE':
                            return 1
                case 1977:
                    match x[0]:
                        case 1964:
                            return 2
                        case 2010:
                            return 3
        case 'C':
            match x[1]:
                case 'MUF':
                    match x[2]:
                        case 1989:
                            return 4
                        case 1977:
                            return 5
                case 'VUE':
                    return 6
        case 'FREGE':
            match x[1]:
                case 'MUF':
                    match x[0]:
                        case 1964:
                            return 7
                        case 2010:
                            return 8
                case 'VUE':
                    match x[2]:
                        case 1989:
                            return 9
                        case 1977:
                            return 10

print(main([2010, 'VUE', 1989, 'FREGE']))
print(main([1964, 'VUE', 1989, 'C']))
print(main([1964, 'VUE', 1977, 'HYPHY']))
print(main([2010, 'VUE', 1977, 'FREGE']))
print(main([2010, 'MUF', 1989, 'FREGE']))