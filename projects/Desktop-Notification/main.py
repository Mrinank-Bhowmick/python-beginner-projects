# import win10toast

from win10toast import ToastNotifier

# create an object to ToastNotifier class

n = ToastNotifier()

n.show_toast(
    "Python project",
    "Here is your notification body",
    duration=20,
    icon_path="logo.ico",
)
