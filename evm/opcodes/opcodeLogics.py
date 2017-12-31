from evm.exceptions import StopExecution

# 0s: STOP and Arithmetic Operations
def stop(computation):
    raise StopExecution('STOP opcode')

def add(computation):
    s0 = computation.stack.pop()
    s1 = computation.stack.pop()
    v1 = s0.toInt()
    v2 = s1.toInt()
    ret = (v1 + v2)
    if ret >=  2**256:
        ret = ret % 2*256
    ret = ret.to_bytes(32, 'big')
    computation.stack.push(ret)

# 50s: Stack, Memory, Storage and Flow operations
def push1(computation):
    value = computation.pc.next()
    computation.stack.push(value)

def sstore(computation):
    pass

def sload(computation):
    pass

def mstore(computation):
    s0 = computation.stack.pop()
    s1 = computation.stack.pop()
    pos = s0.toInt()
    if len(computation.memory) < pos + 31:
        computation.memory.extend(pos, 32)

    computation.memory.write(pos, s1.toBytes())

def mload(computation):
    s0 = computation.stack.pop()
    pos = s0.toInt()
    values = computation.memory.read(pos, 32)
    computation.stack.push(values)



