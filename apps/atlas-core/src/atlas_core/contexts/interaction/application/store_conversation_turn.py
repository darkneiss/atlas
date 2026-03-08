from atlas_core.contexts.interaction.domain.conversation_turn import ConversationTurn
from atlas_core.contexts.interaction.ports.conversation_repository import (
    ConversationRepositoryPort,
)


class StoreConversationTurn:
    def __init__(self, repository: ConversationRepositoryPort) -> None:
        self._repository = repository

    def execute(
        self,
        session_id: str,
        user_utterance: str,
        assistant_reply: str,
    ) -> ConversationTurn:
        turn = ConversationTurn(
            session_id=session_id,
            user_utterance=user_utterance,
            assistant_reply=assistant_reply,
        )
        self._repository.save_turn(turn)
        return turn
