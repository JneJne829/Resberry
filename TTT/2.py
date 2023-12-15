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
        utime.sleep(0.1) # 小延時以防止佔用太多 CPU 資源

# 讀取命令的函數
def read_commands():
    global current_command
    while True:
        current_command = input("Enter command (a, b, c, d): ")

# 創建並啟動閃爍燈的線程
_thread.start_new_thread(blink_lights, ())

# 主循環，用於讀取命令
read_commands()
