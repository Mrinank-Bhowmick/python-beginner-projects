# CryptoTrackerBot
CryptoTrackerBot - check cryptocurrencies prices on telegram

## SUPPORTED COMMANDS:
```
/price - return price of crypto
/help - return help message
/rank - return coins rank
/graph - return coins graph
```
_Note: If this bot is added in groups as admin, in order to keep the chat clean of spam, after few seconds it deletes both the command issued by the user and the message sent by the bot._

## Screenshots:
<p align="left">
<img src="../master/resources/screenshots/screenshot1.jpg" width="250">
<img src="../master/resources/screenshots/screenshot2.jpg" width="250">
</p>

## How to install:

### On Linux:

- Move to the path where you want to create the virtualenv directory
```
cd path
```
- Create a folder containing the env named `ctbenv`
```
virtualenv -p python3 ctbenv 
```
- Install the bot from the zip
```
ctbenv/bin/pip install https://github.com/91dariodev/cryptotrackerbot/archive/master.zip
```
- Run the bot. The first parameter of the command is the token.
```
ctbenv/bin/cryptotrackerbot token
```
- To upgrade the bot:
```
ctbenv/bin/pip install --upgrade https://github.com/91dariodev/cryptotrackerbot/archive/master.zip
```
- To delete everything:
```
rm -rf ctbenv
```
