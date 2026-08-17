"""Demonstrate explicit input validation before an AI workflow.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.validation import validate_record


request = {"task": "summarize", "max_output": 250}
schema = {"task": str, "max_output": int}
issues = validate_record(request, schema, allow_extra=False)

if issues:
    for issue in issues:
        print(f"{issue.field}: {issue.message}")
else:
    print("validation: PASS")
