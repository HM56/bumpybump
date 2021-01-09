# Auto-bumper for Disboard

![bump](https://disboard.org/images/bot-command-image-bump.png)

<p align="center"><img src="https://disboard.org/images/bot-command-image-bump.png"></p>

## Set it up
1. Install Python3 and Pip3, example:

```bash
sudo apt install python3 python3-pip
```

2. Install Discord.py

```bash
pip3 install discord
```

3. Download this repo 

```bash
git clone https://codeberg.org/SnowCode/auto-bump
cd auto-bump
```

4. Get the channel ID by right cliking on the channel where you want to send the bump commands, then click on "Copy ID".

5. Login on Discord in Firefox, press `CTRL` + `SHIFT` + `I`, then select `Storage`, then `Local Storage`, then search for "token" in the search bar, then press `CTRL` + `SHIFT` + `M`, finally, copy the token value.

6. Create a file called `config.py` with the following template:

```python
channel_id = 2345678 # Your channel id here
user_token = "aezoehzaidbzauihbuehizauieyeizae" # Your user token here
```

7. Save the file and start the bot

```bash
python3 bot.py
```

## Usage
Once you ran the command, the server can be automatically bumped. There are two special commands though

| Command | Meaning |
| ------- | ------- |
| `!pause` | Pause the bumping |
| `!continue` | Continue the bumping after a pause and tells you when the next bump will happen |

## Troubleshooting
### "Improper token"
This error message means you may changed your password or provided the wrong token to the configuration file. When you
change your password or revoke your token, you need to start the install again.

### "No module named 'discord'"
See in the installation, make sure you used pip3. If pip3 doesn't work, maybe try `pip install discord`. 

### "No module named 'asyncio'" 
This module should be installed by default, but if it's not, you can install it by running;

```bash
pip3 install asyncio
```

And if the command above fails:

```bash
pip install asyncio
```

### The bot is out of sync
If this happen, you may see in the `!continue` that the time doesn't change. Or the log says "Next bump in -1 day". In this case, try to manually bump and try again.
