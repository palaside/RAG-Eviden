/**
 * AI Engineering Execution Policy v2.0 - Core TypeScript Engine
 * Standard: Next.js 16 + React 19 + Node.js 20+ Production Grade
 * Strict Zero-Any Contract & Runtime Evidence Validation
 */

import { z } from "zod";

// ============================================================================
// 1. Evidence Classification Schemas
// ============================================================================

export const EvidenceGradeSchema = z.enum([
  "VERIFIED",   // Direct primary evidence proves runtime behavior
  "INFERRED",   // Strongly supported but lacks direct runtime proof
  "UNKNOWN",    // Available evidence is insufficient (honest state)
  "NOT_FOUND",  // Definitively searched and absent (valid empirical data)
]);

export type EvidenceGrade = z.infer<typeof EvidenceGradeSchema>;

export const EvidenceSourceTypeSchema = z.enum([
  "PRIMARY_REPOSITORY_EVIDENCE", // Source code, package.json, runtime logs
  "SECONDARY_AI_SUMMARY",        // AI markdown summaries, prior chat history
]);

export type EvidenceSourceType = z.infer<typeof EvidenceSourceTypeSchema>;

export const EvidenceRecordSchema = z.object({
  claim: z.string().min(1).describe("The technical claim made regarding system behavior"),
  grade: EvidenceGradeSchema,
  sourceType: EvidenceSourceTypeSchema,
  primaryProofPath: z.string().optional().describe("Absolute file path or command proving the claim"),
  exitCode: z.number().int().optional().describe("Command exit code if proven via execution"),
  auditTimestamp: z.number().int().positive().default(() => Date.now()),
});

export type EvidenceRecord = z.infer<typeof EvidenceRecordSchema>;

// ============================================================================
// 2. Scope Lock Contract Schemas
// ============================================================================

export const ScopeLockContractSchema = z.object({
  taskId: z.string().uuid(),
  objective: z.string().min(1),
  currentBehavior: z.string().min(1),
  expectedBehavior: z.string().min(1),
  inScope: z.array(z.string().min(1)),
  outOfScope: z.array(z.string().min(1)),
  allowedPaths: z.array(z.string().min(1)),
  forbiddenPaths: z.array(z.string().min(1)),
  dependencies: z.array(z.string()).default([]),
  risks: z.array(z.string()).default([]),
  acceptanceCriteria: z.array(z.string().min(1)),
  validationRequirements: z.array(z.string().min(1)),
});

export type ScopeLockContract = z.infer<typeof ScopeLockContractSchema>;

// ============================================================================
// 3. Instruction Priority Tiers
// ============================================================================

export const InstructionPriorityTierSchema = z.enum([
  "TIER_1_REPOSITORY_MANDATORY_POLICY",
  "TIER_2_APPROVED_TASK_CONTRACT",
  "TIER_3_ARCHITECTURE_ROUTING_STATE_RULES",
  "TIER_4_SECURITY_CODING_STANDARDS",
  "TIER_5_EXECUTION_POLICY",
  "TIER_6_PROJECT_CONVENTIONS",
  "TIER_7_GENERAL_BEST_PRACTICES",
]);

export type InstructionPriorityTier = z.infer<typeof InstructionPriorityTierSchema>;

// ============================================================================
// 4. Policy Violation & Audit Schemas
// ============================================================================

export const PolicyViolationTypeSchema = z.enum([
  "FORBIDDEN_PATH_ACCESSED",
  "UNVERIFIED_CLAIM_PROMOTED",
  "SECONDARY_EVIDENCE_AS_PRIMARY",
  "OUT_OF_SCOPE_MODIFICATION",
  "CIRCUIT_BREAKER_EXCEEDED",
  "ROOT_ROUTE_OVERWRITE_ATTEMPT",
]);

export type PolicyViolationType = z.infer<typeof PolicyViolationTypeSchema>;

export const PolicyViolationSchema = z.object({
  violationType: PolicyViolationTypeSchema,
  violatingPathOrClaim: z.string(),
  reason: z.string(),
  severity: z.enum(["WARNING", "FATAL"]),
  timestamp: z.number().int().positive().default(() => Date.now()),
});

export type PolicyViolation = z.infer<typeof PolicyViolationSchema>;

// ============================================================================
// 5. Policy Enforcement & Verification Engine
// ============================================================================

/**
 * Validates whether an evidence record adheres strictly to the rule:
 * Secondary AI evidence CANNOT independently prove a claim as VERIFIED.
 */
export function validateEvidenceRecord(record: EvidenceRecord): {
  isValid: boolean;
  violation?: PolicyViolation;
} {
  if (
    record.grade === "VERIFIED" &&
    record.sourceType === "SECONDARY_AI_SUMMARY"
  ) {
    return {
      isValid: false,
      violation: {
        violationType: "SECONDARY_EVIDENCE_AS_PRIMARY",
        violatingPathOrClaim: record.claim,
        reason: "Secondary AI documents cannot independently award VERIFIED grade without primary code/test proof.",
        severity: "FATAL",
        timestamp: Date.now(),
      },
    };
  }

  return { isValid: true };
}

/**
 * Validates whether a file path modification is permitted under the ScopeLock contract
 * and protects Root Routes from unrequested overwrites.
 */
export function validateFileModification(
  targetPath: string,
  scopeLock: ScopeLockContract
): {
  isAllowed: boolean;
  violation?: PolicyViolation;
} {
  const normalizedTarget = targetPath.replace(/\\/g, "/").toLowerCase();

  // Root route protection invariant
  const rootProtected = [
    "src/app/page.tsx",
    "src/app/layout.tsx",
    "src/middleware.ts",
  ];

  if (rootProtected.some((p) => normalizedTarget.endsWith(p.toLowerCase()))) {
    const isExplicitlyAllowed = scopeLock.allowedPaths.some((p) =>
      normalizedTarget.includes(p.replace(/\\/g, "/").toLowerCase())
    );

    if (!isExplicitlyAllowed) {
      return {
        isAllowed: false,
        violation: {
          violationType: "ROOT_ROUTE_OVERWRITE_ATTEMPT",
          violatingPathOrClaim: targetPath,
          reason: "Attempted modification of protected root entry point without explicit ScopeLock authorization.",
          severity: "FATAL",
          timestamp: Date.now(),
        },
      };
    }
  }

  // Check forbidden paths
  const isForbidden = scopeLock.forbiddenPaths.some((p) =>
    normalizedTarget.includes(p.replace(/\\/g, "/").toLowerCase())
  );

  if (isForbidden) {
    return {
      isAllowed: false,
      violation: {
        violationType: "FORBIDDEN_PATH_ACCESSED",
        violatingPathOrClaim: targetPath,
        reason: "Path is listed in ScopeLock forbiddenPaths.",
        severity: "FATAL",
        timestamp: Date.now(),
      },
    };
  }

  return { isAllowed: true };
}

