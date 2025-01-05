from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)

# Define the Base class
Base = SQLModel

def get_session():
    with Session(engine) as session:
        yield session
