# discord-life360-bot
A life360 bot for always know where your friends are without picking up the phone

[Life360](https://github.com/harperreed/life360-python) API provided by [Harper Reed](https://github.com/harperreed)

## Setting up
We use [Heroku](https://www.heroku.com/) to host the bot and the keys are kept into the config vars, accessed by the os.environ[] method.
If you want to make a bot like this of your own just create the config vars:
- **disc_key**: with a discord bot key
- **mapsAPI_key**: with a Google Maps API key
- **life360_usr**: with your Life360 email or username
- **life360_psw**: with your Life360 password

only with these set up the bot should function just fine =)

### License
This shit is [unlicensed](./LICENSE). :sunglasses:
