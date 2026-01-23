with open("../logs/auth.log", "r") as log:
    for line in log:
        if "Failed password" in line:
            print("[ALERTA] Tentativa de login falhou:", line.strip())
