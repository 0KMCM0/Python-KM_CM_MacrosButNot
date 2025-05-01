from typing import Any as _Any

__MACROS__: dict[ str, _Any ] = {}

def DEFINE( Name: str, Value: _Any = True ) -> None:
    __MACROS__[ Name ] = Value

def UNDEF( Name: str ) -> None:
    __MACROS__.pop( Name, None )

def IFDEF( Name: str ) -> bool:
    return Name in __MACROS__

def IFNDEF( Name: str ) -> bool:
    return Name not in __MACROS__

def GET( Name: str ) -> bool:
    return __MACROS__[ Name ]
