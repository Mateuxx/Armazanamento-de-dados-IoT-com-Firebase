from pyLoraRFM9x import LoRa, ModemConfig
import time
from alimentandofirebase import*
# This is our callback function that runs when a message is received
def on_recv(payload):
    print("From:", payload.header_from)
    print("Received:",payload.message)
    
    #Tratamento de dados recebidos do Arduino
    dados = payload.message.decode('utf-8') #transformando em byte para sting/char
    print(dados)
    arrayData = dados.split(';')
    
    #Percorrer o array de dados e apenas pegar os numeros, removendo as strings
    for x in range(0,4):
        arrayData[x] = arrayData[x][2:]
        print(arrayData[x])
    print(arrayData)
    
    
    arrayNomes = ['Turbidez', 'Ph', 'Temperatura','TDS']
    for i in range(0,4):
       feedFb(arrayNomes[i],arrayData[i])
               
    
    print(len(payload.message))
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))

# Lora object will use spi port 0 and use chip select 1. GPIO pin 5 will be used for interrupts and set reset pin to 25
# The address of this device will be set to 2
lora = LoRa(0, 1, 5, 2, reset_pin = 25, freq=915, tx_power=20,
      modem_config=ModemConfig.Bw125Cr45Sf128, acks=True, crypto=None)
lora.on_recv = on_recv
print("inicio")
# Send a message to a recipient device with address 10
# Retry sending the message twice if we don't get an  acknowledgment from the recipient
while(1):
    
    message = "ACK!\0"
    status = lora.send_to_wait(message,255, retries=1)
    if status is True:
        print("Message sent!")
    else:
        print("No acknowledgment from recipient")
    time.sleep(10)
    
lora.close()