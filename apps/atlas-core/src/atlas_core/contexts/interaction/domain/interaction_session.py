from dataclasses import dataclass


@dataclass(slots=True)
class InteractionSession:
    session_id: str
    status: str

    def __post_init__(self) -> None:
        self.session_id = self.session_id.strip()
        self.status = self.status.strip()

        if not self.session_id:
            raise ValueError("session_id must not be empty")
        if not self.status:
            raise ValueError("status must not be blank")
