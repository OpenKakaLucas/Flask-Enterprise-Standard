import time
import threading

class Snowflake:
    def __init__(self, machine_id: int):
        self.machine_id = machine_id
        self.sequence = 0
        self.last_timestamp = -1
        self.lock = threading.Lock()

        self.machine_id_bits = 10
        self.sequence_bits = 12

        self.max_machine_id = -1 ^ (-1 << self.machine_id_bits)
        self.max_sequence = -1 ^ (-1 << self.sequence_bits)

        self.machine_id_shift = self.sequence_bits
        self.timestamp_shift = self.sequence_bits + self.machine_id_bits

        # 自定义纪元（2024-01-01）
        self.epoch = 1704067200000

    def _timestamp(self):
        return int(time.time() * 1000)


    def generate(self):
        with self.lock:
            ts = self._timestamp()

            if ts == self.last_timestamp:
                self.sequence = (self.sequence + 1) & self.max_sequence
                if self.sequence == 0:
                    while ts <= self.last_timestamp:
                        ts = self._timestamp()
            else:
                self.sequence = 0

            self.last_timestamp = ts

            return (
                ((ts - self.epoch) << self.timestamp_shift)
                | (self.machine_id << self.machine_id_shift)
                | self.sequence
            )


snowflake = Snowflake(machine_id=1)