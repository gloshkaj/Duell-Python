from abc import ABCMeta
class player:
    __metaclass__ = ABCMeta
    '''
    Function name: play (overriden by human and computer)
    Parameters:
    a_board, the board object passed by reference. It contains the human and computer dice.
    a_view, the view object passed by reference for displaying the updated board.
    '''
    def play(self, a_board, a_view):
        # type: (object, object) -> object
        # type: (object, object) -> object
        #Convention to raise error if not implemented
        raise NotImplementedError