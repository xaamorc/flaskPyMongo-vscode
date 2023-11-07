def mongo_db():
    from flask import current_app as app
    db = app.config.get("DEFAULT_MONGO_INSTANCE", None)
    assert(db), "Database non istanziato!"
    return db