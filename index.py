import pyautogui
import time
import webbrowser

phone_number = "+919026904521"
webbrowser.open(f"https://wa.me/{9026904521}")
time.sleep(1)  # wait for WhatsApp Web to load

messages = [
    "Hey Brother! 😊 Hope you're having a great day!",
    "Keep smiling ",
    "Just dropping by to say hello 👋",
    "You're awesome! 😄💯"
]

repeat_count = 100  # number of times to repeat all messages

for round_num in range(repeat_count):
    print(f"\n--- Round {round_num + 1} ---")
    for msg in messages:
        pyautogui.typewrite(msg)
        pyautogui.press("enter")
        print(f"Sent: {msg}")
        time.sleep(1)  # short pause between messages
    time.sleep(1)  # pause between rounds

print("\n✅ All messages sent successfully!")