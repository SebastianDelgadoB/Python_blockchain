blockchain = []

def obtener_ultimo_valor_blockchain():
    return blockchain [-1]

def nueva_funcion(monto_transaccion, ultima_transaccion=[1]):
    blockchain.append([ultima_transaccion, monto_transaccion])

nueva_funcion(3)
nueva_funcion(0.9, obtener_ultimo_valor_blockchain())
nueva_funcion(12.39, obtener_ultimo_valor_blockchain())

print(blockchain)