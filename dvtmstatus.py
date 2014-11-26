from threading import Thread
import sys

class Writer:

    def __init__(self, parent):
        self.value = ''
        self.parent = parent

    def write(self, value):
        self.value = value
        self.parent.write()

    def __str__(self):
        return str(self.value)


class StatusBar:

    def __init__(self, *values):
        self.items = []
        for v in values:
            if callable(v):
                writer = Writer(self)
                thread = Thread(target=v, args=(writer,), daemon=True)
                self.items.append((writer, thread))
            else:
                self.items.append((v, None))

    def write(self):
        print(''.join(str(i[0]) for i in self.items))
        sys.stdout.flush()

    def start(self):
        threads = [i[1] for i in self.items if i[1] is not None]
        for t in threads:
            t.start()

        for t in threads:
            t.join()
