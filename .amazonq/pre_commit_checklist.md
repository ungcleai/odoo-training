# Pre-Commit Review Checklist

## Before Every Commit

### 1. Code Review
```bash
/review @[modified_files]
```

**Check for:**
- ✅ Security vulnerabilities
- ✅ Code quality issues
- ✅ Best practice violations
- ✅ Secrets in code
- ✅ Performance issues

### 2. Fix Issues
Address all findings from review before proceeding.

### 3. Test Coverage
```bash
/test Generate tests for @[new_models]
```

Ensure tests exist for:
- ✅ New models
- ✅ New methods
- ✅ Business logic
- ✅ Constraints

### 4. Run Tests
```bash
python odoo-bin -c odoo.conf -u y_realestate --test-enable --stop-after-init
```

### 5. Documentation
```bash
/doc Document [new_feature]
```

Update:
- ✅ README.md
- ✅ Docstrings
- ✅ Comments

### 6. Commit
```bash
git add .
git commit -m "feat: [description]"
```

## Quick Command
```bash
# One-line pre-commit check
/review @models/ @views/ @security/
```

## Commit Message Format
```
type: description

Types: feat, fix, refactor, docs, test, chore
```
