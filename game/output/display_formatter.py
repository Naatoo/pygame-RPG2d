def print_message(message):
    print(build_message(message))


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
def build_message(message):
    return ["{}", message, "{}"]