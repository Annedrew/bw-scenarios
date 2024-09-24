from bw2data.data_store import ProcessedDataStore
from bw2data.errors import UnknownObject

from .meta import scenarios


class Scenario(ProcessedDataStore):
    """
    {
        act.id: [
            (act.id, type, amount),
        ]
    }

    """
    _metadata = scenarios

    def __init__(self, name: str):
        super().__init__(name)

        try:
            self.exchanges = self.load()
        except UnknownObject:
            self.exchanges = {}

    def add_exchange(self, from_id, to_id, exchange_type, amount):
        from_act = self.exchanges.get(from_id, [])
        from_act.append((to_id, exchange_type, amount))
        self.exchanges[from_id] = from_act

    def save(self):
        self.write(self.exchanges)

    def process(self, **extra_metadata):
        return

