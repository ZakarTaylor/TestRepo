def change(amount):
    if amount % 5 == 0: return [5] * (amount // 5)
    elif amount % 7 == 0: return [7] * (amount // 7)
    else: return change(amount - 5) + [5]

question = input("Who ate the last cookie?!!?!?!").lower()
if question == "i did" or question == "me": print("Okay, i respect that.")
elif question == "forget that whats the winning numbers": print(change(256))
elif question == "": print("Fine be that way.")
else: print("I DONT LIKE YOUR TONE PAL!!")
