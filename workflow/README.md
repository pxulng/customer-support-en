# Workflow

`support_triage_and_draft_v1.json` is the n8n export of the workflow: a Code node ("Demandes") that supplies the 64 test requests, an Anthropic "Message a model" node with the v1 prompt, and a Code node ("Bloc de lecture") that parses the JSON answer and escalates for safety if it cannot be read. Import it in n8n, paste the chosen prompt from `prompts/` if you want another version, and keep "Maximum Number of Tokens" at 4000.

This export holds the **English translation** of the prompt and of the test requests. The measured results of this repository come from the French original of this workflow.
