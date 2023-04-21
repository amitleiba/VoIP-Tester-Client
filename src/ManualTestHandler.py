from Message import Message
from ManualTestOpcode import ManualTestOpcode
from VTCPManualStatus import VTCPManualStatus

class ManualTestHndler:
    def __init__(self, updateManulTestLabel1, updateManulTestLabel2,
                updateManulTestLabel3):
        self._updateManulTestLabel1 = updateManulTestLabel1
        self._updateManulTestLabel2 = updateManulTestLabel2
        self._updateManulTestLabel3 = updateManulTestLabel3
        self.manualTestHandlers = {
            ManualTestOpcode.MANUAL_TEST_REGISTER_RES: self.onRegisterResualt,
            ManualTestOpcode.MANUAL_TEST_UNREGISTER_RES: self.onUnegisterResualt,
            ManualTestOpcode.MANUAL_TEST_CALL_RES: self.onCallResualt,
            ManualTestOpcode.MANUAL_TEST_HANGUP_RES: self.onHangupResualt,
            ManualTestOpcode.MANUAL_TEST_ANSWER_RES: self.onAnswerResualt,
            ManualTestOpcode.MANUAL_TEST_DECLINE_RES: self.onDeclineResualt
        }
    
    def handleManualTest(self, data: Message):
        opcode = ManualTestOpcode(data.read_integer())
        self.manualTestHandlers.get(opcode)(data)

    def onRegisterResualt(self, data: Message):
        # index = data.read_integer()
        # status = VTCPManualStatus(data.read_integer())
        # uri = data. read_string()

        # if(index == 0):
        #     if(status == VTCPManualStatus.OK):
        #         self._updateManulTestLabel1()
        pass

    def onUnegisterResualt(self, data: Message):
        # index = data.read_integer()
        # status = VTCPManualStatus(data.read_integer())
        pass

    def onCallResualt(self, data: Message):
        # index = data.read_integer()
        # status = VTCPManualStatus(data.read_integer())
        pass

    def onHangupResualt(self, data: Message):
        # index = data.read_integer()
        # status = VTCPManualStatus(data.read_integer())
        pass

    def onAnswerResualt(self, data: Message):
        # index = data.read_integer()
        # status = VTCPManualStatus(data.read_integer())
        pass

    def onDeclineResualt(self, data: Message):
        # index = data.read_integer()
        # status = VTCPManualStatus(data.read_integer())
        pass