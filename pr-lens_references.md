# references/config.md

# Correcting the map: `.github/pr-lens.yml`

The generated document is regenerated on every run, so editing it is pointless. Corrections live in `.github/pr-lens.yml`, an overlay applied over fresh inference every time. Inference never writes back into this file, which is why a correction keeps holding as the code moves.

```yaml
schemaVersion: 0.3.1          # required
lenses: [architecture, data-flow, data-model]
branding: true
map:
  rename:
    - match: functions/src/broadcast/sendBroadcastBulk.ts
      to: Broadcast sender
  exclude:
    - "**/*.test.ts"
    - scripts/**
  lane:
    - match: packages/broadcast-lib/**
      lane: functions
  group:
    - match: id:build-bulk-payload
      group: broadcast-lib
```

Every field except `schemaVersion` is optional, and the file itself is optional. For editor autocomplete, point at the published JSON Schema — no install needed:

```jsonc
{ "$ref": "https://unpkg.com/@coldtea/pr-lens-schema/json-schema/config.schema.json" }
```

## Selectors

A `match` beginning with `id:` addresses exactly one node, as in `id:build-bulk-payload`. Anything else is a repository-relative path glob matched against the node's file paths.

**Prefer the glob.** Ids come from inference and may change when the code does; a path correction survives that. Reach for `id:` only when no path distinguishes the node, or when the node has no files at all (an external service, a queue).

## The four corrections

| | What it does |
| --- | --- |
| `rename` | replaces the inferred label |
| `exclude` | drops matching nodes, and the edges and flow steps that hung from them |
| `lane` | moves matching nodes into a lane, **creating it** when the document declares no such id |
| `group` | clusters matching nodes under a sub-group inside their lane |

Up to 128 of each. They are about intent rather than structure: there is no way to add a node or draw an edge here, and the one thing a correction can bring into existence is a lane, a band a repository wants that inference did not find. It takes the id for its label, because the id is the only name this file carries, so write `lane: infrastructure` rather than `lane: l3`. If the map is wrong in a way corrections cannot express, the fix belongs in the analysis, not in this file.

## Recipes

**"Stop showing me the test files."**
```yaml
map:
  exclude: ["**/*.test.ts", "**/__tests__/**"]
```

**"That node is called the wrong thing."** Match the file it comes from, not its id:
```yaml
map:
  rename:
    - match: server/lib/broadcast/createBroadcastSendTask.ts
      to: Send task
```

**"These belong in a band of their own."** The lane need not exist yet:
```yaml
map:
  lane:
    - match: infra/**
      lane: infrastructure
```

**"Keep the shared library together."**
```yaml
map:
  group:
    - match: packages/broadcast-lib/**
      group: broadcast-lib
```

**"Only draw the architecture."**
```yaml
lenses: [architecture]
```

## Hosted GitHub App comments

The hosted App reads `github` settings from the PR's head commit. Other options apply to the CLI.

| Setting | Default | Effect |
| --- | --- | --- |
| `github.comment.collapsed` | `false` | Start diagrams and details closed. Drawing still runs automatically. |
| `github.draw` | `auto` | `on-demand` leaves a pull request undrawn, with a short notice, until someone comments `@pr-lens draw`. |
| `github.comment.notice` | `true` | `false` drops that notice, so an on-demand repository hears nothing until someone asks. |

## Check it

```bash
npx @coldtea/pr-lens-cli@latest validate .github/pr-lens.yml
```

`pr-lens render` reports any correction that changed nothing about the document it drew. That is a config that has drifted out of date, usually because the file a selector named has moved or gone. It is not an error and nothing stops, but it is worth fixing: a correction that matches nothing is a correction nobody is getting.


# references/graph-document.md

# Authoring a graph document

This page is the whole shape, and what a schema cannot tell you besides: which parts matter, and where documents actually go wrong. `references/example.graph.json` is one document that validates, if you would rather read than be told.

The validator enforces the same thing from a JSON Schema, published at `https://unpkg.com/@coldtea/pr-lens-schema/json-schema/graph-doc.schema.json` if you want it machine-readable.

Every schema here is **strict**: an unknown key is a rejection, not a warning. A field with a default may be left out.

## The document

```json
{
  "schemaVersion": "0.3.1",
  "kind": "graph",
  "title": "Batch broadcast sending through Postmark",
  "summary": "One paragraph answering: what does this change do?",
  "lenses": ["architecture", "data-flow"],
  "provenance": { "repo": { "owner": "…", "name": "…" }, "base": { "sha": "…" }, "head": { "sha": "…" } },
  "lanes": [],
  "nodes": [],
  "edges": [],
  "flows": [],
  "stats": {},
  "views": []
}
```

`lenses` declares what the document carries enough detail to draw: `architecture`, `data-flow`, `data-model`, or any of them together. A document carrying flows must declare `data-flow`; one carrying a `dataModel` must declare `data-model`.

`provenance` is where the document came from: the repository, the base and head commit shas (lowercase hex, 7-40 characters), optionally the pull request and the generator. When you produce a document through the CLI these are filled in from the repository, so do not invent them.

## Ids

`^[A-Za-z0-9][A-Za-z0-9._:/-]*$`, at most 128 characters, unique within their own collection. Use readable kebab-case: `broadcast-sender`, not `n1`. An id ends up in an SVG id, a URL fragment and a comment anchor, so nothing else is allowed through.

## Deltas

Every node, edge, flow and flow step declares one: `added`, `modified`, `removed`, `unchanged`.

`unchanged` is not padding. It is the neighbouring code the change touches, and it is what turns a diagram into a blast radius. A document whose every element is `added` describes a change nobody can place.

## Lanes

1 to 16. Every node belongs to exactly one.

```json
{ "id": "functions", "label": "Cloud Functions", "subtitle": "Node 20", "order": 1 }
```

`order` (0-64) places lanes left to right; ties fall back to array order. Give a lane a `delta` only when the lane itself is new or gone.

## Nodes

1 to 256.

```json
{
  "id": "send-broadcast-bulk",
  "label": "sendBroadcastBulk",
  "kind": "function",
  "delta": "added",
  "lane": "functions",
  "group": "broadcast-lib",
  "subtitle": "(broadcastId) => Promise<void>",
  "summary": "Claims the broadcast, builds one bulk payload and posts it.",
  "files": [{ "path": "functions/src/broadcast/sendBroadcastBulk.ts", "startLine": 1, "endLine": 142 }],
  "badges": ["retry"]
}
```

`kind` is one of `service app module function route job queue datastore cache external ui config test package other`. It drives the card's icon and shape and nothing else; when in doubt, `other` still renders.

`group` clusters nodes inside a lane: a package, a folder that means something. `files` (up to 64) become diff permalinks. `badges` (up to 6) are extra chips; the delta badge is drawn for you, so do not restate it.

## Edges

Up to 512.

```json
{
  "id": "bulk-to-postmark",
  "from": "send-broadcast-bulk",
  "to": "postmark",
  "kind": "http",
  "delta": "added",
  "label": "POST /email/bulk",
  "emphasis": "hero",
  "animated": true
}
```

`kind` is one of `call http rpc event queue data dependency render other`. `emphasis` is `normal` (default), `hero` or `muted`. More than one or two heroes and the emphasis stops meaning anything. `from` and `to` must be node ids you declared. This is the single most common failure.

## Flows

Up to 16, for the data-flow lens.

```json
{
  "id": "send-pipeline",
  "title": "Sending a broadcast",
  "delta": "modified",
  "participants": [{ "node": "queue-route" }, { "node": "send-broadcast-bulk" }, { "node": "postmark" }],
  "messages": [
    { "id": "enqueue", "from": "queue-route", "to": "send-broadcast-bulk", "label": "enqueue job", "kind": "async", "delta": "modified" },
    { "id": "send", "from": "send-broadcast-bulk", "to": "postmark", "label": "POST /email/bulk", "kind": "sync", "delta": "added", "repeat": 4 },
    { "id": "accepted", "from": "postmark", "to": "send-broadcast-bulk", "label": "200 Accepted", "kind": "return", "delta": "added" }
  ]
}
```

- 2 to 12 participants, ordered by array position; each names a node id.
- 1 to 64 messages. **Step order is array order**: there is no step number field, so a document cannot disagree with its own animation.
- `kind` is `sync`, `async`, `return` or `self`. `self` requires `from === to`, and no other kind may have them equal.
- Both endpoints must be participants of that flow, not merely nodes of the document.
- `repeat` says a step happens more than once per run, e.g. 4 batched requests.
- `payload`: what travels on the step. Optional. Only a canvas draws it, so leave it out of a document that is not going to one.

### Sample traffic

```json
{
  "id": "send",
  "from": "send-broadcast-bulk",
  "to": "postmark",
  "label": "POST /email/bulk",
  "kind": "sync",
  "delta": "added",
  "payload": {
    "request": {
      "type": "EmailBatch[500]",
      "shape": "Email[]  // max 500\nEmail = { From: string; To: string; Subject: string }",
      "sample": [{ "From": "news@example.com", "To": "ada@example.com", "Subject": "The batching issue, fixed" }],
      "before": [{ "From": "news@example.com", "To": "ada@example.com", "Cc": "ops@example.com", "Subject": "The batching issue, fixed" }],
      "source": { "path": "tests/fixtures/postmark-batch.json" }
    },
    "response": { "type": "void" }
  }
}
```

- A payload has `request`, `response` or both. One with neither is rejected.
- `type` is required on a side: a name a reader of the code would know, with the count in it for a collection (`EmailBatch[500]`). `void` for a side that carries nothing.
- `shape` is the type signature as text, up to 2048 bytes.
- `sample` and `before` are JSON values written inline, not JSON strings. A string where a value belongs is rejected. Each is at most 8 levels deep and 4096 bytes once serialised. The parser refuses a value over either cap rather than truncating it.
- `before` needs a `sample` to differ from.
- `source` is a file reference, the fixture or type the side was taken from.
- `changedPaths` is filled in when the document is stored, from `before` and `sample`. Do not write it. Up to 64 paths of the form `Metadata.batchId`, `[0].Cc` or `headers["Content-Type"]`.
- Use placeholder values in samples: `ada@example.com`, `cmp_0001`. Never one that could belong to a real person or unlock anything.

## Data model

For the data-model lens. Write one only when the change touched a schema: a migration, an ORM model, a schema or a SQL file. A change that touched no schema has no data model, and the document leaves `dataModel` out.

```json
{
  "stores": [
    { "id": "identity", "label": "Identity", "platform": "Postgres" },
    { "id": "billing", "label": "Billing", "platform": "Postgres" }
  ],
  "tables": [
    {
      "id": "user",
      "label": "User",
      "store": "identity",
      "name": "users",
      "delta": "modified",
      "badges": ["−1 column"],
      "columns": [
        { "name": "id", "type": "uuid", "key": "primary", "delta": "unchanged" },
        { "name": "email", "type": "citext", "delta": "unchanged" },
        { "name": "stripe_customer_id", "type": "text", "delta": "removed" }
      ],
      "files": [{ "path": "migrations/0042_billing_by_org.sql", "startLine": 30, "endLine": 34 }]
    },
    {
      "id": "subscription",
      "label": "Subscription",
      "store": "billing",
      "name": "subscriptions",
      "delta": "modified",
      "badges": ["key moved"],
      "columns": [
        { "name": "id", "type": "uuid", "key": "primary", "delta": "unchanged" },
        { "name": "user_id", "type": "uuid", "key": "foreign", "delta": "removed" },
        { "name": "org_id", "type": "uuid", "key": "foreign", "delta": "added" },
        { "name": "amount_cents", "type": "bigint", "previousType": "int", "delta": "modified" }
      ],
      "files": [{ "path": "migrations/0042_billing_by_org.sql", "startLine": 36, "endLine": 48 }]
    }
  ],
  "relations": [
    { "id": "subscription-user", "from": { "table": "subscription", "column": "user_id" }, "to": { "table": "user", "column": "id" }, "delta": "removed", "label": "billed to the user until now" }
  ]
}
```

- A `store` is a database, a schema or a namespace: the lane a table sits in, so split one database into the schemas or domains a reader would name (identity, workspace, billing) rather than one store for everything; the picture reads left to right. `label` is the team's word for it and `platform` the engine, which goes in the lane header beside the label, so do not repeat the engine in the label. 1 to 16.
- A `table` is a table, a collection or a key family: a Mongo collection with its fields, or a Redis key pattern such as `invoice:{id}:lock` with its fields and ttl, is a table in a store whose `platform` is that engine. `label` is what a reader calls it, `name` the physical name when it differs. 1 to 64 tables, each with 1 to 64 columns. Every table names a store you declared.
- Columns carry a delta each, so a dropped column is drawn struck through and an arrived one in green. `key` is `primary` for the table's own key, `foreign` for a column that holds another table's key, `index` for an index row; leave it out otherwise. A column whose type changed keeps the old spelling in `previousType`, so the picture says `int → bigint`. No table lists a column twice.
- A `relation` runs from the column that holds a key to the column it points at, each end `{ "table", "column" }`, and every end must be a column that table lists. `enforced: false` draws a reference nothing enforces, such as one across stores, as a dotted line. Up to 256.
- A key that moved from one table to another is two relations: the old one `removed`, with a `label` that is a short clause with a verb saying what was true before: who owned, held or paid for what. `user subscription` names the tables and says nothing; `shipped from the warehouse until now` on an orders key says what changed. Then the new one, `added`.
- A column's `type` is a name as the schema spells it, up to 64 characters: `uuid`, `text[]`, `numeric(5,4)`, `timestamp with time zone`. A quote, an equals sign, a slash, a colon or a `--` is refused, because they belong to defaults, literals, connection strings and comments, and the picture shows the shape of the data, never the data. A `summary` says what a table is for and names no value.
- Include the unchanged tables a changed key points at, marked `unchanged`, so the reader sees what hangs off the thing that moved. Leave out tables the change does not touch and nothing touched points at.
- `files` on a table are the migration and model lines that define it; they become the diff links.

## Stats

```json
{ "filesChanged": 27, "additions": 1979, "deletions": 1370, "chips": [{ "label": "Postmark calls", "value": "500x fewer", "tone": "hero" }] }
```

Up to 8 chips, `tone` one of `neutral added modified removed hero`. Per-delta element counts are deliberately absent from the schema: they are derivable from the document, and a stored copy can only go stale.

## Views

The drill-down tree in the comment: up to 32 at the root, nesting up to 32 children each. A document with no views renders as one picture and nothing else.

```json
{
  "id": "the-new-path",
  "title": "The new batch path",
  "lens": "architecture",
  "summary": "What replaced the per-recipient loop.",
  "defaultOpen": false,
  "scope": { "kind": "selection", "nodes": ["send-broadcast-bulk", "postmark"] },
  "children": []
}
```

`scope` is either `{ "kind": "all" }` (the default) or a selection naming at least one node, edge, flow or table. The two are distinct states on purpose: removing the last element a view pointed at can never quietly turn it into a view of everything. A view's `lens` must be one the document declares. A selection may also name lanes, but leave them out: a lane draws every node in it, wanted or not.

### Choosing architecture views

Treat the architecture tree as a set of decisions, not a quota:

1. Ask whether the change affects a user, an external system or a system boundary. If it does, start with a system-context view. If it does not, leave that level out.
2. Show affected applications, services, jobs, data stores and runtimes in a container view. Make it the root when there is no useful context view; otherwise make it a child of that context.
3. Add a component child only when the internals of an affected container matter to the change. Components may be modules, routes or functions, but the view should explain their responsibilities and relationships rather than mirror folders.
4. Stop at components unless someone explicitly asks for code-level detail.

One architecture view may be the right answer for a small change. Each child must move down exactly one level and cover a materially narrower scope. Skip a level when it would be empty, speculative or a repeat of its parent. Do not create two views with substantially the same nodes and edges, and do not infer a boundary from a folder name alone. Keep unchanged direct neighbours when they make the blast radius clear.

Set `defaultOpen: true` on the highest useful architecture view. Lower levels should normally stay collapsed. A data-flow view describes an ordered sequence, so keep it as a separate root instead of placing it inside the architecture hierarchy.

This compact fragment shows the shape. The selected ids refer to elements declared elsewhere in the document:

```json
{
  "views": [
    {
      "id": "checkout-context",
      "title": "Checkout in its environment",
      "lens": "architecture",
      "defaultOpen": true,
      "scope": {
        "kind": "selection",
        "nodes": ["shopper", "commerce-platform", "payment-provider", "fulfilment-system"],
        "edges": ["shopper-to-commerce", "commerce-to-payment", "commerce-to-fulfilment"]
      },
      "children": [
        {
          "id": "checkout-containers",
          "title": "Checkout containers",
          "lens": "architecture",
          "scope": {
            "kind": "selection",
            "nodes": ["storefront", "checkout-api", "orders-db", "payment-provider"],
            "edges": ["storefront-to-checkout", "checkout-to-orders", "checkout-to-payment"]
          },
          "children": [
            {
              "id": "checkout-components",
              "title": "Checkout API components",
              "lens": "architecture",
              "scope": {
                "kind": "selection",
                "nodes": ["checkout-route", "order-service", "payment-client"],
                "edges": ["route-to-orders", "orders-to-payment-client"]
              }
            }
          ]
        }
      ]
    },
    {
      "id": "place-order-flow",
      "title": "Placing an order",
      "lens": "data-flow",
      "scope": { "kind": "selection", "flows": ["place-order"] }
    }
  ]
}
```

## Walkthrough

Optional in the format, but write one for anything that is not trivial: more than one diagram, a diagram with several changed parts, or any flow. Skip it only when the document is one small diagram whose single step would just repeat the title. A canvas or a share page plays it.

```json
{
  "walkthrough": {
    "steps": [
      {
        "id": "four-batch-calls",
        "heading": "Postmark now gets 500 emails per call",
        "body": "One call per batch, and Postmark answers with a result for each message.",
        "stage": { "kind": "flow", "flow": "send-pipeline" },
        "focus": { "kind": "selection", "messages": ["batch-post", "batch-results"] },
        "detail": {
          "text": "sendBroadcastBulk posts each batch to Postmark and reads the results back.",
          "cites": [
            { "text": "sendBroadcastBulk", "ref": { "kind": "node", "node": "send-broadcast-bulk" } },
            { "text": "posts each batch", "ref": { "kind": "message", "flow": "send-pipeline", "message": "batch-post" } },
            { "text": "Postmark", "ref": { "kind": "node", "node": "postmark" } }
          ]
        }
      },
      {
        "id": "old-path-goes-dark",
        "heading": "processBroadcast and sendSingleEmail removed",
        "body": "sendBroadcastBulk does their job for whole batches.",
        "stage": { "kind": "view", "view": "retired-path" },
        "focus": { "kind": "selection", "nodes": ["process-broadcast", "send-single-email"] }
      }
    ]
  }
}
```

A walkthrough is a short guided tour of the diagrams. It has two to twelve steps. Each step shows one diagram, points at one part of it, and says a few words about it.

Every step is one change, never a description of the diagram: the heading names the thing and what happened to it, built from change words such as added, removed, replaced, now, moved and split, and the body is one line on what that means for behaviour, with the numbers when they matter. The headline change is step one and the last step is the last real change. Do not end on a recap: the reader already saw the whole picture when the canvas opened. Write it all for a smart twelve-year-old, in short common words and active voice. The skill page has the rule in full, with examples of a step written well and the same step written badly.

Each step has:

- `heading`: the thing and what happened to it, up to 48 characters, in sentence case. For example "Postmark now gets 500 emails per call".
- `body`: one line under the heading, up to 140 characters, on what the change means for behaviour. For example "One call per batch instead of one call per person". Required: a heading with no body reads as unfinished.
- `stage`: which diagram to show. A document can have several diagrams: its views (the drill-down diagrams) and its flows (the sequence diagrams). `{ "kind": "view", "view": "overview" }` shows the view called `overview`. `{ "kind": "flow", "flow": "send-pipeline" }` shows the flow called `send-pipeline`. Leave `stage` out and the step uses the diagram the reader is already on.
- `focus`: what to zoom in on inside that diagram. `{ "kind": "all" }`, the default, means the whole diagram. A selection means "just these things": name any lanes, nodes, edges, tables or flow steps (`messages`) by id, and the camera zooms to them while everything else dims. A selection must name at least one thing. The canvas lights everything inside one box around what a focus names, so keep it small: up to three nodes and the edges between them on a view of four cards or fewer, one node on a bigger view, and up to three flow steps in a row on a flow. Never name a lane. The skill page has the rule in full.
- `detail`: optional. One or two sentences under the body, up to 240 characters, that name the parts of the diagram the step is about. `text` is the sentence. `cites` turns words in it into links: each cite has `text`, copied letter for letter from the sentence, and a `ref`. A `ref` is `{ "kind": "node", "node": … }`, `{ "kind": "message", "flow": …, "message": … }`, `{ "kind": "view", "view": … }`, `{ "kind": "flow", "flow": … }`, `{ "kind": "table", "table": … }` or `{ "kind": "column", "table": …, "column": … }`. List cites in the order the sentence says them. A detail has one to eight, and no two use the same words. Do not cite files on a canvas you push: with no pull request behind it, a file link shows as plain words.

The validator checks:

- Every id you name exists in the document. A flow step you name must belong to the flow the stage shows, because flow step ids are only unique inside their own flow.
- `messages` needs a stage that shows a flow. Leave it out when the stage is an architecture view.
- Step ids are unique within the walkthrough. Two steps minimum, twelve maximum.
- Every cite's words are in its detail's `text`, in the order the cites are listed. The node, flow step, view, flow, table or column it points to exists in the document.
- A stored map never carries a walkthrough. A map describes the system; a walkthrough tells the story of one change.

A step about the data model stages the view whose lens is `data-model` and focuses `tables`. That is how a moved key gets its story: "Billing follows the org", focused on the two tables it moved between, with the old and new columns cited.

## Layout

```json
{ "direction": "right", "laneOrder": ["api", "functions", "external"], "rank": { "send-broadcast-bulk": 2 } }
```

Hints, not instructions: the renderer owns final placement, so a diagram stays deterministic and a stale hint cannot break it. Absolute coordinates are not expressible. Omitting `layout` entirely is normal.

## File references

```json
{ "path": "functions/src/broadcast/sendBroadcastBulk.ts", "startLine": 1, "endLine": 142, "revision": "head" }
```

Repository-relative POSIX paths: no leading `/`, no drive letter, no backslash, no `..` segment. Lines are 1-based, `endLine` requires `startLine` and may not precede it. `revision` defaults to `head`; use `base` on elements the change removes.

## Length limits

Labels 120 characters, summaries 2000, chip values 32. A data model holds up to 16 stores, 64 tables of 64 columns each, and 256 relations. They are display fields: a label that needs 120 characters is a label the diagram cannot draw. On a payload side, `shape` 2048 bytes, `sample` and `before` 4096 bytes each once serialised and 8 levels deep, `changedPaths` 64 entries.

## Then validate

```bash
npx @coldtea/pr-lens-cli@latest validate .pr-lens/graph.json
```

Every problem is reported at once, with a path into the document. Fix them all and run it again until it is clean.


# references/example.graph.json

{
  "schemaVersion": "0.3.1",
  "kind": "graph",
  "generatedAt": "2026-08-19T18:24:00.000Z",
  "title": "Batch broadcast sending through Postmark",
  "summary": "Broadcast delivery moves from one Postmark request per recipient to batched requests of 500, with suppression filtering pulled in front of the send and the payload builder extracted into a shared library.",
  "lenses": [
    "architecture",
    "data-flow"
  ],
  "provenance": {
    "repo": {
      "owner": "ohansemmanuel",
      "name": "bestregards",
      "host": "github.com"
    },
    "base": {
      "sha": "3f5c1ab9d24e7f08c6b1a5d3e9074c2b8a6f1d40",
      "ref": "main"
    },
    "head": {
      "sha": "b71e0d4c8a92f5361de7c0b4a8f2593d6c1e8a77",
      "ref": "batch-broadcast-send"
    },
    "pullRequest": {
      "number": 128,
      "title": "Send broadcasts in batches of 500",
      "url": "https://github.com/ohansemmanuel/bestregards/pull/128"
    },
    "generator": {
      "name": "pr-lens-examples",
      "version": "0.1.0"
    }
  },
  "lanes": [
    {
      "id": "web",
      "label": "Next.js",
      "subtitle": "Vercel",
      "order": 0
    },
    {
      "id": "functions",
      "label": "Cloud Functions",
      "subtitle": "Firebase",
      "order": 1
    },
    {
      "id": "external",
      "label": "External",
      "subtitle": "Postmark",
      "order": 2
    }
  ],
  "nodes": [
    {
      "id": "broadcast-composer",
      "label": "Broadcast composer",
      "kind": "ui",
      "delta": "unchanged",
      "lane": "web",
      "subtitle": "app/broadcasts/new",
      "summary": "Where an author writes a broadcast and hits send. Untouched by this change.",
      "files": [
        {
          "path": "app/broadcasts/new/page.tsx"
        }
      ],
      "badges": []
    },
    {
      "id": "queue-route",
      "label": "POST /api/broadcasts/queue",
      "kind": "route",
      "delta": "modified",
      "lane": "web",
      "summary": "Writes the queue document. Now stamps the recipient count and batch size the sender will use instead of leaving batching to the worker.",
      "files": [
        {
          "path": "app/api/broadcasts/queue/route.ts",
          "startLine": 24,
          "endLine": 96
        }
      ],
      "badges": [
        "+38 / -12"
      ]
    },
    {
      "id": "broadcast-queue",
      "label": "broadcastQueue",
      "kind": "datastore",
      "delta": "modified",
      "lane": "functions",
      "subtitle": "Firestore collection",
      "summary": "Queue documents gained batchSize and suppressedCount fields, and results are now written back per batch rather than per recipient.",
      "files": [
        {
          "path": "functions/src/broadcast/schema.ts",
          "startLine": 12,
          "endLine": 48
        }
      ],
      "badges": []
    },
    {
      "id": "send-broadcast-bulk",
      "label": "sendBroadcastBulk",
      "kind": "function",
      "delta": "added",
      "lane": "functions",
      "subtitle": "onWrite trigger",
      "summary": "New trigger handler. Fetches suppressions once, builds batched payloads, and posts them to Postmark in chunks of 500.",
      "files": [
        {
          "path": "functions/src/broadcast/sendBroadcastBulk.ts",
          "startLine": 1,
          "endLine": 142
        }
      ],
      "badges": [
        "new"
      ]
    },
    {
      "id": "build-bulk-payload",
      "label": "buildBulkPayload",
      "kind": "function",
      "delta": "added",
      "lane": "functions",
      "summary": "Turns a broadcast and its recipient slice into a Postmark batch request body.",
      "files": [
        {
          "path": "packages/broadcast-lib/src/buildBulkPayload.ts",
          "startLine": 1,
          "endLine": 74
        }
      ],
      "badges": []
    },
    {
      "id": "get-suppressed-emails",
      "label": "getSuppressedEmails",
      "kind": "function",
      "delta": "added",
      "lane": "functions",
      "summary": "Pulls the Postmark suppression dump once per broadcast so suppressed addresses are filtered before any batch is sent.",
      "files": [
        {
          "path": "packages/broadcast-lib/src/getSuppressedEmails.ts",
          "startLine": 1,
          "endLine": 58
        }
      ],
      "badges": []
    },
    {
      "id": "broadcast-lib",
      "label": "broadcast-lib",
      "kind": "package",
      "delta": "added",
      "lane": "functions",
      "subtitle": "packages/broadcast-lib",
      "summary": "New shared package so the queue route and the sender agree on payload shape and batch size.",
      "files": [
        {
          "path": "packages/broadcast-lib/src/index.ts"
        }
      ],
      "badges": [
        "new package"
      ]
    },
    {
      "id": "process-broadcast",
      "label": "processBroadcast",
      "kind": "function",
      "delta": "removed",
      "lane": "functions",
      "subtitle": "onWrite trigger",
      "summary": "The per-recipient loop this change replaces.",
      "files": [
        {
          "path": "functions/src/broadcast/processBroadcast.ts",
          "startLine": 1,
          "endLine": 118,
          "revision": "base"
        }
      ],
      "badges": []
    },
    {
      "id": "send-single-email",
      "label": "sendSingleEmail",
      "kind": "function",
      "delta": "removed",
      "lane": "functions",
      "summary": "One Postmark request per recipient. Gone with the loop that called it.",
      "files": [
        {
          "path": "functions/src/broadcast/sendSingleEmail.ts",
          "startLine": 1,
          "endLine": 46,
          "revision": "base"
        }
      ],
      "badges": []
    },
    {
      "id": "postmark",
      "label": "Postmark",
      "kind": "external",
      "delta": "modified",
      "lane": "external",
      "subtitle": "Email API",
      "summary": "Same provider, different endpoints: the batch endpoint and the suppression dump replace repeated single sends.",
      "files": [],
      "badges": []
    }
  ],
  "edges": [
    {
      "id": "composer-to-queue",
      "from": "broadcast-composer",
      "to": "queue-route",
      "kind": "http",
      "delta": "unchanged",
      "label": "send broadcast",
      "emphasis": "normal",
      "animated": false,
      "files": []
    },
    {
      "id": "queue-to-firestore",
      "from": "queue-route",
      "to": "broadcast-queue",
      "kind": "data",
      "delta": "modified",
      "label": "enqueue job",
      "emphasis": "normal",
      "animated": false,
      "files": []
    },
    {
      "id": "queue-to-lib",
      "from": "queue-route",
      "to": "broadcast-lib",
      "kind": "dependency",
      "delta": "added",
      "label": "batch size",
      "emphasis": "normal",
      "animated": false,
      "files": []
    },
    {
      "id": "firestore-to-bulk",
      "from": "broadcast-queue",
      "to": "send-broadcast-bulk",
      "kind": "event",
      "delta": "added",
      "label": "onWrite",
      "emphasis": "normal",
      "animated": false,
      "files": []
    },
    {
      "id": "firestore-to-process",
      "from": "broadcast-queue",
      "to": "process-broadcast",
      "kind": "event",
      "delta": "removed",
      "label": "onWrite",
      "emphasis": "normal",
      "animated": false,
      "files": []
    },
    {
      "id": "process-to-single",
      "from": "process-broadcast",
      "to": "send-single-email",
      "kind": "call",
      "delta": "removed",
      "label": "per recipient",
      "emphasis": "normal",
      "animated": false,
      "files": []
    },
    {
      "id": "single-to-postmark",
      "from": "send-single-email",
      "to": "postmark",
      "kind": "http",
      "delta": "removed",
      "label": "POST /email · 1 msg/call",
      "emphasis": "normal",
      "animated": false,
      "files": []
    },
    {
      "id": "bulk-to-payload",
      "from": "send-broadcast-bulk",
      "to": "build-bulk-payload",
      "kind": "call",
      "delta": "added",
      "emphasis": "normal",
      "animated": false,
      "files": []
    },
    {
      "id": "bulk-to-suppressions",
      "from": "send-broadcast-bulk",
      "to": "get-suppressed-emails",
      "kind": "call",
      "delta": "added",
      "emphasis": "normal",
      "animated": false,
      "files": []
    },
    {
      "id": "bulk-to-lib",
      "from": "send-broadcast-bulk",
      "to": "broadcast-lib",
      "kind": "dependency",
      "delta": "added",
      "emphasis": "normal",
      "animated": false,
      "files": []
    },
    {
      "id": "suppressions-to-postmark",
      "from": "get-suppressed-emails",
      "to": "postmark",
      "kind": "http",
      "delta": "added",
      "label": "GET suppression dump",
      "emphasis": "normal",
      "animated": true,
      "files": []
    },
    {
      "id": "bulk-to-postmark",
      "from": "send-broadcast-bulk",
      "to": "postmark",
      "kind": "http",
      "delta": "added",
      "label": "500 msgs/call",
      "emphasis": "hero",
      "animated": true,
      "summary": "The change in one edge: a broadcast to 10,000 recipients drops from 10,000 requests to 20.",
      "files": []
    },
    {
      "id": "bulk-to-firestore",
      "from": "send-broadcast-bulk",
      "to": "broadcast-queue",
      "kind": "data",
      "delta": "added",
      "label": "write results",
      "emphasis": "normal",
      "animated": false,
      "files": []
    }
  ],
  "flows": [
    {
      "id": "send-pipeline",
      "title": "Sending a broadcast",
      "summary": "The path a queued broadcast takes now, from enqueue to per-message results.",
      "delta": "modified",
      "participants": [
        {
          "node": "queue-route",
          "label": "queue route"
        },
        {
          "node": "broadcast-queue",
          "label": "Firestore"
        },
        {
          "node": "send-broadcast-bulk",
          "label": "sendBroadcastBulk"
        },
        {
          "node": "postmark",
          "label": "Postmark"
        }
      ],
      "messages": [
        {
          "id": "enqueue",
          "from": "queue-route",
          "to": "broadcast-queue",
          "label": "enqueue broadcast job",
          "kind": "async",
          "delta": "modified",
          "animated": true,
          "files": []
        },
        {
          "id": "trigger",
          "from": "broadcast-queue",
          "to": "send-broadcast-bulk",
          "label": "onWrite trigger",
          "kind": "async",
          "delta": "added",
          "animated": true,
          "files": []
        },
        {
          "id": "suppressions-request",
          "from": "send-broadcast-bulk",
          "to": "postmark",
          "label": "GET suppression dump",
          "kind": "sync",
          "delta": "added",
          "animated": true,
          "files": []
        },
        {
          "id": "suppressions-response",
          "from": "postmark",
          "to": "send-broadcast-bulk",
          "label": "suppressed addresses",
          "kind": "return",
          "delta": "added",
          "animated": true,
          "note": "Fetched once per broadcast, not once per recipient.",
          "files": []
        },
        {
          "id": "batch-post",
          "from": "send-broadcast-bulk",
          "to": "postmark",
          "label": "POST /email/batch · 500 msgs",
          "kind": "sync",
          "delta": "added",
          "animated": true,
          "repeat": 4,
          "note": "One request per 500 recipients; four for this 2,000-recipient broadcast.",
          "files": []
        },
        {
          "id": "batch-results",
          "from": "postmark",
          "to": "send-broadcast-bulk",
          "label": "per-message results",
          "kind": "return",
          "delta": "added",
          "animated": true,
          "files": []
        },
        {
          "id": "write-results",
          "from": "send-broadcast-bulk",
          "to": "broadcast-queue",
          "label": "write results",
          "kind": "async",
          "delta": "added",
          "animated": true,
          "files": []
        }
      ]
    }
  ],
  "stats": {
    "filesChanged": 14,
    "additions": 486,
    "deletions": 212,
    "chips": [
      {
        "label": "Postmark calls",
        "value": "500× fewer",
        "tone": "hero"
      },
      {
        "label": "New",
        "value": "4 units",
        "tone": "added"
      },
      {
        "label": "Retired",
        "value": "2 units",
        "tone": "removed"
      }
    ]
  },
  "views": [
    {
      "id": "overview",
      "title": "Architecture — blast radius",
      "lens": "architecture",
      "summary": "Everything this change touches, across all three lanes.",
      "scope": {
        "kind": "all"
      },
      "defaultOpen": true,
      "children": [
        {
          "id": "new-batch-path",
          "title": "The new batch path",
          "lens": "architecture",
          "summary": "What replaced the per-recipient loop.",
          "scope": {
            "kind": "selection",
            "lanes": [],
            "nodes": [
              "send-broadcast-bulk",
              "build-bulk-payload",
              "get-suppressed-emails",
              "broadcast-lib",
              "postmark"
            ],
            "edges": [
              "bulk-to-payload",
              "bulk-to-suppressions",
              "bulk-to-lib",
              "suppressions-to-postmark",
              "bulk-to-postmark",
              "bulk-to-firestore"
            ],
            "flows": [],
            "tables": []
          },
          "defaultOpen": false,
          "children": []
        },
        {
          "id": "retired-path",
          "title": "What was retired",
          "lens": "architecture",
          "summary": "The single-send path, kept visible so a reviewer can confirm nothing else called it.",
          "scope": {
            "kind": "selection",
            "lanes": [],
            "nodes": [
              "process-broadcast",
              "send-single-email"
            ],
            "edges": [
              "firestore-to-process",
              "process-to-single",
              "single-to-postmark"
            ],
            "flows": [],
            "tables": []
          },
          "defaultOpen": false,
          "children": []
        }
      ]
    },
    {
      "id": "send-pipeline-view",
      "title": "Data flow — sending a broadcast",
      "lens": "data-flow",
      "scope": {
        "kind": "selection",
        "lanes": [],
        "nodes": [],
        "edges": [],
        "flows": [
          "send-pipeline"
        ],
        "tables": []
      },
      "defaultOpen": false,
      "children": []
    }
  ],
  "walkthrough": {
    "steps": [
      {
        "id": "four-batch-calls",
        "heading": "Postmark now gets 500 emails per call",
        "body": "One call per batch, and Postmark answers with a result for each message.",
        "stage": {
          "kind": "flow",
          "flow": "send-pipeline"
        },
        "focus": {
          "kind": "selection",
          "lanes": [],
          "nodes": [],
          "edges": [],
          "messages": [
            "batch-post",
            "batch-results"
          ],
          "tables": []
        }
      },
      {
        "id": "route-queues",
        "heading": "Route now queues the job instead of sending",
        "body": "The API call finishes at once. A worker sends the mail later.",
        "stage": {
          "kind": "flow",
          "flow": "send-pipeline"
        },
        "focus": {
          "kind": "selection",
          "lanes": [],
          "nodes": [],
          "edges": [],
          "messages": [
            "enqueue"
          ],
          "tables": []
        }
      },
      {
        "id": "batches-of-500",
        "heading": "sendBroadcastBulk added for whole batches",
        "body": "Nothing loops over recipients any more. The sender works on a whole batch at a time.",
        "stage": {
          "kind": "view",
          "view": "new-batch-path"
        },
        "focus": {
          "kind": "selection",
          "lanes": [],
          "nodes": [
            "send-broadcast-bulk"
          ],
          "edges": [],
          "messages": [],
          "tables": []
        }
      },
      {
        "id": "suppression-first",
        "heading": "getSuppressedEmails added before the send",
        "body": "It pulls the blocked addresses once, before any batch is built.",
        "stage": {
          "kind": "view",
          "view": "new-batch-path"
        },
        "focus": {
          "kind": "selection",
          "lanes": [],
          "nodes": [
            "get-suppressed-emails"
          ],
          "edges": [],
          "messages": [],
          "tables": []
        }
      },
      {
        "id": "old-path-goes-dark",
        "heading": "processBroadcast and sendSingleEmail removed",
        "body": "sendBroadcastBulk does their job for whole batches.",
        "stage": {
          "kind": "view",
          "view": "retired-path"
        },
        "focus": {
          "kind": "selection",
          "lanes": [],
          "nodes": [
            "process-broadcast",
            "send-single-email"
          ],
          "edges": [],
          "messages": [],
          "tables": []
        }
      }
    ]
  },
  "layout": {
    "direction": "right",
    "laneOrder": [
      "web",
      "functions",
      "external"
    ],
    "rank": {
      "queue-route": 0,
      "send-broadcast-bulk": 1,
      "postmark": 2
    }
  }
}

