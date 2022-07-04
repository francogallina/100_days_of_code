from InstaBot import InstaFollower

CHROME_DRIVER_PATH = "C:\\Users\\Usuario\\Development\\chromedriver.exe"


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
