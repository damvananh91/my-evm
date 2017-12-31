import itertools
import functools


from evm.exceptions import (
    FullStack,
    InsufficientStack,
    InvalidOpcode,
    StopExecution
)

from evm.opcodes import opcodes
from evm.pc import PC
from evm.utils import ceil32

class BaseComputation(object):
    def __init__(self, opcodes):
        self.opcodes = opcodes

        self.memory = Memory()
        self.stack = Stack()

    def mimic(self, bytecodes):
        """
        Print out EVM stack, memory, PC, OPcode during EVM execution
        :param bytecodes:  string of bytecod
        :return:  None
        """
        def split2(txt):
            while txt:
                yield txt[:2]
                txt = txt[2:]

        bytecodes = bytes(list(map(functools.partial(int, base=16), split2(bytecodes))))
        print('Bytecodes: ', ','.join('{:02X}'.format(b) for b in bytecodes))
        self.pc = PC(bytecodes)

        while True:
            try:
                print('PC: ', self.pc.pc)
                oc = ord(self.pc.next())
                ocFunc = self.opcodes[oc]
                print('Opcode: {}'.format(ocFunc.mnemonic))
                ocFunc(self)
                print('Memory: \n', self.memory)
                print('Stack: \n', self.stack)

            except KeyError as e:
                raise InvalidOpcode('Unknown opcode {}'.format(e))
            except StopExecution as e:
                break




class Word(object):
    def __init__(self, w):
        if len(w) < 32:
            w = bytes([0] * (32 - len(w))) + w
        self._word = bytes(w)

    def __str__(self):
        return ','.join(['{:02X}'.format(b) for b in self._word])

    def toInt(self):
        return int.from_bytes(self._word, 'big')

    def toBytes(self):
        return self._word

class Memory:
    def __init__(self):
        self._bytes = bytearray()

    def __len__(self):
        return len(self._bytes)

    def __str__(self):
        return ','.join('{:02X}'.format(b) for b in self._bytes)
    def extend(self, startPos, size):
        """
        Extend memory in chunk of 32 bytes

        :param startPos:  starting index
        :param size: size to be at least extended
        :return:  None
        """
        if size == 0:
            return

        newSize = ceil32(startPos + size)
        if newSize <= len(self):
            return

        self._bytes.extend(itertools.repeat(0, newSize - len(self)))

    def read(self, startPos, size):
        """
        Read memory

        :param startPos:  starting index
        :param size: size to be read
        :return:  bytes of values
        """
        return bytes(self._bytes[startPos:startPos+size])

    def write(self, startPos, values):
        """
        Write to memory. Ensure bytes to be extended to required length before this operation.

        :param startPos:  starting index
        :param values: list of values to write into
        :return:  boolean value based on success
        """

        if len(self) < startPos + len(values):
            return False
        else:
            for idx, v in enumerate(values):
                self._bytes[startPos + idx] = v
            return True

class Stack:
    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def __str__(self):
        return "\n".join(str(w) for w in self._stack)

    def push(self, x):
        if len(self._stack) > 1023:
            raise FullStack('Stack limit reached')
        self._stack.append(Word(x))

    def pop(self):
        try:
            return self._stack.pop()
        except IndexError:
            raise InsufficientStack()

    def dup(self, position):
        idx = -1 * position
        try:
            self._stack.push(self._stack[idx])
        except IndexError:
            raise InsufficientStack('Insufficient stack items for DUP{0}'.format(position))


if __name__ == "__main__":
    bc = BaseComputation(opcodes.OPCODES)
    # bc.mimic('604060205260205100')
    bc.mimic('604060200100')
