try:
    import win32evtlog
except ImportError:
    win32evtlog = None


def read_security_logs():
    if win32evtlog is None:
        raise RuntimeError(
            "win32evtlog is only available on Windows systems. "
            "This script cannot read Windows Security logs on Linux."
        )

    server = "localhost"
    logtype = "Security"

    hand = win32evtlog.OpenEventLog(server, logtype)

    flags = (
        win32evtlog.EVENTLOG_BACKWARDS_READ
        | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    )

    events = []
    records = win32evtlog.ReadEventLog(hand, flags, 0)

    for event in records[:50]:
        events.append(
            {
                "EventID": event.EventID & 0xFFFF,
                "Time": str(event.TimeGenerated),
            }
        )

    return events