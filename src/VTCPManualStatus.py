from enum import Enum

class VTCPManualStatus(Enum):
    OK = 200

    #Client Error 4xx

    CLIENT_ERROR = 400
    CLIENT_ILLEGAL_ACTION = 401

    #Server Error 5xx

    SERVER_ERROR = 500 