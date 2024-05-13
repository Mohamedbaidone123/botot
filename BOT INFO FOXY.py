


#Youtube : The Foxy
#Instagram : @the_foxy999
#Telegram : the foxy

import requests  
import datetime
import telebot
import time
import os
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7022806622:AAHv1yEY2OP6ARQaq_plLfNgqkmRUkpb8ic'
admin_ids = ['2093600923']

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda msg: True)
def main(msg: Message):
    print(msg.text)
    os.system('clear')
    
    if msg.text.startswith("/start"):
        keyboard = InlineKeyboardMarkup()
        url_button = InlineKeyboardButton(text="᧒᥆Ꭵꪀ ꪀ᥆᭙ 👀", url="https://t.me/SecretShieldd")
        keyboard.add(url_button)
        bot.reply_to(msg, "𝗪𝗘𝗟𝗖𝗢𝗠𝗘 👋 \n𝗙𝗢𝗥 𝗚𝗘𝗧 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 𝗔𝗕𝗢𝗨𝗧 𝗜𝗗 ℹ 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 ++", reply_markup=keyboard)
    
    if msg.text.startswith("++"):
        print(msg.text)
        os.system('clear')
        
        target_id = msg.text[2:]
        try: 
            target_id = int(target_id)
        except: 
            bot.reply_to(msg, "لم يتم التعرف على الايدي!!")
            return 
        

        quoted_message = bot.reply_to(msg, "⧉ 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗜𝗡𝗙𝗢...⌛")
        
        url =  "https://freefireapi.com.br/api/search_id?id={}&region=sg".format(target_id)
        response = requests.get(url=url)
        target_id_data = response.json()
        
        info = info_message(target_id_data)
        
        keyboard = InlineKeyboardMarkup()
        url_button = InlineKeyboardButton(text="⧉ ƒ᥆ᖇ ꪔ᥆ᖇᥱ Ꭵꪀƒ᥆ 👀", url="https://t.me/SecretShieldd")
        keyboard.add(url_button)
        
        bot.edit_message_text(chat_id=msg.chat.id, message_id=quoted_message.message_id, text=info, reply_markup=keyboard, parse_mode='HTML')


def info_message(target_id_data):
    basic_info = target_id_data.get('basicInfo', {})
    social_info = target_id_data.get('socialInfo', {})
    clan_basic_info = target_id_data.get('clanBasicInfo', {})
    profile_info = target_id_data.get('profileInfo', {})
    captain_basic_info = target_id_data.get('captainBasicInfo', {})
    
    info_message = f"⦉ 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗜𝗡𝗙𝗢 ⦊\n\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗜𝗗 ➩ <code>{basic_info.get('accountId', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗡𝗔𝗠𝗘 ➩ <code>{basic_info.get('nickname', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗘𝗫𝗣 ➩ <code>{basic_info.get('exp', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗟𝗜𝗞𝗘𝗗 ➩ <code>{basic_info.get('liked', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗕𝗜𝗢 ➩ <code>{social_info.get('signature', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗟𝗔𝗡𝗚 ➩ <code>{social_info.get('language', 'None')}</code>\n\n" \
                   f"⦉ 𝗚𝗨𝗜𝗟𝗗 𝗜𝗡𝗙𝗢 ⦊\n\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗖𝗟𝗔𝗡 𝗜𝗗 ➩ <code>{clan_basic_info.get('clanId', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗟𝗘𝗔𝗗𝗘𝗥 ➩ <code>{clan_basic_info.get('captainId', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗡𝗔𝗠𝗘 ➩ <code>{clan_basic_info.get('nickname', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗟𝗘𝗩𝗘𝗟 ➩ <code>{clan_basic_info.get('clanLevel', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗖𝗔𝗣𝗔𝗖𝗜𝗧𝗬 ➩ <code>{clan_basic_info.get('capacity', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗠𝗘𝗠𝗕𝗘𝗥 ➩ <code>{clan_basic_info.get('memberNum', 'None')}</code>\n\n" \
                   f"⦉ 𝗥𝗔𝗡𝗞𝗘𝗗 𝗜𝗡𝗙𝗢 ⦊\n\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗥𝗔𝗡𝗞𝗘𝗗 𝗣𝗢𝗜𝗡𝗧 ➩ <code>{basic_info.get('rankingPoints', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗦𝗘𝗔𝗦𝗢𝗡 ➩ <code>{basic_info.get('seasonId', 'None')}</code>\n\n" \
                   f"⦉ 𝗣𝗥𝗢𝗙𝗜𝗟𝗘 𝗜𝗡𝗙𝗢 ⦊\n\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗔𝗩𝗔𝗧𝗔𝗥 🆔 ➩ <code>{profile_info.get('avatarId', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗦𝗞𝗜𝗡 𝗖𝗢𝗟𝗢𝗥 ➩ <code>{profile_info.get('skinColor', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗖𝗟𝗢𝗧𝗛𝗘𝗦 ➩ <code>{profile_info.get('clothes', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗜𝗦𝗦𝗘𝗟𝗘𝗖𝗧𝗘𝗗 ➩ <code>{profile_info.get('isSelected', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗣𝗩𝗘𝗣𝗥𝗜𝗠𝗔𝗥𝗬𝗪𝗘𝗔𝗣𝗢𝗡 ➩ <code>{profile_info.get('pvePrimaryWeapon', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗘𝗡𝗗𝗧𝗜𝗠𝗘 ➩ <code>{profile_info.get('endTime', 'None')}</code>\n\n" \
                   f"⦉ 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗜𝗡𝗙𝗢 ⦊\n\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗡𝗔𝗠𝗘 ➩ <code>{captain_basic_info.get('nickname', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗟𝗘𝗩𝗘𝗟 ➩ <code>{captain_basic_info.get('level', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗘𝗫𝗣 ➩ <code>{captain_basic_info.get('exp', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗥𝗔𝗡𝗞 ➩ <code>{captain_basic_info.get('rank', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗥𝗔𝗡𝗞𝗜𝗡𝗚 𝗣𝗢𝗜𝗡𝗧𝗦 ➩ <code>{captain_basic_info.get('rankingPoints', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗝𝗢𝗕 𝗥𝗢𝗟𝗘 ➩ <code>{captain_basic_info.get('role', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗕𝗔𝗗𝗚𝗘 𝗖𝗢𝗨𝗡𝗧 ➩ <code>{captain_basic_info.get('badgeCnt', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗕𝗔𝗗𝗚𝗘 𝗜𝗗 ➩ <code>{captain_basic_info.get('badgeId', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗦𝗘𝗔𝗦𝗢𝗡 ➩ <code>{captain_basic_info.get('seasonId', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗟𝗜𝗞𝗘𝗗 ➩ <code>{captain_basic_info.get('liked', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗟𝗔𝗦𝗧 𝗟𝗢𝗚𝗜𝗡 ➩ <code>{captain_basic_info.get('lastLoginAt', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗖𝗦 𝗥𝗔𝗡𝗞 ➩ <code>{captain_basic_info.get('csRank', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗖𝗦 𝗥𝗔𝗡𝗞𝗜𝗡𝗚 𝗣𝗢𝗜𝗡𝗧𝗦 ➩ <code>{captain_basic_info.get('csRankingPoints', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗠𝗔𝗫 𝗥𝗔𝗡𝗞 ➩ <code>{captain_basic_info.get('maxRank', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗖𝗦 𝗠𝗔𝗫 𝗥𝗔𝗡𝗞 ➩ <code>{captain_basic_info.get('csMaxRank', 'None')}</code>\n" \
                   f"<a href='https://t.me/SecretShieldd'><u>⎚</u></a> 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗔𝗧 ➩ <code>{captain_basic_info.get('createAt', 'None')}</code>"
    
    return info_message



bot.infinity_polling()
