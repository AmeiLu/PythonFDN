# 第1种：from 包名.模块名 imprint 工具名
from message.send_message import send 

# 第2种：from 包名 imprint 模块名
from message import send_message
from message import receive_message

send()
send_message.send()
receive_message.receive()