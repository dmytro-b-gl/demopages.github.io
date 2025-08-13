---
title: PostgreSQL Indexing 101
nav_order: 30
---
# PostgreSQL Indexing 101

A micro-crash course.

## Common types
- **BTREE** (default): equality and range (`=`, `<`, `BETWEEN`).
- **GIN**: full-text search & JSONB containment.
- **HASH**: equality-only (rarely needed; BTREE is fine most of the time).

## Examples
```sql
-- Composite BTREE index for typical filters
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- JSONB containment with GIN
CREATE INDEX idx_docs_gin ON docs USING GIN (data jsonb_path_ops);
```

## Notes
- Put **most selective columns first** in composite indexes.
- Avoid redundant indexes; they slow writes.
- Always check plans: `EXPLAIN (ANALYZE, BUFFERS) ...`

---
**Prev:** [Kubernetes Probes](../devops/kubernetes-probes.md) · **Back:** [Home](../index.md)
