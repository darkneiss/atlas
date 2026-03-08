from dataclasses import dataclass


@dataclass(slots=True)
class ConversationTurn:
    session_id: str
    user_utterance: str
    assistant_reply: str

    def __post_init__(self) -> None:
        self.session_id = self.session_id.strip()
        self.user_utterance = self.user_utterance.strip()
        self.assistant_reply = self.assistant_reply.strip()

        if not self.session_id:
            raise ValueError("session_id must not be empty")
        if not self.user_utterance:
            raise ValueError("user_utterance must not be blank")
        if not self.assistant_reply:
            raise ValueError("assistant_reply must not be blank")
