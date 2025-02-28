from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
ADMIN_ID = env('ADMIN_ID')
BASE_URL = 'http://127.0.0.1:8000/api/v1'
