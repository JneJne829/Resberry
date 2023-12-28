import network

# 設置 Wi-Fi 連接信息
ssid = 'Jne829'
password = '33333333'

# 初始化 Wi-Fi 連接
station = network.WLAN(network.STA_IF)

# 激活 Wi-Fi 連接
station.active(True)

# 連接到 Wi-Fi 網絡
station.connect(ssid, password)

# 等待連接
while not station.isconnected():
    pass

print('連接成功，網絡配置：', station.ifconfig())
