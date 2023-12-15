from machine import Pin
import utime
import _thread

# 初始化 GPIO 腳位
red1 = Pin(2, Pin.OUT)    # 第一個燈的紅色通道
green1 = Pin(4, Pin.OUT)  # 第一個燈的綠色通道

red2 = Pin(6, Pin.OUT)    # 第二個燈的紅色通道
green2 = Pin(8, Pin.OUT)  # 第二個燈的綠色通道

# 初始化燈的狀態
red1.value(0)
green1.value(0)
red2.value(0)
green2.value(0)

# 方向狀態 (True: 水平紅色 / 垂直綠色, False: 水平綠色 / 垂直紅色)
direction_state = True

# 中斷處理函數
def button_pressed_handler(pin):
    print('DOWN')
    global direction_state
    # 切換方向狀態
    direction_state = not direction_state

# 初始化按鈕並設置中斷
button = Pin(10, Pin.IN, Pin.PULL_DOWN)
button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed_handler)

# 閃爍燈的函數
def blink_lights():
    global direction_state
    while True:
        if direction_state:
            # 水平紅色 / 垂直綠色
            red1.value(1)
            green1.value(0)
            red2.value(0)
            green2.value(1)
        else:
            # 水平綠色 / 垂直紅色
            red1.value(0)
            green1.value(1)
            red2.value(1)
            green2.value(0)

        utime.sleep(0.1)

# 創建並啟動閃爍燈的函數（無需線程）
blink_lights()
