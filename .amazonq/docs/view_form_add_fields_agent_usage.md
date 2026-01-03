# View Form Add Fields Agent Usage Guide

## Quick Start

Use the `@view_form_add_fields_agent` prompt to add new fields to existing Odoo form views.

## Usage Format

```
@view_form_add_fields_agent

Target Model: {model_name}
View ID: {form_view_xml_id}

Fields to Add:
1. Field Name: {field_name}
   - Position Reference: {existing_field_name}
   - Position Type: {before/after/inside}
   - Target Group/Page: {group_or_page_location}
   - String: {field_label}
   - Additional attributes: {other_attributes}

2. Field Name: {field_name_2}
   - ...
```

## Example 1: Add Fields to Basic Group

```
@view_form_add_fields_agent

Target Model: y.realestate.property
View ID: form_real_estate_root

Fields to Add:
1. Field Name: active
   - Position Reference: name
   - Position Type: after
   - Target Group: Basic Information Group
   - String: Active
   - Attributes: invisible="0"

2. Field Name: state
   - Position Reference: active
   - Position Type: after
   - Target Group: Basic Information Group
   - String: Status
   - Attributes: required="1", readonly="1"
```

## Example 2: Add Fields to Notebook Page

```
@view_form_add_fields_agent

Target Model: y.realestate.property
View ID: form_real_estate_root

Fields to Add:
1. Field Name: property_type_id
   - Position Reference: description
   - Position Type: before
   - Target Group: Details Page
   - String: Property Type
   - Attributes: required="1"

2. Field Name: tag_ids
   - Position Reference: property_type_id
   - Position Type: after
   - Target Group: Details Page
   - String: Tags
   - Attributes: widget="many2many_tags"
```

## Example 3: Add Field with Custom Attributes

```
@view_form_add_fields_agent

Target Model: y.realestate.property
View ID: form_real_estate_root

Fields to Add:
1. Field Name: total_area
   - Position Reference: living_area
   - Position Type: after
   - Target Group: Property Details Group
   - String: Total Area (sqm)
   - Attributes: readonly="1", colspan="2"
```

## Common Field Attributes

- **string**: Field label
- **required**: Make field mandatory
- **readonly**: Make field read-only
- **invisible**: Hide field conditionally
- **colspan**: Column span (1-4)
- **nolabel**: Hide field label
- **placeholder**: Placeholder text
- **widget**: Custom widget (e.g., many2many_tags, statusbar)

## Related Agents

- **@model_add_fields_agent**: Add fields to Odoo models
- **@view_tree_add_fields_agent**: Add fields to tree/list views
- **@view_form_add_fields_agent**: Add fields to form views (this agent)
- **@view_search_add_fields_agent**: Add fields/filters to search views
