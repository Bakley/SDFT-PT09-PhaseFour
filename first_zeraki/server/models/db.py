from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
    # fk_hand_gun_soldier_id_soldiers
)

db = SQLAlchemy(metadata=metadata)
