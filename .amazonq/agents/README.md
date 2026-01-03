# Odoo Development Agents

This folder contains agent prompt definitions for Odoo development tasks.

## Available Agents

### Model Agents
- `model_create_agent.md` - Create new Odoo models
- `model_add_fields_agent.md` - Add fields to existing models

### View Agents
- `view_create_agent.md` - Create new views (tree, form, search, kanban)
- `view_form_add_fields_agent.md` - Add fields to form views
- `view_form_add_group_agent.md` - Add groups/pages to form views
- `view_search_add_fields_agent.md` - Add fields/filters to search views
- `view_tree_add_fields_agent.md` - Add fields to tree views

### Menu Agents
- `menu_add_item_agent.md` - Add menu items

## Usage

Reference agents in chat using `@agent_name.md` syntax.

Example: `@model_create_agent.md`

## Documentation

Usage documentation is located in `../docs/` folder (excluded from chat context).
