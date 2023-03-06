def main(x):
    match x[2]:
        case 2015:
            match x[0]:
                case 1961:
                    match x[1]:
                        case 'SMALI':
                            return 0
                        case 'ZIMPL':
                            return 1
                case 1978:
                    match x[1]:
                        case 'SMALI':
                            return 2
                        case 'ZIMPL':
                            return 3
                case 1998:
                    return 4
        case 1972:
            match x[0]:
                case 1961:
                    return 5
                case 1978:
                    match x[3]:
                        case 1979:
                            return 6
                        case 1966:
                            return 7
                        case 1998:
                            return 8
                case 1998:
                    return 9
        case 1968:
            return 10
        
print(main([1961, 'ZIMPL', 1968, 1966]))
print(main([1978, 'ZIMPL', 2015, 1979]))
print(main([1961, 'ZIMPL', 1972, 1966]))
print(main([1998, 'ZIMPL', 2015, 1979]))
print(main([1998, 'ZIMPL', 1972, 1966]))