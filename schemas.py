from datetime import datetime
from pydantic import BaseModel
from dbservice import EmployeeRole

class BranchRequest(BaseModel):
    branch_name:str
    branch_location:str

class BranchResponse(BranchRequest):
    id:int

class LoginRequest(BaseModel):
    email:str
    password:str

class EmployeeCreate(BaseModel):
    employee_name:str
    employee_email:str
    national_id :int
    password_branch : str
    role: EmployeeRole

class EmployeeResponse(EmployeeCreate):
    id:int

class ShelfTypeRequest(BaseModel):
    size :str
    description: str
    price :float

class ShelfTypeResponse(ShelfTypeRequest):
    id: int

class ShelfRequest(BaseModel):
    account_number:str
    status:str
    shelf_type_id: int

class ShelfResponse(ShelfRequest):
    id:str

class PaymentMethodRequest(BaseModel):
    payment_method: str

class PaymentRequest(BaseModel):
    payment_method_id:int
    shelf_id:int
    amount: float
    payment_date:datetime
    status:str

class PaymentResponse(PaymentRequest):
    id:str

class ClientCreate(BaseModel):
    client_name:str
    client_email: str
    phone_number:str
    start_date: datetime
    shelf_id:int

