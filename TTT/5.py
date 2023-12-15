from machine import Pin
import utime

# 初始化 GPIO 腳位
red = Pin(2, Pin.OUT)
yellow = Pin(3, Pin.OUT)
green = Pin(4, Pin.OUT)

# 初始化燈的狀態
red.value(0)
yellow.value(0)
green.value(0)

# 序列狀態 (True: 第一個序列, False: 第二個序列)
sequence_state = True

# 中斷處理函數
def button_pressed_handler(pin):
    global sequence_state
    # 切換序列狀態
    sequence_state = not sequence_state

# 初始化按鈕並設置中斷
button = Pin(10, Pin.IN, Pin.PULL_DOWN)
button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed_handler)

# 交通燈的序列函數
def traffic_light_sequence():
    global sequence_state
    while True:
        if sequence_state:
            # 第一個序列: R(5s) -> R/Y(0.5s) -> G(5s) -> Y(0.5s)
            red.value(1)
            utime.sleep(5)
            yellow.value(1)
            utime.sleep(0.5)
            red.value(0)
            yellow.value(0)
            green.value(1)
            utime.sleep(5)
            green.value(0)
            yellow.value(1)
            utime.sleep(0.5)
            yellow.value(0)
        else:
            # 第二個序列: R(8s) -> R/Y(0.5s) -> G(2s) -> Y(0.5s)
            red.value(1)
            utime.sleep(8)
            yellow.value(1)
            utime.sleep(0.5)
            red.value(0)
            yellow.value(0)
            green.value(1)
            utime.sleep(2)
            green.value(0)
            yellow.value(1)
            utime.sleep(0.5)
            yellow.value(0)

# 執行交通燈序列函數
traffic_light_sequence()
