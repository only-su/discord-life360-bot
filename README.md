# discord-life360-bot
A life360 bot to always know where your friends are without picking up the phone

[Life360 API](https://github.com/harperreed/life360-python) provided by [Harper Reed](https://github.com/harperreed)

## Setting up
We use [Heroku](https://www.heroku.com/) to host the bot and the keys are kept into the config vars, accessed by the os.environ[] method.
If you want to make a bot like this of your own just upload these project to a heroku app and create the following config vars:
- **disc_key**: with a discord bot key
- **mapsAPI_key**: with a Google Maps API key
- **life360_usr**: with your Life360 email or username
- **life360_psw**: with your Life360 password

only with these set up the bot should function just fine =)

### ATTENTION
Note that the app is configured for our native language(PT-BR), we plan to make a special messages archive to hold the messages and facilitate the port to any language but by now it will require you to make cahnges inside the code.

### License
This shit is [unlicensed](./LICENSE). :sunglasses:
