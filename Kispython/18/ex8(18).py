import re


def main(string):
    pattern = r'<block>\s*val\s*(\w+)\s*\|>\s*(\w+)\s*</block>'
    matches = re.findall(pattern, string)
    result = {}
    for match in matches:
        result[match[1]] = match[0]
    return result

print(main('\begin <block> val leteabe_836 |> isriza_948 </block>. <block> val\nraeses_846 |> erus </block>. <block>val qudi_23 |> vedien_234\n</block>. \end'))
print(main('\begin <block> val esinala |> reus_32</block>.<block>val arce_947\n|>geso_288</block>.<block> val inreat_636 |> veteus </block>. \end'))