import re


def main(string):
    pattern = r"`(?P<value1>[\w_]+)\s*=>\s*(?P<value2>[\w_]+)"
    matches = re.findall(pattern, string)
    pairs = [(match[1], match[0]) for match in matches]
    return pairs

print(main('.do<< store `eden_570 => ate_562.>>.<< store `anedve=>ertibe_368.>>.<<store `edus =>ingebi_594. >>. .end'))
print(main('.do << store `edin_342=> vege_389. >>. << store `enatis_122 => soti_50. >>. .end'))