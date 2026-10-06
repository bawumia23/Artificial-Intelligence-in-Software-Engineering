# AI: SQL to ORM Refactoring and Security Analysis

## Overview
A procedural Python script that uses `mysql.connector` with raw,
parameterized SQL was refactored into a SQLAlchemy ORM version using an
AI assistant, followed by an analysis of the security and
maintainability benefits.

## Tool Used
GEMINI

## Files
- `initial_script.py` - the original script from the assignment
  (`get_connection` and `create_user`; the other functions were
  truncated in the assignment text).
- `refactored_orm.py` - the AI-generated SQLAlchemy ORM version: a
  declarative `User` model, table creation, and ORM equivalents of
  create, get, update, delete and list.

## What Was AI-Generated and What Was Not
`refactored_orm.py` and the comparison of raw SQL versus the ORM are AI
output, included here unmodified. The prompt and the written
reflection on abstraction and maintainability are my own work and are
in the accompanying Google Doc submission.

## Known Limitations of the AI Output
- `DB_PASSWORD` falls back to a hardcoded default if the environment
  variable is unset.
- The CRUD functions catch the broad `Exception`.
- The type hints (`User | None`, `list[User]`) require Python 3.10+.

## Running It
Requires SQLAlchemy 1.4+, `mysql-connector-python`, and a MySQL
database. Set `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` and
`DB_NAME`, then run `python3 refactored_orm.py`.
