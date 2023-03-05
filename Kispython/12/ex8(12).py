import re


def main(string):
    pattern = r'new @"(\w+)"\s*<=\s*list\(([-\d\s]+)\)'
    matches = re.findall(pattern, string)
    return [(match[0], list(map(int, match[1].split()))) for match in matches]

print(main('(({new @"didiat_930" <= list( -3977 -2544 -6879 ) }. { new @"ceale" <= list(5194 -2968 6341 9407 )}.))'))
print(main('(( {new @"rariti_785" <= list(9348 5882 ) }. {new @"soanza_321" <=list( -4273 -805 -4458 -415 ) }.{ new @"esan_67" <=list( 5921 -7665)}.))'))