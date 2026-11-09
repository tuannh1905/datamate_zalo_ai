import pytest
from src.inference.executor_voter import parse_completion


def test_parse_completion_cte_with():
    text = """Notes:
- Using a CTE to aggregate.
TYPE: number
```sql
WITH a AS (
    SELECT 100 AS v
)
SELECT v * 2 FROM a;
```
"""
    pred_type, sql = parse_completion(text)
    assert pred_type == "number"
    assert sql is not None
    assert sql.startswith("WITH a AS")
    assert "SELECT v * 2 FROM a" in sql


def test_parse_completion_unclosed_block():
    text = """Notes:
- Outputting revenue.
TYPE: percent
```sql
SELECT ROUND(rate, 2) FROM metrics
"""
    pred_type, sql = parse_completion(text)
    assert pred_type == "percent"
    assert sql is not None
    assert "SELECT ROUND(rate, 2) FROM metrics" in sql


def test_parse_completion_multiple_blocks():
    text = """Notes:
- First draft:
```sql
SELECT 0;
```
- Improved query:
TYPE: string
```sql
SELECT product_name FROM products LIMIT 1;
```
"""
    pred_type, sql = parse_completion(text)
    assert pred_type == "string"
    assert sql is not None
    assert "SELECT product_name FROM products LIMIT 1" in sql


def test_parse_completion_missing_type_fails():
    text = """Notes:
- Calculation notes here.
```sql
SELECT 42;
```
"""
    pred_type, sql = parse_completion(text)
    # When TYPE is missing, pred_type should be None (failing the candidate sample)
    assert pred_type is None
