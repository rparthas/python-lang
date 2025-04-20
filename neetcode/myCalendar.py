class MyCalendarThree:

    def __init__(self):
        self.timeline = {}

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline[startTime] = self.timeline.get(startTime, 0) + 1
        self.timeline[endTime] = self.timeline.get(endTime, 0) - 1

        max_booking = 0
        ongoing = 0

        for time in sorted(self.timeline.keys()):
            ongoing += self.timeline[time]
            max_booking = max(max_booking, ongoing)

        return max_booking


if __name__ == "__main__":
    myCalendarThree = MyCalendarThree()
    myCalendarThree.book(10, 20); # return 1
    myCalendarThree.book(50, 60); # return 1
    myCalendarThree.book(10, 40); # return 2
    myCalendarThree.book(5, 15); # return 3
    myCalendarThree.book(5, 10); # return 3
    myCalendarThree.book(25, 55); # return 3
