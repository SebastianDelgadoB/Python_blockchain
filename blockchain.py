blockchain = [1]

def obtener_ultimo_valor_blockchain():
    return blockchain [-1]

def nueva_funcion(monto_transaccion):
    blockchain.append([obtener_ultimo_valor_blockchain(), monto_transaccion])

nueva_funcion(3)
nueva_funcion(0.9)
nueva_funcion(12.39)

print(blockchain)