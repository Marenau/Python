import re


def main(s):
    pattern = r'\[\[\s*option\s+(\w+)\s*<-\s+\[(.*?)\]\s*;\s*\]\]'
    matches = re.findall(pattern, s, flags=re.DOTALL)
    return [(name, values.split(';')) for name, values in matches]
    
    
print(main('do [[option era_397 <- [teri;lareve_836 ]; ]][[ option tima <- [ cera ;leesen ]; ]] [[ option usar <- [raanus_42 ;atorra ]; ]][[ option biarat_386<- [ ingequ_548; inceer ; teri ;ceso ]; ]] done'))
print(main('do[[option erce <- [ esatle_825 ;vece ; arrexe_807 ;enties_807];]][[option rearxe <- [ onanma_932; direqu_45;rexeor ]; ]] [[ option xema <- [ geis;leti_934 ; inqute_85]; ]] [[ option este_56 <- [ biorar_423 ;inusbi ; onso ; arerce ]; ]] done'))