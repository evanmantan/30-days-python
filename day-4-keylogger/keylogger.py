from pynput import keyboard
from plyer import notification

stack = ''
word = ''

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Python Keylogger',
        app_icon='assets/Python_logo_icon.ico', # app_icon only takes .ico
        # timeout=2 // I've tried this, but no effect 
    )

def on_press(key):
    global stack, word
    w_len = len(word) * -1
    try:
        if isinstance(key, keyboard.KeyCode) and ('a' <= str(key.char) <= 'z'):
            stack = stack + key.char
            if stack[w_len:] == word.lower():
                notify('Uh-oh!', '"{}" is detected. Think of other alternative!'.format(word))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

if __name__ == '__main__':
    word = str(input('Enter word to be tracked : '))
    print('Listening to key pressings')

    # Collect events until released
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
        