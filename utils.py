from tortoise import Tortoise

from db.models import Field, Well


async def initdb():
    await Tortoise.init(
        db_url='sqlite://:memory:',
        modules={'models': ['db.models']}
    )
    await Tortoise.generate_schemas()


async def populate():
    field = await Field.create(name='Carichan')
    well = await Well.create(name='99R', field=field)
    return 0
