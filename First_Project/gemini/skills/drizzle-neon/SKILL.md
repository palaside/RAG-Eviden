---
name: drizzle-neon
description: >
  Manage schema design, SQL migrations, relationship queries, and connection pooling
  for Neon Serverless PostgreSQL using Drizzle ORM.
---

# Drizzle ORM & Neon Serverless PostgreSQL Skill

## 1. Core Architecture
- Neon uses Serverless HTTP / WebSocket connection pooling (`@neondatabase/serverless`).
- Drizzle connects using `drizzle-orm/neon-http` for edge/serverless speed, or `drizzle-orm/neon-serverless` with WebSocket for interactive transactions.

## 2. Directory Standard
- Schema: `src/db/schema.ts`
- Client: `src/lib/db.ts`
- Config: `drizzle.config.ts`

## 3. Best Practices
1. **Always use timestamps with timezone**: `timestamp("created_at", { withTimezone: true }).defaultNow().notNull()`.
2. **Never run raw destructive SQL**: Use `npx drizzle-kit push` for rapid prototyping or `npx drizzle-kit generate` for audited migrations.
3. **Clerk User ID Mapping**: Store Clerk user IDs in `varchar("user_id", { length: 256 }).notNull().unique()`.

