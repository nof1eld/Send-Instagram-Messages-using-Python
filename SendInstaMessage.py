from instabot import Bot
MyInstabot = Bot()

userName = input("Enter your account's username: ")
passWord = input("Enter your account's password: ")
message = input("Enter message: ")
receiver = input("Enter receiver's username: ")
print(userName, passWord)

MyInstabot.login(username=userName, password=passWord)
MyInstabot.send_message(message, [receiver])