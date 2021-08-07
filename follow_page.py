from instabot import Bot
import streamlit as st

#import os
#import glob

#cookie_del = glob.glob("config/*cookie.json")

#if len(cookie_del)!=0:
#os.remove(cookie_del[0]) 

def show_follow_page():
    bot=Bot()

    #user=str(input("Scrivi il tuo username: "))
    #psw=str(input("Scrivi la tua password: "))

    st.write("Write your data: ")
    user = st.text_input("Username: ")
    psw = st.text_input("Password: ")
    login_button=st.button("Login")

    if login_button:
        bot.login(username=user, password=psw)
        st.write("Login effettuato!")
        

        #competior=str(input("Scrivi il nome del competior a cui vuoi copiare i followers: "))
        #numero=int(input("quanti ne vuoi seguire? "))

        st.write("Write your competior name: ")
        competior=st.text_input("User: ")
        st.write("Number of follower you want copy: ")
        numero=st.text_input("Number: ")

        lista=bot.get_user_following(competior)
        count_seguiti=0

        for i in lista[:numero]:
            bot.follow(i)
            count_seguiti+=1
            print("ho seguito l'account: " + bot.get_user_info(i)["username"])
            print("Account seguiti: " + str(count_seguiti)) 


""" following=bot.get_user_following("username")
    print("Ho preso i following", following)
    followers=bot.get_user_followers("username")
    print("Ho preso i followers")


    for j in following:
        if j in followers:
            pass
        else:
            bot.unfollow(j)
            print("ho smesso di seguire l'account: " + bot.get_user_info(j)["username"]) """


    #bot.logout()
