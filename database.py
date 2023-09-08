from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL (change this to your database URL)
DATABASE_URL = 'sqlite:///books_library.db'

# Create an SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a Session class for database interactions
Session = sessionmaker(bind=engine)

# Function to get a database session
def get_session():
    return Session()
