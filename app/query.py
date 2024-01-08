from models import Base
from app.connect import engine

Base.metadata.create_all(engine)