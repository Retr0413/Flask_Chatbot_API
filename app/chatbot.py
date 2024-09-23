from transformers import pipeline
from flask import current_app
from flask_mysqldb import MySQL

# GPT-2モデルの読み込み
generator = pipeline('text-generation', model='gpt2')

# シンプルなAI応答の関数(AIモデルに置き換え可能)
def get_bot_response(user_message):
    response = generator(user_message, max_length=50, num_return_sequences=1)
    bot_response = response[0]['generated_text']

    # 会話をDBに保存
    save_conversation_to_db(user_message, bot_response)

    return bot_response

def save_conversation_to_db(user_message, bot_response):
    mysql = MySQL(current_app)
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO conversations (user_message, bot_response) VALUES (%s, %s)",
        (user_message, bot_response)
    )
    mysql.connection.commit()
    cur.close()