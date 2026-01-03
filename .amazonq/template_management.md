# Template Management Guide

## Adding New Templates

### When to Create a Template
- Pattern is used 3+ times in the project
- Code has been verified and tested
- Pattern follows Odoo best practices
- Code represents a reusable structure

### Template Creation Process
1. Identify reusable code pattern
2. Extract common structure
3. Replace specific values with placeholders
4. Add explanatory comments
5. Save to appropriate `.amazonq/templates/` subdirectory
6. Update `template_index.md` with new template entry
7. Test template with real use case

### Placeholder Naming Convention
Use uppercase with underscores:
- `{MODEL_NAME}` - Technical model name
- `{MODEL_CLASS}` - Python class name
- `{MODEL_DESCRIPTION}` - Human-readable description
- `{MODULE_NAME}` - Module technical name
- `{VIEW_ID}` - XML view identifier
- `{FIELD_NAME}` - Field technical name
- `{TABLE_NAME}` - Database table name

### Template Categories

#### Current Categories
- `models/` - Python model classes
- `views/` - XML view definitions
- `security/` - Access rights and rules
- `wizards/` - TransientModel wizards

#### Expandable Categories
- `controllers/` - Web controllers
- `reports/` - Report templates
- `data/` - Data initialization
- `tests/` - Unit test patterns

## Updating Existing Templates

### Version Control
- Keep template history in comments
- Document changes with date and reason
- Maintain backward compatibility when possible

### Update Process
1. Identify improvement or fix needed
2. Update template file
3. Add change comment at top of template
4. Update `template_index.md` if needed
5. Review existing code using old template
6. Consider migration guide if breaking change

## Template Quality Standards

### Must Have
- Clear placeholder names
- Explanatory comments
- Proper indentation
- Complete structure (no partial patterns)
- Follows Odoo standards

### Must Not Have
- Hardcoded specific values
- Project-specific logic
- Incomplete patterns
- Deprecated Odoo patterns

## Usage Tracking

### Monitor Template Effectiveness
- Track which templates are used most
- Identify missing templates from common patterns
- Gather feedback on template clarity
- Update based on Odoo version changes

## Example: Adding New Template

```python
# File: .amazonq/templates/models/state_workflow_template.py

from odoo import models, fields, api

class {MODEL_CLASS}(models.Model):
    _name = '{MODEL_NAME}'
    _description = '{MODEL_DESCRIPTION}'
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', required=True)
    
    def action_confirm(self):
        self.write({'state': 'confirmed'})
    
    def action_done(self):
        self.write({'state': 'done'})
    
    def action_cancel(self):
        self.write({'state': 'cancelled'})
```

Then update `template_index.md`:
```markdown
### Models
- **state_workflow_template.py**: State workflow pattern with action methods
```

## Maintenance Schedule
- Monthly: Review template usage
- Quarterly: Update for Odoo version changes
- As needed: Add new patterns
- Annually: Archive unused templates
