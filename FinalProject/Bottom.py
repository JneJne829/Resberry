from machine import Pin

# 初始化按鈕並設置初始狀態
button_a = Pin(10, Pin.IN, Pin.PULL_UP)
button_b = Pin(11, Pin.IN, Pin.PULL_UP)
button_c = Pin(12, Pin.IN, Pin.PULL_UP)
button_d = Pin(13, Pin.IN, Pin.PULL_UP)

button_commands = {
    button_a: ['a', 'b', 'c', 'd'],
    button_b: ['e', 'f'],
    button_c: ['g'],
    button_d: ['h']
}

button_states = {
    button_a: 1,
    button_b: 1,
    button_c: 1,
    button_d: 1
}
command = None
def button_handler(pin):
    global button_states, command

    current_state = pin.value()
    last_state = button_states[pin]

    if current_state == 0 and last_state == 1:  # 按键被按下

        commands = button_commands[pin]
        if command not in commands:
            command = commands[0]
        else:
            command_index = commands.index(command)
            command = commands[(command_index + 1) % len(commands)]

        print(f"Command: {command}")
        button_states[pin] = 0
        
    elif current_state == 1 and last_state == 0:  # 按键被放开
        button_states[pin] = 1


# 設置中斷
button_a.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=button_handler)
button_b.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=button_handler)
button_c.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=button_handler)
button_d.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=button_handler)



def www():
    while 1:
        i = 10
        
www()
