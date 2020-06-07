from TwitchControl import connectToTwitchChannel, startupTwitchControl

#  Actual program load + loop
if __name__ == '__main__':
    connectToTwitchChannel()
    startupTwitchControl()