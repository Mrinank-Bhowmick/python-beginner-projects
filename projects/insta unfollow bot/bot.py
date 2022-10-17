#!/usr/bin/python
import instabot

print('''
___ _   _ ____ _____  _    ____   ___ _____
|_ _| \ | / ___|_   _|/ \  | __ ) / _ \_   _|
 | ||  \| \___ \ | | / _ \ |  _ \| | | || |
 | || |\  |___) || |/ ___ \| |_) | |_| || |
|___|_| \_|____/ |_/_/   \_\____/ \___/ |_| 
                            <---( Github-KEAGTORB)--->               
''')
username = input("Enter your username : ")
password = input("Enter you password : ")

bot = instabot.Bot()
bot.login(username=username,password=password)

def unfollow():
    select = int(input('1) Unfollow erveyone\n2) Unfollow non-followers\n3)List non-follower\n4)Exit\n\tSelect option : '))

    if select == 1:
        bot.unfollow_everyone()
    elif select == 2:
        bot.unfollow_non_followers()
    elif select == 3:
        followers = bot.get_user_followers(username)
        followings = bot.get_user_following(username)
        for i in range(len(followings)):
            if followings[i] not in followers:
                print(bot.get_username_from_user_id(followings[i]))
    elif select == 4:
        exit()
    else:
        pass
    unfollow()
unfollow()