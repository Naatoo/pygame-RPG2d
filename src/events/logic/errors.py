from business_logic import LogicErrors
from business_logic.exceptions import InvalidOperationException, NotPermittedException


class Errors(LogicErrors):

    CANT_INTERACT_WITH_ITEM_TOO_FAR = InvalidOperationException(u'item is too far away.')
