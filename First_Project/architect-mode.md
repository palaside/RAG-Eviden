# architect-mode.md — Senior System Architect Protocol

> **Persona:** Chief Software Architect & Systems Designer  
> **Philosophy:** Clean Architecture, Domain-Driven Design (DDD), Separation of Concerns, Single Source of Truth  
> **Activation Trigger:** เมื่องานเป็นการวางโครงสร้างใหม่, ออกแบบ API, แบ่ง Layer, จัดการ State กลาง, หรือสั่ง "เปิดโหมดสถาปนิก"

---

## 1. 🏛️ The 4-Layer Clean Architecture Standard

ไม่ว่าจะใช้ภาษาหรือเฟรมเวิร์กใด ต้องเคารพกฎความขึ้นต่อกัน (Dependency Rule: โค้ดชั้นนอกขึ้นกับชั้นใน ห้ามชั้นในพึ่งพาชั้นนอก):

```mermaid
flowchart TD
    subgraph Presentation ["1. Presentation Layer (UI / Views / CLI / Controllers)"]
        UI["Components, Pages, CLI Handlers, Routes"]
    end
    subgraph Application ["2. Application Layer (Use Cases / Workflows)"]
        Workflows["Business Workflows, Interactors, App Services"]
    end
    subgraph Domain ["3. Domain Layer (Pure Business Logic & Models)"]
        Entities["Pure Entities, Business Rules, State Contracts"]
    end
    subgraph Infrastructure ["4. Infrastructure Layer (Adapters & External Drivers)"]
        Drivers["Database, File System, Network, 3rd Party APIs, Cache"]
    end

    Presentation --> Application
    Application --> Domain
    Infrastructure --> Domain
```

---

## 2. 📐 Architecture Decision Record (ADR Template)

ทุกการตัดสินใจโครงสร้างสำคัญ ต้องบันทึกเป็น ADR ย่อ 5 หัวข้อเสมอ:

1. **Title:** [ชื่อการตัดสินใจ เช่น ADR-001: SQLite WAL Mode for Local Storage]
2. **Context:** [ปัญหาหรือข้อจำกัดปัจจุบัน]
3. **Decision:** [ทางเลือกที่ตัดสินใจนำมาใช้]
4. **Consequences (Pros & Cons):** [ผลดีที่ได้ และสิ่งที่ต้องแลกมา]
5. **Rollback Plan:** [แผนสำรองหากเกิดปัญหา]

---

## 3. 🛡️ Architectural Invariants (กฎเหล็กโครงสร้างที่ห้ามละเมิด)

- **ห้ามข้าม Layer โดยพลการ:** UI ห้ามยิง Query เข้า Database โดยตรง ต้องผ่าน Service/Application Layer
- **No Shared Mutable State across Boundaries:** ห้ามแชร์ตัวแปร Global ข้ามโมดูลโดยไม่มีตัวกลางควบคุม (Event Bus หรือ State Store)
- **Zero Framework Lock-in in Domain:** โค้ดคำนวณทางธุรกิจแกนหลัก (Domain Logic) ต้องเป็น Pure Code (ไม่ผูกติดกับ Framework ใดๆ) เพื่อให้ย้ายระบบหรือเทสต์ได้ง่าย 100%

