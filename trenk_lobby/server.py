from aiohttp import web
from aiohttp.abc import AbstractAccessLogger
import asyncio
import random

# Server URL: http://127.0.0.1:8080/
defPort = 9999

hosts = set([])
routes = web.RouteTableDef()

@routes.get('/trenk/hosts')
async def handleGet(request):
	print('received')
	ip = ''
	if len(hosts) > 0: # If ip present
		ip = random.sample(hosts, 1)[0] # Get random ip
		hosts.remove(ip) # Remove ip from set
	else: # Otherwise add client's own ip to list
		hosts.add(request.remote)
	print(hosts)
	# Client knows they are hosting if they receive no ip
	return web.Response(text = ip) 

@routes.delete('/trenk/hosts')
async def handleDelete(request):
	ip = request.remote
	hosts.remove(ip)
	return web.Response()

app = web.Application()
app.add_routes(routes)
web.run_app(app, port = defPort)