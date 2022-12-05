from typing import Optional

from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="クリ＝ニングを取りに行く")
    done: bool = Field(False, description="完了フラグ")
