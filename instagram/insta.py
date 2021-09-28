from instapy import InstaPy

# login credentials
insta_username = 'dpkpr'
insta_password = 'Love261954'

# login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# follow by list
session.follow_by_list(['hardy', 'keenu'], times=1, sleep_delay=600, interact=False)
