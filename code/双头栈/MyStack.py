# 双头栈
class MyStack(object):

    def __init__(self):
        self.stack = []

    def r_push(self, x: int) -> None:
        self.stack.append(x)

    def l_push(self, x: int) -> None:
        self.stack[0:0] = [x]

    def l_pop(self) -> int:
        if self.stack:
            m = self.stack[0]
            del self.stack[0]
            return m
        else:
            raise LookupError('stack is empty')

    def r_pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            raise LookupError('stack is empty')
