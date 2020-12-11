from migrate_models import *
import datetime

database.create_all()

budget =Budget(BudgetID=4,money=27000)

fam_member = \
    FamilyMember(FamilyMemberID=1,UserName="Alpha",FirstName="Terry",
                 LastName="wolf",email="poli",password="1111",phone="123456789",Budget=budget)

pers_acc=PersonalAccount(ID=7,FamilyMember=fam_member,amount=200)

stor = story(StoryID=1,PersonalAccount=pers_acc, transaction=True, price=150,data=datetime.datetime(year=2021, month=7, day=12))

oper = Operations(OperationsID=7,amount=50,direction=True,PersonalAccount=pers_acc,Budget=budget)

database.session.add(budget)
database.session.add(fam_member)
database.session.add(pers_acc)
database.session.add(stor)
database.session.add(oper)

database.session.commit()
