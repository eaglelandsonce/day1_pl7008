---
name: invoice-overdue-dashboard
description: Use when reviewing an Excel invoice register to identify invoices that are overdue and unpaid, highlight their complete rows in red, and create or refresh a summary dashboard showing paid and unpaid invoice counts and total amounts.
---

# Review invoices, flag overdue unpaid rows, and build a dashboard

Use this skill on an invoice table or invoice-shaped data range. Apply changes directly to the active workbook while preserving the source data, existing formulas, tables, filters, frozen panes, and established formatting wherever possible.

## Expected invoice fields

Identify columns by header meaning rather than fixed column letters. Prefer these headers and accept close equivalents:

- **Invoice Number**: invoice ID, invoice no., reference
- **Amount (GBP)**: amount, invoice amount, total, gross amount
- **Due Date**: payment due date, due
- **Payment Settled**: paid, settled, payment status
- **Invoice Status**: status
- Optional dimensions: **Customer Name**, **Invoice Category**, **Region**, **Sales Rep**, **Priority Level**, **Days Overdue**

If several possible columns match, use the columns inside the invoice table or main contiguous invoice range. Do not guess when the amount, due-date, or payment-status field cannot be identified reliably. Explain which required header is missing and stop before editing.

## Business rules

Use the workbook's current date for overdue testing.

An invoice is **paid** when either:

- Payment Settled is Yes, Paid, True, 1, Settled, or equivalent; or
- Invoice Status is Paid or Settled.

An invoice is **unpaid** when it is not classified as paid. This includes No, Unpaid, False, 0, Sent, Viewed, Draft, Overdue, Partially Paid, blank, or similar open statuses unless the workbook clearly defines another rule.

An invoice is **overdue and unpaid** only when:

1. Due Date is a valid date earlier than TODAY(); and
2. The invoice is unpaid.

Do not classify blank or invalid due dates as overdue. Flag them separately for review if encountered. Do not rely only on an existing Days Overdue value or an Invoice Status of Overdue because either may be stale.

## Steps

1. Locate the main invoice table or data range and confirm that it has headers and at least one data row.
2. Preserve the original sheet name. If the range is not already an Excel table, convert only the contiguous invoice range to a table with headers when this can be done without disrupting merged cells or surrounding content.
3. Determine paid, unpaid, and overdue-unpaid status using the business rules above.
4. Apply conditional formatting to the full data-row width for every overdue and unpaid invoice:
   - light red fill: `#FFC7CE`
   - dark red font: `#9C0006`
   - apply to data rows only, not the header or totals row
   - use a formula-based rule tied to Due Date and payment state so the highlight updates when data changes
5. If a **Days Overdue** column exists, refresh it with a formula equivalent to:
   - `=IF(AND([@[Due Date]]<TODAY(), unpaid-test), TODAY()-[@[Due Date]], 0)`
   - preserve blanks for invalid or blank due dates when practical
   If the column does not exist, do not add it unless the user asks.
6. Create or refresh a worksheet named **Invoice Dashboard**. If it already exists, update the skill-created dashboard area rather than creating duplicate dashboard sheets.
7. Build a summary table with these rows:
   - Paid
   - Unpaid
   - Total
   and these columns:
   - Payment Status
   - Invoice Count
   - Total Amount (use the source currency from the amount header; default to GBP only when the source header explicitly indicates GBP)
8. Use formulas linked to the source invoice table, not hardcoded results. Prefer structured references and `COUNTIFS`/`SUMIFS`. When payment state can be derived from multiple fields, add a clearly labeled helper column to the source table only if needed for reliable formulas, and name it **Calculated Payment State**.
9. Include these KPI values near the top of the dashboard:
   - Total invoices
   - Paid invoices
   - Unpaid invoices
   - Total invoiced amount
   - Paid amount
   - Unpaid amount
   - Overdue unpaid invoices
   - Overdue unpaid amount
10. Add two editable charts linked to the summary table:
    - a doughnut chart for paid versus unpaid invoice count
    - a clustered column chart for paid versus unpaid total amount
11. Format the dashboard professionally:
    - title: **Invoice Summary Dashboard**
    - dark blue header fill with white bold text
    - currency with thousands separators and two decimals
    - whole numbers for counts
    - clear spacing, readable column widths, hidden gridlines on the dashboard only
    - use green for paid, red for unpaid/overdue, and blue for totals
12. Add an **As of** label using `=TODAY()` and format it as a readable date.
13. Verify before finishing:
    - every red source row is both overdue and unpaid
    - paid invoices are not included in overdue highlights even if their due dates are in the past
    - the Paid count plus Unpaid count equals Total count
    - the Paid amount plus Unpaid amount equals Total invoiced amount
    - dashboard formulas refer to the current source table and expand with new rows
    - there are no formula errors

## Formula guidance

Prefer a helper column named **Calculated Payment State** when the workbook contains both Payment Settled and Invoice Status. Its row formula should return `Paid` when either field indicates payment; otherwise return `Unpaid`.

With a table named `InvoicesTable`, example dashboard formulas are:

- Paid count: `=COUNTIF(InvoicesTable[Calculated Payment State],"Paid")`
- Unpaid count: `=COUNTIF(InvoicesTable[Calculated Payment State],"Unpaid")`
- Paid amount: `=SUMIFS(InvoicesTable[Amount (GBP)],InvoicesTable[Calculated Payment State],"Paid")`
- Unpaid amount: `=SUMIFS(InvoicesTable[Amount (GBP)],InvoicesTable[Calculated Payment State],"Unpaid")`
- Overdue unpaid count: `=COUNTIFS(InvoicesTable[Calculated Payment State],"Unpaid",InvoicesTable[Due Date],"<"&TODAY())`
- Overdue unpaid amount: `=SUMIFS(InvoicesTable[Amount (GBP)],InvoicesTable[Calculated Payment State],"Unpaid",InvoicesTable[Due Date],"<"&TODAY())`

Adapt table and column names to the workbook. If a helper column is unnecessary because one reliable payment-status column exists, reference that column directly.

## Safeguards

- Never overwrite invoice values with summary values.
- Do not delete source rows, sheets, formulas, comments, or existing charts.
- Do not treat zero-value invoices as missing.
- Exclude blank rows and totals rows from invoice counts.
- Preserve the workbook's locale and currency conventions.
- If dates are stored as text, convert only values that can be parsed confidently; otherwise flag them for review.
- If the source is filtered, summarize all table rows unless the user explicitly asks for visible rows only.

## Completion message

Briefly report:

- how many overdue unpaid invoices were highlighted
- the overdue unpaid total amount
- that **Invoice Dashboard** was created or refreshed
- any rows skipped because of missing or invalid required data
