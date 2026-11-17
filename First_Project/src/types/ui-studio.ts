/**
 * 360° UI Studio Specification & Unified State Contract
 * Standard: Next.js 16 + React 19 Production Grade (Strict Zero-Any)
 * Single Source of Truth (SSOT) with Zod Runtime Validation
 */

import { z } from "zod";

// ============================================================================
// 1. Meta Session & Agent Status Schemas
// ============================================================================

export const AgentStatusSchema = z.enum([
  "IDLE",
  "COMPILING_LIVE",
  "WARNING_CONTRAST",
  "ERROR_OVERLAPPING",
  "CRITICAL_FAILURE",
]);

export type AgentStatus = z.infer<typeof AgentStatusSchema>;

export const MetaSessionSchema = z.object({
  sessionId: z.string().uuid(),
  timestamp: z.number().int().nonnegative(),
  tokenUsage: z.number().int().nonnegative().default(0),
  agentStatus: AgentStatusSchema.default("IDLE"),
  activeBreakpoint: z.enum(["DESKTOP", "TABLET", "MOBILE"]).default("DESKTOP"),
});

export type MetaSession = z.infer<typeof MetaSessionSchema>;

// ============================================================================
// 2. Context Preset Matrix Schemas (6-Axis Context)
// ============================================================================

export const ArchitecturalBaseSchema = z.enum([
  "DASHBOARD",
  "LANDING_PAGE",
  "MOBILE_INTERFACE",
  "ECOMMERCE",
]);

export const DomainIndustrySchema = z.enum([
  "CYBERSECURITY",
  "FINTECH",
  "AI_DEEPTECH",
  "LUXURY_BRAND",
]);

export const ToneAestheticSchema = z.enum([
  "TACTICAL_NEO_BRUTALISM",
  "EXECUTIVE_LUXURY",
  "DEEP_SPACE_MINIMAL",
]);

export const KineticVelocitySchema = z.enum([
  "SNAP_100MS",
  "FLUID_300MS",
]);

export const LayoutDensitySchema = z.enum([
  "COMPACT_8PX",
  "SPACIOUS_24PX",
]);

export const TargetFrameworkSchema = z.enum([
  "TAILWIND_V4",
  "PURE_CSS",
  "REACT_TSX",
]);

export const ContextPresetSchema = z.object({
  architecturalBase: ArchitecturalBaseSchema.default("DASHBOARD"),
  domainIndustry: DomainIndustrySchema.default("CYBERSECURITY"),
  toneAesthetic: ToneAestheticSchema.default("TACTICAL_NEO_BRUTALISM"),
  kineticVelocity: KineticVelocitySchema.default("SNAP_100MS"),
  layoutDensity: LayoutDensitySchema.default("COMPACT_8PX"),
  targetFramework: TargetFrameworkSchema.default("TAILWIND_V4"),
});

export type ContextPreset = z.infer<typeof ContextPresetSchema>;

// ============================================================================
// 3. Layout Engine Schemas
// ============================================================================

export const DisplaySystemSchema = z.enum([
  "CSS_GRID",
  "FLEXBOX",
  "BLOCK_INLINE",
  "ABSOLUTE_HUD",
]);

export const LayoutEngineSchema = z.object({
  displaySystem: DisplaySystemSchema.default("CSS_GRID"),
  columns: z.number().int().min(1).max(24).default(12),
  rows: z.number().int().min(1).max(24).default(6),
  gapPx: z.number().int().multipleOf(4).default(8),
  paddingPx: z.number().int().multipleOf(4).default(16),
  isContainerConstrained: z.boolean().default(true),
  maxContainerWidthPx: z.number().int().positive().default(1440),
});

export type LayoutEngine = z.infer<typeof LayoutEngineSchema>;

// ============================================================================
// 4. Design Tokens & Geometry Schemas
// ============================================================================

/**
 * Strict Radius Limit Constraint:
 * 0px (None), 2px (Critical/Micro), 4px (Premium/Max Allowed)
 */
export const RadiusTokenSchema = z.union([
  z.literal(0),
  z.literal(2),
  z.literal(4),
]);

export type RadiusToken = z.infer<typeof RadiusTokenSchema>;

export const ColorPaletteSchema = z.object({
  bgPrimary: z.string().regex(/^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$/),
  bgSurface: z.string().regex(/^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$/),
  bgElevated: z.string().regex(/^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$/),
  accentPrimary: z.string().regex(/^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$/),
  accentAlert: z.string().regex(/^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$/),
  textPrimary: z.string().regex(/^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$/),
  textSecondary: z.string().regex(/^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$/),
});

export type ColorPalette = z.infer<typeof ColorPaletteSchema>;

export const VisualEffectsSchema = z.object({
  backdropBlurPx: z.number().int().min(0).max(64).default(16),
  hairlineBorderWidthPx: z.number().min(0.5).max(2).default(1),
  specularGlowOpacity: z.number().min(0).max(1).default(0.15),
  boxShadowIntensity: z.number().min(0).max(1).default(0.5),
});

export type VisualEffects = z.infer<typeof VisualEffectsSchema>;

export const TypographyTokensSchema = z.object({
  fontHeading: z.string().default("Space Grotesk"),
  fontBody: z.string().default("Inter"),
  fontCode: z.string().default("JetBrains Mono"),
  antiDisplacementLock: z.literal(true).default(true), // Always true to enforce CLS = 0
});

export type TypographyTokens = z.infer<typeof TypographyTokensSchema>;

export const DesignTokensSchema = z.object({
  palette: ColorPaletteSchema,
  radiusPx: RadiusTokenSchema.default(0),
  effects: VisualEffectsSchema.default({
    backdropBlurPx: 16,
    hairlineBorderWidthPx: 1,
    specularGlowOpacity: 0.15,
    boxShadowIntensity: 0.5,
  }),
  typography: TypographyTokensSchema.default({
    fontHeading: "Space Grotesk",
    fontBody: "Inter",
    fontCode: "JetBrains Mono",
    antiDisplacementLock: true,
  }),
});

export type DesignTokens = z.infer<typeof DesignTokensSchema>;

// ============================================================================
// 5. Unified State Object (Single Source of Truth)
// ============================================================================

export const UnifiedStateSchema = z.object({
  metaSession: MetaSessionSchema,
  contextPreset: ContextPresetSchema,
  layoutEngine: LayoutEngineSchema,
  designTokens: DesignTokensSchema,
});

export type UnifiedState = z.infer<typeof UnifiedStateSchema>;

// ============================================================================
// 6. Dual-Track Event Actions & Dispatch Contracts
// ============================================================================

export type Track1DirectDOMAction = {
  type: "DIRECT_DOM_INJECT";
  payload: {
    tokenKey: string;
    value: string;
  };
};

export type Track2ThrottledCompileAction = {
  type: "THROTTLED_COMPILE_TRIGGER";
  payload: {
    targetFramework: z.infer<typeof TargetFrameworkSchema>;
    stateSnapshot: UnifiedState;
  };
};

export type StudioAction =
  | Track1DirectDOMAction
  | Track2ThrottledCompileAction
  | { type: "SET_RADIUS"; payload: RadiusToken }
  | { type: "SET_COLOR"; payload: { key: keyof ColorPalette; value: string } }
  | { type: "SET_AGENT_STATUS"; payload: AgentStatus }
  | { type: "RESTORE_SNAPSHOT"; payload: UnifiedState };

// ============================================================================
// 7. Initial Default State Constant (Tactical Neo-Brutalism Starter)
// ============================================================================

export const DEFAULT_UNIFIED_STATE: UnifiedState = {
  metaSession: {
    sessionId: "00000000-0000-0000-0000-000000000000",
    timestamp: Date.now(),
    tokenUsage: 0,
    agentStatus: "IDLE",
    activeBreakpoint: "DESKTOP",
  },
  contextPreset: {
    architecturalBase: "DASHBOARD",
    domainIndustry: "CYBERSECURITY",
    toneAesthetic: "TACTICAL_NEO_BRUTALISM",
    kineticVelocity: "SNAP_100MS",
    layoutDensity: "COMPACT_8PX",
    targetFramework: "TAILWIND_V4",
  },
  layoutEngine: {
    displaySystem: "CSS_GRID",
    columns: 12,
    rows: 6,
    gapPx: 8,
    paddingPx: 16,
    isContainerConstrained: true,
    maxContainerWidthPx: 1440,
  },
  designTokens: {
    palette: {
      bgPrimary: "#121214",
      bgSurface: "#0B0C10",
      bgElevated: "#1F2833",
      accentPrimary: "#FFB000",
      accentAlert: "#8B0000",
      textPrimary: "#F0F2F5",
      textSecondary: "#9AA0A6",
    },
    radiusPx: 0,
    effects: {
      backdropBlurPx: 16,
      hairlineBorderWidthPx: 1,
      specularGlowOpacity: 0.15,
      boxShadowIntensity: 0.5,
    },
    typography: {
      fontHeading: "Space Grotesk",
      fontBody: "Inter",
      fontCode: "JetBrains Mono",
      antiDisplacementLock: true,
    },
  },
};

