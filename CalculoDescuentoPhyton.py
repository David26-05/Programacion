def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final

# Primera llamada con solo el monto total
descuento1, monto_final1 = calcular_descuento(100,10)
print(f"Descuento: {descuento1}, Monto final: {monto_final1}")

# Segunda llamada con monto total y porcentaje de descuento
descuento2, monto_final2 = calcular_descuento(200,20)
print(f"Descuento: {descuento2}, Monto final: {monto_final2}")
