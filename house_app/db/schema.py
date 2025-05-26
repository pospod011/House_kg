from pydantic import BaseModel


class UserProfileSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    password: str

    class Config:
        from_attributes = True


class HouseSchema(BaseModel):
    area: int
    year: int
    garage: int
    total_basement: int
    bath: int
    overall_quality: int
    neighborhood: str
    price: int


    class Config:
        from_attributes = True

