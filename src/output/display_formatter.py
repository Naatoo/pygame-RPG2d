def formatter(sign="-", quantity=50):
    def decorate(func):
        def formatted(*args):
            result = func(*args)
            prepare_places = [item * quantity if len(item) < 3 else item for item in result]
            final_message = "\n".join(prepare_places).format(*(sign for _ in range(quantity * 2)))
            return final_message
        return formatted
    return decorate


@formatter(sign="+", quantity=25)
def move_mes(message):
    return ["{}", message, "{}"]


@formatter(sign="-", quantity=40)
def items_mes(message):
    return ["{}", message, "{}"]
