import os
from os import getenv
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    def __init__(self):
        # load environment definition
        self.load_environment()

        self.DATABASE = getenv('DATABASE')
        self.DATABASE_HOST = getenv('DATABASE_HOST')
        self.DATABASE_PORT = int(getenv('DATABASE_PORT')) if getenv('DATABASE') else ""
        self.DATABASE_USERNAME = getenv('DATABASE_USERNAME')
        self.DATABASE_PASSWORD = getenv('DATABASE_PASSWORD')

    @staticmethod
    def load_environment():
        environment_config = {
            'dev': 'config-dev.env',
            'hmg': 'config-hmg.env',
            'prd': 'config-prd.env',
        }

        dotenv_override = {
            'dev': True,
            'hmg': False,
            'prd': False
        }

        stage_set = os.getenv('ENVIRON', 'dev')

        dotenv_path = os.path.join(BASE_DIR, environment_config[stage_set])

        override_system_env = dotenv_override[stage_set]
        load_dotenv(dotenv_path, override_system_env)
