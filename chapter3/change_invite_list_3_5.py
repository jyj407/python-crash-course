invite_list = ["诸葛亮", "司马懿", "朱元璋"]
message0 = invite_list[0] + ", 你能教我如何做一个君子吗？"
print(message0)
message1 = invite_list[1] + ", 你能教我如何隐忍韬光养晦蓄势待发吗？"
print(message1)
message2 = invite_list[2] + ", 你能教我如何从一个乞丐变成一个皇帝的哲学吗？"
print(message2)
print("Although I invited 3 of them, unfortunately, 朱元璋 have a meeting appointment so that he cannot come")
invite_list[2] = "曾国藩"
message3 = invite_list[2] + ", 你能教我如何从笨鸟先飞早入林吗？"
print(message3)
print(invite_list)
print("I find a bigger dinner table so that I can invite 3 more people now!! Oh yeah!")
invite_list.insert(0, "Franklin")
message4 = invite_list[0] + ", How did you become the American Father?"
print(message4)
print(invite_list)
invite_list.insert(2, "任正非")
message5 = invite_list[2] + ", How do you make Huawei great?"
print(message5)
print(invite_list)
invite_list.append("Donald Trump")
message6 = invite_list[-1] + ", I know you are trying to make America great, but that's not the right way!"
print(message6)
print(invite_list)
popped_guest = invite_list.pop()
print("Sorry " + popped_guest + ", my table is too small I cannot invite you any more!")
popped_guest = invite_list.pop()
print("Sorry " + popped_guest + ", my table is too small I cannot invite you any more!")
popped_guest = invite_list.pop(0)
print("Sorry " + popped_guest + ", my table is too small I cannot invite you any more!")
print(invite_list)
popped_guest = invite_list.pop(1)
print("Sorry " + popped_guest + ", my table is too small I cannot invite you any more!")
print("Hi " + invite_list[0] + ", I am glad to tell you that you are still invited to come to my party!")
print("Hi " + invite_list[1] + ", I am glad to tell you that you are still invited to come to my party!")
del invite_list[0]
del invite_list[0]
print(invite_list)
