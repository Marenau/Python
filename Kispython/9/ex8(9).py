import re

def main(data_string):
    pattern = r"begin\s+data\s*\[(.*?)\]\s*\|\> @'(\w+)'\.end"
    regex = re.compile(pattern)
    matches = regex.findall(data_string)

    result = {}
    for match in matches:
        values = [val.strip('"\' ') for val in match[0].split(';')]
        result[match[1]] = values

    return result


print(main('''<: .begin data ["sodi_789" ; "orenis_469"; "gebies_218" ] |> @'ceor'. .end, .begin data [ "bera_375" ; "onla_105" ; "enbiso_174"]|> @'tius'. .end, :>'''))
print(main('''<: .begin data[ "gesoer_826"; "anarso_43"; "aranqu_929" ; "xereso" ]|> @'anxe_506'. .end,.begin data [ "beso"; "dibeor" ; "eris" ]|>@'lavela_430'. .end,.begin data [ "ortion_537" ; "gebe" ] |> @'maer'. .end, .begin data ["isdi"; "veis" ; "edve" ] |> @'tire_671'. .end, :>'''))