# Agent Naming Standards

## Agent File Naming Convention

All agent prompt files MUST follow this naming pattern:

```
{scope}_{action}_{target}_agent.md
```

### Components:
- **scope**: The domain or area (e.g., model, view, security, data)
- **action**: The operation (e.g., add, modify, delete, create)
- **target**: What is being acted upon (e.g., fields, records, rules)

### Examples:
- `model_add_fields_agent.md` - Add fields to models
- `view_tree_add_fields_agent.md` - Add fields to tree views
- `view_form_add_fields_agent.md` - Add fields to form views
- `view_search_add_fields_agent.md` - Add fields to search views
- `security_add_rules_agent.md` - Add security rules
- `data_create_records_agent.md` - Create data records

### Usage File Naming:
Agent usage documentation follows:
```
{scope}_{action}_{target}_agent_usage.md
```

Example: `model_add_fields_agent_usage.md`

## Consistency Rules:
- Use snake_case for all components
- Keep names concise but descriptive
- Maintain consistent terminology across related agents
- Always end with `_agent.md` suffix
