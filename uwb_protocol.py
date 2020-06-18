import threading
import datetime

class UWBFrame_Exception(Exception):
    def __init__(self, err='UWB Frame Error'):
        Exception.__init__(self, err)


class UWBFrame_NoValid_exception(UWBFrame_Exception):
    def __init__(self, err='UWB Frame is not received'):
        Exception.__init__(self, err)


class UWBFrame_NotComplete_Exception(UWBFrame_Exception):
    def __init__(self, err='UWB Frame is not complete.'):
        Exception.__init__(self, err)