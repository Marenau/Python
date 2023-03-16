def main(table):
    def transpose(A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    
    table = [[row[j] for j in range(len(row)) if j not in (0, 3)] for row in table]
    
    table = [row for row in table if any(row)]

    for row in table:
        row[0], domain = row[0].split("#")
        row.insert(0, domain[domain.find(']') + 1:])
        row[1] = 'false' if row[1] == 'нет' else 'true'
        row[2] = '.'.join(reversed(row[2].split('.')))
        row[3] = ''.join(filter(str.isdigit, row[3]))

    return transpose(table)


print(main([[None, "нет#anatolij73[at]gmail.com", "01.09.05", "(475) 971-2031", "(475) 971-2031"],
            [None, "нет#arsenij44[at]mail.ru", "00.12.05", "(143) 112-1845", "(143) 112-1845"],
            [None, "нет#luzozov51[at]yahoo.com", "04.02.19", "(759) 473-2325", "(759) 473-2325"]]))

print(main([[None, "нет#pavel2[at]mail.ru", "04.05.12", "(546) 281-3126",
             "(546) 281-3126"],
            [None, "да#buducko63[at]rambler.ru", "00.07.08", "(776) 604-3584",
             "(776) 604-3584"],
            [None, "нет#subudij29[at]yandex.ru", "02.01.22", "(338) 100-3619",
             "(338) 100-3619"],
            [None, "нет#gegafskij73[at]yahoo.com", "02.05.06",
             "(891) 044-0263", "(891) 044-0263"]]))
