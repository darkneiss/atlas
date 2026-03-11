from dataclasses import dataclass
from math import isnan


@dataclass(slots=True)
class MemoryFact:
    source: str
    confidence: float

    def __post_init__(self) -> None:
        if not isinstance(self.source, str):
            raise ValueError("source must be a string")

        self.source = self.source.strip()
        if isinstance(self.confidence, bool) or not isinstance(
            self.confidence,
            (int, float),
        ):
            raise ValueError("confidence must be numeric")

        self.confidence = float(self.confidence)

        if not self.source:
            raise ValueError("source must not be blank")
        if isnan(self.confidence):
            raise ValueError("confidence must be a valid number")
        if self.confidence < 0.0:
            raise ValueError("confidence must be greater than or equal to 0")
        if self.confidence > 1.0:
            raise ValueError("confidence must be less than or equal to 1")
