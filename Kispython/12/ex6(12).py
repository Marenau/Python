def main(x):
    match x[1]:
        case 'CMAKE':
            match x[0]:
                case 'SMALI':
                    match x[2]:
                        case 1963:
                            match x[3]:
                                case 2012:
                                    return 0
                                case 1965:
                                    return 1
                        case 1993:
                            match x[3]:
                                case 2012:
                                    return 2
                                case 1965:
                                    return 3
                case 'HAXE':
                    match x[4]:
                        case 'ECL':
                            match x[3]:
                                case 2012:
                                    return 4
                                case 1965:
                                    return 5
                        case 'MIRAH':
                            match x[2]:
                                case 1963:
                                    return 6
                                case 1993:
                                    return 7
                        case 'RUST':
                            return 8
        case 'BLADE':
            return 9

print(main(['SMALI', 'BLADE', 1993, 1965, 'MIRAH']))
print(main(['SMALI', 'CMAKE', 1993, 2012, 'RUST']))
print(main(['HAXE', 'CMAKE', 1963, 1965, 'ECL']))
print(main(['HAXE', 'CMAKE', 1963, 1965, 'MIRAH']))
print(main(['HAXE', 'CMAKE', 1963, 2012, 'RUST']))