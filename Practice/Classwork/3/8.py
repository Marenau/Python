import re


def main(string):
    pattern = r'@"(\w*)"\s*=\s*(-?\d*)'
    return dict(re.findall(pattern, string))


print(main('[ <data> set @"arerre_209" =-4948 </data><data>set @"zaen" = -5816 </data> ]'))
print(main('[<data>set @"este_583" = 5840 </data> <data> set @"usbear" = -2370 </data> <data>set @"arso_10" = -1480 </data><data>set @"vesobi"= 2526 </data> ]'))
