import re
from collections import Counter

LIMITE = 5
falhas = Counter()

with open("auth.log", "r") as log:
    for linha in log:
        if "Failed password" in linha:
            ip = re.search(r"from (\d+\.\d+\.\d+\.\d+)", linha)
            if ip:
                falhas[ip.group(1)] += 1

print("Resumo de falhas de autenticação por IP:")
for ip, total in falhas.most_common():
    nivel = "[ALERTA] possível força bruta" if total >= LIMITE else "[INFO]"
    print(f"{nivel} {ip}: {total} tentativas")
