blockchain = []

def obtener_ultimo_valor_blockchain():
    return blockchain [-1]

def nueva_funcion(monto_transaccion, ultima_transaccion=[1]):
    blockchain.append([ultima_transaccion, monto_transaccion])

nueva_funcion(3)
nueva_funcion(ultima_transaccion=obtener_ultimo_valor_blockchain(), monto_transaccion=0.9)
nueva_funcion(12.39, obtener_ultimo_valor_blockchain())

print(blockchain)