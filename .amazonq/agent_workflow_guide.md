# Amazon Q Agent Modes - Workflow Guide

## Quick Reference

### `/dev` - Multi-File Feature Development
**Use for:** Creating complete features with multiple files

**Example:**
```
/dev Create customer management feature with model, views, and security
/dev @odoo_crud Add invoice module
/dev Implement property booking system
```

**Output:** Multiple files created/modified in one operation

---

### `/test` - Auto Test Generation
**Use for:** Generating unit tests for existing code

**Example:**
```
/test Generate tests for @models/property.py
/test @odoo_test Create tests for customer model
/test Add test coverage for @models/booking.py
```

**Output:** Complete test files with multiple test cases

---

### `/review` - Code Review & Security Scan
**Use for:** Pre-commit quality and security checks

**Example:**
```
/review Check @models/property.py
/review Scan @views/ for issues
/review Security check before commit
```

**Output:** 
- Security vulnerabilities (SAST)
- Code quality issues
- Best practice violations
- Secrets detection

---

### `/doc` - Documentation Generation
**Use for:** Creating documentation

**Example:**
```
/doc Document @models/property.py
/doc Create README for booking feature
/doc Generate API docs for @controllers/
```

**Output:** README, docstrings, API documentation

---

## Recommended Workflow

### 1. Development Phase
```bash
# Use /dev for multi-file features
/dev @odoo_crud Create property booking feature

# Result: model + views + security + menu
```

### 2. Testing Phase
```bash
# Use /test for test generation
/test @odoo_test Generate tests for booking model

# Result: Complete test suite
```

### 3. Review Phase (Before Commit)
```bash
# Use /review for quality check
/review Check @models/booking.py @views/booking_views.xml

# Result: Security + quality report
```

### 4. Documentation Phase
```bash
# Use /doc for documentation
/doc Document booking feature

# Result: README and inline docs
```

---

## Combining with Saved Prompts

### Saved Prompts Available
- `@odoo_model` - Create model with template
- `@odoo_views` - Create view set
- `@odoo_crud` - Complete CRUD feature
- `@odoo_test` - Test generation guide

### Usage Examples
```bash
# Development with prompt
/dev @odoo_crud Create customer feature

# Testing with prompt
/test @odoo_test for customer model

# Review before commit
/review @models/ @views/
```

---

## Pre-Commit Checklist

Before every commit, run:
```bash
1. /review @[modified_files]
2. Fix any issues found
3. /test Generate tests if missing
4. Run tests
5. Commit
```

---

## Tips

### Multi-File Operations
```bash
# Create entire module structure
/dev Create complete sales order module with:
- Model (y_sales_order)
- Views (list, form, search)
- Security rules
- Workflow (draft → confirmed → done)
```

### Context Stacking
```bash
# Review multiple areas
/review @models/ @views/ @security/

# Test multiple models
/test @models/customer.py @models/invoice.py
```

### Template Integration
All agent modes automatically use your templates from `.amazonq/templates/`

---

## Quick Commands

| Task | Command |
|------|---------|
| New feature | `/dev @odoo_crud Create [name]` |
| Generate tests | `/test @odoo_test for [model]` |
| Pre-commit check | `/review @[files]` |
| Add docs | `/doc Document [feature]` |

---

**Remember:** Agent modes work WITH your templates and rules automatically!
