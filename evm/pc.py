import io

class PC(object):
    def __init__(self, bytecodes):
        self._code = io.BytesIO(bytecodes)

    @property
    def pc(self):
        return self._code.tell()

    @pc.setter
    def pc(self, pos):
        return self._code.seek(min(len(self._code), pos))

    def next(self):
        return self._code.read(1)

    def seek(self, idx):
        anchor = self.pc
        self.pc = idx
        try:
            yield self
        finally:
            self.pc = anchor
