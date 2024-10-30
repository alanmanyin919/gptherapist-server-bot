"""

Sample bot that echoes back messages.

This is the simplest possible bot and a great place to start if you want to build your own bot.

"""

from __future__ import annotations
from constants import POE_ACCESS_KEY, BOT_NAME
from typing import AsyncIterable

import fastapi_poe as fp
from modal import App, Image, asgi_app
from devtools import PrettyFormat

pformat = PrettyFormat(width=85)


class EchoBot(fp.PoeBot):
    async def get_response(
        self, request: fp.QueryRequest
    ) -> AsyncIterable[fp.PartialResponse]:
        last_message = request.query[-1].content
        print(pformat(request))
        yield fp.PartialResponse(text=last_message)


REQUIREMENTS = ["fastapi-poe==0.0.48", "devtools==0.12.2"]
image = Image.debian_slim().pip_install(*REQUIREMENTS)
app = App("log-bot-poe")


@app.function(image=image)
@asgi_app()
def fastapi_app():
    bot = EchoBot()
    # see https://creator.poe.com/docs/quick-start#configuring-the-access-credentials
    app = fp.make_app(bot, access_key=POE_ACCESS_KEY, bot_name=BOT_NAME)
    # # app = fp.make_app(bot, allow_without_key=True)
    return app
