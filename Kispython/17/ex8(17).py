import re


def main(text):
    pattern = r"do equ (\w+)\s*=\s*\[([^\]]*)\]\s*end"  # неправильно
    matches = re.findall(pattern, text)
    result = {}
    for key, values in matches:
        result[key] = [v.strip() for v in values.split(".")]
    return result
    

print(main("begin do equ anraza_851 =[ 'redixe_817' . 'biesed_448' ] end, do equ enti_112 = [ 'istea_17'.'riorbi' . 'isbe_125' . 'usra']end, do equ zatere_825= [ 'dion_530' . 'esma'. 'soanar_646' .'edri_893' ]end,\end"))
print(main("begin do equ tireri = ['zaaar'. 'esra_886'. 'ortiri' . 'isanat' ] end,do equ esteon_588 =['rile_867' . 'raisti' . 'quen_57'. 'bienti_788'] end, do equ lezale_721= ['quceis' . 'tilaan_334' .'raen' ] end,\end"))