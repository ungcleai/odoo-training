# Project Context

## Module Information
- **Name**: Y Real Estate
- **Technical Name**: y_realestate
- **Odoo Version**: 19
- **Database**: PostgreSQL

## Current Models
- `y.realestate.property` - Property management

## Business Rules
- Properties must have expected_price > 0
- Property names are required
- Active flag defaults to True

## Architecture Decisions
- Use `y_` prefix for all custom models
- Use `<list>` tag for list views (Odoo 19)
- Follow template-first development
- Security: user and manager access levels

## Dependencies
- base (Odoo core)

## Future Enhancements
- Add booking system
- Add customer management
- Add reporting
