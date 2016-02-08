from aiohttp import web
import asyncio

from jinja2 import Environment, FileSystemLoader
from sqlalchemy import select
from settings import Tracks, conn

env = Environment(loader=FileSystemLoader('./templates'))

dsn = 'dbname=izzzymusic user=izzzy password=ooFxfq111 host=izzzymusic.cpez7q0oykol.us-west-2.rds.amazonaws.com'

page_size = 15

async def music_list(request):
    template = env.get_template('music_list.html')
    s = select([Tracks]).order_by('-id').limit(page_size)
    result = conn.execute(s)
    objects_list = [dict(zip(c.keys(), c.values())) for c in result]
    for obj in objects_list:
        obj['str'] = "%s - %s" % (obj['artist'], obj['title'])
    return web.Response(body=template.render(objects_list=objects_list).encode('utf-8'))


async def music_list_ajax(request):
    offset = int(request.GET['page']) * page_size if 'page' in request.GET else 0
    template = env.get_template('music_list_ajax.html')
    s = select([Tracks]).order_by('-id').limit(page_size).offset(offset)
    result = conn.execute(s)
    objects_list = [dict(zip(c.keys(), c.values())) for c in result]
    for obj in objects_list:
        obj['str'] = "%s - %s" % (obj['artist'], obj['title'])
    return web.Response(body=template.render(objects_list=objects_list).encode('utf-8'))