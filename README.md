# HyreNet QA Testing Project
**Manual & Automation Testing – ISO/IEEE Aligned**

Quality assurance activities for the HyreNet AI-powered assessment platform as part of **GUVI Career Carnival 2026 BugAThon**.

## 🎯 Purpose
Identify, analyze, and document functional defects using structured, industry-standard QA practices aligned with IEEE 829 / ISO/IEC/IEEE 29119 standards.

## 🔍 Scope

### In Scope
- User authentication (login)
- Dashboard accessibility & navigation
- Question creation (manual & AI-assisted)
- Test creation, configuration, & scheduling
- Validation handling, negative scenarios, & edge cases
- AI feature reliability & failure handling

### Out of Scope
- Performance testing
- Security penetration testing
- Backend API testing

## 📋 Testing Approach

### 4.1 Manual Testing

**Artifacts prepared:**
- Test Scenarios
- Test Cases
- Requirement Traceability Matrix (RTM)
- Bug Report

### 4.2 Automation Testing
| Framework | Tool | Language | Design Pattern |
|-----------|------|----------|---------------|
| PyTest | Selenium WebDriver | Python | Page Object Model (POM) |

**Automated flows:**
- Login page access
- Credential input
- Sign-in action

## 🐛 Defect Summary
**High-impact defects identified:**

- AI-generated questions lacking relevance/consistency
- AI test generation failing with system errors
- Missing validation for mandatory numeric fields
- Test submission allowed with empty objective/programming questions
- Generic/unclear AI failure error messages

**All defects documented
# hyrenet-qa-bugathon
