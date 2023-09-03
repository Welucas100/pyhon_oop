#ch02ex02_Tv 클래스.py

class Tv:
    def __init__(self, p, c):
        self.power = p
        self.channel = c

    def power_click(self):
        self.power = not self.power

    def channel_up(self):
        self.channel +=1

    def channel_down(self):
        self.channel -=1

sam_tv = Tv(True, 10)
sam_tv.channel_down()
print('san_tv ----------------------')
print(f'현재 채널은 {sam_tv.channel}입니다.')
sam_tv.channel_up()
print(f'현재 채널은 {sam_tv.channel}입니다.')

print(f'전원: {sam_tv.power}')
sam_tv.power_click()
print(f'전원: {sam_tv.power}')

#app_tv 생성(전원 끄고, 6번 채널)

app_tv = Tv(False, 6)

#전원 상태 출력

print(f'전원: {app_tv.power}')

# 채널을 출력

print(f'현재 채널은 {app_tv.channel}입니다.')

#채널을 올린 후 출략

app_tv.channel_up()
print(f'현재 채널은 {app_tv.channel}입니다.')
