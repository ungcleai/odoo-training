# View Create Agent Usage Guide

## Quick Start

Use the `@view_create_agent` prompt to create new Odoo views with support for multiple view types.

## Usage Format

```
@view_create_agent

File Option: {new/existing}
File Path: {path/to/file.xml OR new_filename.xml}
View Types: {tree, form, search, kanban} (comma separated for multiple)
Target Model: {model_name}
Create Action: {yes/no}

Tree View:
- View ID: {tree_view_xml_id}
- Fields: {field_list}

Form View:
- View ID: {form_view_xml_id}
- Fields: {field_list}

Search View:
- View ID: {search_view_xml_id}
- Fields: {field_list}
- Filters: {filter_list}

Action (if Create Action: yes):
- Action ID: {action_xml_id}
- Action Name: {action_display_name}
- View Mode: {tree,form,search}
- Help Text: {empty_state_message}

Additional Options: {options}
```

## Example 1: Create Multiple Views with Action (New File)

```
@view_create_agent

File Option: new
File Path: property_offer_views.xml
View Types: tree, form, search
Target Model: y_property_offer
Create Action: yes

Tree View:
- View ID: view_property_offer_tree
- Fields:
  1. name (Offer Reference, 150px)
  2. property_id (Property, 200px)
  3. partner_id (Customer, 150px)
  4. price (Offer Price, 120px)
  5. status (Status, 100px)

Form View:
- View ID: view_property_offer_form
- Fields:
  1. name (Offer Reference, required)
  2. property_id (Property, required)
  3. partner_id (Customer, required)
  4. price (Offer Price, required)
  5. validity_days (Validity Days)
  6. status (Status, widget=statusbar)

Search View:
- View ID: view_property_offer_search
- Fields:
  1. name (Offer Reference)
  2. property_id (Property)
  3. partner_id (Customer)
- Filters:
  1. filter_pending (Pending, domain=[('status','=','pending')])
  2. filter_accepted (Accepted, domain=[('status','=','accepted')])
  3. group_by_property (Property, context={'group_by':'property_id'})

Action:
- Action ID: action_property_offer
- Action Name: Property Offers
- View Mode: tree,form
- Help Text: Create your first property offer
```

## Example 2: Create Views Without Action (Add to Existing File)

```
@view_create_agent

File Option: existing
File Path: views/property_type_views.xml
View Types: tree, form
Target Model: y_property_type
Create Action: no

Tree View:
- View ID: view_property_type_tree
- Fields:
  1. name (Type Name, 200px)
  2. description (Description, 300px)
  3. active (Active, 80px)

Form View:
- View ID: view_property_type_form
- Fields:
  1. name (Type Name, required)
  2. description (Description)
  3. property_ids (Properties, widget=one2many_list)
  4. active (Active)
```

## Example 3: Create All View Types with Action (New File)

```
@view_create_agent

File Option: new
File Path: property_tag_views.xml
View Types: tree, form, search, kanban
Target Model: y_property_tag
Create Action: yes

Tree View:
- View ID: view_property_tag_tree
- Fields:
  1. name (Tag Name, 200px)
  2. color (Color, 100px)
  3. property_count (Properties, 100px)

Form View:
- View ID: view_property_tag_form
- Fields:
  1. name (Tag Name, required)
  2. color (Color, widget=color_picker)
  3. property_ids (Properties, widget=many2many_tags)

Search View:
- View ID: view_property_tag_search
- Fields:
  1. name (Tag Name)
- Filters:
  1. group_by_color (Color, context={'group_by':'color'})

Kanban View:
- View ID: view_property_tag_kanban
- Fields:
  1. name (display as card title)
  2. color (display as card color)
  3. property_count (display as badge)

Action:
- Action ID: action_property_tag
- Action Name: Property Tags
- View Mode: kanban,tree,form
- Help Text: Create your first property tag
```



## Creating Multiple Views

### Benefits
- Create complete view set in one request
- Consistent field usage across views
- Single file for related views
- Efficient development workflow
- Optional action creation for menu integration

### Supported Combinations
- Single view: `tree` or `form` or `search` or `kanban`
- Common pairs: `tree, form` or `tree, form, search`
- Complete set: `tree, form, search, kanban`

## Action Creation

### When to Create Action
- **Yes**: When creating new model views that need menu access
- **No**: When adding alternative views or extending existing views

### View Mode Order
- First view type in `view_mode` is the default view
- Order determines view switching sequence
- Common patterns:
  - `tree,form` - List first, then details
  - `kanban,tree,form` - Kanban first, then list and details
  - `form,tree` - Form first (for single record focus)

## Supported View Types

### Tree View
- List/table display
- Column-based layout
- Sorting and filtering
- Optional columns

### Form View
- Detailed record view
- Field grouping
- Tabbed interface (notebooks)
- Custom widgets

### Search View
- Search fields
- Predefined filters
- Group by options
- Custom domains

### Kanban View
- Card-based display
- Drag and drop
- Grouping support
- Custom templates

## File Options

### New File
- Creates a new XML file in `views/` directory
- Automatically updates `__manifest__.py` data list
- Use for new model views

### Existing File
- Adds view to existing XML file
- Does not modify `__manifest__.py` (already listed)
- Use when grouping related views together

## Related Agents

- **@view_create_agent**: Create new Odoo views (this agent)
- **@view_tree_add_fields_agent**: Add fields to existing tree views
- **@view_form_add_fields_agent**: Add fields to existing form views
- **@view_form_add_group_agent**: Add groups/pages to form views
- **@view_search_add_fields_agent**: Add fields/filters to search views
- **@model_create_agent**: Create new Odoo models
