from flask import Blueprint, request, jsonify
from .chatbot import get_bot_response

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_message = data.get('message', '')
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})