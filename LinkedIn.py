from linkedin_api import Linkedin

api = Linkedin('*****@gmail.com', '*****')

profile = input('input username:')

print(api.get_profile(profile))
