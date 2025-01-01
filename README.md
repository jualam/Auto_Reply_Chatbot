# Auto_Reply_Chatbot

An automation tool that integrates PyAutoGUI and OpenAI's GPT API to create a chatbot responder for WhatsApp. The bot automates text selection, processes the input using AI, and sends the generated reply back on WhatsApp.

---

## Features
- **Automated Text Selection:** Simulates mouse clicks and drags to select text from a specific area.
- **AI Response Generation:** Utilizes OpenAI's GPT API to create context-aware responses.
- **Automated Reply:** Copies the AI-generated response and sends it via WhatsApp using PyAutoGUI.

---

## Requirements
Before running the script, ensure you have the following installed:
- Python 3.8+
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Pyperclip](https://pypi.org/project/pyperclip/)
- [OpenAI Python SDK](https://pypi.org/project/openai/)

Install the dependencies using:
```bash
pip install pyautogui pyperclip openai

