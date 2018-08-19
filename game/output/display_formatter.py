def build_message(message):
    print_message(standard_format("+").format(message))


def standard_format(sign):
    deco = "{}".format(sign) * 50
    return "\n".join([deco, "{}", deco])


def print_message(message):
    print(message)
