import asyncio
import aiohttp

from socialknife import SocialKnife

async def get_alarms():
    """Get sub count for Drzzs."""
    async with aiohttp.ClientSession() as session:
        socialknife = SocialKnife(LOOP, session)
        data = await socialknife.get_count('youtube', 'UC7G4tLa4Kt6A9e3hJ-HO8ng')
        print(data)

LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(get_alarms())