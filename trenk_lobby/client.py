import aiohttp
import asyncio

SERVER_URL = 'http://127.0.0.1:6666/trenk/hosts'

async def post(session, url, payload):
	async with session.post(url, data = payload) as response:
		return await response.text()
		
async def get(session, url):
	async with session.get(url) as response:
		return await response.text()

async def main(payload):
	async with aiohttp.ClientSession() as session:
		# html = await post(session, SERVER_URL, payload)
		html = await get(session, SERVER_URL)
		print(html)

loop = asyncio.get_event_loop()

while True:
	loop.run_until_complete(main(input()))