# Model Add Fields Agent Usage Guide

## CRITICAL: Implementation Priority

The `@model_add_fields_agent` prompt will ALWAYS create a new inheritance class using `_inherit` attribute. It will NEVER modify the original model class directly. This approach follows Odoo's standard inheritance pattern and takes ABSOLUTE PRECEDENCE over any other optimization directives.

## Quick Start

Use the `@model_add_fields_agent` prompt to add new fields to existing Odoo models.

## Usage Format

```
@model_add_fields_agent

Target Model: {model_name}

Fields to Add:
1. Field Name: {field_name}
   - Type: {field_type}
   - String: {field_label}
   - Required: {true/false}
   - Default: {default_value}
   - Additional attributes: {other_attributes}

2. Field Name: {field_name_2}
   - Type: {field_type_2}
   - ...
```

## Example Usage

```
@model_add_fields_agent

Target Model: y.realestate.property

Fields to Add:
1. Field Name: active
   - Description: Manage property status available or not
   - Type: Boolean
   - String: Active
   - Required: False
   - Default: True
   - Help: Manage the status of the property usage

2. Field Name: state
   - Description: Track property state or property
   - Type: Selection
   - String: State
   - Required: True
   - Default: new
   - Copy: False
   - Selection Options: [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')]
   - Help: The current state of the property.
```

## Related Agents

- **@model_add_fields_agent**: Add fields to Odoo models (this agent)
- **@view_tree_add_fields_agent**: Add fields to tree/list views
- **@view_form_add_fields_agent**: Add fields to form views
- **@view_search_add_fields_agent**: Add fields/filters to search views

## Supported Field Types

- **Boolean**: True/False fields
- **Char**: Text fields with size limit
- **Text**: Large text fields
- **Integer**: Whole numbers
- **Float**: Decimal numbers
- **Date**: Date fields
- **Datetime**: Date and time fields
- **Selection**: Dropdown with predefined options
- **Many2one**: Foreign key relationships
- **One2many**: Reverse foreign key relationships
- **Many2many**: Many-to-many relationships

## Field Attributes

- **string**: Field label in UI
- **required**: Whether field is mandatory
- **default**: Default value
- **size**: Maximum length for Char fields
- **copy**: Whether field is copied when duplicating record
- **readonly**: Whether field is read-only
- **help**: Tooltip text
- **selection**: Options for Selection fields
- **digits**: Precision for Float fields

## Best Practices

1. Use snake_case for field names
2. Provide meaningful string labels
3. Set appropriate default values
4. Use copy=False for unique fields
5. Add help text for complex fields
6. Follow Odoo naming conventions

## Pre-Implementation Checklist

Before requesting field additions, ensure you have:
- [ ] Correct target model name
- [ ] Complete field specifications
- [ ] Field types and attributes defined
- [ ] Selection options (if applicable)
- [ ] Default values specified