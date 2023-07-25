from collections import deque

from src.common.piece import Piece
from src.common.move import Move
from src.common.leap import Leap
from src.common.position import Position
from src.common.playergamestate import PlayerGameState
from src.common.board import Board
from src.common.gamepiece import GamePiece
from src.common.rules import Rules
from src.common.rulesstandard import RulesStandard
from src.common.rulesdumb import RulesDumb
from src.common.playerstate import PlayerState

class JsonConverter():
    '''
    JsonConverter is used to convert checkers data representations into json
    format to be sent and read over TCP connections.

        
    Piece will be represented as a string. 
    The string is that of the enum values: "O", "X", or " "

    GamePiece will be represented as a string. 
    The string will be a combination of the string represented of Piece and 
    a string representing if its a king. "K" if it is a king or "_" if its 
    not a king.

    Position will be represented as
    {'row': int, 'column': int}

    Leap will be represented as 
    {'start_position': Position, 
    'end_position': Position, 
    'capture_positions': [Position],
    'promote_positions': [Position]}

    Move will be represented as
    [Leap]

    Board will be represented as 
    {'row_size': int, 
    'column_size': int,
    'board': [[GamePiece]]}


    PlayerState will be represented as
    {'piece': Piece}

    PlayerGameState will be represented as
    {'board': Board,
    'rules': Rules,
    'players': [PlayerState],
    'turn': int}

    Rules will be represented as a string of
    'RulesStandard' or 'RulesDumb'  
    '''

    def piece_to_json(self, piece: Piece) -> str:
        '''
        Convert Piece to str

        Piece will be represented as a string. 
        The string is that of the enum values: "O", "X", or " "

        @params: piece: Piece

        @params: str
        '''

        return piece.value
    

    def json_to_piece(self, json: str) -> Piece:
        '''
        Convert str to Piece

        Piece will be represented as a string. 
        The string is that of the enum values: "O", "X", or " "

        @params: json: str

        @params: Piece
        '''

        return Piece(json)
    

    def move_to_json(self, move: Move) -> list:
        '''
        Convert move to json format

        Move will be represented as
        [Leap]

        Leap will be represented as 
        {'start_position': Position, 
        'end_position': Position, 
        'capture_positions': [Position],
        'promote_positions': [Position]}

        Position will be represented as
        {'row': int, 'column': int}
        '''

        json = []
        while move.leaps_remaining() > 0:
            json.append(self.__leap_to_json(move.get_next_leap()))
        return json
    

    def __leap_to_json(self, leap: Leap) -> dict:
        '''
        convert leap to json.

        Leap will be represented as 
        {'start_position': Position, 
        'end_position': Position, 
        'capture_positions': [Position],
        'promote_positions': [Position]}

        Position will be represented as
        {'row': int, 'column': int}
        
        @params: leap: Leap

        @returns: dict
        '''

        start_json = self.__position_to_json(leap.get_start_position())
        end_json = self.__position_to_json(leap.get_end_position())
        capture_json = []
        for position in leap.get_capture_positions():
            capture_json.append(self.__position_to_json(position))
        promote_position = []
        for position in leap.get_promote_positions():
            promote_position.append(self.__position_to_json(position))

        return {'start_position': start_json, 
                'end_position': end_json, 
                'capture_positions': capture_json, 
                'promote_positions': promote_position}
    

    def __position_to_json(self, position: Position) -> dict:
        '''
        convert position to json

        Position will be represented as
        {'row': int, 'column': int}

        @param: position

        @return: dict
        '''

        return {'row':position.get_row(),'column':position.get_column()}
    

    def json_to_move(self, json: list) -> Move:
        '''
        Convert json to Move

        Move will be represented as
        [Leap]

        Leap will be represented as 
        {'start_position': Position, 
        'end_position': Position, 
        'capture_positions': [Position],
        'promote_positions': [Position]}

        Position will be represented as
        {'row': int, 'column': int}

        @param: json: Dict

        @return: Move
        '''

        leaps = []
        for leap_json in json:
            leaps.append(self.__json_to_leap(leap_json))
        return Move(deque(leaps))
    

    def __json_to_leap(self, json: dict) -> Leap:
        '''
        convert json to Leap

        Leap will be represented as 
        {'start_position': Position, 
         'end_position': Position, 
         'capture_positions': [Position],
         'promote_positions': [Position]}

        Position will be represented as
        {'row': int, 'column': int}

        @param: json: dict

        @return: Leap
        '''

        start_position = self.__json_to_position(json['start_position'])
        end_position = self.__json_to_position(json['end_position'])
        capture_positions = []
        for json_position in json['capture_positions']:
            capture_positions.append(self.__json_to_position(json_position))
        promote_positions = []
        for json_position in json['promote_positions']:
            promote_positions.append(self.__json_to_position(json_position))

        return Leap(start_position, 
                    end_position, 
                    capture_positions, 
                    promote_positions)
    

    def __json_to_position(self, json: dict) -> Position:
        '''
        convert json to Position

        Position will be represented as
        {'row': int, 'column': int}

        @param: json: dict

        @return: Position
        '''

        return Position(json['row'], json['column'])
    

    def playergamestate_to_json(self, playergamestate: PlayerGameState) -> dict:
        '''
        Convert playergamestate to json.
        
        PlayerGameState will be represented as
        {'board': Board,
        'rules': Rules,
        'players': [PlayerState],
        'turn': int}
        
        Board will be represented as 
        {'row_size': int, 
        'column_size': int,
        'board': [[GamePiece]]}

        GamePiece will be represented as a string. 
        The string will be a combination of the string represented of Piece and 
        a string representing if its a king. "K" if it is a king or "_" if its 
        not a king.

        PlayerState will be represented as
        {'piece': Piece}    

        Rules will be represented as a string of
        'RulesStandard' or 'RulesDumb' 

        @param: playergamestate: PlayerGameState

        @return: dict
        '''

        return {'board': self.__board_to_json(playergamestate.get_board()),
                'rules': self.__rules_to_json(playergamestate.get_rules()),
                'players': self.__playerstates_to_json(playergamestate.get_players()),
                'turn': playergamestate.get_turn()}
    

    def __playerstates_to_json(self, playerstates: list[PlayerState]) -> list:
        '''
        convert list of playerstate into json

        PlayerState will be represented as
        {'piece': Piece}    

        @param: playerstates: list[PlayerState]

        @return: dict
        '''

        json = []
        for playerstate in playerstates:
            json.append({'piece': self.piece_to_json(playerstate.get_piece())})
        return json
    

    def __rules_to_json(self, rules: Rules) -> str:
        '''
        convert rules to json

        Rules will be represented as a string of
        'RulesStandard' or 'RulesDumb' 

        @param: rules: Rules

        @return: str
        '''

        if isinstance(rules, RulesStandard):
            return 'RulesStandard'
        elif isinstance(rules, RulesDumb):
            return 'RulesDumb'
    

    def __board_to_json(self, board: Board) -> dict:
        '''
        convert board to json

        Board will be represented as 
        {'row_size': int, 
        'column_size': int,
        'board': [[GamePiece]]}

        GamePiece will be represented as a string. 
        The string will be a combination of the string represented of Piece and 
        a string representing if its a king. "K" if it is a king or "_" if its 
        not a king.

        @param: board: Board

        @return: dict
        '''
        
        row_size = board.get_row_size()
        column_size = board.get_column_size()
        board_list = []
        for r in range(row_size):
            row = []
            for c in range(column_size):
                gamepiece = board.get_gamepiece(Position(r,c))
                row.append(self.__gamepiece_to_json(gamepiece))
            board_list.append(row)
        return {'row_size': row_size,
                'column_size': column_size,
                'board': board_list}
    

    def __gamepiece_to_json(self, gamepiece: GamePiece) -> str:
        '''
        convert gamepiece to json

        GamePiece will be represented as a string. 
        The string will be a combination of the string represented of Piece and 
        a string representing if its a king. "K" if it is a king or "_" if its 
        not a king.

        @param: gamepiece: GamePiece

        @return: str
        '''

        output = gamepiece.get_piece().value
        if gamepiece.is_king():
            output += "K"
        else:
            output += "_"
        return output
    

    def json_to_playergamestate(self, json: dict) -> PlayerGameState:
        '''
        Convert json to playergamestate.
        
        PlayerGameState will be represented as
        {'board': Board,
        'rules': Rules,
        'players': [PlayerState],
        'turn': int}
        
        Board will be represented as 
        {'row_size': int, 
        'column_size': int,
        'board': [[GamePiece]]}

        GamePiece will be represented as a string. 
        The string will be a combination of the string represented of Piece and 
        a string representing if its a king. "K" if it is a king or "_" if its 
        not a king.

        PlayerState will be represented as
        {'piece': Piece}    

        Rules will be represented as a string of
        'RulesStandard' or 'RulesDumb' 

        @param: playergamestate: PlayerGameState

        @return: dict
        '''

        return PlayerGameState(self.__json_to_board(json['board']),
                               self.__json_to_rules(json['rules']),
                               self.__json_to_players(json['players']),
                               json['turn'])
    

    def __json_to_players(self, json: list) -> PlayerState:
        '''
        convert json to list of playerstates

        PlayerState will be represented as
        {'piece': Piece}  

        @param: json
        
        @return: PlayerState
        '''

        players = []
        for playerstate_json in json:
            players.append(
                PlayerState(self.json_to_piece(playerstate_json['piece'])))  
        return players

    

    def __json_to_rules(self, json: str) -> Rules:
        '''
        convert json to Rules

        Rules will be represented as a string of
        'RulesStandard' or 'RulesDumb' 

        @param: json: str

        @return: Rules
        '''

        if json == 'RulesStandard':
            return RulesStandard()
        elif json == 'RulesDumb':
            return RulesDumb()
    

    def __json_to_board(self, json: dict) -> Board:
        '''
        convert json to board

        Board will be represented as 
        {'row_size': int, 
        'column_size': int,
        'board': [[GamePiece]]}

        GamePiece will be represented as a string. 
        The string will be a combination of the string represented of Piece and 
        a string representing if its a king. "K" if it is a king or "_" if its 
        not a king.

        @param: json: dict

        @return: Board
        '''

        row_size = json['row_size']
        column_size = json['column_size']
        board_list = []
        for row_json in json['board']:
            row = []
            for gamepiece_json in row_json:
                row.append(self.__json_to_gamepiece(gamepiece_json))
            board_list.append(row)
        return Board(row_size, column_size, board_list)
    

    def __json_to_gamepiece(self, json: str) -> GamePiece:
        '''
        convert json to GamePiece

        GamePiece will be represented as a string. 
        The string will be a combination of the string represented of Piece and 
        a string representing if its a king. "K" if it is a king or "_" if its 
        not a king.

        @param: json: str

        @return: GamePiece
        '''

        is_king = json[1] == 'K'
        return GamePiece(Piece(json[0]), is_king)
                




