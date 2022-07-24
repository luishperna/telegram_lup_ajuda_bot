# Importando bibliotecas/módulos necessários para o funcionamento
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
from os import getenv
import customization_variables.messages as messages
import customization_variables.information as information

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurando o cliente no telegram usando as variáveis de ambiente
bot = Client(
    'lup_ajuda_bot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
    )

# Teclado com opções de escolhas para o usuário clicar
@bot.on_message(filters.command('escolher'))
async def teclado_para_escolher(client, message):
    teclado = ReplyKeyboardMarkup(
        information.lista_escolhas_teclado, 
        resize_keyboard=True
    )
    await message.reply(messages.texto_opcoes_teclado,
        reply_markup = teclado
    )

# Interagindo com o comando /ambulancia digitado pelo usuário
@bot.on_message(filters.command('ambulancia'))
async def ambulancia(client, message):
    await message.reply(messages.texto_ambulancia)
    await bot.send_contact(message.chat.id,
        messages.texto_ambulancia, information.nome_contato_ambulancia
    )

# Interagindo com o comando /bombeiros digitado pelo usuário
@bot.on_message(filters.command('bombeiros'))
async def bombeiros(client, message):
    await message.reply(messages.texto_bombeiros)
    await bot.send_contact(message.chat.id,
        messages.texto_bombeiros, information.nome_contato_bombeiros
    )

# Interagindo com o comando /direitos digitado pelo usuário
@bot.on_message(filters.command('direitos'))
async def direitos(client, message):
    await message.reply(messages.texto_direitos)
    await bot.send_contact(message.chat.id,
        messages.texto_direitos, information.nome_contato_direitos
    )

# Interagindo com o comando /policia digitado pelo usuário
@bot.on_message(filters.command('policia'))
async def policia(client, message):
    await message.reply(messages.texto_policia)
    await bot.send_contact(message.chat.id,
        messages.texto_policia, information.nome_contato_policia
    )

# Interagindo com o comando /emocional digitado pelo usuário
@bot.on_message(filters.command('emocional'))
async def emocional(client, message):
    await message.reply(messages.texto_emocional)
    await bot.send_contact(message.chat.id,
        messages.texto_emocional, information.nome_contato_emocional
    )

# Interagindo com o comando /justica_mulher digitado pelo usuário
@bot.on_message(filters.command('justica_mulher'))
async def justica_mulher(client, message):
    await message.reply(messages.texto_justica_mulher)
    await bot.send_contact(message.chat.id,
        messages.texto_justica_mulher, information.nome_contato_justica_mulher
    )

# Interagindo com o comando /elogio digitado pelo usuário
@bot.on_message(filters.command('elogio'))
async def elogio(client, message):
    await message.reply(messages.texto_elogio)

# Interagindo com o comando /motivar digitado pelo usuário
@bot.on_message(filters.command('motivar'))
async def motivar(client, message):
    await message.reply(messages.texto_motivar)

# Interagindo com o comando /fofura digitado pelo usuário
@bot.on_message(filters.command('fofura'))
async def fofura(client, message):
    await bot.send_photo(message.chat.id,
        information.link_imagem_fofura
    )

# Interagindo com o comando /frase digitado pelo usuário
@bot.on_message(filters.command('frase'))
async def frase(client, message):
    await message.reply(messages.texto_frase)

# Interagindo com o comando /musica digitado pelo usuário
@bot.on_message(filters.command('musica'))
async def musica(client, message):
    await message.reply(messages.texto_musica)

# Filtrando imagens ou vídeos que o usuário possa enviar
@bot.on_message(filters.photo | filters.sticker | filters.animation | filters.video)
async def filtrando_imagens(client, message):
    await message.reply(messages.texto_imagens_ou_videos)

# Filtrando audios que o usuário possa enviar
@bot.on_message(filters.voice | filters.audio)
async def filtrando_audios(client, message):
    await message.reply(messages.texto_audios)

# Interagindo com o usuário a partir de qualquer mensagem enviada
@bot.on_message()
async def mensagens_gerais(client, message):
    await message.reply(messages.texto_geral)

# Executando o bot
bot.run()
