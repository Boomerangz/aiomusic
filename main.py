from aiohttp import web
from music.music_list import music_list, music_list_ajax

import settings



app = web.Application()
app.router.add_static('/static/', settings.STATIC_DIR, name='static')
route = web.StaticRoute(None, '/static/', settings.STATIC_DIR)
route._method = 'HEAD'
app.router.register_route(route)

app.router.add_route('GET', '/', music_list)
app.router.add_route('GET', '/music/ajax/', music_list_ajax)

web.run_app(app)