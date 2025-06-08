import re

LOG_PATTERN = re.compile(
    r"^(?P<time>\w+\s+\d+\s+\d+:\d+:\d+).*?query\[(?P<qtype>[^\]]+)\]\s+(?P<domain>\S+)\s+from\s+(?P<ip>\S+)"
)
