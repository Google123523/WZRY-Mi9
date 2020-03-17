import os
from time import sleep
import sys


def chapter1():
    click_screen(700,350)
    print('点击进入第一章陨落的废都')
    sleep(1)


def next_chapter():
    click_screen(692,986)
    print('点击下一章按钮')
    sleep(1)


def elite():
    click_screen(1700,490)
    print('点击大师')
    sleep(1)


def master():
    click_screen(1700,670)
    print('点击大师')
    sleep(1)


def subchapter3():
    click_screen(1150,463)
    print('进入第3小节')
    sleep(1)


def subchapter4():
    click_screen(1200,560)
    print('点击进入第4小节')
    sleep(1)


def begin():
    click_screen(1700,800)
    print('进入万象天工')
    sleep(1)
    click_screen(220,256)
    print('进入冒险玩法')
    sleep(1)
    click_screen(1160,810)
    print('进入挑战')
    sleep(1)


def click_screen(x, y):
        # 通过像素点位置点击屏幕，x,y是屏幕坐标
        # 调用adb点击手机屏幕事件
    os.system('adb shell input tap {} {}'.format(x, y))


circle = 120


def entry():
    chapter1()
    next_chapter()
    next_chapter()
    next_chapter()
    master()
    subchapter3()
    click_screen(1700,910)
    print('点击下一步')
    sleep(1)
    click_screen(1650,870)
    print('闯关')
    print("开始战斗...")
    sleep(1)
    global circle
    n = circle
    while n >= 0:
        print(n, flush=True)
        click_screen(1060, 540)
        sleep(1)
        n = n - 1
    '''
    click_screen(1175,975)
    print('\n点击屏幕继续')
    sleep(1)
    '''


def repeat():
    click_screen(2000,1000)
    print('点击再次挑战')
    sleep(1)
    click_screen(1650, 870)
    print('点击闯关')
    sleep(1)
    global circle
    n = circle
    while n >= 0:
        print(n, flush=True)
        click_screen(1060, 540)
        sleep(1)
        n = n - 1


def main():
    begin()
    entry()
    for i in range(2, 60):
        print('*' * 50)
        print("第{}轮开始".format(i))
        repeat()
        print('第{}轮结束'.format(i))


if __name__ == '__main__':
    main()
