from pydantic import BaseModel, Field, ConfigDict



class SpecializationCreate(BaseModel):
    name: str = Field(max_length=100, min_length=2)
    description: str = Field(default=None)
    

class SpecializationUpdate(BaseModel):
    id: int
    name: str | None = Field(max_length=100, min_length=2, default=None)
    description: str | None = Field(default=None)


class SpecializationResponse(SpecializationCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
