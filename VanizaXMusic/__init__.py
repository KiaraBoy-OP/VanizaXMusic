from VanizaXMusic.core.bot import Hotty
from VanizaXMusic.core.dir import dirr
from VanizaXMusic.core.git import git
from VanizaXMusic.core.userbot import Userbot
from VanizaXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
