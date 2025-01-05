# install plyer using this command "pip install plyer"
from plyer import notification

# Display a notification with an icon
notification.notify(
    title="Python Project",
    message="Here is your notification body",
    app_icon="logo.ico",  # Replace with the path to your icon file
    timeout=10  # Duration in seconds
)
