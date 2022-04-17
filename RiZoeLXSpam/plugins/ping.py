

from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Riz.on(events.NewMessage(pattern=".bot"))
@Riz2.on(events.NewMessage(pattern=".bot"))
@Riz3.on(events.NewMessage(pattern=".bot"))
@Riz4.on(events.NewMessage(pattern=".bot"))
@Riz5.on(events.NewMessage(pattern=".bot"))
@Riz6.on(events.NewMessage(pattern=".bot"))
@Riz7.on(events.NewMessage(pattern=".bot"))
@Riz8.on(events.NewMessage(pattern=".bot"))
@Riz9.on(events.NewMessage(pattern=".bot"))
@Riz10.on(events.NewMessage(pattern=".bot"))
async def bote):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Connecting.... To the Server !!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"<u>**Oғғɪᴄɪᴀʟ Sᴘᴀᴍ Mᴀᴄʜɪɴᴇ Oɴʟʏ Fᴏʀ Sᴛʀᴀɴɢᴇʀs Fᴀᴍɪʟʏ !!**</u>\n\n#𝐅𝐚𝐬𝐭𝐞𝐬𝐭_𝐒𝐩𝐚𝐦𝐦𝐢𝐧𝐠_𝐒𝐞𝐫𝐯𝐞𝐫.\n\n𝗦𝗲𝗿𝘃𝗲𝗿 𝗦𝗽𝗲𝗲𝗱 :-\n**{ms}** 𝙼𝚋𝙿𝚜")                       


# ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀
# ▒█▀▀▄ ▒█░░▒█ ░▒█░░
# ▒█▄▄█ ▒█▄▄▄█ ░▒█░░
