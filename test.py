import asyncio
import sqlite3
from io import BytesIO
from pathlib import Path

from httpx import AsyncClient
from PIL import Image

args = ""


async def handle_mcpic():
    async def fetch(name: Path):
        # url = f"{base_url}{name.stem}?format={name.suffix}&name=orig"
        url = f"{host}{name.stem}?format=jpg&name={size}"
        try:
            r = await client.get(url, timeout=10)
            return BytesIO(r.content)
        except:
            pass

    host = "https://pbs.twimg.com/media/"
    text = args
    num = min(int(text), 20) if (text := text[:2]).isdigit() and int(text) else 1
    size = "large" if num < 5 else "small" if num > 10 else "medium"
    db_path = Path(__file__) / "nonebot_plugin_mcpic" / "mcpic.db"
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM images ORDER BY RANDOM() LIMIT ?", [num])
    rows = c.fetchall()
    conn.close()
    async with AsyncClient() as client:
        tasks = [asyncio.create_task(fetch(Path(row[0]))) for row in rows]
        segs = await asyncio.gather(*tasks)
    segs = list(filter(None, segs))
    for seg in segs:
        Image.open(seg).show()


async def avgsize():
    async def fetch(name: Path):
        url = f"{host}{name.stem}?format=jpg&name={size}"
        try:
            r = await client.head(url, timeout=10)
            return int(r.headers["content-length"])
        except:
            pass

    host = "https://pbs.twimg.com/media/"
    num = 100
    size = "large"
    db_path = Path(__file__).parent / "mcpic.db"
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM images ORDER BY RANDOM() LIMIT ?", [num])
    rows = c.fetchall()
    conn.close()
    async with AsyncClient() as client:
        tasks = [asyncio.create_task(fetch(Path(row[0]))) for row in rows]
        sizes = await asyncio.gather(*tasks)
    sizes = list(filter(None, sizes))
    print(sum(sizes) / len(sizes))


asyncio.run(handle_mcpic())
