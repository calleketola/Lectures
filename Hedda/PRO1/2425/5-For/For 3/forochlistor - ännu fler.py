import random

##############
## ÖVNING 1 ##
##############

"""
2020-12-01
https://adventofcode.com/2020/day/1

After saving Christmas five years
in a row, you've decided to take
a vacation at a nice resort on a
tropical island. Surely, Christmas
will go on without you.

The tropical island has its own
currency and is entirely cash-only.
The gold coins used there have a
little picture of a starfish; the
locals just call them stars. None
of the currency exchanges seem to
have heard of them, but somehow,
you'll need to find fifty of these
coins by the time you arrive so you
can pay the deposit on your room.

To save your vacation, you need to
get all fifty stars by December 25th.

Collect stars by solving puzzles.
Two puzzles will be made available
on each day in the Advent calendar;
the second puzzle is unlocked when
you complete the first. Each puzzle
grants one star. Good luck!

Before you leave, the Elves in
accounting just need you to fix your
expense report (your puzzle input);
apparently, something isn't quite
adding up.

Specifically, they need you to find
the two entries that sum to 2020 and
then multiply those two numbers together.

For example, suppose your expense
report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum
to 2020 are 1721 and 299. Multiplying
them together produces 1721 * 299 = 514579,
so the correct answer is 514579.

Of course, your expense report is much
larger. Find the two entries that sum to 2020; what do you get if you multiply them together?


--- Part Two ---
The Elves in accounting are thankful
for your help; one of them even offers
you a starfish coin they had left over
from a past vacation. They offer you a
second one if you can find three numbers
in your expense report that meet the
same criteria.

Using the above example again, the three
entries that sum to 2020 are 979, 366,
and 675. Multiplying them together
produces the answer, 241861950.

In your expense report, what is the
product of the three entries that sum
to 2020?
"""

# Det här hjälper dig att läsa in
# alla värden
with open("2020-day01.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = int(data[i])

##############
## ÖVNING 2 ##
##############

"""
2021-12-01
https://adventofcode.com/2021/day/1


You're minding your own business on a
ship at sea when the overboard alarm
goes off! You rush to see if you can
help. Apparently, one of the Elves
tripped and accidentally sent the
sleigh keys flying into the ocean!

Before you know it, you're inside a
submarine the Elves keep ready for
situations like this. It's covered in
Christmas lights (because of course it
is), and it even has an experimental
antenna that should be able to track
the keys if you can boost its signal
strength high enough; there's a little
meter that indicates the antenna's
signal strength by displaying 0-50
stars.

Your instincts tell you that in order
to save Christmas, you'll need to get
all fifty stars by December 25th.

Collect stars by solving puzzles. Two
puzzles will be made available on each
day in the Advent calendar; the second
puzzle is unlocked when you complete
the first. Each puzzle grants one star.
Good luck!

As the submarine drops below the surface
of the ocean, it automatically performs
a sonar sweep of the nearby sea floor.
On a small screen, the sonar sweep
report (your puzzle input) appears:
each line is a measurement of the sea
floor depth as the sweep looks further
and further away from the submarine.

For example, suppose you had the
following report:

199
200
208
210
200
207
240
269
260
263
This report indicates that, scanning
outward from the submarine, the sonar
sweep found depths of 199, 200, 208,
210, and so on.

The first order of business is to
figure out how quickly the depth
increases, just so you know what you're
dealing with - you never know if the
keys will get carried into deeper water
by an ocean current or a fish or
something.

To do this, count the number of times
a depth measurement increases from the
previous measurement. (There is no
measurement before the first
measurement.) In the example above,
the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7
measurements that are larger than the
previous measurement.

How many measurements are larger than
the previous measurement?

--- Part Two ---

Considering every single measurement
isn't as useful as you expected: there's
just too much noise in the data.

Instead, consider sums of a three-
measurement sliding window. Again
considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
Start by comparing the first and second
three-measurement windows. The measurements
in the first window are marked A (199, 200,
208); their sum is 199 + 200 + 208 = 607. The
second window is marked B (200, 208, 210);
its sum is 618. The sum of measurements in
the second window is larger than the sum of
the first, so this first comparison increased.

Your goal now is to count the number of times
the sum of measurements in this sliding window
increases from the previous sum. So, compare A
with B, then compare B with C, then C with D,
and so on. Stop when there aren't enough
measurements left to create a new three-
measurement sum.

In the above example, the sum of each three-
measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
In this example, there are 5 sums that are
larger than the previous sum.

Consider sums of a three-measurement sliding
window. How many sums are larger than the
previous sum?
"""

# Det här hjälper dig att läsa in
# alla värden
with open("2021-day01.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = int(data[i])

##############
## ÖVNING 3 ##
##############


"""
Santa's reindeer typically eat regular
reindeer food, but they need a lot of
magical energy to deliver presents on
Christmas. For that, their favorite
snack is a special type of star fruit
that only grows deep in the jungle.
The Elves have brought you on their
annual expedition to the grove where
the fruit grows.

To supply enough magical energy, the
expedition needs to retrieve a minimum
of fifty stars by December 25th.
Although the Elves assure you that the
grove has plenty of fruit, you decide
to grab any fruit you see along the way,
just in case.

Collect stars by solving puzzles. Two
puzzles will be made available on each
day in the Advent calendar; the second
puzzle is unlocked when you complete
the first. Each puzzle grants one star.
Good luck!

The jungle must be too overgrown and
difficult to navigate in vehicles or
access from the air; the Elves'
expedition traditionally goes on foot.
As your boats approach land, the Elves
begin taking inventory of their
supplies. One important consideration is
food - in particular, the number of
Calories each Elf is carrying (your
puzzle input).

The Elves take turns writing down the
number of Calories contained by the
various meals, snacks, rations, etc. that
they've brought with them, one item per
line. Each Elf separates their own
inventory from the previous Elf's
inventory (if any) by a blank line.

For example, suppose the Elves finish
writing their items' Calories and end
up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

This list represents the Calories of the
food carried by five Elves:

The first Elf is carrying food with 1000,
2000, and 3000 Calories, a total of 6000
Calories.
The second Elf is carrying one food item
with 4000 Calories.
The third Elf is carrying food with 5000
and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000,
8000, and 9000 Calories, a total of 24000
Calories.
The fifth Elf is carrying one food item with
10000 Calories.
In case the Elves get hungry and need extra
snacks, they need to know which Elf to ask:
they'd like to know how many Calories are
being carried by the Elf carrying the most
Calories. In the example above, this is
24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories.
How many total Calories is that Elf carrying?


--- Part Two ---

By the time you calculate the answer to the
Elves' question, they've already realized
that the Elf carrying the most Calories of
food might eventually run out of snacks.

To avoid this unacceptable situation, the
Elves would instead like to know the total
Calories carried by the top three Elves
carrying the most Calories. That way, even
if one of those Elves runs out of snacks,
they still have two backups.

In the example above, the top three Elves are
the fourth Elf (with 24000 Calories), then
the third Elf (with 11000 Calories), then the
fifth Elf (with 10000 Calories). The sum of
the Calories carried by these three elves is
45000.

Find the top three Elves carrying the most
Calories. How many Calories are those Elves
carrying in total?
"""
with open("2022-day01.txt") as f:
    data = f.readlines()



