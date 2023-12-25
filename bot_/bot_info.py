import decorator

@decorator.message_text_decorator
def show_bot_info(Message,bot):
    return "Этот бот будет фиксировать результаты твоих тренеровок"