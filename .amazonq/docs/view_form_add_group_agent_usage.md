# View Form Add Group Agent Usage Guide

## Quick Start

Use the `@view_form_add_group_agent` prompt to add new groups, pages, or notebooks to existing Odoo form views.

## Usage Format

```
@view_form_add_group_agent

Target Model: {model_name}
View ID: {form_view_xml_id}

Element to Add:
- Element Type: {group/page/notebook}
- Label: {element_label}
- Position Reference: {existing_element}
- Position Type: {before/after/inside}
- Fields (optional):
  1. Field Name: {field_name_1}
  2. Field Name: {field_name_2}
```

## Example 1: Add New Group with Fields

```
@view_form_add_group_agent

Target Model: y.realestate.property
View ID: form_real_estate_root

Element to Add:
- Element Type: group
- Label: Financial Information
- Position Reference: description
- Position Type: after
- Fields:
  1. Field Name: expected_price
  2. Field Name: selling_price
  3. Field Name: best_offer
```

## Example 2: Add New Page to Existing Notebook

```
@view_form_add_group_agent

Target Model: y.realestate.property
View ID: form_real_estate_root

Element to Add:
- Element Type: page
- Label: Additional Details
- Position Reference: description_page
- Position Type: after
- Fields:
  1. Field Name: property_type_id
  2. Field Name: tag_ids
  3. Field Name: salesperson_id
```

## Example 3: Add New Notebook with Multiple Pages

```
@view_form_add_group_agent

Target Model: y.realestate.property
View ID: form_real_estate_root

Element to Add:
- Element Type: notebook
- Position Reference: garden_area
- Position Type: after
- Pages:
  1. Page Label: Offers
     Fields:
       - offer_ids
  2. Page Label: Documents
     Fields:
       - document_ids
```

## Element Types

### Group
- Creates a new field grouping section
- Default 2-column layout
- Use for organizing related fields

### Page
- Creates a new tab in existing notebook
- Use for additional sections in tabbed interface

### Notebook
- Creates a new tabbed interface
- Contains multiple pages
- Use for major section organization

## Common Attributes

- **string**: Element label/title
- **colspan**: Column span (1-4)
- **col**: Number of columns inside group
- **invisible**: Conditional visibility
- **autofocus**: Auto-focus on page (for pages)

## Related Agents

- **@model_add_fields_agent**: Add fields to Odoo models
- **@view_form_add_fields_agent**: Add fields to existing form groups
- **@view_form_add_group_agent**: Add new groups/pages/notebooks (this agent)
- **@view_tree_add_fields_agent**: Add fields to tree/list views
- **@view_search_add_fields_agent**: Add fields/filters to search views
