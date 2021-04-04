# Lebedev Discord Bot
# by Aleksandrov Alexander 26.01.20

import discord
import re
import random
from discord import File

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class MyClient(discord.Client):

	async def on_ready(self):
		print('Logged in as {0}!'.format(self.user))

		game = discord.Game("ну играет и играет")
		await client.change_presence(status=discord.Status.online, activity=game)

	async def on_message(self, message):

		print('Message from {0.author}: {0.content}'.format(message))

		channel = message.channel

		if not message.author.bot:

			if message.content.lower().startswith('лл команды'):
				await channel.send("```asciidoc\nКоманды:\n---------\nну <текст>\n---------\nлл <текст>\n---------\nll (две латинские л) <текст>\n---------\nлебедев <текст>\n---------\nлл/ну/ll/лебедев команды - список команд\n---------\nМожно написать любой текст, бот найдёт случайный глагол или случайное слово и преобразует его.\n---------\n```")

			if message.content.lower().startswith('ну команды'):
				await channel.send("```asciidoc\nКоманды:\n---------\nну <текст>\n---------\nлл <текст>\n---------\nll (две латинские л) <текст>\n---------\nлебедев <текст>\n---------\nлл/ну/ll/лебедев команды - список команд\n---------\nМожно написать любой текст, бот найдёт случайный глагол или случайное слово и преобразует его.\n---------\n```")

			if message.content.lower().startswith('ll команды'):
				await channel.send("```asciidoc\nКоманды:\n---------\nну <текст>\n---------\nлл <текст>\n---------\nll (две латинские л) <текст>\n---------\nлебедев <текст>\n---------\nлл/ну/ll/лебедев команды - список команд\n---------\nМожно написать любой текст, бот найдёт случайный глагол или случайное слово и преобразует его.\n---------\n```")

			if message.content.lower().startswith('лебедев команды'):
				await channel.send("```asciidoc\nКоманды:\n---------\nну <текст>\n---------\nлл <текст>\n---------\nll (две латинские л) <текст>\n---------\nлебедев <текст>\n---------\nлл/ну/ll/лебедев команды - список команд\n---------\nМожно написать любой текст, бот найдёт случайный глагол или случайное слово и преобразует его.\n---------\n```")

			if message.content.lower().startswith('ну') or message.content.lower().startswith('лл') or message.content.lower().startswith('лебедев') or message.content.lower().startswith('ll'):

				usermessage = []
				verbs = []

				channel = message.channel

				usermessage = re.sub("[^\w]", " ",  message.content).split()

				i = 0

				while i < len(usermessage):

					if usermessage[i].lower() == 'ну':
						usermessage.remove(usermessage[i])

					if usermessage[i].lower() == 'лл':
						usermessage.remove(usermessage[i])

					if usermessage[i].lower() == 'll':
						usermessage.remove(usermessage[i])

					if usermessage[i].lower() == 'я':
						usermessage[i] = 'ты'

					if usermessage[i].lower() == 'мы':
						usermessage[i] = 'вы'

					if usermessage[i].lower() == 'наши':
						usermessage[i] = 'ваши'

					if usermessage[i].lower() == 'наш':
						usermessage[i] = 'ваш'

					if usermessage[i].lower() == 'наше':
						usermessage[i] = 'ваше'

					if usermessage[i].lower().endswith('ать'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ить'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('еть'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('лся'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('лась'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ись'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ат'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ут'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ют'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ит'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ет'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ете'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ите'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ал'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ала'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ла'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('им'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ем'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ешь'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('ишь'):
						verbs.append(usermessage[i])
					if usermessage[i].lower().endswith('есть'):
						verbs.append(usermessage[i])

					if usermessage[i].lower().endswith('быть'):
						verbs.append(usermessage[i])

					if usermessage[i].lower().endswith('дам'):
						usermessage[i] = "дашь"
					if usermessage[i].lower().endswith('ем'):
						usermessage[i] = "ешь"

					if not usermessage[i].lower().endswith('ол'):

						if usermessage[i].endswith('л'):
							verbs.append(usermessage[i])

					i += 1


				secure_random = random.SystemRandom()

				if (len(verbs) == 0):

					randomword = secure_random.choice(usermessage)

					randomimage = random.randint(1,20)

					if randomimage == 1:
						img = Image.open("lebedev.jpg")

					if randomimage == 2:
						img = Image.open("lebedev2.png")

					if randomimage == 3:
						img = Image.open("lebedev3.png")

					if randomimage == 4:
						img = Image.open("lebedev4.png")

					if randomimage == 5:
						img = Image.open("lebedev5.png")

					if randomimage == 6:
						img = Image.open("lebedev6.png")

					if randomimage == 7:
						img = Image.open("lebedev7.png")

					if randomimage == 8:
						img = Image.open("lebedev8.png")

					if randomimage == 9:
						img = Image.open("lebedev9.png")

					if randomimage == 10:
						img = Image.open("lebedev10.png")

					if randomimage == 11:
						img = Image.open("lebedev11.png")

					if randomimage == 12:
						img = Image.open("lebedev12.png")

					if randomimage == 13:
						img = Image.open("lebedev13.png")

					if randomimage == 14:
						img = Image.open("lebedev14.png")

					if randomimage == 15:
						img = Image.open("lebedev15.png")

					if randomimage == 16:
						img = Image.open("lebedev16.png")

					if randomimage == 17:
						img = Image.open("lebedev17.png")

					if randomimage == 18:
						img = Image.open("lebedev18.png")

					if randomimage == 19:
						img = Image.open("lebedev19.png")

					if randomimage == 20:
						img = Image.open("lebedev20.png")

					draw = ImageDraw.Draw(img)

					font = ImageFont.truetype("Montserrat-Bold.ttf", 96)

					if len(randomword)>12:

						fillcolor="white"
						shadowcolor="black"

						text = "Ну длинное слово"
						text2 = "и длинное слово"
						
						x, y = 20, 685
						x1, y1 = 20, 780

						font = ImageFont.truetype("Montserrat-Bold.ttf", 72)

						draw.text((x-4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x-4, y+4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y+4), text, font=font, fill=shadowcolor)

						draw.text((x, y), text, font=font, fill=fillcolor)

						draw.text((x1-4, y1-4), text2, font=font, fill=shadowcolor)
						draw.text((x1+4, y1-4), text2, font=font, fill=shadowcolor)
						draw.text((x1-4, y1+4), text2, font=font, fill=shadowcolor)
						draw.text((x1+4, y1+4), text2, font=font, fill=shadowcolor)

						draw.text((x1, y1), text2, font=font, fill=fillcolor)

						img.save('sample-out.jpg')

						await channel.send(file=discord.File('sample-out.jpg'))


					if len(randomword)>=5 and len(randomword)<13:

						fillcolor="white"
						shadowcolor="black"

						text = "Ну " + randomword.lower()
						text2 = "и " + randomword.lower()

						x, y = 20, 685
						x1, y1 = 20, 780

						draw.text((x-4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x-4, y+4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y+4), text, font=font, fill=shadowcolor)

						draw.text((x, y), text, font=font, fill=fillcolor)

						draw.text((x1-4, y1-4), text2, font=font, fill=shadowcolor)
						draw.text((x1+4, y1-4), text2, font=font, fill=shadowcolor)
						draw.text((x1-4, y1+4), text2, font=font, fill=shadowcolor)
						draw.text((x1+4, y1+4), text2, font=font, fill=shadowcolor)

						draw.text((x1, y1), text2, font=font, fill=fillcolor)

						img.save('sample-out.jpg')

						await channel.send(file=discord.File('sample-out.jpg'))


					if len(randomword)<5:

						fillcolor="white"
						shadowcolor="black"

						x, y = 20, 780

						text = "Ну " + randomword.lower() + " и " + randomword.lower()

						draw.text((x-4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x-4, y+4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y+4), text, font=font, fill=shadowcolor)

						draw.text((x, y), text, font=font, fill=fillcolor)

						img.save('sample-out.jpg')

						await channel.send(file=discord.File('sample-out.jpg'))


				else:

					randomverb = secure_random.choice(verbs)

					randomimage = random.randint(1,20)

					if randomimage == 1:
						img = Image.open("lebedev.jpg")

					if randomimage == 2:
						img = Image.open("lebedev2.png")

					if randomimage == 3:
						img = Image.open("lebedev3.png")

					if randomimage == 4:
						img = Image.open("lebedev4.png")

					if randomimage == 5:
						img = Image.open("lebedev5.png")

					if randomimage == 6:
						img = Image.open("lebedev6.png")

					if randomimage == 7:
						img = Image.open("lebedev7.png")

					if randomimage == 8:
						img = Image.open("lebedev8.png")

					if randomimage == 9:
						img = Image.open("lebedev9.png")

					if randomimage == 10:
						img = Image.open("lebedev10.png")

					if randomimage == 11:
						img = Image.open("lebedev11.png")

					if randomimage == 12:
						img = Image.open("lebedev12.png")

					if randomimage == 13:
						img = Image.open("lebedev13.png")

					if randomimage == 14:
						img = Image.open("lebedev14.png")

					if randomimage == 15:
						img = Image.open("lebedev15.png")

					if randomimage == 16:
						img = Image.open("lebedev16.png")

					if randomimage == 17:
						img = Image.open("lebedev17.png")

					if randomimage == 18:
						img = Image.open("lebedev18.png")

					if randomimage == 19:
						img = Image.open("lebedev19.png")

					if randomimage == 20:
						img = Image.open("lebedev20.png")

					draw = ImageDraw.Draw(img)

					font = ImageFont.truetype("Montserrat-Bold.ttf", 96)

					if len(randomverb)>12:

						fillcolor="white"
						shadowcolor="black"

						text = "Ну длинное слово"
						text2 = "и длинное слово"

						x, y = 20, 685
						x1, y1 = 20, 780

						font = ImageFont.truetype("Montserrat-Bold.ttf", 72)

						draw.text((x-4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x-4, y+4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y+4), text, font=font, fill=shadowcolor)

						draw.text((x, y), text, font=font, fill=fillcolor)

						draw.text((x1-4, y1-4), text2, font=font, fill=shadowcolor)
						draw.text((x1+4, y1-4), text2, font=font, fill=shadowcolor)
						draw.text((x1-4, y1+4), text2, font=font, fill=shadowcolor)
						draw.text((x1+4, y1+4), text2, font=font, fill=shadowcolor)

						draw.text((x1, y1), text2, font=font, fill=fillcolor)

						img.save('sample-out.jpg')

						await channel.send(file=discord.File('sample-out.jpg'))

					if len(randomverb)>=5 and len(randomverb)<13:

						fillcolor="white"
						shadowcolor="black"

						text = "Ну " + randomverb.lower()
						text2 = "и " + randomverb.lower()

						x, y = 20, 685
						x1, y1 = 20, 780

						draw.text((x-4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x-4, y+4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y+4), text, font=font, fill=shadowcolor)

						draw.text((x, y), text, font=font, fill=fillcolor)

						draw.text((x1-4, y1-4), text2, font=font, fill=shadowcolor)
						draw.text((x1+4, y1-4), text2, font=font, fill=shadowcolor)
						draw.text((x1-4, y1+4), text2, font=font, fill=shadowcolor)
						draw.text((x1+4, y1+4), text2, font=font, fill=shadowcolor)

						draw.text((x1, y1), text2, font=font, fill=fillcolor)

						img.save('sample-out.jpg')

						await channel.send(file=discord.File('sample-out.jpg'))

					if len(randomverb)<5:

						fillcolor="white"
						shadowcolor="black"

						x, y = 20, 780

						text = "Ну " + randomverb.lower() + " и " + randomverb.lower()

						draw.text((x-4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y-4), text, font=font, fill=shadowcolor)
						draw.text((x-4, y+4), text, font=font, fill=shadowcolor)
						draw.text((x+4, y+4), text, font=font, fill=shadowcolor)

						draw.text((x, y), text, font=font, fill=fillcolor)

						img.save('sample-out.jpg')

						await channel.send(file=discord.File('sample-out.jpg'))


client = MyClient()
client.run('ваш токен')
