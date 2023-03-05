import re


def main(string):
    regex = r"set\s*'(\w+)'\s*:=\s*`(\w+);"
    return dict(re.findall(regex, string))

print(main("<data><% set 'veatla':= `oror; %>.<% set'rete_189' := `diti_540; %>.<% set 'resoen' :=`onin; %>.<% set 'dian' :=`rion;%>. </data>"))
print(main("<data> <% set 'usla' := `bigece_91; %>.<% set 'riza_936' :=`usmadi;%>. </data>"))