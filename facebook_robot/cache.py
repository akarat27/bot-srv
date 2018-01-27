from flask_caching import Cache

def config_cache(app):
    cache = Cache(app, config={'CACHE_TYPE': 'redis'})