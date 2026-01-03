# Amazon Q Features - Quick Reference

## 🚀 Agent Modes

### `/dev` - Multi-File Development
```bash
/dev @odoo_crud Create customer management
/dev Implement booking system with model, views, security
```

### `/test` - Test Generation
```bash
/test @odoo_test Generate tests for @models/property.py
/test Add test coverage for booking model
```

### `/review` - Code Review (Pre-Commit)
```bash
/review @models/ @views/
/review Check @models/property.py for issues
```

### `/doc` - Documentation
```bash
/doc Document @models/property.py
/doc Create README for booking feature
```

---

## 📝 Saved Prompts

Located in: `~/.aws/amazonq/prompts/`

### Available Prompts
- `@odoo_model` - Create model with template
- `@odoo_views` - Create complete view set
- `@odoo_crud` - Full CRUD feature
- `@odoo_test` - Test generation guide

### Usage
```bash
/dev @odoo_crud Create invoice module
/test @odoo_test for customer model
```

---

## 🎯 Context References

```bash
@file_name.py          # Include specific file
@folder_name/          # Include entire folder
@workspace             # Smart workspace context
@prompt_name           # Use saved prompt
```

---

## ⚡ Inline Completions

**Trigger:** `Alt+C` (Windows) or `Option+C` (Mac)

Real-time AI code suggestions as you type.

---

## 📋 Workflow Examples

### Create New Feature
```bash
1. /dev @odoo_crud Create sales order feature
2. /test @odoo_test for sales order model
3. /review @models/sales_order.py @views/sales_order_views.xml
4. Fix issues
5. Commit
```

### Add Tests to Existing Code
```bash
/test @odoo_test Generate tests for @models/property.py
```

### Pre-Commit Check
```bash
/review @models/ @views/ @security/
```

### Document Feature
```bash
/doc Document booking feature in @models/booking.py @views/booking_views.xml
```

---

## 🔧 Custom Rules (Auto-Applied)

Located in: `.amazonq/rules/`

- `odoo_development_standards.md` - Odoo 19 standards
- `template_first_development.md` - Template enforcement
- `agent_naming_standards.md` - Naming conventions

**All rules automatically applied to every request!**

---

## 📚 Templates (Auto-Used)

Located in: `.amazonq/templates/`

- Models: `base_model_template.py`
- Views: `list_view_template.xml`, `form_view_template.xml`, `search_view_template.xml`
- Security: `access_rights_template.csv`

**Agent modes automatically use templates!**

---

## ✅ Daily Workflow

### Morning
```bash
# Start new feature
/dev @odoo_crud Create [feature_name]
```

### Development
```bash
# Use inline completions: Alt+C
# Reference files: @file_name
```

### Before Lunch
```bash
# Generate tests
/test @odoo_test for new models
```

### Before Commit
```bash
# Review code
/review @modified_files

# Fix issues
# Run tests
# Commit
```

---

## 🎓 Tips

1. **Combine modes**: `/dev` → `/test` → `/review` → commit
2. **Use saved prompts**: Faster than typing requirements
3. **Context stacking**: `@models/ @views/` reviews multiple areas
4. **Templates work automatically**: No need to reference manually
5. **Pre-commit always**: `/review` before every commit

---

## 📞 Quick Commands Cheat Sheet

| Task | Command |
|------|---------|
| New feature | `/dev @odoo_crud Create [name]` |
| Generate tests | `/test @odoo_test for [model]` |
| Pre-commit | `/review @[files]` |
| Add docs | `/doc Document [feature]` |
| Use template | Automatic with `/dev` |
| Include file | `@file_name` |
| Include folder | `@folder_name/` |
| Saved prompt | `@prompt_name` |

---

**See also:**
- `agent_workflow_guide.md` - Detailed workflow
- `pre_commit_checklist.md` - Commit checklist
- `template_index.md` - Available templates
