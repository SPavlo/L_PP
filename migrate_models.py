from coder import database

BaseModel = database.Model

class Budget(BaseModel):
    __tablename__ = 'budget'
    BudgetID = database.Column(database.INTEGER, primary_key=True)
    money = database.Column(database.INTEGER)

class FamilyMember(BaseModel):
    __tablename__ = 'FamilyMember'
    FamilyMemberID = database.Column(database.INTEGER, primary_key=True)
    UserName =database.Column(database.VARCHAR(45))
    FirstName=database.Column(database.VARCHAR(45))
    LastName=database.Column(database.VARCHAR(45))
    email=database.Column(database.VARCHAR(45))
    password=database.Column(database.VARCHAR(45))
    phone=database.Column(database.VARCHAR(45))
    Budget_BudgetID=database.Column(database.INTEGER,database.ForeignKey(Budget.BudgetID))
    Budget = database.relationship(Budget)

class PersonalAccount(BaseModel):
    __tablename__ = 'PersonalAccount'
    ID = database.Column(database.INTEGER,primary_key=True)
    FamilyMemberID = database.Column(database.INTEGER,database.ForeignKey(FamilyMember.FamilyMemberID))
    FamilyMember = database.relationship(FamilyMember)
    amount = database.Column(database.INTEGER)

class story(BaseModel):
    __tablename__ = 'Story'
    StoryID=database.Column(database.INTEGER, primary_key=True)
    PersonalAccount_ID \
        = database.Column(database.INTEGER, database.ForeignKey(PersonalAccount.ID))
    PersonalAccount = database.relationship(PersonalAccount)
    transaction =database.Column(database.BOOLEAN)
    price=database.Column(database.INTEGER)
    data = database.Column(database.DATETIME)

class Operations(BaseModel):
    __tablename__ = 'Operations'
    OperationsID = database.Column(database.INTEGER, primary_key=True)
    amount = database.Column(database.INTEGER)
    direction = database.Column(database.BOOLEAN)
    PersonalAccount_ID = database.Column(database.INTEGER,database.ForeignKey(PersonalAccount.ID))
    PersonalAccount = database.relationship(PersonalAccount)
    Budget_BudgetID = database.Column(database.INTEGER,database.ForeignKey(Budget.BudgetID))
    Budget = database.relationship(Budget)

database.create_all()