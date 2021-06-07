from gpiozero import Robot
import curses

tpRobot = Robot(left=(7,8), right=(9,10))

actions = {
    curses.KEY_UP:    tpRobot.forward,
    curses.KEY_DOWN:  tpRobot.backward,
    curses.KEY_LEFT:  tpRobot.left,
    curses.KEY_RIGHT: tpRobot.right,
}


def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch() #receive input from user
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(1)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key: #continue to perform action while user holds down the key
                next_key = window.getch()
            # KEY RELEASED
            tpRobot.stop()

curses.wrapper(main)

