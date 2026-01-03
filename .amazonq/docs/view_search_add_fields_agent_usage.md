# View Search Add Fields Agent Usage Guide

## Quick Start

Use the `@view_search_add_fields_agent` prompt to add new fields and filters to existing Odoo search views.

## Usage Format

```
@view_search_add_fields_agent

Target Model: {model_name}
View ID: {search_view_xml_id}

Fields to Add:
1. Element Type: {field/filter}
   Field Name: {field_name}
   - Position Reference: {existing_field_name}
   - Position Type: {before/after}
   - String: {field_label}
   - Additional attributes: {other_attributes}

2. Element Type: {field/filter}
   Field Name: {field_name_2}
   - ...
```

## Example 1: Add Searchable Fields

```
@view_search_add_fields_agent

Target Model: y.realestate.property
View ID: search_real_estate_root

Fields to Add:
1. Element Type: field
   Field Name: postcode
   - Position Reference: name
   - Position Type: after
   - String: Postcode

2. Element Type: field
   Field Name: expected_price
   - Position Reference: postcode
   - Position Type: after
   - String: Expected Price
```

## Example 2: Add Status Filters

```
@view_search_add_fields_agent

Target Model: y.realestate.property
View ID: search_real_estate_root

Fields to Add:
1. Element Type: filter
   Filter Name: filter_new
   - Position Reference: name
   - Position Type: after
   - String: New
   - Domain: [('state', '=', 'new')]

2. Element Type: filter
   Filter Name: filter_sold
   - Position Reference: filter_new
   - Position Type: after
   - String: Sold
   - Domain: [('state', '=', 'sold')]

3. Element Type: filter
   Filter Name: filter_active
   - Position Reference: filter_sold
   - Position Type: after
   - String: Active Only
   - Domain: [('active', '=', True)]
```

## Example 3: Add Group By Filters

```
@view_search_add_fields_agent

Target Model: y.realestate.property
View ID: search_real_estate_root

Fields to Add:
1. Element Type: filter
   Filter Name: group_by_state
   - Position Reference: name
   - Position Type: after
   - String: Status
   - Context: {'group_by': 'state'}

2. Element Type: filter
   Filter Name: group_by_postcode
   - Position Reference: group_by_state
   - Position Type: after
   - String: Postcode
   - Context: {'group_by': 'postcode'}
```

## Element Types

### Searchable Fields
- Use `Element Type: field` for text/number search
- Adds search capability for the field

### Filters
- Use `Element Type: filter` for predefined searches
- Use `Domain` attribute for filter conditions
- Use `Context` attribute for grouping (group_by)

## Common Attributes

- **string**: Field/filter label
- **domain**: Filter condition (e.g., [('state', '=', 'new')])
- **context**: Context variables (e.g., {'group_by': 'state'})
- **filter_domain**: Custom search domain
- **help**: Tooltip text

## Related Agents

- **@model_add_fields_agent**: Add fields to Odoo models
- **@view_tree_add_fields_agent**: Add fields to tree/list views
- **@view_form_add_fields_agent**: Add fields to form views
- **@view_search_add_fields_agent**: Add fields/filters to search views (this agent)
