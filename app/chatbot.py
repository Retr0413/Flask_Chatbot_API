from flask import current_app
from flask_mysqldb import MySQL

# シンプルなAI応答の関数(AIモデルに置き換え可能)
def get_bot_response(user_message):
    bot_response = generate_bot_response(user_message) # AI応答生成関数
    save_conversation_to_db(user_message, bot_response)
    return bot_response

def generate_bot_response(user_massage):
    # ここにAIモデルを統合する
    if "hello" in user_massage.lower():
        return "Hello How can I assist you today?"
    return "i'm not sure how to response to that"

def save_conversation_to_db(user_message, bot_response):
    mysql = MySQL(current_app)
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO conversations (user_message, bot_response) VALUES (%s, %s)",
        (user_message, bot_response)
    )
    mysql.connection.commit()
    cur.close()