/**
 * Advanced AI Agent Framework Architecture - Core TypeScript Engine
 * Standard: Next.js 16 + React 19 + Node.js 20+ Production Grade
 * Architecture: 5 Pillars × 6 Sub-items (Strict Zero-Any Contract)
 */

import { z } from "zod";

// ============================================================================
// Pillar 1: Prompt Engineering Types
// ============================================================================

export const PersonaRoleSchema = z.enum([
  "ROOT_ARCHITECT",
  "TECH_LEAD",
  "CHEAT_CODE_DEVELOPER",
  "FORENSIC_QA_AUDITOR",
]);

export type PersonaRole = z.infer<typeof PersonaRoleSchema>;

export const PromptContractSchema = z.object({
  persona: PersonaRoleSchema,
  missionBackground: z.string().min(1),
  taskInstructions: z.array(z.string().min(1)),
  invariantsGuardrails: z.array(z.string().min(1)),
  outputEnvelopeFormat: z.string().default("JSON_ENVELOPE"),
  fewShotExamples: z.array(
    z.object({
      input: z.string(),
      badOutput: z.string(),
      goodOutput: z.string(),
      rationale: z.string(),
    })
  ).default([]),
});

export type PromptContract = z.infer<typeof PromptContractSchema>;

// ============================================================================
// Pillar 2: Context Engineering Types
// ============================================================================

export const ContextBudgetTierSchema = z.enum([
  "TIER_S_CAVEMAN", // Max 2,000 tokens
  "TIER_M_STANDARD", // Max 8,000 tokens
  "TIER_L_ARCHITECT", // Max 32,000 tokens
  "TIER_XL_FORENSIC", // Max 128,000 tokens
]);

export type ContextBudgetTier = z.infer<typeof ContextBudgetTierSchema>;

export const DynamicEnvironmentContextSchema = z.object({
  currentGitBranch: z.string(),
  uncommittedChangesCount: z.number().int().nonnegative(),
  operatingSystem: z.enum(["WINDOWS", "LINUX", "DARWIN"]),
  nodeVersion: z.string(),
  activeListeningPorts: z.array(z.number().int().positive()),
  missingEnvKeys: z.array(z.string()).default([]),
});

export type DynamicEnvironmentContext = z.infer<typeof DynamicEnvironmentContextSchema>;

export const ContextHydrationPayloadSchema = z.object({
  tier: ContextBudgetTierSchema.default("TIER_M_STANDARD"),
  tokenBudgetCap: z.number().int().positive(),
  retrievedDocumentIds: z.array(z.string()),
  shortTermScratchpad: z.string().default(""),
  environment: DynamicEnvironmentContextSchema,
});

export type ContextHydrationPayload = z.infer<typeof ContextHydrationPayloadSchema>;

// ============================================================================
// Pillar 3: Harness Engineering Types
// ============================================================================

export const ToolCallRequestSchema = z.object({
  callId: z.string().uuid(),
  toolName: z.string(),
  argumentsPayload: z.record(z.string(), z.unknown()),
  isHighRiskAction: z.boolean().default(false),
  requiresHumanApproval: z.boolean().default(false),
});

export type ToolCallRequest = z.infer<typeof ToolCallRequestSchema>;

export const ToolCallResponseSchema = z.object({
  callId: z.string().uuid(),
  exitCode: z.number().int(),
  stdout: z.string(),
  stderr: z.string(),
  durationMs: z.number().nonnegative(),
  telemetrySpanId: z.string().optional(),
});

export type ToolCallResponse = z.infer<typeof ToolCallResponseSchema>;

// ============================================================================
// Pillar 4: Loop Engineering Types
// ============================================================================

export const LoopPhaseSchema = z.enum([
  "PLAN",
  "ACT",
  "OBSERVE",
  "REFLECT",
  "CIRCUIT_BREAKER_HALTED",
  "COMPLETED",
]);

export type LoopPhase = z.infer<typeof LoopPhaseSchema>;

export const CircuitBreakerConfigSchema = z.object({
  maxIterations: z.literal(3).default(3), // Hard limit <= 3 loops
  currentIteration: z.number().int().min(0).max(3).default(0),
  isTripped: z.boolean().default(false),
  trippedReason: z.string().optional(),
});

export type CircuitBreakerConfig = z.infer<typeof CircuitBreakerConfigSchema>;

export const ActiveTaskLockSchema = z.object({
  taskId: z.string(),
  title: z.string(),
  startedAt: z.number().int().positive(),
  status: z.enum(["IN_PROGRESS", "SELF_HEALING", "VERIFIED", "ESCALATED"]),
  activeLoopCount: z.number().int().min(0).max(3).default(0),
  lastRootCause: z.string().optional(),
});

export type ActiveTaskLock = z.infer<typeof ActiveTaskLockSchema>;

// ============================================================================
// Pillar 5: Graph Engineering Types
// ============================================================================

export const GraphNodeIdSchema = z.enum([
  "NODE_START",
  "NODE_CONTEXT_HYDRATION",
  "NODE_PROMPT_COMPILATION",
  "NODE_EXECUTION_LOOP",
  "NODE_HARNESS_DISPATCH",
  "NODE_VERIFICATION_GATE",
  "NODE_CIRCUIT_BREAKER",
  "NODE_ARTIFACT_EMISSION",
  "NODE_SUCCESS_TERMINATION",
]);

export type GraphNodeId = z.infer<typeof GraphNodeIdSchema>;

export const ArtifactOutputSchema = z.object({
  artifactId: z.string().uuid(),
  title: z.string(),
  fileBasename: z.string(),
  absolutePath: z.string(),
  summary: z.string(),
  format: z.enum(["MARKDOWN", "TYPESCRIPT", "MERMAID", "JSON"]),
  content: z.string(),
});

export type ArtifactOutput = z.infer<typeof ArtifactOutputSchema>;

// ============================================================================
// The Unified Sovereign Agent State Machine
// ============================================================================

export const SovereignAgentStateSchema = z.object({
  sessionId: z.string().uuid(),
  currentNode: GraphNodeIdSchema.default("NODE_START"),
  promptContract: PromptContractSchema,
  contextHydration: ContextHydrationPayloadSchema,
  circuitBreaker: CircuitBreakerConfigSchema,
  activeTask: ActiveTaskLockSchema.nullable().default(null),
  recentToolCalls: z.array(ToolCallResponseSchema).default([]),
  producedArtifacts: z.array(ArtifactOutputSchema).default([]),
});

export type SovereignAgentState = z.infer<typeof SovereignAgentStateSchema>;

// ============================================================================
// Engine Transition Reducer Helper
// ============================================================================

export function advanceAgentState(
  prevState: SovereignAgentState,
  action:
    | { type: "START_TASK"; payload: ActiveTaskLock }
    | { type: "RECORD_TOOL_CALL"; payload: ToolCallResponse }
    | { type: "INCREMENT_LOOP"; payload: { rootCause?: string } }
    | { type: "TRIP_CIRCUIT_BREAKER"; payload: { reason: string } }
    | { type: "COMPLETE_TASK"; payload: ArtifactOutput }
): SovereignAgentState {
  switch (action.type) {
    case "START_TASK":
      return {
        ...prevState,
        currentNode: "NODE_EXECUTION_LOOP",
        activeTask: action.payload,
      };

    case "RECORD_TOOL_CALL":
      return {
        ...prevState,
        recentToolCalls: [action.payload, ...prevState.recentToolCalls.slice(0, 9)],
      };

    case "INCREMENT_LOOP": {
      const nextIteration = prevState.circuitBreaker.currentIteration + 1;
      if (nextIteration >= 3) {
        return {
          ...prevState,
          currentNode: "NODE_CIRCUIT_BREAKER",
          circuitBreaker: {
            ...prevState.circuitBreaker,
            currentIteration: 3,
            isTripped: true,
            trippedReason: action.payload.rootCause ?? "Max 3 Loops exceeded",
          },
        };
      }
      return {
        ...prevState,
        circuitBreaker: {
          ...prevState.circuitBreaker,
          currentIteration: nextIteration,
        },
      };
    }

    case "TRIP_CIRCUIT_BREAKER":
      return {
        ...prevState,
        currentNode: "NODE_CIRCUIT_BREAKER",
        circuitBreaker: {
          ...prevState.circuitBreaker,
          isTripped: true,
          trippedReason: action.payload.reason,
        },
      };

    case "COMPLETE_TASK":
      return {
        ...prevState,
        currentNode: "NODE_SUCCESS_TERMINATION",
        producedArtifacts: [action.payload, ...prevState.producedArtifacts],
        activeTask: null,
      };

    default:
      return prevState;
  }
}

