---
name: r2-presigned-upload
description: >
  Secure direct client-to-Cloudflare-R2 presigned URL generator with zero egress fees,
  MIME type validation, and signed temporary upload tokens.
---

# Cloudflare R2 Presigned Upload Skill

## 1. Flow
```
Client (Browser) -> Requests Signed URL -> Server (Next.js Route Handler /api/upload)
Server -> Generates 60s PutObjectCommand URL via @aws-sdk/s3-request-presigner -> Client
Client -> PUT direct to Cloudflare R2 with file bytes
Client -> Saves file metadata / public URL into Neon Database
```

## 2. Security Rules
1. **Never expose R2 Secret Keys** to the frontend.
2. Validate file size and MIME type on the server **before** issuing presigned URLs.
3. Restrict upload URLs with a short TTL (typically 60-120 seconds).
4. Sanitise filenames using random UUIDs: `${crypto.randomUUID()}-${file.name}`.

