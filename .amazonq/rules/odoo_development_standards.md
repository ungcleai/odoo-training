# Odoo Development Standards & Architecture Rules

## Core Odoo Architecture Principles

### 0. Model Naming Convention (CRITICAL)
- **MANDATORY**: All custom model class names MUST start with `y_` prefix
- This prevents confusion with Odoo standard model names
- Example: `y_realestate_property`, `y_sale_order`, `y_product_template`
- **DO NOT** create models without the `y_` prefix

### 1. Odoo 19 View Terminology (CRITICAL)
- **MANDATORY**: In Odoo 19, use "list" instead of "tree" for list views
- **View XML Element**: Use `<list>` tag, NOT `<tree>` tag
- **Action view_mode**: Use "list" (e.g., "list,form"), NOT "tree"
- **View Type Reference**: Always refer to it as "list view", NOT "tree view"
- Example: `<field name="view_mode">list,form</field>`
- **DO NOT** use "tree" terminology in Odoo 19 development

### 2. MVC Pattern
- **Models**: Business logic in `models/` directory
- **Views**: UI definitions in `views/` directory  
- **Controllers**: Web controllers in `controllers/` directory

### 3. Module Structure
```
module_name/
├── __init__.py
├── __manifest__.py
├── models/
├── views/
├── controllers/
├── security/
├── data/
├── static/
└── wizard/
```

### 4. Model Development Rules
- Use `models.Model` for persistent data
- Use `models.TransientModel` for wizards
- Always define `_name`, `_description`
- Use proper field types: `Char(size=X)`, `Text`, `Integer`, `Float`, `Boolean`, `Date`, `Datetime`
- Define relationships: `Many2one`, `One2many`, `Many2many`
- Use `@api.depends` for computed fields
- Use `@api.constrains` for validation
- Follow naming: snake_case for fields, CamelCase for classes

### 5. View Development Rules
- List views: Use `<list>` with proper field widths (NOT `<tree>` in Odoo 19)
- Form views: Use `<form>` with `<sheet>`, `<group>`, `<notebook>`
- Search views: Include searchable fields and filters
- Always define view inheritance with `inherit_id`
- Use proper field attributes: `string`, `required`, `readonly`, `invisible`

### 6. Security Rules
- Define access rights in `security/ir.model.access.csv`
- Use record rules for row-level security
- Format: `id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`

### 7. Data Files
- Use `<data noupdate="1">` for demo/initial data
- Use proper XML structure with `<record>` elements
- Reference other records with `ref()` function

### 8. Manifest Requirements
```python
{
    'name': 'Module Name',
    'version': '1.0',
    'depends': ['base'],  # Always include dependencies
    'data': [
        'security/ir.model.access.csv',
        'views/view_file.xml',
        'data/data_file.xml',
    ],
    'installable': True,
    'application': True,
}
```

### 9. Field Constraints & Validation
- Use `size` parameter for Char fields
- Use `digits` parameter for Float fields
- Use `selection` for dropdown options
- Use `default` for default values
- Use `copy=False` for unique fields

### 10. Odoo ORM Methods
- `create()`, `write()`, `unlink()` for CRUD operations
- `search()`, `browse()` for data retrieval
- `filtered()`, `mapped()`, `sorted()` for recordset operations
- Use `sudo()` carefully for permission elevation

### 11. Best Practices
- Keep methods small and focused
- Use meaningful variable names
- Add proper docstrings
- Handle exceptions appropriately
- Use `_logger` for debugging
- Follow Odoo coding guidelines
- Test thoroughly before deployment

## Development Workflow
1. Define model structure first
2. Create security access rules
3. Build views (list → form → search)
4. Add menu items and actions
5. Create initialization data
6. Test functionality
7. Add constraints and validation

## Common Patterns
- **Computed Fields**: `@api.depends` + `compute` method
- **Onchange Methods**: `@api.onchange` for dynamic behavior  
- **Constraints**: `@api.constrains` for validation
- **Inheritance**: Extend existing models/views
- **Wizards**: TransientModel for user interactions

Always refer to these standards when developing Odoo customizations.