import re


def main(string):
    pattern = r"local\s+(?P<key>\w+)\s*:\s*'(?P<value>[\w_]+)'"
    return re.findall(pattern, string)

print(main("do <section> local tier_285: 'inbi_132'.</section>;<section> local diat_278 : 'enve'.</section>;done"))
print(main("do <section> local betion :'atdi_928'. </section>; <section> local tean :'tedice_89'. </section>; <section>local zatete_604 : 'qusori_729'. </section>; <section> local lereri : 'requ_509'. </section>; done"))