# OctoBot

![octopus](https://user-images.githubusercontent.com/81108192/177814143-2e42c922-3908-4566-8145-f3b49916e114.png)

## Description
[Octobot](https://www.octobot.online/) is a powerful, fully modular open-source cryptocurrency trading robot.

This repository contains all the features of the bot (trading tools, evaluation engines, the backtesting toolkit, ...).
[Octobot's tentacles](https://github.com/Drakkar-Software/OctoBot-tentacles) contains the bot's strategies and user interfaces.

To install OctoBot with its tentacles, just use the [latest release for your system](https://github.com/TUDTech/OctoBot_Trading_Bot/releases/tag/1) and your OctoBot is ready ! 

Find the answers to the most common questions in [our FAQ](https://www.octobot.info/usage/frequently-asked-questions-faq).

## Your Octobot

![twitter-interface](https://user-images.githubusercontent.com/81108192/178025095-84f8cb67-1181-4cc1-82cd-d8a261bbeec1.png)

OctoBot is highly customizable using its configuration and tentacles system. 
You can build your own bot using the infinite [configuration](https://www.octobot.online/guides/#trading_modes) possibilities such as 
**technical analysis**, **social media processing** or even **external statistics management** like google trends.

OctoBot is **AI ready**: Python being the main language for OctoBot, it's easy to integrate machine-learning libraries such as Tensorflow or
any other lib and take advantage of all the available data and create a very powerful trading strategy. 

Octobot's main feature is **evolution** : you can [install](https://www.octobot.info/advanced_usage/tentacle-manager), 
[modify](https://developer.octobot.info/guides/customize-your-octobot) and even [create](https://developer.octobot.info/guides/developer-guide) any tentacle you want to build your ideal cryptocurrency trading robot. You can even share your OctoBot evolutions!

## Hardware requirements
- CPU : 1 Core / 1GHz
- RAM : 250 Mb
- Disk : 1 Gb

## Installation
OctoBot's installation is **very simple**... because **very documented** ! See the [installation guides](https://www.octobot.online/guides/#installation) for more info.

#### [With executable](https://www.octobot.info/installation/with-binary)
Follow the [2 steps installation guide](https://www.octobot.online/executable_installation/) 

#### [With Docker](https://www.octobot.info/installation/with-docker)
Follow the [docker installation guide](https://www.octobot.online/docker_installation/) 

In short :
```
docker run -itd --name OctoBot -p 80:5001 -v $(pwd)/user:/octobot/user -v $(pwd)/tentacles:/octobot/tentacles -v $(pwd)/logs:/octobot/logs drakkarsoftware/octobot:stable
```
And then open [http://localhost](http://localhost).

With docker-compose : 
```
docker-compose up -d
```
And then open [https://octobot.localhost](https://octobot.localhost).

#### [With pip](https://octobot.click/gh-pip-install)

In short :
```
pip install OctoBot>=0.4.1
Octobot
```

#### [With python sources](https://octobot.click/gh-python-install)
Follow the [python installation guide](https://www.octobot.online/python_installation/) 

In short :
```
git clone https://github.com/TUDTech/OctoBot_Trading_Bot.git
cd OctoBot
python3 -m pip install -Ur requirements.txt
python3 start.py
```

## Exchanges

![ascendex-logo](https://user-images.githubusercontent.com/81108192/178025918-3c58f2b6-92d3-46d5-85fb-c965b51ee766.png)
![binance-logo](https://user-images.githubusercontent.com/81108192/178025919-caf39ac0-6b9b-4b35-a17a-800f5315f12d.png)
![bitmex-logo](https://user-images.githubusercontent.com/81108192/178025922-d6c30fa4-eb92-4f2b-9743-5c2f9c7eec13.png)
![coinbasepro-logo](https://user-images.githubusercontent.com/81108192/178025924-2a0fe1b6-39cf-46c3-8dbc-4efdba02c2a3.png)
![ftx-logo](https://user-images.githubusercontent.com/81108192/178025926-9ec181d2-faac-4740-a3c6-b37334e6d202.png)
![gateio-logo](https://user-images.githubusercontent.com/81108192/178025930-fcb98c34-5aff-404c-91f6-b02d02e7d2c4.png)
![huobi-logo](https://user-images.githubusercontent.com/81108192/178025932-fc9a684f-db49-4b13-b2ec-ac0ca09af6b6.png)
![kucoin-logo](https://user-images.githubusercontent.com/81108192/178025933-1377ead6-088e-423d-b778-2bb9a3bb8e21.png)
![okex-logo](https://user-images.githubusercontent.com/81108192/178025936-21ec5445-6d43-4101-9c4f-7dc5a88c76ab.png)

Octobot supports many [exchanges](https://octobot.click/gh-exchanges) thanks to the ccxt. 
To activate trading on an exchange, just configure OctoBot with your api keys as described [on the exchange documentation](https://www.octobot.online/guides/#exchanges).

## Disclaimer
Do not risk money which you are afraid to lose. USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS 
AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS. 

Always start by running a trading bot in simulation mode and do not engage money
before you understand how it works and what profit/loss you should
expect.

Do not hesitate to read the source code and understand the mechanism of this bot.
