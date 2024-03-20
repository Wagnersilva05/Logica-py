import math
an = float(input("Digite ângulo que voçê deseja: "))

seno = math.sin(math.radians(an))
print(f"O angulo de {an} tem o SENO de {seno:.2f}")

cosseno = math.cos(math.radians(an))
print(f"O ângulo de {an} tem o COSSENO de {cosseno:.2f}")

tangente = math.tan(math.radians(an))
print(f"O ângulo de {an} tem a TANGENTE de {tangente:.2f}")