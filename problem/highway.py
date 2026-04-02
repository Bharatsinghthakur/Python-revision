"""
We would like to catch people who are driving at unsafe speeds on the highway. To help us do that, we would like to identify journeys where a driver does either of the following:

* Drive 130 km/h or greater in any individual 10km segment of tollway.
* Drive 120 km/h or greater in any two 10km segments of tollway.

For example, consider the following journey:

1000.000 TST002 270W ENTRY
1275.000 TST002 260W EXIT

In this case, the driver of TST002 drove 10 km in 275 seconds. We can calculate that this driver drove an average speed of ~130.91 km/hr over this segment:

10 km * 3600 sec/hr
------------------- = 130.91 km/hr
275 sec

Note that:
* A license plate may have multiple journeys in one file, and if they drive at unsafe speeds in both journeys, both should be counted.
* We do not mark speeding if they are not on the highway (i.e. for any driving between an EXIT and ENTRY event).
* Speeding is only marked once per journey. For example, if there are 4 segments 120 km/h or greater, or multiple segments 130 km/h or greater, the journey is only counted once.

3-
1) Write a function catch_speeders in LogFile that returns a collection of license plates that drove at unsafe speeds during a journey in the LogFile.
If the same license plate drives at unsafe speeds during two different journeys, the license plate should appear twice (once for each journey they drove at unsafe speeds)

"""

import re
from typing import Iterable, List, Tuple, Dict, Optional


class LogFile:
    """
    Expects log lines in the format:
    <timestamp_sec> <plate> <location> <event>

    Example:
    "1000.000 TST002 270W ENTRY"
    "1275.000 TST002 260W EXIT"

    Notes:
    - timestamp: float or int (seconds)
    - plate: string without spaces
    - location: string like '270W', '260E' (we use the numeric km part; letters are direction)
    - event: 'ENTRY' | 'EXIT' | <any other on-highway marker name if present>
    We treat any event between ENTRY and EXIT as an on-highway marker (segment boundary).
    """

    KM_RE = re.compile(r"^(\d+)([a-z]+)$", re.IGNORECASE)

    def __init__(self, lines: Iterable[str]):
        self.raw_lines = list(lines)


    @staticmethod
    def _parse_line(line: str) -> Tuple[float, str, int, str]:
        """
        Parse a log line into (timestamp, plate, km_numeric, event).
        """
        parts = line.strip().split()
        if len(parts) < 4:
            raise ValueError(f"Invalid log line (needs 4 tokens): {line}")

        ts_s, plate, location, event = parts[:4]

        try:
            ts = float(ts_s)
        except ValueError:
            raise ValueError(f"Invalid timestamp: {ts_s!r} in line: {line}")

        m = LogFile.KM_RE.match(location)
        if not m:
            raise ValueError(
                f"Invalid location (no leading km digits): {location!r} in line: {line}"
            )

        km_numeric = int(m.group(1))

        return ts, plate, km_numeric, event.upper()

    def catch_speeders(self) -> List[str]:
        """
        Returns a list of license plates that had at least one unsafe-speed journey.
        If a plate has multiple unsafe journeys, it appears multiple times (once per unsafe journey).
        """

        parsed = [self._parse_line(l) for l in self.raw_lines]
        parsed.sort(key=lambda x: x[0])

        state: Dict[str, Dict[str, object]] = {}
        result: List[str] = []
        
        # will attach this object into our state - for each number plate
        def ensure_state(plate: str):
            if plate not in state:
                state[plate] = {
                    "in_journey": False,
                    "last_point": None,
                    "seg120_count": 0,
                    "flagged_130": False,
                }

        for ts, plate, km, ev in parsed:
            ensure_state(plate)
            st = state[plate]
            # print(plate)
            print(st)

            if ev == "ENTRY":
                st["in_journey"] = True
                st["last_point"] = (ts, km)
                st["seg120_count"] = 0
                st["flagged_130"] = False
                continue

            if not st["in_journey"]:
                continue

            last = st["last_point"]
            if last is None:
                st["last_point"] = (ts, km)
                continue

            last_ts, last_km = last
            dt = ts - last_ts

            if dt <= 0:
                st["last_point"] = (ts, km)
                if ev == "EXIT":
                    st["in_journey"] = False
                continue

            km_delta = abs(km - last_km)

            if km_delta == 0:
                st["last_point"] = (ts, km)

            elif km_delta % 10 == 0:
                segments = km_delta // 10
                avg_speed = (km_delta * 3600.0) / dt

                if avg_speed >= 130.0:
                    st["flagged_130"] = True

                if avg_speed >= 120.0:
                    st["seg120_count"] += segments

                st["last_point"] = (ts, km)

            else:
                st["last_point"] = (ts, km)

            if ev == "EXIT":
                if st["flagged_130"] or st["seg120_count"] >= 2:
                    result.append(plate)

                st["in_journey"] = False
                st["last_point"] = None
                st["seg120_count"] = 0
                st["flagged_130"] = False

        return result

lines = [
    "1000.000 TST002 270W ENTRY",
    "1275.000 TST002 260W EXIT"
]

log = LogFile(lines)
print(log.catch_speeders())