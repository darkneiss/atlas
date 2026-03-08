# Conversational Head

## Status

Draft

## Goal

Define the expected behaviour of Atlas in phase 1 as a conversational head.

Atlas must be able to receive user input, process it coherently, update its operational state, render a matching head expression, generate a spoken response, and return to an idle state.

## Scope

This specification covers the core interaction flow of Atlas phase 1:

- receiving user input as text or speech
- managing operational state transitions
- generating assistant replies
- updating head expression
- synthesizing spoken output
- persisting conversation and memory-related data

## Out of Scope

This specification does not cover:

- navigation
- body movement
- ROS2 integration
- external tools and automation
- scheduled tasks
- autonomous initiative
- advanced vision
- multiple simultaneous users
- distributed execution across several compute nodes

## Actors

- User
- Atlas Core
- Atlas Head

## Preconditions

- Atlas Core is running
- Atlas Head is connected
- Atlas identity is available
- memory storage is available
- speech services are available or mocked
- Atlas is not in ERROR state

## Main Interaction Flow

Before this flow, Atlas bootstraps from `BOOTING` to `IDLE`.

1. Atlas starts interaction in `IDLE`
2. The user provides an input to Atlas
3. Atlas transitions to `LISTENING`
4. Atlas captures or receives the user utterance
5. Atlas transitions to `THINKING`
6. Atlas loads relevant identity and memory context
7. Atlas generates an assistant reply
8. Atlas selects the appropriate head expression for the current state
9. Atlas transitions to `TALKING`
10. Atlas synthesizes spoken output
11. Atlas persists the conversation turn
12. Atlas stores any new memory facts or episodes derived from the interaction
13. Atlas transitions back to `IDLE`

## Operational States

Atlas phase 1 supports the following operational states:

- `BOOTING`
- `IDLE`
- `LISTENING`
- `THINKING`
- `TALKING`
- `SLEEPING`
- `ERROR`

## Head Expressions

Atlas Head supports at least the following expressions:

- `IDLE`
- `LISTENING`
- `THINKING`
- `TALKING`
- `CONFUSED`
- `ERROR`
- `SLEEPING`

## State to Expression Mapping

Unless explicitly overridden, the head expression must match the operational state:

- `IDLE` -> `IDLE`
- `LISTENING` -> `LISTENING`
- `THINKING` -> `THINKING`
- `TALKING` -> `TALKING`
- `SLEEPING` -> `SLEEPING`
- `ERROR` -> `ERROR`

## Business Rules

1. Atlas can only have one operational state at a time.
2. Atlas must not transition to `TALKING` unless an assistant reply has been generated.
3. Every conversation turn belongs to exactly one interaction session.
4. A conversation turn must contain the user utterance and the assistant reply.
5. A memory fact must include at least:
   - a source
   - a confidence value
6. The head expression must remain consistent with the current operational state unless an explicit override is requested.
7. A failure in speech synthesis must not corrupt the interaction session history.
8. A failure in memory persistence must be surfaced as an error or degraded result, not silently ignored.

## Acceptance Criteria

### AC-001
Given Atlas is in `IDLE`
When a user input is received
Then Atlas transitions to `LISTENING`

### AC-002
Given Atlas has received a valid user utterance
When processing begins
Then Atlas transitions to `THINKING`

### AC-003
Given Atlas is in `THINKING`
When a valid assistant reply is generated
Then Atlas transitions to `TALKING`

### AC-004
Given Atlas transitions to an operational state
When no explicit visual override exists
Then Atlas Head displays the matching expression

### AC-005
Given Atlas completes a conversation turn
When the reply has been synthesized or prepared
Then the turn is persisted with:
- session identifier
- user utterance
- assistant reply
- timestamps

### AC-006
Given a new memory fact is derived from the interaction
When it is persisted
Then it must include source and confidence

### AC-007
Given Atlas finishes a successful interaction
When the conversation turn is complete
Then Atlas returns to `IDLE`

### AC-008
Given Atlas cannot generate a valid reply
When the interaction fails
Then Atlas must not enter `TALKING`
And Atlas must transition to a safe state such as `IDLE` or `ERROR`

## Notes for TDD

The first implementation should be driven from tests.

Recommended first test targets:

1. operational state transitions
2. state-to-expression mapping
3. successful handling of a conversation turn
4. prevention of invalid transition to `TALKING`
5. persistence requirements for conversation turns
6. validation rules for memory facts

Recommended implementation order:

1. domain model for operational state and expression mapping
2. interaction session and conversation turn rules
3. application use case for handling a user utterance
4. persistence ports
5. adapters
