def main(x):
    match x[1]:
        case 'SELF':
            match x[2]:
                case 'WISP':
                    match x[0]:
                        case 'SWIFT':
                            match x[3]:
                                case 'VOLT':
                                    return 0
                                case 'NSIS':
                                    return 1
                        case 'YACC':
                            match x[4]:
                                case 'GLSL':
                                    return 2
                                case 'PIC':
                                    return 3
                                case 'GOLO':
                                    return 4
                        case 'COOL':
                            return 5
                case 'PHP':
                    match x[4]:
                        case 'GLSL':
                            match x[3]:
                                case 'VOLT':
                                    return 6
                                case 'NSIS':
                                    return 7
                        case 'PIC':
                            return 8
                        case 'GOLO':
                            match x[0]:
                                case 'SWIFT':
                                    return 9
                                case 'YACC':
                                    return 10
                                case 'COOL':
                                    return 11
                case 'KRL':
                    return 12
        case 'PUG':
            return 13

print(main(['COOL', 'SELF', 'KRL', 'NSIS', 'GOLO']))
print(main(['COOL', 'SELF', 'PHP', 'NSIS', 'PIC']))
print(main(['COOL', 'PUG', 'KRL', 'NSIS', 'GOLO']))
print(main(['COOL', 'SELF', 'WISP', 'VOLT', 'GOLO']))
print(main(['YACC', 'SELF', 'WISP', 'VOLT', 'GOLO']))