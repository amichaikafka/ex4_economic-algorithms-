import csv


def parlament_dev(f, filename, votes: dict = {}, limit: bool = True):
    seats = {}
    ls = []
    if limit:
        min = sum(votes.values()) * 0.0325
        temp=votes.copy()
        for k, v in temp.items():
            if v < min:
                del votes[k]

    ls.append(list(votes.keys()))
    ls[0].insert(0,"")
    for i in votes.keys():
        seats[i] = 0
    votes_dev = votes.copy()
    mandat = 0
    ls.append([0 for i in range(len(seats))])
    ls[1].insert(0, "חלוקה")
    if f(0) == 0:
        t = list(votes.copy().values())
        t.insert(0, "מנות")
        ls.append(t)
        ls.append([1 for i in range(len(seats))])
        ls[3].insert(0, "חלוקה")
        for i in votes.keys():
            seats[i] = 1
        mandat = len(votes)
    while mandat < 120:
        for p in votes.keys():
            votes_dev[p] = votes[p] / f(seats[p])
        max_party = max(votes_dev.items(), key=lambda k: k[1])[0]
        seats[max_party] += 1
        t = list(votes_dev.copy().values())
        t.insert(0, "מנות")
        ls.append(t)
        t = list(seats.copy().values())
        t.insert(0, "חלוקה")
        ls.append(t)
        # print(votes_dev)
        # print(seats)
        mandat += 1

    ls.append(["סיכום"])
    print("Samery")
    for v, k in seats.items():
        ls.append([v, k])
        print(v, ":", k)
    print("Total:", sum(seats.values()))

    ls.append(["סה\"כ", sum(seats.values())])
    with open(filename, 'a', newline="") as file:
        csvwriter = csv.writer(file)  # 2. create a csvwriter object
        csvwriter.writerow(ls[0])  # 4. write the header
        csvwriter.writerows(ls[1:])  # 5. write the rest of the data


if __name__ == '__main__':
    party_vote = {"הליכוד": 1066892, "יש עתיד": 614112, "שס": 316008, "כחול לבן": 292257, "ימינה": 273836,
                  "העבודה": 268767, "יהדות התורה": 248391, "ישראל ביתנו": 248370, "הציונות הדתית": 225641,
                  "הרשימה המשותפת": 212583, "תקווה חדשה": 209161, "מרצ": 202218, "רע\"מ": 167064,
                  "הכלכלית": 34883, "רפא": 17346, "הפיראטים": 1309, "אני ואתה": 1291, "התקווה לשינוי": 1189,
                  "המפץ החברתי": 811, "משפט צדק": 729, "צומת": 663, "עם שלם": 592, "סדר חדש": 514,
                  "קמ\"ה": 486, "אפשרי": 463, "הלב היהודי": 443, "עצמנו": 441, "הגוש התנ\"כי": 429,
                  "עולם חדש": 429, "ברית השותפות": 408, "הישראלים": 395, "שמע": 395, "דעם": 385,
                  "מנהיגות חברתית": 256, "מען": 253, "חץ": 226, "אנחנו": 220, "כבוד האדם": 196, "דמוקרטית": 0}

    print("______________jefferson_______________")
    parlament_dev(f=lambda m: m + 1, votes=party_vote.copy(), filename="jefferson.csv")
    print("______________without limit____________")
    parlament_dev(f=lambda m: m + 1, votes=party_vote, filename="jefferson.csv",limit=False)
    print("_________________adams_________________")
    parlament_dev(f=lambda m: m, votes=party_vote.copy(), filename="adams.csv")
    print("______________without limit____________")
    parlament_dev(f=lambda m: m, votes=party_vote, filename="adams.csv",limit=False)
    print("_________________webster_________________")
    parlament_dev(f=lambda m: m + 0.5, votes=party_vote.copy(), filename="webster.csv")
    print("______________without limit____________")
    parlament_dev(f=lambda m: m + 0.5, votes=party_vote, filename="webster.csv",limit=False)

