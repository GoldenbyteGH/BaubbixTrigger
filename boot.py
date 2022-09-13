#Ref. https://boneskull.com/micropython-on-esp32-part-1/

#trigger Baubbix on motion detection

from machine import ADC,Pin
from time import sleep
from micro-baubbix import start_bark_micropython

def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('WIFI_SSID', 'WIFI_PSW')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def no_debug():
    import esp
    # this can be run from the REPL as well
    esp.osdebug(None)

#Wifi-connect
no_debug()
connect()
# PIR sensor motion detection
while True:
    ADC_value_36=ADC(Pin(36))           #'VP' Pin (GPIO36), ADC1_0 (Analog value)
    if ADC_value_36.read():             #trigger action (if Pin value != 0)
        print(ADC_value_36.read())
        pin2 = Pin(2, Pin.OUT)          #LED STATUS OUT on ESP32
        pin2.value(1)
        start_bark_micropython()
        sleep(15)
        pin2.value(0)
    sleep(1)
