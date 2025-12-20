# Model Create Agent Usage Guide

## Quick Start

Use the `@model_create_agent` prompt to create new Odoo models following development standards.

## CRITICAL: Model Naming
All model names MUST start with `y_` prefix (e.g., `y_property_offer`, `y_customer_feedback`).

## Usage Format

```
@model_create_agent

File Option: {new/existing}
File Path: {path/to/file.py OR new_filename.py}
Model Name: y_{model_name}
Description: {model_description}
Order By: {field_name} {asc/desc}

Fields:
1. Field Name: {field_name}
   - Type: {field_type}
   - String: {field_label}
   - Required: {true/false}
   - Default: {default_value}
   - Additional attributes: {other_attributes}

2. Field Name: {field_name_2}
   - ...
```

## Example 1: Create Property Offer Model (New File)

```
@model_create_agent

File Option: new
File Path: property_offer.py
Model Name: y_property_offer
Description: Property Offer Management
Order By: id desc

Fields:
1. Field Name: name
   - Type: Char
   - String: Offer Reference
   - Required: True
   - Size: 100

2. Field Name: price
   - Type: Float
   - String: Offer Price
   - Required: True

3. Field Name: status
   - Type: Selection
   - String: Status
   - Required: True
   - Default: pending
   - Selection Options: [('pending', 'Pending'), ('accepted', 'Accepted'), ('refused', 'Refused')]

4. Field Name: property_id
   - Type: Many2one
   - String: Property
   - Required: True
   - Relation: y.realestate.property

5. Field Name: partner_id
   - Type: Many2one
   - String: Customer
   - Required: True
   - Relation: res.partner

6. Field Name: validity_days
   - Type: Integer
   - String: Validity (days)
   - Default: 7
```

## Example 2: Create Property Type Model (Add to Existing File)

```
@model_create_agent

File Option: existing
File Path: models/main.py
Model Name: y_property_type
Description: Property Type Classification
Order By: name asc

Fields:
1. Field Name: name
   - Type: Char
   - String: Type Name
   - Required: True
   - Size: 50

2. Field Name: description
   - Type: Text
   - String: Description

3. Field Name: property_ids
   - Type: One2many
   - String: Properties
   - Relation: y.realestate.property
   - Inverse: property_type_id

4. Field Name: active
   - Type: Boolean
   - String: Active
   - Default: True
```

## Example 3: Create Property Tag Model (New File with Computed Field)

```
@model_create_agent

File Option: new
File Path: property_tag.py
Model Name: y_property_tag
Description: Property Tags for Classification
Order By: name asc

Fields:
1. Field Name: name
   - Type: Char
   - String: Tag Name
   - Required: True
   - Size: 30

2. Field Name: color
   - Type: Integer
   - String: Color Index

3. Field Name: property_ids
   - Type: Many2many
   - String: Properties
   - Relation: y.realestate.property

4. Field Name: property_count
   - Type: Integer
   - String: Property Count
   - Compute: _compute_property_count
   - Store: False

Computed Methods:
- Method: _compute_property_count
  Depends: property_ids
  Logic: Count number of properties with this tag
```

## File Options

### New File
- Creates a new Python file in `models/` directory
- Automatically updates `models/__init__.py` with import
- Use when creating standalone model

### Existing File
- Adds model class to existing Python file
- Does not modify `__init__.py` (already imported)
- Use when grouping related models together

## Supported Field Types

- **Char**: Text with size limit
- **Text**: Large text fields
- **Integer**: Whole numbers
- **Float**: Decimal numbers
- **Boolean**: True/False fields
- **Date**: Date only
- **Datetime**: Date and time
- **Selection**: Dropdown with options
- **Many2one**: Foreign key relationship
- **One2many**: Reverse foreign key
- **Many2many**: Many-to-many relationship

## Common Field Attributes

- **string**: Field label
- **required**: Mandatory field
- **default**: Default value
- **size**: Max length (Char fields)
- **copy**: Copy on duplicate
- **readonly**: Read-only field
- **help**: Tooltip text
- **selection**: Options (Selection fields)
- **relation**: Related model (relational fields)
- **inverse**: Inverse field (One2many)
- **compute**: Compute method name
- **store**: Store computed value

## Related Agents

- **@model_create_agent**: Create new Odoo models (this agent)
- **@model_add_fields_agent**: Add fields to existing models
- **@view_tree_add_fields_agent**: Add fields to tree views
- **@view_form_add_fields_agent**: Add fields to form views
- **@view_search_add_fields_agent**: Add fields to search views
