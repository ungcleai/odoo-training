# Code Template Knowledge Base

## Purpose
Verified, reusable code templates for Odoo 19 development. Always reference these templates before creating new code.

## Available Templates

### Models
- **base_model_template.py**: Standard Odoo model structure with common patterns
- **computed_field_template.py**: Computed field implementation with @api.depends
- **constraint_template.py**: Validation constraints with @api.constrains

### Views
- **list_view_template.xml**: List view structure (Odoo 19 standard)
- **form_view_template.xml**: Form view with sheet, groups, and notebook
- **search_view_template.xml**: Search view with filters and groupby

### Security
- **access_rights_template.csv**: Security access rights format

### Wizards
- **wizard_template.py**: TransientModel wizard pattern

## Usage Instructions
1. Identify the code type needed (model, view, security, etc.)
2. Reference the appropriate template from `.amazonq/templates/`
3. Adapt template placeholders to specific requirements
4. Maintain template structure and patterns
5. Never deviate from verified patterns without explicit user request

## Template Variables
Templates use these placeholders:
- `{MODEL_NAME}`: Model technical name (e.g., y_realestate_property)
- `{MODEL_CLASS}`: Python class name (e.g., YRealestateProperty)
- `{MODEL_DESCRIPTION}`: Human-readable description
- `{MODULE_NAME}`: Module technical name
- `{VIEW_ID}`: XML view ID
- `{FIELD_NAME}`: Field technical name
