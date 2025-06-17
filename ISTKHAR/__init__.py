from ISTKHAR.core.bot import MD
from ISTKHAR.core.dir import dirr
from ISTKHAR.core.git import git
from ISTKHAR.core.userbot import Userbot
from ISTKHAR.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = MD()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
