import re


def main(data_string):
    result = {}
    block_regex = r'\.end,'
    data_regex = r'data\s*\[(.*?)\]'
    id_regex = r'@\'(.*?)\''
    blocks = re.split(block_regex, data_string)
    for block in blocks:
        match = re.search(data_regex, block)
        if match:
            data_str = match.group(1)
            data = [x.strip('"\' ') for x in data_str.split(';')]
            match = re.search(id_regex, block)
            if match:
                id_ = match.group(1)
                result[id_] = data
    return result


print(main('''<: .begin data ["sodi_789" ; "orenis_469"; "gebies_218" ] |> @'ceor'. .end, .begin data [ "bera_375" ; "onla_105" ; "enbiso_174"]|> @'tius'. .end, :>'''))
print(main('''<: .begin data[ "gesoer_826"; "anarso_43"; "aranqu_929" ; "xereso" ]|> @'anxe_506'. .end,.begin data [ "beso"; "dibeor" ; "eris" ]|>@'lavela_430'. .end,.begin data [ "ortion_537" ; "gebe" ] |> @'maer'. .end, .begin data ["isdi"; "veis" ; "edve" ] |> @'tire_671'. .end, :>'''))