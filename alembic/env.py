from sqlalchemy import engine_from_config, pool
from sqlalchemy import MetaData

from alembic import context
from models import Base  # Замініть `your_model_module` на ім'я файлу, де знаходяться ваші моделі

# Цей блок коду завантажує конфігурацію з alembic.ini
config = context.config
config.set_main_option('sqlalchemy.url', 'postgresql://postgres:12345@localhost:5432/postgres')

# Підключення до бази даних
connectable = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix='sqlalchemy.',
    poolclass=pool.NullPool)

# Завантаження метаданих
target_metadata = MetaData()
target_metadata.reflect(bind=connectable)

# Задаємо метадані для Alembic
def run_migrations_online():
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
