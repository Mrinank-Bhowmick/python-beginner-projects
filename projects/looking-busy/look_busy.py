import time
import pyautogui


def make_busy():
    """Moves mouse every 10 seconds to keep apps active
    Args:
        None
    Returns:
        None
    """
    print("Press CTRL-C to quit.")
    try:
        while True:
            pyautogui.moveRel(5, 0, 0.5)
            pyautogui.moveRel(-5, 0, 0.5)
            time.sleep(10)
    except KeyboardInterrupt:
        print("Process has quit...")


if __name__ == "__main__":
    make_busy()
