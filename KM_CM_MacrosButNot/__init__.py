from typing import Any as _Any

__MACROS__: dict[ str, _Any ] = {}

def DEFINE( Name: str, Value: _Any = True ) -> None:
    __MACROS__[ Name ] = Value

def UNDEF( Name: str ) -> None:
    __MACROS__.pop( Name, None )

def IFDEF( Name: str ) -> bool:
    try:
        __MACROS__[ Name ]
        return True
    except: return False

def IFNDEF( Name: str ) -> bool:
    try:
        __MACROS__[ Name ]
        return False
    except: return True

def GET( Name: str ) -> bool:
    return __MACROS__[ Name ]
