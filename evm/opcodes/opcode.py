import functools

class Opcode(object):
    mnemonic = None
    gasCost = None


    @classmethod
    def asOpcode(cls, logicFunc, mnemonic, gasCost):
        if gasCost:
            @functools.wraps(logicFunc)
            def wrappedLogicFunc(computation):
                # TODO: compute gas
                return logicFunc(computation)
        else:
            wrappedLogicFunc = logicFunc

        props = {
            '__call__': staticmethod(wrappedLogicFunc),
            'mnemonic': mnemonic,
            'gasCost': gasCost
        }
        opcodeClass = type("opcode:{}".format(mnemonic), (cls, ), props)

        return opcodeClass()


asOpcode = Opcode.asOpcode
