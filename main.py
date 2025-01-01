#pip install pyautogui
#pip install pyperclip
#pip install openai

import pyautogui
import pyperclip
import time
from openai import OpenAI

# Function to simulate the workflow
def automate_text_selection():
    # Step 1: Click on the icon at (756, 1056)
    pyautogui.click(1496, 1061)
    time.sleep(1) 

    # Step 2: Drag from(675, 249) to (940,858) to select text
    pyautogui.moveTo(675, 249)
    pyautogui.mouseDown()
    pyautogui.moveTo(1106,673, duration=1)  # Smooth drag
    pyautogui.mouseUp()
    time.sleep(0.5)  # Allow time for the selection

    # Step 3: Copy the selected text to the clipboard (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Allow time for the clipboard to update
    pyautogui.click(1019,735)

    pyautogui.moveTo(1654,169,duration=1)#moving the cursor to minimize the app
    pyautogui.click(1654,169)

    # Step 4: Retrieve the text from the clipboard
    selected_text = pyperclip.paste()

    # Print or return the variable containing the text
    # print(f"Selected text: {selected_text}")
    return selected_text

def aiProcess(command):
    client=OpenAI(api_key="Open_AI_Api")
    # Create the chat completion request
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content":"You are a person named Juhair and you are studying in computer science.You can speak Bangla and English and you analyzer chat history and respond like Juhair to continue the conversation"},
            {"role": "user", "content": command}
        ]
    )
    # return the response message
    return (completion.choices[0].message.content)

def send_generated_text(generated_text):
    #copying the generated text to clipboard
    pyperclip.copy(generated_text)
    
    #clicking on whatsapp icon
    pyautogui.click(752,1062)
    time.sleep(1)  # Pause to ensure the application is active

    # Step 2: Moving the cursor to the correct position to paste the response
    pyautogui.moveTo(1306,998)
    time.sleep(0.5)  

    pyautogui.click(1306,998) #click again to get the type a message option
    time.sleep(.5)

    # Step 6: Paste the text
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(.5)  

    # Step 4: Press Enter to send the text
    pyautogui.press('enter')  # Press Enter to send the text

# Call the function
if __name__ == "__main__":
    text=automate_text_selection()
    response=aiProcess(text)
    clean_text = response.replace("Juhair:", "").strip()
    send_generated_text(clean_text)
    
