If (chat.chat_type != "private") {
  Bot.sendMessage("[Write me in private](https://t.me/" + bot.name + ")", {
    disable_web_page_preview: true
  })
  return
}

if (params) {
  if (params.includes("find")) {
    Bot.runCommand("/find " + params)
    return
  }
  if (params.includes("cct")) {
    Bot.runCommand("/ctr#ans " + params)
    return
  }
  if (params.includes("fincod")) {
    Bot.runCommand("/fincod " + params)
    return
  }
}
var int = [
  [
    {
      text: "🧡 Join Our Channel 💚",
      url: "https://t.me/igdealsbykashif"
    }
  ],
  [{ text: "✅ Proceed", callback_data: "/next" }]
]
Api.sendPhoto({
  photo: "https://ibb.co/X3KRcDn",
  caption:
    "👮<b> Hello Dear</b> " +
    user.first_name +
    "! \n\n<i>Please Join Channel to Access Bot</i>\n\n<b>💛 Join Our</b> <a href='https://t.me/GriefLKSeller'>Shop Channel</a>",
  parse_mode: "html",
  disable_web_page_preview: true,
  reply_markup: { inline_keyboard: int }
})

Bot.setProperty("Chat" + user.telegramid, chat, "json")
var adm = Bot.getProperty("adminID")
if (user.username != undefined) {
  var hh = "[@" + user.username + "]"
} else {
  var hh = ""
}
function touchingOwnLink() {
  Bot.sendMessage("*❌ Stop Clicking Your Own Link*")
}
function attractedByUser(refUser) {
  Api.sendMessage({
    chat_id: refUser.telegramid,
    text:
      "<b>🔋 You Got a New </b><a href='tg://user?id=" +
      user.telegramid +
      "'>Referral</a> " +
      hh +
      "",
    parse_mode: "html",
    disable_web_page_preview: true
  })
}
function alreadyStarted() {}

var tracks = {
  onTouchOwnLink: touchingOwnLink,
  onAtractedByUser: attractedByUser,
  onAlreadyAttracted: alreadyStarted
}

Libs.ReferralLib.track(tracks)
var new_user = User.getProperty("new_user")
if (!new_user) {
  var stat = Libs.ResourcesLib.anotherChatRes("status", "global")
  stat.add(1)
  Api.sendMessage({
    chat_id: 1481322134,
    text:
      "➕ <b>New User Notification</b> ➕\n\n👤<b>User:</b> <a href='tg://user?id=" +
      user.telegramid +
      "'>" +
      user.first_name +
      "</a> " +
      hh +
      "\n\n🆔<b> User ID :</b> <code>" +
      user.telegramid +
      "</code>",
    parse_mode: "html",
    disable_web_page_preview: true
  })
  User.setProperty("new_user", true, "boolean")
}


Ye photo kahah hai
