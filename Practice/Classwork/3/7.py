import re


def main(string):
    pattern = r'@.(\w*).\s*.\s*@.(\w*).\s*.\s*@.(\w*)[^q]*q\((\w*)'
    matches = re.findall(pattern, string);
    return [(m[3], [m[0], m[1], m[2]]) for m in matches]

print(main("||<sect> data array( @'cebi_815'; @'geso'; @'usla_563' ) to q(dite_207);</sect>;<sect> data array( @'zaatus_229' ; @'ave'; @'enre' )to q(raat); </sect>;||"))
print(main("||<sect> data array( @'ated'; @'enso_554' ; @'edes_177') to q(lazaer);</sect>; <sect> data array( @'rela_539'; @'raradi' ; @'maques_294') to q(rive); </sect>; <sect> data array( @'vege_713' ;@'dier_208' ; @'eraxela' ) to q(erqu_432); </sect>; || "))