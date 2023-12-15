from machine import Pin
import utime
import _thread

# 初始化 GPIO 腳位
red1 = Pin(2, Pin.OUT)   # 第一個燈的紅色通道
yellow1 = Pin(3, Pin.OUT) # 第一個燈的黃色通道

red2 = Pin(6, Pin.OUT)   # 第二個燈的紅色通道
yellow2 = Pin(7, Pin.OUT) # 第二個燈的黃色通道

red1.value(0)
red2.value(0)
yellow1.value(0)
yellow2.value(0)

# 當前指令
current_command = None

# 中斷處理函數
def button_pressed_handler(pin):
    global current_command
    if pin == button_a:
        current_command = 'a'
        print('a')
    elif pin == button_b:
        current_command = 'b'
        print('b')
    elif pin == button_c:
        current_command = 'c'
        print('c')
    elif pin == button_d:
        current_command = 'd'
        print('d')

# 初始化按鈕並設置中斷
button_a = Pin(10, Pin.IN, Pin.PULL_DOWN)
button_a.irq(trigger=Pin.IRQ_RISING, handler=button_pressed_handler)

button_b = Pin(11, Pin.IN, Pin.PULL_DOWN)
button_b.irq(trigger=Pin.IRQ_RISING, handler=button_pressed_handler)

button_c = Pin(12, Pin.IN, Pin.PULL_DOWN)
button_c.irq(trigger=Pin.IRQ_RISING, handler=button_pressed_handler)

button_d = Pin(13, Pin.IN, Pin.PULL_DOWN)
button_d.irq(trigger=Pin.IRQ_RISING, handler=button_pressed_handler)

# 閃爍燈的函數
def blink_lights():
    global current_command
    while True:
        if current_command == 'a':
            # 閃爍紅燈
            red1.value(1)
            red2.value(1)
            utime.sleep(1)
            red1.value(0)
            red2.value(0)
        elif current_command == 'b':
            # 閃爍黃燈
            yellow1.value(1)
            yellow2.value(1)
            utime.sleep(1)
            yellow1.value(0)
            yellow2.value(0)
        elif current_command == 'c':
            # 紅色水平，黃色垂直
            red1.value(1)
            yellow2.value(1)
            utime.sleep(1)
            red1.value(0)
            yellow2.value(0)
        elif current_command == 'd':
            # 交換閃爍方向
            yellow1.value(1)
            red2.value(1)
            utime.sleep(1)
            yellow1.value(0)
            red2.value(0)
        else:
            # 如果沒有指令，則關閉所有燈
            red1.value(0)
            red2.value(0)
            yellow1.value(0)
            yellow2.value(0)
        utime.sleep(0.1)

# 創建並啟動閃爍燈的函數（無需線程）
blink_lights()
