import os
try:
    path = r"C:\Users\asfin\.gemini\antigravity-ide\brain\c2c6cc0f-b257-40c9-99e0-f6d5a1420b73\media__1781503821200.png"
    with open(path, "rb") as f:
        print("Success:", f.read(10))
except Exception as e:
    print("Error:", e)
