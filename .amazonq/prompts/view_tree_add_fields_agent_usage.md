# View Tree Add Fields Agent Usage Guide

## Quick Start

Use the `@view_tree_add_fields_agent` prompt to add new fields to existing Odoo tree/list views.

## Usage Format

```
@view_tree_add_fields_agent

Target Model: {model_name}
View ID: {tree_view_xml_id}

Fields to Add:
1. Field Name: {field_name}
   - Position Reference: {existing_field_name}
   - Position Type: {before/after}
   - String: {field_label}
   - Width: {column_width}
   - Additional attributes: {other_attributes}

2. Field Name: {field_name_2}
   - ...
```

## Example 1: Add Status Fields to Tree View

```
@view_tree_add_fields_agent

Target Model: y.realestate.property
View ID: tree_real_estate_root

Fields to Add:
1. Field Name: active
   - Position Reference: name
   - Position Type: after
   - String: Active
   - Width: 80px

2. Field Name: state
   - Position Reference: active
   - Position Type: after
   - String: Status
   - Width: 120px
```

## Example 2: Add Price and Date Columns

```
@view_tree_add_fields_agent

Target Model: y.realestate.property
View ID: tree_real_estate_root

Fields to Add:
1. Field Name: expected_price
   - Position Reference: living_area
   - Position Type: after
   - String: Expected Price
   - Width: 150px
   - Attributes: optional="show"

2. Field Name: date_availability
   - Position Reference: expected_price
   - Position Type: after
   - String: Available From
   - Width: 120px
```

## Example 3: Add Optional Column with Conditional Display

```
@view_tree_add_fields_agent

Target Model: y.realestate.property
View ID: tree_real_estate_root

Fields to Add:
1. Field Name: selling_price
   - Position Reference: expected_price
   - Position Type: after
   - String: Selling Price
   - Width: 150px
   - Attributes: optional="hide", invisible="state != 'sold'"
```

## Common Field Attributes

- **string**: Column header label
- **width**: Column width (e.g., "100px", "10%")
- **optional**: Column visibility control (show, hide)
- **invisible**: Conditional visibility
- **readonly**: Make column read-only
- **sum**: Show sum at bottom (for numeric fields)
- **avg**: Show average at bottom (for numeric fields)

## Related Agents

- **@model_add_fields_agent**: Add fields to Odoo models
- **@view_tree_add_fields_agent**: Add fields to tree/list views (this agent)
- **@view_form_add_fields_agent**: Add fields to form views
- **@view_search_add_fields_agent**: Add fields/filters to search views
