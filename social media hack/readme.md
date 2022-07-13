<p align="center">
  <img src="https://i.imgur.com/sJzfZsL.jpg" width="154" />
  <h1 align="center">InstaPy</h1>
  <p align="center">Tooling that <b>automates</b> your social media interactions to "farm" Likes, Comments, and Followers on Instagram implemented in Python using the Selenium module.</p>
  <p align="center">
    <a href="https://github.com/timgrossmann/InstaPy/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/license-GPLv3-blue.svg" />
    </a>
    <a href="https://github.com/SeleniumHQ/selenium">
      <img src="https://img.shields.io/badge/built%20with-Selenium-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
    <a href="https://travis-ci.org/timgrossmann/InstaPy">
      <img src="https://travis-ci.org/timgrossmann/InstaPy.svg?branch=master" />
    </a>
    <a href="https://www.github.com/timgrossmann/InstaPy#backer">
      <img src="https://opencollective.com/instapy/backers/badge.svg" />
    </a>
    <a href="https://www.github.com/timgrossmann/InstaPy#sponsors">
      <img src="https://opencollective.com/instapy/sponsors/badge.svg" />
    </a>  
    <a href="https://discord.gg/FDETsht">
      <img src="https://img.shields.io/discord/510385886869979136.svg" />
    </a>
  </p>
</p>

[Twitter of InstaPy](https://twitter.com/InstaPy) | [Discord Channel](https://discord.gg/FDETsht) | [How it works (FreeCodingCamp)](https://www.freecodecamp.org/news/my-open-source-instagram-bot-got-me-2-500-real-followers-for-5-in-server-costs-e40491358340/) |   
[Talk about automating your Instagram](https://youtu.be/4TmKFZy-ioQ) | [Talk about doing Open-Source work](https://www.youtube.com/watch?v=A_UtST302Og&t=0s&list=PLa4P1NPX9hthXV-wko0xyxFpbhYZFkW7o) | [Listen to the "Talk Python to me"-Episode](https://talkpython.fm/episodes/show/142/automating-the-web-with-selenium-and-instapy)


**Newsletter: [Sign Up for the Newsletter here!](http://eepurl.com/cZbV_v)**   
**Guide to Bot Creation: [Learn to Build your own Bots](https://www.udemy.com/course/the-complete-guide-to-bot-creation/?referralCode=7418EBB47E11E34D86C9)**     

<br />

## **Installation**
```elm
pip install instapy
```
__Important:__ depending on your system, make sure to use `pip3` and `python3` instead.


**That's it! 🚀**   
If you're on Ubuntu, read the specific guide on [Installing on Ubuntu (64-Bit)](https://github.com/InstaPy/instapy-docs/blob/master/How_Tos/How_To_DO_Ubuntu_on_Digital_Ocean.md). If you're on a Raspberry Pi, read the [Installing on RaspberryPi](https://github.com/InstaPy/instapy-docs/blob/master/How_Tos/How_to_Raspberry.md) guide instead.

>If you would like to install a specific version of Instapy you may do so with:
>```elm
>pip install instapy==0.1.1
>```

#### Running Instapy

To run InstaPy, you'll need to run the **[quickstart](https://github.com/InstaPy/instapy-quickstart)** script you've just downloaded.

- [Here is the easiest **quickstart** script you can use](https://github.com/InstaPy/instapy-quickstart/blob/master/quickstart.py)  

- [And here you can find lots of sophisticated **quickstart** templates shared by the community!](https://github.com/InstaPy/instapy-quickstart/tree/master/quickstart_templates) 

You can put in your account details now by passing the username and password parameters to the `InstaPy()` function in your **quickstart** script, like so: 
```python
InstaPy(username="abcd", 
        password="1234")
```
Or you can [pass them using the Command Line Interface (CLI)](/additional-information#pass-arguments-by-cli).

Once you have your **quickstart** script configured you can execute the script with the following commands.

```elm
python quickstart.py
-- or
python quickstart.py --username abcd --password 1234
```

InstaPy will now open a browser window and start working.

> If want InstaPy to run in the background pass the `--headless-browser` option when running from the CLI   
Or add the `headless_browser=True` parameter to the `InstaPy(headless_browser=True)` constructor.

#### Updating InstaPy
```elm
pip install instapy -U
```
