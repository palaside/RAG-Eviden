# 🔄 PROJECT FLOW: ชวกม.2 (Digital Evidence & Court Dossier Architecture)

## 1. System Interaction Architecture (Mermaid)

```mermaid
graph TD
    subgraph Intake ["Phase 1: Evidence Ingestion & Forensic Intake"]
        A1["Raw LINE Chat Screenshots (106 Images)"] --> B1["Binary MD5 Hash Audit & De-duplication"]
        A2["Bank Transaction Slips"] --> B1
        B1 --> B2["Unique Evidence Pool (997 Files)"]
    end

    subgraph OCR ["Phase 2: High-Speed Hybrid OCR Engine"]
        B2 --> C1["PyMuPDF Raster Extraction"]
        C1 --> C2["Tesseract OCR v5.5 (Multi-threaded tha.traineddata)"]
        C1 --> C3["OpenThai 2.0 OCR Markdown (iapp/nemotron)"]
        C2 --> D1["Bounding Boxes & Text Snippets"]
        C3 --> D1
    end

    subgraph Transformation ["Phase 3: Transformation & Indexing"]
        D1 --> E1["Searchable PDF Generator (render_mode=3, tahoma.ttf)"]
        D1 --> E2["Chronological Stitching & Stitch-Overlap Removal"]
        D1 --> E3["BM25 Vector & Token Vault (PyThaiNLP Tokenizer)"]
        E1 --> F1["FINAL_EVIDENCE_JINNIPHA_Searchable.pdf"]
        E2 --> F2["MASTER_TRANSCRIPT_CHRONOLOGICAL.md"]
        E2 --> F3["COURT_TIMELINE_DOSSIER.md"]
        E3 --> F4["evidence_vault.jsonl"]
    end

    subgraph LegalTriage ["Phase 4: Statutory Legal Triage Engine"]
        F3 --> G1["Legal Triage Engine (run_legal_triage.py)"]
        H1["thai_law_master_reference.json (SSOT Database)"] --> G1
        G1 --> I1["Civil Code Mapping (CCC Sec 653, 193/14, 224)"]
        G1 --> I2["Penal Code Mapping (CPC Sec 341, 343 Fraud)"]
        I1 --> J1["LEGAL_TRIAGE_DOSSIER.md (Court-Ready Mapping Table)"]
        I2 --> J1
    end

    subgraph CourtAction ["Phase 5: Prosecution & Legal Remedies"]
        J1 --> K1["Police Station (Criminal Complaint - Fraud)"]
        J1 --> K2["Small Claims / Civil Court (Action for Loan Recovery)"]
        J1 --> K3["Legal Counsel (Formal Notice of Demand)"]
    end
```

---

## 2. Step-by-Step Data Flow

1. **Step 1 (Ingestion):** User inputs scattered screenshots from LINE chat and bank transfer slips.
2. **Step 2 (De-duplication):** MD5 binary hash verifies unique files and removes redundant copies across subfolders.
3. **Step 3 (Dual OCR Engine):**
   - High-speed multi-threaded Tesseract OCR extracts raw tokens and timestamps within seconds.
   - OpenThai 2.0 OCR parses complex layout, headers, and Thai tabular structures.
4. **Step 4 (Invisible Layer Rendering):** PyMuPDF embeds invisible Thai Unicode text directly atop the scanned raster image matching exact coordinate boxes, rendering the PDF searchable via `Ctrl + F` in standard PDF viewers without altering visual appearance.
5. **Step 5 (Chronological Reconstruction):** Timestamps (`16:04 น.`, `16:20 น.`, etc.) and consecutive text overlaps are resolved to generate a continuous transcript narrative.
6. **Step 6 (Legal Triage Mapping):** The statutory knowledge base matches borrowing expressions, repayment promises, and false pretense excuses with specific sections of the Thai Civil and Commercial Code and Criminal Code, citing binding Supreme Court precedents.
7. **Step 7 (Court Package Export):** Outputs structured markdown dossiers and searchable PDFs ready for printing and filing with investigative authorities.

---

## 3. Business Logic Constraints

- **Zero-AI-Hallucination:** Transcripts must strictly reflect OCR text verified against image pixels.
- **Thai Unicode Preservation:** Text layers must utilize native TrueType fonts (`tahoma.ttf`) to prevent missing glyphs or broken tone marks.
- **PDPA & Evidence Confidentiality:** Personal identifiers, raw screenshots, and sensitive financial logs are shielded from public repository commits via `.gitignore`.
