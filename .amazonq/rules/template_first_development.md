# Template-First Development Rule

## MANDATORY: Template Reference Before Code Generation

### Rule: Always Check Templates First
Before generating ANY new code, you MUST:

1. **Check `.amazonq/template_index.md`** to identify relevant templates
2. **Read the appropriate template** from `.amazonq/templates/` directory
3. **Use the template structure** as the foundation for new code
4. **Adapt placeholders** to match specific requirements
5. **Preserve verified patterns** from templates

### Template Priority Order
1. Exact match template (e.g., list view → list_view_template.xml)
2. Similar pattern template (e.g., new model → base_model_template.py)
3. Composite templates (combine multiple templates if needed)

### When Creating New Code

#### Models
- **ALWAYS** start with `base_model_template.py`
- Add computed fields using `computed_field_template.py` pattern
- Add constraints using `constraint_template.py` pattern
- Maintain: `_name`, `_description`, `_order` structure

#### Views
- **List views**: Use `list_view_template.xml` (Odoo 19 `<list>` tag)
- **Form views**: Use `form_view_template.xml` (sheet + group structure)
- **Search views**: Use `search_view_template.xml` (filters + groupby)

#### Security
- **ALWAYS** use `access_rights_template.csv` format
- Maintain column order: id, name, model_id:id, group_id:id, permissions

#### Wizards
- **ALWAYS** start with `wizard_template.py`
- Use TransientModel pattern

### Template Adaptation Process
1. Read template file
2. Identify placeholders: {MODEL_NAME}, {MODEL_CLASS}, etc.
3. Replace placeholders with actual values
4. Add specific fields/logic while maintaining structure
5. Keep comments that explain patterns

### Quality Assurance
- Templates are pre-verified and tested
- Deviating from templates requires explicit user approval
- If template doesn't exist, create code following existing template patterns
- After creating new verified code, suggest adding it as a template

### Benefits
- ✅ Consistent code quality
- ✅ Reduced errors
- ✅ Faster development
- ✅ Maintainable codebase
- ✅ Best practices enforcement

## Example Workflow

**User Request**: "Create a new model for customers"

**Agent Process**:
1. Check `template_index.md` → Find "base_model_template.py"
2. Read `templates/models/base_model_template.py`
3. Adapt template:
   - {MODEL_NAME} → y_customer
   - {MODEL_CLASS} → YCustomer
   - {MODEL_DESCRIPTION} → Customer Management
4. Add specific fields (email, phone, etc.)
5. Generate final code maintaining template structure

**DO NOT** generate code from scratch when templates exist.
