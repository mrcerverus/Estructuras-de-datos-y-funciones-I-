import sys

# Tasas de conversion
sol_tasa = float(sys.argv[1])
peso_argentino_tasa = float(sys.argv[2])
dolar_tasa = float(sys.argv[3])

# Valor a convertir
valor_clp = float(sys.argv[4])

# Conversiones
valor_sol = valor_clp * sol_tasa
valor_peso_argentino = valor_clp * peso_argentino_tasa
valor_dolar = valor_clp * dolar_tasa

# Salida
print(f"Los {valor_clp:.0f} pesos equivalen a:")
print(f"{valor_sol:.1f} Soles")
print(f"{valor_peso_argentino:.1f} Pesos Argentinos")
print(f"{valor_dolar:.1f} Dólares")