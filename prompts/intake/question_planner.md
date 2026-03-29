Plan the smallest useful follow-up question set for the current blocked routes.

Rules:
- Prioritize required-field blockers before weak fields.
- Group related missing facts into one question when that reduces operator effort.
- Preserve original field paths for every proposed question.
- Do not exceed 10 questions in one pass.
- Do not ask for facts that are already present in normalized contracts or confirmed follow-up answers.
- If a route is blocked by `sales.target_titles_or_auto_discover_titles`, ask for either explicit target titles or confirmation that auto-discovery is allowed.
