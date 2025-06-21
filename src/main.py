import os
from utils import get_youtube_data, create_database, save_data_to_database
from src.config import config
from dotenv import load_dotenv


def main():
    # api_key = os.getenv('YT_API_KEY')
    load_dotenv(dotenv_path="C:/Users/vadimko4/PycharmProjects/Youtube_api_project/.env")
    api_key = os.getenv("YT_API_KEY")
    channel_ids = [
        'UC-OVMPlMA3-YCIeg4z5z23A',  # moscowpython
        # 'UCwHL6WHUarjGfUM_586me8w',  # highload
    ]
    params = config()

    data = get_youtube_data(api_key, channel_ids)
    create_database('youtube', params)
    # save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()