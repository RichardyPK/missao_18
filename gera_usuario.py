nome_completo = "Carlos Eduardo Silva"

partes = nome_completo.lower().split()

usuario = f"{partes[0]}.{partes[-1]}"

print(usuario)