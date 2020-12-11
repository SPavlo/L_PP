from logging.config import fileConfig
from alembic import context
import os,sys

current_path = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(current_path, '..')
sys.path.append(ROOT_PATH)

from migrate_models import *
from coder import engine


config = context.config
fileConfig(config.config_file_name)

def work():
    connectable = engine
    with connectable.connect() as con:
        context.configure(
            connection=con, target_metadata=BaseModel.metadata
        )

        with context.begin_transaction():
            context.run_migrations()
work()
