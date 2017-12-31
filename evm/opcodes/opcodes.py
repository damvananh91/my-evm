from evm.opcodes.opcode import asOpcode
from evm.opcodes import opcodeValues
from evm.opcodes import opcodeLogics


OPCODES = {
    opcodeValues.ADD: asOpcode(
        logicFunc=opcodeLogics.add,
        mnemonic='ADD',
        gasCost=0
    ),
    opcodeValues.PUSH1: asOpcode(
        logicFunc=opcodeLogics.push1,
        mnemonic='PUSH1',
        gasCost=0
    ),
    opcodeValues.MSTORE: asOpcode(
        logicFunc=opcodeLogics.mstore,
        mnemonic='MSTORE',
        gasCost=0,
    ),
    opcodeValues.MLOAD: asOpcode(
        logicFunc=opcodeLogics.mload,
        mnemonic='MLOAD',
        gasCost=0,
    ),
    opcodeValues.SSTORE: asOpcode(
        logicFunc=opcodeLogics.sstore,
        mnemonic='SSTORE',
        gasCost=0
    ),
    opcodeValues.SLOAD: asOpcode(
        logicFunc=opcodeLogics.sload,
        mnemonic='SLOAD',
        gasCost=0
    ),
    opcodeValues.STOP: asOpcode(
        logicFunc=opcodeLogics.stop,
        mnemonic='STOP',
        gasCost=0
    )
}
