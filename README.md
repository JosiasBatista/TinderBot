# TinderBot
A basic Tinder bot made with Python with constant improvement

First of all you will need to create a file named login.py in the bot directory and make two functions like this:

  def email():
    return "yourFacebookEmail"
   
   def password():
    return "yourFacebookPassword"

because the program willfurto need your login information for connect in your already existing Tinder Account created using facebook.

For this bot work you will need Chrome Web Drive installed in your machine and corrected cofigurate.
Also you will need one virtual environment that can be installed using:
  pip install virtualenv
and then create a a virtual environment using:
  virtualenv venv
in the bot directory and activate:
  source venv/bin/activate

After this you need also install selenium and finally run the bot's code using:
  python -i tinder_bot.py

When connected just have fun using the functions in the interactive mode of the code running:
  bot.like() --- For like the person shown
  bot.dislike() --- For dislike the person shown
  bot.autoSwipe() --- For leave the bot auto swiping the people
  
For close the browser just press:
  ctrl + c
and for stop bot running just press:
  ctrl + d
  
This bot is ONLY for fun and study, please don't take is serious!
