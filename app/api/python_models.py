from typing import Optional
from sqlmodel import Field  # type: ignore
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.future import Engine

__all__ = [
    "Session",
    "Products",
    "Customers",
    "Sales_Transactions",
    "Sales_Invoices"
]

def __dir__():
    return __all__

DATABASE_PATH = "/data/database.sqlite"


class Products(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    base_price: float
    stock: int
    is_taxable: bool = Field(default=True)
    selling_unit: str = Field(default="unit")
    discount: int = Field(default=0)
    description: Optional[str]

    @classmethod
    def add_new_product(cls, engine: Engine,
                        name: str,
                        base_price: float,
                        stock: int,
                        is_taxable: bool = True,
                        selling_unit: str = "unit",
                        discount: int = 0,
                        description: Optional[str] = None):
        with Session(engine) as session:
            session.add(cls(
                name=name,
                base_price=base_price,
                stock=stock,
                is_taxable=is_taxable,
                selling_unit=selling_unit,
                discount=discount,
                description=description
            ))
            session.commit()


class Customers(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    date_joined: str
    purchase_count: int = Field(default=0)
    return_count: int = Field(default=0)
    first_name: str
    last_name: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    country: Optional[str]
    city: Optional[str]
    street: Optional[str]
    address: Optional[str]


class Sales_Transactions(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    customer: int = Field(foreign_key=Customers.id)
    product: int = Field(foreign_key=Products.id)
    quantity: int
    timestamp: str
    # transaction_type: str
    is_credit: bool
    description: Optional[str]


class Sales_Invoices(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    reference_number: str
    other_party: int = Field(foreign_key=Customers.id)
    invoice_type: str
    transactions: int = Field(foreign_key=Sales_Transactions.id)
    time_issued: str
    total_untaxed: float
    total_taxed: float
    net_total: float
    discount_on_total: int = Field(default=0)
    link_to_PDF: Optional[str]
    note: Optional[str]


ENGINE = create_engine(f"sqlite://{DATABASE_PATH}", echo=True)
SQLModel.metadata.create_all(ENGINE)
