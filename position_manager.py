from datetime import datetime


class PositionManager:

    def __init__(self):

        self.active = {}

    def already_alerted(self, pair, candle_time):

        key = f"{pair}_{candle_time}"

        return key in self.active

    def register(self, pair, candle_time):

        key = f"{pair}_{candle_time}"

        self.active[key] = datetime.now()

    def clear_old(self):

        remove = []

        now = datetime.now()

        for key, value in self.active.items():

            age = (now - value).seconds

            if age > 7200:
                remove.append(key)

        for key in remove:
            del self.active[key]