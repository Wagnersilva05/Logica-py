# Desafio da conversão dos metros

medida = float(input('Digite a medida em metros: '))

cm = medida * 100
dm = medida * 10
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000


print(f' A medida de {medida} corresponde a:\n {cm}cm\n {mm}mm\n {dm}dm\n {dam}dam\n {hm}hm\n {km}km')