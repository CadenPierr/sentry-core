# For each lead in my check list, check if it appears in my verified lists.
# If yes, print Verified. If no, print Unverified.

v_leads = ["Matthew", "Luke", "John", "David", "Moses"]
c_leads = ["Luke", "Mark", "Jacob", "David", "Adam"]


for name in c_leads:
    if name in v_leads:
        print("Verified")
    else:
        print("Unverified")


