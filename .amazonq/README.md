# Code Template Knowledge Base

## Objective

Provide Amazon Q with verified, reusable code templates to ensure:
- **Consistent code quality** across all development
- **Reduced errors** by using tested patterns
- **Faster development** through template reuse
- **Maintainable codebase** with standardized structures

## How It Works

Amazon Q automatically references templates before generating any new code, ensuring all output follows verified patterns.

## Directory Structure

```
.amazonq/
├── template_index.md              # Template catalog (start here)
├── templates/                     # Template library
│   ├── models/                    # Python model templates
│   ├── views/                     # XML view templates
│   ├── security/                  # Security templates
│   └── wizards/                   # Wizard templates
├── rules/
│   └── template_first_development.md  # Enforces template usage
└── template_management.md         # Maintenance guide
```

## Usage Guidelines

### For Amazon Q Agent

**Before generating code:**
1. Check `template_index.md` for relevant template
2. Read template from `templates/` directory
3. Replace placeholders with actual values
4. Maintain template structure
5. Add specific logic as needed

### For Developers

**Using templates manually:**
```bash
# 1. Browse available templates
cat .amazonq/template_index.md

# 2. Copy template
cp .amazonq/templates/models/base_model_template.py models/my_new_model.py

# 3. Replace placeholders
# {MODEL_NAME} → y_my_model
# {MODEL_CLASS} → YMyModel
# {MODEL_DESCRIPTION} → My Model Description

# 4. Add specific fields/logic
```

**Adding new templates:**
1. Create verified code pattern
2. Replace specific values with `{PLACEHOLDERS}`
3. Save to appropriate `templates/` subdirectory
4. Update `template_index.md`

## Template Placeholders

| Placeholder | Example | Usage |
|-------------|---------|-------|
| `{MODEL_NAME}` | `y_realestate_property` | Model technical name |
| `{MODEL_CLASS}` | `YRealestateProperty` | Python class name |
| `{MODEL_DESCRIPTION}` | `Property Management` | Human-readable name |
| `{VIEW_ID}` | `property_view` | XML view identifier |
| `{FIELD_NAME}` | `property_type` | Field technical name |

## Available Templates

### Models
- `base_model_template.py` - Standard model with common patterns

### Views
- `list_view_template.xml` - List view (Odoo 19 `<list>` tag)
- `form_view_template.xml` - Form with sheet/group structure
- `search_view_template.xml` - Search with filters

### Security
- `access_rights_template.csv` - Access rights format

## Example Usage

**Request:** "Create a customer model"

**Amazon Q Process:**
1. Reads `base_model_template.py`
2. Replaces: `{MODEL_NAME}` → `y_customer`
3. Replaces: `{MODEL_CLASS}` → `YCustomer`
4. Adds specific fields (email, phone)
5. Generates verified code

## Benefits

✅ **Quality**: All code follows verified patterns  
✅ **Speed**: No need to write boilerplate from scratch  
✅ **Consistency**: Same structure across entire project  
✅ **Maintainability**: Easy to update and understand  
✅ **Best Practices**: Templates enforce Odoo standards  

## Quick Start

1. **View templates**: Check `template_index.md`
2. **Ask Amazon Q**: "Create a new model for products"
3. **Q automatically uses**: `base_model_template.py`
4. **Result**: Verified, consistent code

## Maintenance

- Add templates when patterns are used 3+ times
- Update templates when Odoo standards change
- See `template_management.md` for details

## Integration with Development Rules

Templates work with:
- `odoo_development_standards.md` - Odoo 19 best practices
- `agent_naming_standards.md` - File naming conventions
- `template_first_development.md` - Template enforcement rule

---

**Last Updated:** 2024  
**Odoo Version:** 19  
**Status:** Active
