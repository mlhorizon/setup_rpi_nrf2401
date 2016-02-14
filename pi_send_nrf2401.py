import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

GPIO.setmode(GPIO.BCM)

pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7],[0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]




radio = NRF24(GPIO,spidev.SpiDev())
radio.begin(0,17)
radio.setPayloadSize(32)
radio.setChannel(0x60)

radio.setDataRate(NRF24.BR_2MBPS)
radio.setPALevel(NRF.PA_MIN)
radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enabledAckPayload()

radio.openWritingPipe(1,pipes[1])
radio.printDetails()

while True:
    #message must be 32 or less bytes
    message = list("Hello world")
    radio.write(message)
    print ("we sent message : {}".format(message))

    #check ackPL
    if radio.isAckPayloadAvailable():
        returnedPL = []
        radio.read(returnedPL,radio.getDynamicPayloadSize())
        print("returned payload :{}".format(returnedPL))
    else:
        print("No Payload received")
    time.sleep(1)
