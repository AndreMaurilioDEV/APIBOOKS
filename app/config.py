class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///projeto.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class TestingConfig(Config):
    TESTING = True 
    SQLALCHEMY_DATABASE_URI = "sqlite:///memory:"