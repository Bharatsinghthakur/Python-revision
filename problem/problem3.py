"""
You are working on an accounting program for an event's ticketing system.

At the end of the day, all the payments received from the payment gateway have to be matched with the users who bought the tickets. There is always a 1-to-1 match between the users and the payments.

Write a function that, given the payment, pricing, and user data, returns a data structure that links the names of the users to their payment IDs, based on the rules described below.

First, orders can be matched by the users' emails. If the emails don't match, use the payment amounts. For each payment amount, there will be at most one payment that cannot be matched via the email.

For this problem, we can assume the names are unique.

Users:
Name        | Email              | Purchase | Quantity
-----------------------------------------------------
John A.     | john.a@mail.com   | Top      | 3
James S.    | j.s@mail.com      | Economy  | 2
Stacy C.    | stacy.c@test.com  | Economy  | 2
Bobby B.    | bob@mail.com      | Medium   | 10
Michelle X. | mix@test.com      | Medium   | 10
Linda F.    | l.f@mail.com      | Top      | 10
Betty T.    | b.t@mail.com      | ThreeEco | 1
Nancy L.    | n.l@test.com      | TwoEco   | 1
Daniel O.   | d.o@mail.com      | OneEco   | 1
Mike E.     | m.e@mail.com      | FourEco  | 1
Matthew R.  | mr@test.com       | OneEco   | 5
Albert K.   | albert@test.com   | OneEco   | 5
Payment Gateway:
ID  | Email              | Amount
---------------------------------
1   | john2@mail.com     | 33
2   | michellee@mail.com | 60
4   | james@mail.com     | 8
3   | stacy.c@test.com   | 8
5   | bob@mail.com       | 60
6   | email not found    | 110
7   | email not found    | 1
8   | email not found    | 2
9   | email not found    | 3
99  | email not found    | 4
10  | mr@test.com        | 5
11  | a@mail.com         | 5
Ticket Prices:
Ticket   | Price
----------------
Economy  | 4
Top      | 11
Medium   | 6
OneEco   | 1
TwoEco   | 2
ThreeEco | 3
FourEco  | 4
Expected Results:
matching(users, payments, prices) => # Payment ID -> Name

5  -> Bobby B.    # Bobby's email (bob@mail.com) matches
3  -> Stacy C.    # Stacy's email (stacy.c@test.com) matches
10 -> Matthew R.  # Matthew's email (mr@test.com) matches

6  -> Linda F.    # The amount matches, 10 Top tickets at 11
7  -> Daniel O.   # The amount matches, 1 OneEco ticket at 1
8  -> Nancy L.    # The amount matches, 1 TwoEco ticket at 2
9  -> Betty T.    # The amount matches, 1 ThreeEco ticket at 3
99 -> Mike E.     # The amount matches, 1 FourEco ticket at 4

1  -> John A.     # John's amount matches, being the only payment for 33 with 3 Top tickets at 11
2  -> Michelle X. # It's the only payment for 60 without a matching email
4  -> James S.    # James because it's the only other payment for 8
11 -> Albert K.   # It's the only other payment for 5 without a matching email
Complexity Variables:
U = number of users or payments
T = number of ticket prices

Users:

users = [

["John A.", "john.a@mail.com
", "Top", "3"],
["James S.", "j.s@mail.com
", "Economy", "2"],
["Stacy C.", "stacy.c@test.com
", "Economy", "2"],
["Bobby B.", "bob@mail.com
", "Medium", "10"],
["Michelle X.", "mix@test.com
", "Medium", "10"],
["Linda F.", "l.f@mail.com
", "Top", "10"],
["Betty T.", "b.t@mail.com
", "ThreeEco", "1"],
["Nancy L.", "n.l@test.com
", "TwoEco", "1"],
["Daniel O.", "d.o@mail.com
", "OneEco", "1"],
["Mike E.", "m.e@mail.com
", "FourEco", "1"],
["Matthew R.", "mr@test.com
", "OneEco", "5"],
["Albert K.", "albert@test.com
", "OneEco", "5"]

]

Payments:

payments = [

["1", "john2@mail.com
", "33"],
["2", "michellee@mail.com
", "60"],
["4", "james@mail.com
", "8"],
["3", "stacy.c@test.com
", "8"],
["5", "bob@mail.com
", "60"],
["6", "email not found", "110"],
["7", "email not found", "1"],
["8", "email not found", "2"],
["9", "email not found", "3"],
["99", "email not found", "4"],
["10", "mr@test.com
", "5"],
["11", "a@mail.com
", "5"]

]

Ticket Prices:

prices = [

["Economy", "4"],
["Top", "11"],
["Medium", "6"],
["OneEco", "1"],
["TwoEco", "2"],
["ThreeEco", "3"],
["FourEco", "4"]

]

"""


users = [

["John A.", "john.a@mail.com", "Top", "3"],
["James S.", "j.s@mail.com", "Economy", "2"],
["Stacy C.", "stacy.c@test.com", "Economy", "2"],
["Bobby B.", "bob@mail.com", "Medium", "10"],
["Michelle X.", "mix@test.com", "Medium", "10"],
["Linda F.", "l.f@mail.com", "Top", "10"],
["Betty T.", "b.t@mail.com", "ThreeEco", "1"],
["Nancy L.", "n.l@test.com", "TwoEco", "1"],
["Daniel O.", "d.o@mail.com", "OneEco", "1"],
["Mike E.", "m.e@mail.com", "FourEco", "1"],
["Matthew R.", "mr@test.com", "OneEco", "5"],
["Albert K.", "albert@test.com", "OneEco", "5"]

]

payments = [
["1", "john2@mail.com", "33"],
["2", "michellee@mail.com", "60"],
["4", "james@mail.com", "8"],
["3", "stacy.c@test.com", "8"],
["5", "bob@mail.com", "60"],
["6", "email not found", "110"],
["7", "email not found", "1"],
["8", "email not found", "2"],
["9", "email not found", "3"],
["99", "email not found", "4"],
["10", "mr@test.com", "5"],
["11", "a@mail.com", "5"]
]

prices = [
["Economy", "4"],
["Top", "11"],
["Medium", "6"],
["OneEco", "1"],
["TwoEco", "2"],
["ThreeEco", "3"],
["FourEco", "4"]
]

# def matching(users,payments,prices):

#     price_map = {}

#     for ticket , price in prices:
#         price_map[ticket] = int(price)
    
#     # prepare user datastructure
#     user_info = {}
#     email_to_user = {}
#     amount_to_users = {}

#     for name,email,ticket,qty in users:
#         qty = int(qty)
#         total_amount = price_map[ticket] * qty

#         # store user info
#         user_info[name] = {
#             "email":email,
#             "amount":total_amount
#         }

#         # To map user
#         email_to_user[email] = name

#         #map to users

#         if total_amount not in amount_to_users:
#             amount_to_users[total_amount] = []
#             amount_to_users[total_amount].append(name)

#         # match payments in email 

#     result= {}
#     unmatched_payments = [] 

#     for pid,pay_email,pay_amount in payments:
#             pid = int(pid)
#             pay_amount = int(pay_amount)

#             if pay_email in email_to_user:
#                 # direct email match
#                 user = email_to_user[pay_email]
#                 result[pid] = user
#                 # remove matched user from amount bucket

#                 amt = user_info[user]['amount']
#                 if user in amount_to_users.get(amt,[]):
#                     amount_to_users[amt].remove(user)
            
#             else:
#                 unmatched_payments.append((pid,pay_amount))
        

#     for pid,pay_amount in unmatched_payments:
#             candidates = amount_to_users.get(pay_amount,[])

#             if len(candidates) == 3:
#                 result[pid] = candidates[0]
#                 amount_to_users[pay_amount].remove(candidates[0])
#             else:
#                 raise Exception(f"ambigious amount matching for amount {pay_amount}")

#     return print(dict(sorted(result.items())))
# matching(users,payments,prices)

def matching(users, payments, prices):

    # Step 1: price map
    price_map = {}
    for ticket, price in prices:
        price_map[ticket] = int(price)

    # Step 2: prepare structures
    user_info = {}
    email_to_user = {}
    amount_to_users = {}

    for name, email, ticket, qty in users:
        email = email.strip()
        qty = int(qty)
        total_amount = price_map[ticket] * qty

        user_info[name] = {
            "email": email,
            "amount": total_amount
        }

        email_to_user[email] = name

        # ✅ FIX: always append
        if total_amount not in amount_to_users:
            amount_to_users[total_amount] = []

        amount_to_users[total_amount].append(name)

    # Step 3: match by email
    result = {}
    unmatched_payments = []

    for pid, pay_email, pay_amount in payments:
        pay_email = pay_email.strip()
        pay_amount = int(pay_amount)

        if pay_email in email_to_user:
            user = email_to_user[pay_email]
            result[pid] = user

            amt = user_info[user]['amount']
            if user in amount_to_users.get(amt, []):
                amount_to_users[amt].remove(user)
        else:
            unmatched_payments.append((pid, pay_amount))

    # Step 4: match by amount
    for pid, pay_amount in unmatched_payments:
        candidates = amount_to_users.get(pay_amount, [])

        # ✅ FIX: just pick remaining user
        if candidates:
            user = candidates.pop()
            result[pid] = user
    
    return dict(sorted(result.items(), key=lambda x: int(x[0])))

print(matching(users,payments,prices))