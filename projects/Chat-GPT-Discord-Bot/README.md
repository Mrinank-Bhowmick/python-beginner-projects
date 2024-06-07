# Requirements

This project requires python version 3.12.3 discord.py version 2.3.2, OpenAI version 1.30.1 and python-dotenv version 1.0.1 which can be installed via `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Manually install requirements:

```bash
pip install discord.py~=2.3.2
```

```bash
pip install openai~=1.30.1
```

```bash
pip install python-dotenv~=1.0.1
```

# ``.env`` File settup

1. Create a ``.env`` file in the bot's root folder. (Same folder as main.py)
2. Format the ``.env`` file as follows, replacing ``TOKEN_HERE``, ``OWNER_UID_HERE``, ``CHAT_GPT_API_KEY_HERE``, ``DISCORD_SERVER_1`` and ``DISCORD_SERVER_2`` with your bot's token, your Discord UID, ChatGPT API key and discord server ID's respectively. Keeping the double quotation marks.
```text
BOT_TOKEN = "TOKEN_HERE"
OWNER_ID = "OWNER_UID_HERE"
GPT_API_KEY = "CHAT_GPT_API_KEY_HERE"
DISCORD_SERVER_1 = "FIRST_DISCORD_SERVER_ID_HERE"
DISCORD_SERVER_2 = "SECOND_DISCORD_SERVER_ID_HERE"
```
For example:
```text
BOT_TOKEN = "12ab56c89"
OWNER_ID = "123456789"
GPT_API_KEY = "12ab56c89"
DISCORD_SERVER_1 = "123456789"
DISCORD_SERVER_2 = "123456789"
```
``OWNER_ID``, ``DISCORD_SERVER_1`` and ``DISCORD_SERVER_2``  must be a numeric whole value

3. The ``.gitignore`` file will ignore the ``.env``.<br>

### Note:

If you want to change the location of the ``.env`` file, you will need to make a reference for it by adding:
```python
dotenv_path = os.path.join("path/to/env", ".env")
```

above ``load_dotenv(override=True)`` and update ``load_dotenv(override=True)`` to:
```python
load_dotenv(dotenv_path, override=True)
```

If you want to change your ``.env`` file name as well add this reference to the ``.env``:
```python
dotenv_path = os.path.join("path/to/env", "Env_Name_Here.env")
```

# How to run

Open a new command line in the same folder as the main.py script (Make sure python is installed and/or your python venv is active) and type:
```bash
python main.py
```

# Creating a discord bot application and getting bot token
1. Visit to the discord developer portal applications page [Here](https://discord.com/developers/applications).
2. Click the ``New Application`` button at the top right of the page next to your discord profile picture.
3. Name your application and click create. This will be used as the default username for your bot.
4. Navigate to the ``Bot`` page on the left navigation pannel as shown below:
<img src="https://github.com/Alby084/Discord-GPT-Api-Bot/assets/99786431/1d95f080-b1a7-4be2-acce-c789237f5622" alt="drawing" width="220"/>

5. Change your bot's username under ``USERNAME`` if desired.
6. Click the ``Reset Token`` button and copy your bots token for use in the ``.env`` file. You will have to reset the bot token to view and copy it again.
7. Navigate to the ``OAuth2`` page on the left navigation pannel as shown below:
<img src="https://github.com/Alby084/Discord-GPT-Api-Bot/assets/99786431/18dc9f85-380e-4dc3-b6e8-ba29f31ed5a8" alt="drawing" width="220"/>

8. Select ``bot`` under ``OAuth2 URL Generator`` ``SCOPES`` and select ``Administrator`` under ``BOT PERMISSIONS`` ``GENERAL PERMISSIONS``.
9. Copy the generated discord link under ``GENERATED URL`` at the bottom of the page and paste this link into your web browsers address bar.
10. Follow the prompts to add your bot to any discord server where you have the ``Manage Server`` or ``Administrator`` permission.

# Getting ID's and GPT API key

### Getting your discord UID
1. On Discord, go to Settings > Advanced
2. Scroll down and make sure that Developer Mode is **on**
3. Exit settings and left click on your profile picture at the bottom left of discord (same place as the settings button) and click ``Copy User ID`` as shown below:

<img src="https://github.com/Alby084/Discord-GPT-Api-Bot/assets/99786431/a6de8ccb-206b-4656-abe2-35bb36751f7f" alt="drawing" width="380"/> <br>

### Getting discord server ID
1. On Discord, go to Settings > Advanced
2. Scroll down and make sure that Developer Mode is **on**
3. Exit settings and right click on the server(s) your bot is in
and click ``Copy Server ID`` as shown below:

<img src="https://github.com/Alby084/python-beginner-projects/assets/99786431/cd4e8349-b916-4f51-adc4-fd774465483f" alt="drawing" width="220"/> <br>

### Getting chat GPT API key
1. Visit the openai playground website settings page [Here](https://platform.openai.com/settings/organization/general).
2. Click the ``Create Project`` button at the bottom of the settings list as shown below:
<img src="https://github.com/Alby084/Discord-GPT-Api-Bot/assets/99786431/867e01a4-e628-4a36-9436-a56f5c30c12d" alt="drawing" width="220"/>

3. Name your project and click the ``Create`` button.
4. Navigate to the ``API keys`` page above the settings page on the left side navigation pannel. Alternatively you can click [Here](https://platform.openai.com/api-keys).
5. Click the ``Create new secret key`` button.
6. Choose ``You`` under ``Owned by``. Name your API key something descriptive and select the new project you just created in the ``Project`` dropdown. Set ``Permissions`` as ``All`` and click the ``Create secret key`` button as shown below:

<img src="https://github.com/Alby084/Discord-GPT-Api-Bot/assets/99786431/29ee99c3-5187-4082-b833-3c80580d0b4b" alt="drawing" width="220"/> <br>


### Note on GPT ``Credit balance``:
Ensure you have an available ``Credit balance``. You can check on the ``Billing`` page in ``Settings`` or by clicking [Here](https://platform.openai.com/settings/organization/billing/overview). If you do not have a ``Credit balance`` you will need to add money (credit) to your account otherwise this discord bot's chat GPT functionality will not work.
