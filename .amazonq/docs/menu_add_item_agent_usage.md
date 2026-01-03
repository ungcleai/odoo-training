# Menu Add Item Agent Usage Guide

## Quick Start

Use the `@menu_add_item_agent` prompt to add new menu items to existing Odoo menu.xml files.

## Usage Format

```
@menu_add_item_agent

File Path: {path/to/menu.xml}
Menu Type: {root/parent/child}
Menu ID: {menu_xml_id}
Menu Name: {menu_display_name}
Parent Menu: {parent_menu_id} (if parent or child)
Sequence: {order_number}
Create Action: {yes/no}

Action (if Create Action: yes):
- Action ID: {action_xml_id}
- Action Name: {action_display_name}
- Model: {model_name}
- View Mode: {tree,form,kanban}
```

## Example 1: Add Child Menu with Action

```
@menu_add_item_agent

File Path: views/menu.xml
Menu Type: child
Menu ID: menu_property_offer
Menu Name: Property Offers
Parent Menu: menu_real_estate_root
Sequence: 20
Create Action: yes

Action:
- Action ID: action_property_offer
- Action Name: Property Offers
- Model: y_property_offer
- View Mode: tree,form
```

**Expected Output:**
```xml
<!-- Start add at 20241220-1530: Adding Property Offers menu -->
<record id="action_property_offer" model="ir.actions.act_window">
    <field name="name">Property Offers</field>
    <field name="res_model">y_property_offer</field>
    <field name="view_mode">tree,form</field>
</record>

<menuitem id="menu_property_offer" name="Property Offers" parent="menu_real_estate_root" action="action_property_offer" sequence="20"/>
<!-- End add at 20241220-1530: Adding Property Offers menu -->
```

## Example 2: Add Parent Menu (No Action)

```
@menu_add_item_agent

File Path: views/menu.xml
Menu Type: parent
Menu ID: menu_real_estate_settings
Menu Name: Settings
Parent Menu: menu_real_estate_root
Sequence: 100
Create Action: no
```

**Expected Output:**
```xml
<!-- Start add at 20241220-1535: Adding Settings parent menu -->
<menuitem id="menu_real_estate_settings" name="Settings" parent="menu_real_estate_root" sequence="100"/>
<!-- End add at 20241220-1535: Adding Settings parent menu -->
```

## Example 3: Add Child Menu Under Settings

```
@menu_add_item_agent

File Path: views/menu.xml
Menu Type: child
Menu ID: menu_property_type
Menu Name: Property Types
Parent Menu: menu_real_estate_settings
Sequence: 10
Create Action: yes

Action:
- Action ID: action_property_type
- Action Name: Property Types
- Model: y_property_type
- View Mode: tree,form
```

**Expected Output:**
```xml
<!-- Start add at 20241220-1540: Adding Property Types menu -->
<record id="action_property_type" model="ir.actions.act_window">
    <field name="name">Property Types</field>
    <field name="res_model">y_property_type</field>
    <field name="view_mode">tree,form</field>
</record>

<menuitem id="menu_property_type" name="Property Types" parent="menu_real_estate_settings" action="action_property_type" sequence="10"/>
<!-- End add at 20241220-1540: Adding Property Types menu -->
```

## Menu Types

### Root Menu
- Top-level menu in main menu bar
- No parent attribute
- No action attribute
- Example: Real Estate, Sales

### Parent Menu
- Submenu under root or another parent
- Has parent attribute
- No action attribute
- Groups related child menus
- Example: Configuration, Settings

### Child Menu
- Menu item that opens views
- Has parent attribute
- Has action attribute
- Opens specific model views
- Example: Properties, Offers, Tags

## Menu Hierarchy Example

```
Real Estate (root)
├── Properties (child with action)
├── Offers (child with action)
└── Settings (parent)
    ├── Property Types (child with action)
    └── Property Tags (child with action)
```

## Sequence Guidelines
- Lower numbers appear first
- Common ranges:
  - 1-10: Primary menus
  - 10-50: Regular menus
  - 50-100: Secondary menus
  - 100+: Settings/Configuration

## Related Agents

- **@menu_add_item_agent**: Add menu items (this agent)
- **@view_create_agent**: Create views with actions
- **@model_create_agent**: Create new Odoo models
