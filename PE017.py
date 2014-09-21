dc = {1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight",
    9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
    13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
    30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
    80: "eighty", 90: "ninety",}

def solve():
    count = 0
    for i in range(1, 1001):
        a = i/1000
        b = (i-a*1000)/100
        c = (i-a*1000-b*100)/10
        d = i%10
        if a == 1:
            count += len("one") + len("thousand")
        if a == 0 and b > 0:
            count += len(dc[b])
            count += len("hundred")
            if not (c == 0 and d == 0):
                count += len("and")
        if c*10+d in dc:
            count += len(dc[c*10+d])
        else:
            if c > 0:
                count += len(dc[c*10])
            if d > 0:
                count += len(dc[d])

    print count

if __name__ == '__main__':
    solve()
