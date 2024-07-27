class SavingAccount: ...

class CheckingAccount: ...

class Stock: ...

class Bond: ...

class RealEstate: ...

class BankAccount(SavingAccount, CheckingAccount): ...

class Security(Stock, Bond): ...

class InsurableItem(BankAccount, RealEstate): ...

class Asset(Security, RealEstate): ...

class InterestBearingItem(Security, BankAccount): ...
