from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    telegram_token: str = '132asdsad65:GGHP82Pkl40U1233adsad9DXCxZc2lVQ'
    key_id: str = 'K2Lsdgvxxa23LD'
    key_secret: str = 'K2Lsdgvxxa23LD'
    authorization: str = 'jesafg231ASD2fgk'

    class Config:
        env_file = '.env'


settings = Settings()
