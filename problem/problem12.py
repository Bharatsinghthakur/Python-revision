"""
================================================================================
TOLL BOOTH LOG ANALYSIS PROJECT
================================================================================

BACKGROUND:
We are writing software to analyze logs for toll booths on a highway. This
highway is a divided highway with limited access; the only way on to or off
of the highway is through a toll booth.

TOLL BOOTH TYPES:
There are three types of toll booths:

* ENTRY (E in the diagram) toll booths, where a car goes through a booth as
  it enters the highway.

* EXIT (X in the diagram) toll booths, where a car goes through a booth as
  it exits the highway.

* MAINROAD (M in the diagram), which have sensors that record a license plate
  as a car drives through at full speed.

HIGHWAY DIAGRAM:
(West-bound side)
---<----------X--------M--------<--------E--------<--------
Exit Booth         Entry Booth

(East-bound side)
------E--------M--------X--------<------
Entry Booth         Exit Booth

TOLL BOOTH LOCATIONS:
Tollbooths are placed every ten kilometers.

LOG LINE FORMAT:
Log lines look like this in the file:

34400.409 SXY288 210E ENTRY
52160.132 ABC123 400W ENTRY

Where:
* 34400.409 is the timestamp in seconds since the software was started.
* SXY288 is the license plate of the vehicle passing through the toll booth.
* 210E is the location and traffic direction of the toll booth. Here, the toll
  booth is at 210 kilometers from the start of the tollway, and the E indicates
  that the toll booth was on the east-bound traffic side.
* ENTRY indicates which type of toll booth the vehicle went through. This is one
  of ENTRY, EXIT, or MAINROAD.

================================================================================
CODE AND TESTS
================================================================================

"""

import collections
import unittest


class LogEntry:
    """
    Represents an entry from a single log line.
    """

    def __init__(self, log_line):

        # first bug fix is hrere
        tokens = log_line.split()
        self.timestamp = float(tokens[0])
        self.license_plate = tokens[1]
        self.booth_type = tokens[3]
        self.location = int(tokens[2][:-1])
        direction_letter = tokens[2][-1]
        if direction_letter == "E":
            self.direction = "EAST"
        elif direction_letter == "W":
            self.direction = "WEST"
        else:
            raise ValueError

    def __str__(self):
        return (
            "<LogEntry timestamp: %f license: %s location: %d direction: %s booth_type: %s>"
            % (
                self.timestamp,
                self.license_plate,
                self.location,
                self.direction,
                self.booth_type,
            )
        )


class LogFile(collections.abc.Sequence):
    """
    Represents a file containing a number of log lines, converted to LogEntry
    objects.
    """

    def __init__(self, file_handle):
        self.log_entries = []
        for line in file_handle:
            log_entry = LogEntry(line.strip())
            self.log_entries.append(log_entry)

    def __getitem__(self, index):
        return self.log_entries[index]

    def __len__(self):
        return len(self.log_entries)

    def count_journeys(self):
        # track which vehicles are currently on highways
        vehicle_state = {}
        journeys = 0
        # print(self.log_entries[1])
        for entry in self.log_entries:

            license_plate = entry.license_plate
            booth_type = entry.booth_type

            if booth_type == "ENTRY":
                vehicle_state[license_plate] = True

            elif booth_type == "MAINROAD":
                # vehicle passing through (no state change)
                pass

            elif booth_type == "EXIT":
                # vehicle exiting
                if license_plate in vehicle_state and vehicle_state[license_plate]:
                    journeys += 1
                    vehicle_state[license_plate] = False

        return journeys

    # def count_journeys(self):
    #     vehicle_state = {}
    #     journeys = 0

    #     for entry in self.log_entries:
    #         plate = entry.license_plate
    #         booth = entry.booth_type

    #         if booth == "ENTRY":
    #             # only allow entry if vehicle is NOT already inside
    #             if vehicle_state.get(plate) is not True:
    #                 vehicle_state[plate] = True

    #         elif booth == "EXIT":
    #             # only count if vehicle was inside
    #             if vehicle_state.get(plate) is True:
    #                 journeys += 1
    #                 vehicle_state[plate] = False

    #     return journeys


class TestSuite(unittest.TestCase):
    # These tests are not meant to be exhaustive, and primarily show usage.

    def test_log_file(self):
        with open("test/tollbooth_small.log") as fh:
            log_file = LogFile(fh)
            self.assertEqual(len(log_file), 13)
            for entry in log_file:
                self.assertTrue(type(entry) == LogEntry)

    def test_log_entry(self):
        log_line = "44776.619 KTB918 310E MAINROAD"
        log_entry = LogEntry(log_line)
        self.assertEqual(log_entry.timestamp, 44776.619)
        self.assertEqual(log_entry.license_plate, "KTB918")
        self.assertEqual(log_entry.location, 310)
        self.assertEqual(log_entry.direction, "EAST")
        self.assertEqual(log_entry.booth_type, "MAINROAD")

        log_line = "52160.132 ABC123 400W ENTRY"
        log_entry = LogEntry(log_line)
        self.assertEqual(log_entry.timestamp, 52160.132)
        self.assertEqual(log_entry.license_plate, "ABC123")
        self.assertEqual(log_entry.location, 400)
        self.assertEqual(log_entry.direction, "WEST")
        self.assertEqual(log_entry.booth_type, "ENTRY")

    def test_count_journeys(self):
        with open("test/tollbooth_small.log") as fh:
            log_file = LogFile(fh)
            self.assertEqual(3, log_file.count_journeys())

        with open("test/tollbooth_medium.log") as fh:
            log_file = LogFile(fh)
            self.assertEqual(63, log_file.count_journeys())

if __name__ == "__main__":
        unittest.main()


# """
# The following log entries contain complete journeys for vehicles with license
# plates JOX304 and THX138:"""
# SAMPLE LOG DATA:
# 90750.191 JOX304 250E ENTRY
# 91081.684 JOX304 260E MAINROAD
# 91082.101 THX138 110E ENTRY
# 91483.251 JOX304 270E MAINROAD
# 91873.920 THX138 120E MAINROAD
# 91874.493 JOX304 280E EXIT

# ...

# 91982.102 THX138 290E EXIT
# 92301.302 THX138 300E ENTRY
# 92371.302 THX138 310E EXIT

# JOURNEY ANALYSIS:
# → This log contains 3 complete journeys:
#   • JOX304: 1 journey
#   • THX138: 2 journeys

# The log contains only complete journeys, there are no missing entries.

# ================================================================================
# TASKS
# ================================================================================

# TASK 1-1: CODE REVIEW AND UNDERSTANDING
# Read through and understand the code and comments below. Feel free to run the
# code and tests.

# TASK 1-2: BUG FIX
# The tests are not passing due to a bug in the code. Make the necessary changes
# to LogEntry to fix the bug.

# BACKGROUND INFORMATION:
# We are interested in how many people are using the highway, and so we would like
# to count how many complete journeys are taken in the log file.

# A complete journey consists of:
#   * A driver entering the highway through an ENTRY toll booth.
#   * The driver passing through some number of MAINROAD toll booths (possibly 0).
#   * The driver exiting the highway through an EXIT toll booth.

# TASK 2-1: IMPLEMENT COUNT_JOURNEYS METHOD
# Write a function in LogFile named count_journeys() that returns how many
# complete journeys there are in the given LogFile.

# ================================================================================
# END OF DOCUMENT
# ================================================================================
# we are going good !!