import discord
import random
import asyncio
from discord.ext import commands
from discord import app_commands

class aclient(discord.Client):
    def __init__(self):
         super().__init__(intents=discord.Intents.default())
         self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync() #id = None ou corta (guild = discord.Object(id = 1050218275583316018)
            self.synced = True
        print(f'estou on como {self.user}.')

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name = 'teste', description = 'verifica se estou on')
async def slash1(interaction: discord.Interaction):
    await interaction.response.send_message(f'olá {interaction.user.mention}, estou funcionando!')

@tree.command(name = 'namoro', description = 'selecione alguém e veja sua chance de namorar')
async def slash2(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f'há {random.randint(1,101)}% de chance de {interaction.user.mention} e {name} namorarem  💘')    

@tree.command(name = 'biceps', description = 'mede o tamanho do seu braço')
async def slash6(interaction: discord.Interaction):
    await interaction.response.send_message(f'{interaction.user.mention} tem {random.randint(1,101)}cm de braço 💪')

@tree.command(name = 'pesca' or 'pescar', description = 'o que será que vc pesca?')
async def slash3(interaction: discord.Interaction):
    fish_list = ['um salmão  :tropical_fish: ',
    f'um baiacú  :blowfish: ',
    f'um sapo  :frog: ',
    f'um tubarão  :shark: ',
    f'um peixe  :fish: ',
    f'um peixe-gato  :smirk_cat: ',
    f'uma sereia  :mermaid: ',
    f'um polvo  :octopus: ',
    f'um jacaré  :crocodile: ',
    f'uma tartaruga  🐢 ',
    f'um golfinho  🐬 ',
    f'uma baleia  🐋 ',
    f'uma lagartixa  🦎 ',
    f'uma foca  🦭 ',
    f'uma lontra  🦦 ',
    f'uma lagosta  🦞 ',
    f'um camarão  🦐 ',
    f'um caranguejo  🦀 ',
    f'um cocô  💩 ',
    f'uma lula  🦑 ']
    await interaction.response.send_message(f' :fishing_pole_and_fish: {interaction.user.mention} você pescou {random.choice(fish_list)} de {random.randint(1,151)}cm!')

@tree.command(name = 'violencia' or 'violência', description = 'quer cometer um ato de violência contra quem?')
async def slash4(interaction: discord.Interaction, name: str):
    vio_list = [f'quebrou o teclado na cabeça de {name}  :keyboard: ',
    f'deu uma flechada no joelho de {name}  :bow_and_arrow: ',
    f'acertou {name} com um taco de baseball  :cricket_game: ',
    f'acertou {name} com uma chave inglesa  :wrench: ',
    f'dividiu {name} com um machado, bem ao meio  :axe: ',
    f'esmagou {name} no muro com um carro  :blue_car:  vruumm ',
    f'deu uma raquetada na nuca de {name}  :badminton: ',
    f'tacou uma pedra no olho de {name}  🪨 ',
    f'arrancou os cabelos de {name}  🧑‍🦲 ',
    f'deu um puxão de calcinha em {name}  👙 ',
    f'deu uma tijolada em {name}  🧱 ',
    f'mordeu a orelha de {name}  👂 ',
    f'tacou um chinelo em {name}  🩴 ',
    f'deu uma cadeirada em {name}  🪑 ',
    f'tacou um relógio em {name}  🕰️ ',
    f'tacou o mouse em {name}  🖱️ ',
    f'tacou bosta de vaca em {name}  🐄💩 ',
    f'tacou um balde de água gelada em {name}  🪣🌊 ',
    f'tacou uma manga em {name}  🥭 ',
    f'tacou uma roda em {name}  🛞 ',
    f'tacou uma árvore de natal em {name}  🎄 ',
    f'deu um golpe de judô em {name}  🥋 ',
    f'fez {name} desaparecer com um soco  🪄 ',
    f'tacou uma engrenagem em {name}  ⚙️ ',
    f'acertou {name} com um boomerang na ida e na volta  🪃 ',
    f'passou com um carrinho de compras por cima de {name}  🛒 ',
    f'deu uma skatada nas costas de {name}  🛹 ',
    f'levou {name} para outro planeta na bica  🛸 ',
    f'derrubou a casa de {name} com um trator  🚜 ',
    f'prendeu {name} em uma âncora e jogou no mar  ⚓ ',
    f'tacou uma vassoura em {name}  🧹 ',
    f'tacou um violino em {name}  🎻 ',
    f'bateu em {name} com um caixão  ⚰️ ']
    await interaction.response.send_message(f'{interaction.user.mention} {random.choice(vio_list)} ')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

client.run('T0KEN')