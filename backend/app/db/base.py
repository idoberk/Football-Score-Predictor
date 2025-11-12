# from sqlalchemy import create_engine, text
# from dotenv import load_dotenv
# import os

# load_dotenv()

# engine = create_engine(
#     url = os.getenv('DATABASE_URL'),
#     echo = True
# )

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass