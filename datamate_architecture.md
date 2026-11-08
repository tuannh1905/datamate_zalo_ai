# DataMate Challenge: AI Agent for Tabular QA

## Overview
DataMate is a competition challenging participants to build an AI agent capable of answering natural-language Vietnamese questions directly from structured tabular data (CSV, Excel, SQLite) belonging to small Vietnamese businesses (e.g., grocery stores, pharmacies, bubble-tea shops).

The agent must output a correct answer based on the provided business data or explicitly choose to **abstain** or return **unanswerable** when the data cannot support the query.

## Data Inputs
For each query, the agent receives:
1. **Data Package (`data/<business_id>/`)**: Contains one or more raw data files (`.csv`, `.xlsx`, `.sqlite`) covering 12–30 months of activity (up to 300,000 rows).
2. **README.md**: A file within the data package containing the business description and data dictionary notes (quality varies significantly).
3. **Question**: A natural-language query in Vietnamese (e.g., "thang nay hang nao ban cham nhat, ton nhieu ma ban ko dc").
4. **As-of Date (`as_of_date`)**: The anchor date to resolve relative time expressions (e.g., "tháng này", "tuần rồi").
5. **Rulebook (`rulebook.md`) & Calendar (`calendar.csv`)**: Shared rules and a solar-lunar calendar defining default business logic (e.g., revenue calculation, week start days, Tết window). Note: The rulebook may change between test splits.

## Outputs & Submission Format
Submissions require a `submission.jsonl` file with one JSON object per question. The agent must return one of the following answer types:

### Standard Data Types
*   **string**: e.g., `{"id": "q_01234", "type": "string", "answer": "Sting dâu 330ml"}`
*   **number**: e.g., `{"id": "q_01235", "type": "number", "answer": 48250000}`
*   **percent**: e.g., `{"id": "q_01236", "type": "percent", "answer": -12.45}`
*   **date**: (Format YYYY-MM-DD) e.g., `{"id": "q_01237", "type": "date", "answer": "2026-08-15"}`
*   **boolean**: e.g., `{"id": "q_01238", "type": "boolean", "answer": true}`
*   **list**: e.g., `{"id": "q_01239", "type": "list", "answer": ["Cà phê sữa", "Bạc xỉu", "Trà đào"]}`
*   **table**: e.g., `{"id": "q_01240", "type": "table", "answer": {"columns": ["khach_hang", "so_tien_no"], "rows": [["Chị Lan", 3200000], ["Anh Tú", 1500000]]}}`

### Fallback Types
*   **unanswerable**: Used when the provided data lacks the necessary information to compute the answer.
    *   e.g., `{"id": "q_01241", "type": "unanswerable", "reason": "Dữ liệu không có giá vốn nên không tính được lợi nhuận"}`
*   **abstain**: Used when the agent chooses not to answer (e.g., due to low confidence or SQL execution failure). Missing answers default to abstain.
    *   e.g., `{"id": "q_01242", "type": "abstain"}`

## Evaluation Rules (Per-Question Scoring)
Answers are evaluated as **correct**, **wrong**, or **abstain**. There is no partial credit. An answer is correct only if its `type` matches the reference and its `value` meets the specific matching criteria:

*   **number**: Exact match. Values are integers or rounded to 2 decimals.
*   **percent**: Exact match after rounding to 2 decimal places. The sign must be correct.
*   **string**: Normalized exact equality. Normalization process: Unicode NFC -> lowercase -> non-alphanumeric characters replaced by space -> strip leading/trailing and collapse whitespace. Diacritics are kept. Matches if it equals any accepted form (including its item code) found in the reference `alias` list.
*   **date**: Exact match in ISO format (`yyyy-mm-dd` or `yyyy-mm`).
*   **boolean**: Exact match (`true`/`false`).
*   **list**: Exact ordered match, evaluated position by position according to string/number rules.
*   **table**: Columns matched by normalized name or position. Rows matched as a set according to string/number rules.
*   **unanswerable**: Correct if and only if the reference is unanswerable.
*   **abstain**: Scored as abstain (0 points), regardless of the reference.

### Ranking Queries
For ranking questions or "...nhất" (top/bottom) questions, ordering is based on the specified criterion (descending) over valid orders only. Ties are broken by item code in ascending order. If fewer than k candidates exist, the reference includes all of them.

### Final Score (Penalized Accuracy)
The final leaderboard metric is **Penalized Accuracy (PA)**, calculated over N questions:
PA = (1/N) * sum(s_i)
Where s_i is:
*   +1 if the answer is correct.
*   0 if the answer is abstain.
*   -1 if the answer is wrong.

Any answer given to an unanswerable question counts as wrong. Ties are broken first by the total inference time in the organizers' re-run, then by submission time.

## Execution Environment (Docker)
The final submission must be a self-contained Docker image holding:
*   Source code (training and inference).
*   Model weights (Offline inference only).
*   A `predict.sh` entrypoint script.
*   The script must read data from `/data`, output to `/result/submission.jsonl`, and write detailed execution logs to `/result/logs/` for re-run verification.
