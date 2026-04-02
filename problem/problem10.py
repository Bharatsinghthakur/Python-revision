# speed detection at highway
"""
We would like to catch people who are driving at unsafe speeds on the highway. To help us do that, we would like to identify journeys where a driver does either of the following:
* Drive 130 km/h or greater in any individual 10km segment of tollway.
* Drive 120 km/h or greater in any two 10km segments of tollway.

For example, consider the following journey:
1000.000 TST002 270W ENTRY
1275.000 TST002 260W EXIT

In this case, the driver of TST002 drove 10 km in 275 seconds. We can calculate that this driver drove an average speed of ~130.91km/hr over this segment:

10 km * 3600 sec/hr
-------------------- = 130.91 km/hr
275 sec

Note that:
* A license plate may have multiple journeys in one file, and if they drive at unsafe speeds in both journeys, both should be counted.
* We do not mark speeding if they are not on the highway (i.e. for any driving between an EXIT and ENTRY event).
* Speeding is only marked once per journey. For example, if there are 4 segments 120 km/h or greater, or multiple segments 130km/h or greater, the journey is only counted once.

3-
1) Write a function catch_speeders in LogFile that returns a collection of license plate s that drove at unsafe speeds during a journey in the LogFile.
If the same license plate drives at unsafe speeds during two different journeys, the license plate should appear twice (once for each journey they drove at unsafe speeds)

import re
from typing import import Iterable, List, Tuple, Dict, Optional

class LogFile:

  #  Expects log lines in the format:
  # <timestamp_sec> <plate> <location> <event>
  #  Example:
   # "1000.000 TST002 270W ENTRY"
   # "1275.000 TST002 260W EXIT"

   # Notes:
   # - timestamp: float or int (seconds)
   # - plate: string without spaces
   #- location: string like '270W', '260E' (we use the numeric km part; letters are direction)
   # - event: 'ENTRY' | 'EXIT' | <any other on-highway marker name if present>
   # We treat any event between ENTRY and EXIT as an on-highway marker (segment boundary).


    KM_RE = re.compile(r"^(\d+)([a-z]+)$", re.IGNORECASE)

    def __init__(self, lines: Iterable[str]):
        self.raw_lines = list(lines)

    @staticmethod
    def _parse_line(line: str) -> Tuple[float, str, int, str]:

        Parse a log line into (timestamp, plate, km_numeric, event).

        parts = line.strip().split()
        if len(parts) < 4:
            raise ValueError(f"Invalid log line (needs 4 tokens): {line}")

        try:
            ts = float(ts_s)
        except ValueError:
            raise ValueError(f"Invalid timestamp: {ts_s|r} in line: {line}")

        m = LogFile.KM_RE.match(location)
        if not m:
            raise ValueError(f"Invalid location (no leading km digits): {location!r} in line: {line}")
        km_numeric = int(m.group(1))

        return ts, plate, km_numeric, event.upper()

    def ensure_state(plate: str):
        if plate not in state:
            state[plate] = {
                "in_journey": False,
                "last_point": None,  # type: Optional[Tuple[float, int]]
                "seg120_count": 0,  # type: int
                "flagged_130": False  # type: bool
            }

        for ts, plate, km, ev in parsed:
            ensure_state(plate)
            st = state[plate]

            if ev == "ENTRY":
                # Start (or restart) a new journey for this plate
                st["in_journey"] = True
                st["last_point"] = (ts, km)
                st["seg120_count"] = 0
                st["flagged_130"] = False
                continue

            if not st["in_journey"]:
                # Ignore all off-highway events
                continue

            # We are on-highway. Every event is a boundary to compute segments against the previous point.
            last = st["last_point"]
            if last is None:
                st["last_point"] = (ts, km)
                # continue; though in practice this shouldn't happen after ENTRY
                continue

            last_ts, last_km = last
            dt = ts - last_ts
            if dt <= 0:
                # Non-increasing timestamps; ignore the segment for safety
                # Update last point to current to avoid compounding errors
                st["last_point"] = (ts, km)
                if ev == "EXIT":
                    # Close journey without marking (invalid timing)
                    st["in_journey"] = False

            try:
                ts = float(ts_s)
            except ValueError:
                raise ValueError(f"Invalid timestamp: {ts_s|r} in line: {line}")

            m = LogFile.KM_RE.match(location)
            if not m:
                raise ValueError(f"Invalid location (no leading km digits): {location!r} in line: {line}")
            km_numeric = int(m.group(1))

            return ts, plate, km_numeric, event.upper()

            km_delta = abs(km - last_km)

            if km_delta == 0:
                # No distance moved; not a segment.
                st["last_point"] = (ts, km)
            elif km_delta % 10 == 0:
                # Number of 10km segments crossed between last and current markers.
                segments = km_delta // 10

                # Conservative assumption:
                # Apply the average speed across the span to each 10km segment (if multiple).
                # If your policy requires *only* exact 10km hops, replace 'segments' with:
                # segments = 1 if km_delta == 10 else 0
                # and guard accordingly.
                # Speed (km/h) = distance(km) * 3600 / time(sec)
                # For each 10km segment => speed_per_segment = (10 * 3600) / (dt / segments)
                # That simplifies to avg_speed across span = (km_delta * 3600) / dt.
                avg_speed = (km_delta * 3600.0) / dt

                if avg_speed >= 130.0:
                    st["flagged_130"] = True
                if avg_speed >= 120.0:
                    st["seg120_count"] += segments

                st["last_point"] = (ts, km)
            else:
                # Not aligned to 10km boundaries; we can't build a 10km segment from this hop.
                # We still advance the chain so next boundary can be evaluated.
                st["last_point"] = (ts, km)

            if ev == "EXIT":
                # At journey end, decide if unsafe
                if st["flagged_130"] or st["seg120_count"] >= 2:
                    result.append(plate)
                # Reset state for the next journey
                st["in_journey"] = False
                st["last_point"] = None
                st["seg120_count"] = 0

            st["flagged_130"] = False

        # If any plate is still 'in_journey' without an EXIT, we do not mark it (incomplete journey)
        return result

    def catch_speeders(self) -> List[str]:

        Returns a list of license plates that had at least one unsafe-speed journey.
        If a plate has multiple unsafe journeys, it appears multiple times (once per unsafe journey).


        # Parse and sort all logs by timestamp to ensure chronological processing
        parsed = [self._parse_line(l) for l in self.raw_lines]
        parsed.sort(key=lambda x: x[0])

        # State per plate while on-highway
        # - in_journey: whether the plate is currently on the tollway
        # - last_point: (ts, km) of the last on-highway event
        # - seg120_count: number of 10km segments in this journey with speed >= 120
        # - flagged_130: True if any 10km segment speed >= 130
        state: Dict[str, Dict[str, object]] = {}
        result: List[str] = []
"""
