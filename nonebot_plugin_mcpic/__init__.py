import asyncio
import sqlite3
from io import BytesIO
from pathlib import Path

from httpx import AsyncClient
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="随机MC图",
    description="随机从推特获取并发送MC建筑图片",
    usage="使用命令:mc|建筑+数量 e.g: mc,建筑20",
    type="application",
    homepage="https://github.com/wlm3201/nonebot-plugin-mcpic",
    supported_adapters={"~onebot.v11"},
)
mcpic = on_command("mc", aliases={"MC", "建筑"})


@mcpic.handle()
async def handle_mcpic(args: Message = CommandArg()):
    async def init_db():
        db_url = "https://raw.githubusercontent.com/wlm3201/nonebot-plugin-mcpic/main/nonebot_plugin_mcpic/mcpic.db"
        async with AsyncClient() as client:
            r = await client.get(db_url)
            db_path.write_bytes(r.content)

    async def get_pic(name: Path):
        # url = f"{base_url}{name.stem}?format={name.suffix}&name=orig"
        url = f"{host}{name.stem}?format=jpg&name={size}"
        try:
            r = await client.get(url, headers={"host": "pbs.twimg.com"})
            return MessageSegment.image(BytesIO(r.content))
        except:
            pass

    text = args.extract_plain_text()
    num = min(int(text), 20) if (text := text[:2]).isdigit() and int(text) else 1
    size = "large" if num < 5 else "small" if num > 10 else "medium"
    db_path = Path(__file__).parent / "mcpic.db"
    if not db_path.exists():
        try:
            await init_db()
        except:
            return
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT name FROM images ORDER BY RANDOM() LIMIT ?", [num])
    rows = c.fetchall()
    conn.close()
    async with AsyncClient(verify=0) as client:
        host = "https://192.229.233.50/media/"
        tasks = [asyncio.create_task(get_pic(Path(row[0]))) for row in rows]
        segs = await asyncio.gather(*tasks)
    segs = list(filter(None, segs))
    await mcpic.finish(segs)
