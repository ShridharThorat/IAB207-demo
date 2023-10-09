# Purpose: Create the database - run whenever you update the models.py file
from travel import db, create_app
app = create_app()
ctx = app.app_context()
ctx.push()
db.create_all()
quit()