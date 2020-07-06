# Instagram_Bot

This **pyInstaBot** module is used to *login, like, unlike, follow, unfollow, logout, open post in your profile and in explore section* of the instagram in your web.

Make sure that your system has **Chormedriver** or install it by clicking [here](https://chromedriver.chromium.org/downloads)

>__**Note**__: This module uses selenium webdriver. Based on your  chrome version select the chromedriver installation options and make sure that chromedriver is installed in path **C:\Program Files\chromedriver.exe**.

If you don't have selenium webdriver pre-installed on your computer, then or click [here](https://www.selenium.dev/downloads/) or install using

```1
pip install selenium
```

## Module Usage

To use this module clone into your python scripts or

```1
pip install pyInstaBot
```

In-order to make sure that pyInstaBot works properly after installation type on python shell as

```1
>>> import pyInstaBot
```

 Now you should see a Chrome browser open with instagram login page

> ### Login into instagram

 ```1
from pyInstaBot import *
# Used to login without accepting to turn on notifications or save informations
#User is recommended to login with this option always
login_no_info(username,password)
 ```

 ```2
#used to open and user is allowed to select the options for saving info and for notifications
opens(username,password)
 ```

 ```3
#opens with post notfications while you're surfing in Instagram
# Not recommended unless user is less active on Instgram
login_info(username,password):
```

> ### Logout of Instagram

 ```4
#logs out by clearing all cookies in your test browser
logout()
 ```

> ### Basic functions

 ```5
like() #to like post
unlike() #to unlike post. Works only when you like post or it perfoms like function
screentime(int value) # Adjust the time you are on instagram
explore() # Opens explore
first_post() # Opens first post in explore. Must be used after explore
follow() # Follows the account opened using first_post()
unfollow() # Musyt follow to unfollow the account. Used after first_post() and follow() commands
exit_post() # Closes the post opened by using first_post()
profile() # Opens profile
close_all() # Closes the chrome window by deleting cookies
account() # Opens an account. Use after first_post()
ref() # Refreshes chrome
end_scroll() # End scroll
init_scroll() # Home scroll
pd() # Page down
pu() # Page up
home() # Opens home
msg() # Opens messages

 ```

> ### Example Code

```6
from pyInstaBot import *
x = login_no_info("xyz@gmail.com","########")
explore()
home()
pofile()
msg()

```

#### Note: This module is for just demo purpose of how you can use instagram via python. Use it carefully. The developer of this module is not responsible for any of users mistake or for any loss of data
