from linkedin_api import Linkedin

api = Linkedin('marwaosman9975@gmail.com', '*****')

profile = input('input username:')

print(api.get_profile(profile))
