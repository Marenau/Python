def main(x):
    match x[1]:
        case 1959:
            return 13
        case 1961:
            return 12
        case 1986:
            match x[3]:
                case 'SAGE':
                    return 11
                case 'CHUCK':
                    match x[0]:
                        case 1970:
                            return 10
                        case 2001:
                            return 9
                        case 1987:
                            match x[4]:
                                case 2010:
                                    return 8
                                case 1975:
                                    return 7
                case 'SCSS':
                    match x[2]:
                        case 'LASSO':
                            match x[0]:
                                case 1970:
                                    return 6
                                case 2001:
                                    return 5
                                case 1987:
                                    return 4
                        case 'EC':
                            return 3
                        case 'DM':
                            match x[0]:
                                case 1970:
                                    return 2
                                case 2001:
                                    return 1
                                case 1987:
                                    return 0

print(main([1987, 1959, 'DM', 'SAGE', 2010]))
print(main([1987, 1986, 'DM', 'SAGE', 2010]))
print(main([1987, 1986, 'EC', 'CHUCK', 2010]))
print(main([1970, 1961, 'LASSO', 'SAGE', 1975]))
print(main([1987, 1986, 'EC', 'CHUCK', 1975]))