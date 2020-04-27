# helpers for Javascript expression formatting

import re

SCRIPT_RE = re.compile(r"<(-*)/script>")


def camelcase_to_underscore(str):
    # https://djangosnippets.org/snippets/585/
    return (
        re.sub("(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))", "_\\1", str).lower().strip("_")
    )


def escape_script(text):
    """
    Escape `</script>` tags in 'text' so that it can be placed within a `<script>` block without
    accidentally closing it. A '-' character will be inserted for each time it is escaped:
    `<-/script>`, `<--/script>` etc.
    """
    return SCRIPT_RE.sub(r"<-\1/script>", text)
