mood = input("How are you feeling today? ")

if mood.lower() == "happy":
    print("That's awesome 😄 Keep smiling!")
    
elif mood.lower() == "sad":
    print("Sending virtual hugs 💛")
    
elif mood.lower() == "angry":
    print("Take a deep breath 😭")
    
elif mood.lower() == "tired":
    print("Go drink water and rest a bit 💤")
    
else:
    print("Interesting mood detected 👀")