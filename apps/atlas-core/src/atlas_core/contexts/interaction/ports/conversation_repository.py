from typing import Protocol

from atlas_core.contexts.interaction.domain.conversation_turn import ConversationTurn


class ConversationRepositoryPort(Protocol):
    def save_turn(self, turn: ConversationTurn) -> None:
        ...
