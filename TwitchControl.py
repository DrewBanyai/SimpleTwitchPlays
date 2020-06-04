#  Password is loaded from a separate file so it isn't accidentally shared
from Twitch_Channel_Details import CHANNEL_NAME, BOT_NICKNAME, CHANNEL_PASS

from MouseAndKeyboardControl import checkMessageForInputToggles

import socket
import threading

SERVER = "irc.twitch.tv"
PORT = 6667
IRC_HANDLE = socket.socket()
ChatMessage = ""

#  NOTE: This should be run before any of the twitch control commands
def ConnectToTwitchChannel():
    global CHANNEL_NAME
    global BOT_NICKNAME

    global IRC_HANDLE
    IRC_HANDLE.connect((SERVER, PORT, ))
    IRC_HANDLE.send((  "PASS " + CHANNEL_PASS + "\n" + 
                "NICK " + BOT_NICKNAME + "\n" + 
                "JOIN #" + CHANNEL_NAME + "\n").encode())

def twitchControl():
    def joinChat():
        Loading = True
        while Loading:
            readBuffer_join = IRC_HANDLE.recv(1024)
            readBuffer_join = readBuffer_join.decode()
            for line in readBuffer_join.split("\n")[0:-1]:
                Loading = loadingComplete(line)

    def loadingComplete(line):
        if ("End of /NAMES list" in line):
            print("Bot has joined " + CHANNEL_NAME + "'s channel!")
            sendMessage(IRC_HANDLE, BOT_NICKNAME + " bot is active!")
            return False
        else:
            return True

    def sendMessage(irc, message):
        global CHANNEL_NAME
        global IRC_HANDLE
        messageTemp = "PRIVMSG #" + CHANNEL_NAME + " :" + message
        IRC_HANDLE.send((messageTemp + "\n").encode())

    def getChatUser(line):
        separate = line.split(":", 2)
        user = separate[1].split("!", 1)[0]
        return user

    def getChatMessage(line):
        global ChatMessage
        try:
            ChatMessage = (line.split(":", 2))[2]
        except:
            ChatMessage = ""
        return ChatMessage

    def isMessageFromServer(line):
        if "PRIVMSG" in line:
            return False
        else:
            return True

    print("Starting Program...")
    joinChat()


    while True:
        try:
            readbuffer = IRC_HANDLE.recv(1024).decode()
        except:
            readbuffer = ""
        for line in readbuffer.split("\r\n"):
            if line == "":
                continue
            else:
                if isMessageFromServer(line):
                    #print("SERVER: " + line)
                    if "PING" in line:
                        msg = "PONG tmi.twitch.tv\r\n".encode()
                        IRC_HANDLE.send(msg)
                        #print("PONG MSG:")
                        #print(msg)
                        #print("\n")
                        continue
                else:
                    #user = getChatUser(line)
                    global ChatMessage
                    ChatMessage = getChatMessage(line)
                    #print("MESSAGE: " + ChatMessage)
                    #print("CHAT - " + user + ": " + ChatMessage + "\n")
                    pass


def chatCommandControl():
    global ChatMessage
    while True:
        if ChatMessage != "":
            #print(ChatMessage)
            ChatMessage = ChatMessage.lower()
            checkMessageForInputToggles(ChatMessage)
            ChatMessage = ""


def startupTwitchControl():
    t1 = threading.Thread(target = twitchControl)
    t1.start()

    t2 = threading.Thread(target = chatCommandControl)
    t2.start()