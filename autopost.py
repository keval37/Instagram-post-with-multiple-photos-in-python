from instagrapi import Client
from instagrapi.types import Usertag, Location, List

# set instagram credentials 
ACCOUNT_USERNAME='test_user'
ACCOUNT_PASSWORD='******'

settings = {
   "uuids": {
      "phone_id": "57d64c41-a916-3fa5-bd7a-3796c1dab122",
      "uuid": "8aa373c6-f316-44d7-b49e-d74563f4a8f3",
      "client_session_id": "6c296d0a-3534-4dce-b5aa-a6a6ab017443",
      "advertising_id": "8dc88b76-dfbc-44dc-abbc-31a6f1d54b04",
      "device_id": "android-e021b636049dc0e9"
   },
   "cookies":  {},  # set here your saved cookies
   "last_login": 1596069420.0000145,
   "device_settings": {
      "cpu": "h1",
      "dpi": "640dpi",
      "model": "h1",
      "device": "RS988",
      "resolution": "1440x2392",
      "app_version": "117.0.0.28.123",
      "manufacturer": "LGE/lge",
      "version_code": "168361634",
      "android_release": "6.0.1",
      "android_version": 23
   },
   "user_agent": "Instagram 117.0.0.28.123 Android (23/6.0.1; ...US; 168361634)"
}
cl = Client(settings)
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
print(user_id)
user = cl.user_info_by_username(ACCOUNT_USERNAME)
print(user)

medias = cl.album_upload(paths=['/Users/keval/Downloads/django-logo-big.jpg','/Users/keval/Downloads/django-logo-big.jpg'], caption="Test caption for photo with #hashtags")