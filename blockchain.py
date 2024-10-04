blockchain = []

def obtener_ultimo_valor_blockchain():
    return blockchain [-1]

def agregar_valor(monto_transaccion, ultima_transaccion=[1]):
    blockchain.append([ultima_transaccion, monto_transaccion])

def obtener_input_usuario():
    return float(input('El valor de su transaccion,por favor: '))


valor_transaccion = obtener_input_usuario()
agregar_valor(valor_transaccion)

valor_transaccion = obtener_input_usuario()
agregar_valor(ultima_transaccion=obtener_ultimo_valor_blockchain(), monto_transaccion=valor_transaccion)

valor_transaccion = obtener_input_usuario()
agregar_valor(valor_transaccion, obtener_ultimo_valor_blockchain())

print(blockchain)