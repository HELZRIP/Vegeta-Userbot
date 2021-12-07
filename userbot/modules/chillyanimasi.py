# credit @pikyus1
# own rendy

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.thanks(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "╔══╦╗────╔╗─╔╗╔╗\n"
                     "╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗\n"
                     "─║║║║║╬║║║╩║╚╗╔╣║║║║\n"
                     "─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")


@register(outgoing=True, pattern='^.malam(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╔═╦═╦╗╔═╦══╦═╦══╗\n"
                     "║═╣═╣║║╬║║║║╬╠╗╔╝\n"
                     "╠═║═╣╚╣║║║║║║║║║\n"
                     "╚═╩═╩═╩╩╩╩╩╩╩╝╚╝\n\n"
                     "╔══╦═╦╗╔═╦══╗\n"
                     "║║║║╬║║║╬║║║║\n"
                     "║║║║║║╚╣║║║║║\n"
                     "╚╩╩╩╩╩═╩╩╩╩╩╝")


@register(outgoing=True, pattern='^.rumah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAMBAR RUMAH**\n"
                     "╱◥◣\n"
                     "│∩ │◥███◣ ╱◥███◣\n"
                     "╱◥◣ ◥████◣▓∩▓│∩ ║\n"
                     "│╱◥█◣║∩∩∩ ║◥█▓ ▓█◣\n"
                     "││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║\n"
                     "๑۩๑๑۩๑๑ ۩๑๑۩๑▓๑۩๑๑۩๑")


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Punten**")


@register(outgoing=True, pattern='^.idiot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("\n╭╮╱╱╭╮"
                     "\n┃╰╮╭╯┃"
                     "\n╰╮╰╯╭┻━┳╮╭╮"
                     "\n╱╰╮╭┫╭╮┃┃┃┃"
                     "\n╱╱┃┃┃╰╯┃╰╯┃"
                     "\n╱╱╰╯╰━━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮"
                     "\n┃╭━╮┃"
                     "\n┃┃╱┃┣━┳━━╮"
                     "\n┃╰━╯┃╭┫┃━┫"
                     "\n┃╭━╮┃┃┃┃━┫"
                     "\n╰╯╱╰┻╯╰━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╭╮╱╱╱╭╮"
                     "\n┃╭━━╯╱┃┃╱╱╭╯╰╮"
                     "\n┃╰━━┳━╯┣┳━┻╮╭╯"
                     "\n┃╭━━┫╭╮┣┫╭╮┃┃"
                     "\n┃╰━━┫╰╯┃┃╰╯┃╰╮"
                     "\n╰━━━┻━━┻┻━━┻━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━╮╱╭╮"
                     "\n┃┃╰╮┃┃"
                     "\n┃╭╮╰╯┣━━╮"
                     "\n┃┃╰╮┃┃╭╮┃"
                     "\n┃┃╱┃┃┃╰╯┃"
                     "\n╰╯╱╰━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╱╱╱╱╭╮╱╭╮"
                     "\n╰╮╭╮┃╱╱╱╱╱┃┃╭╯╰╮"
                     "\n╱┃┃┃┣━━┳╮╭┫╰┻╮╭╯"
                     "\n╱┃┃┃┃╭╮┃┃┃┃╭╮┃┃"
                     "\n╭╯╰╯┃╰╯┃╰╯┃╰╯┃╰╮"


@register(outgoing=True, pattern="^.fak$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(".                       /¯ )")
        await e.edit(".                       /¯ )\n                      /¯  /")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")

CMD_HELP.update({
    "animasi":
    "`.rumah` ; `.malam` ; `.thanks` ; `.punten` ; `idiot` ; `.fak`\
    \nUsage: liat aja."
})
