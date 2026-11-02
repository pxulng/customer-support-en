# Process: before and after

> Diagram for the fictional client. The "after" is the target to test, not a measured result.

## Current process (manual)

```mermaid
flowchart LR
    A["Request received<br/>(email or form)"] --> B["Manual triage<br/>by an advisor"]
    B --> C["Look up the procedure"]
    C --> D["Write the reply"]
    B --> E["Sensitive case"]
    E --> F["Escalation to a manager"]
    D --> G["Sent to the customer"]
    F --> G
```

## Target process (with the assistant)

```mermaid
flowchart LR
    A["Request received"] --> B["Assistant: classification<br/>(type, urgency, escalate yes/no)"]
    B -->|"Standard case"| C["Assistant: draft<br/>based on the cited procedure"]
    B -->|"Sensitive case or doubt"| E["Escalation to a manager<br/>+ holding message to the customer"]
    C --> D["Advisor: review<br/>and approval"]
    D --> G["Sent to the customer"]
    E --> G
```

**Principle:** the assistant never replies on its own. A human reviews every draft and handles every sensitive case.
