from typing import Optional

from pydantic import BaseModel, Field

# BaseModelを継承したTaskのベースモデル、基本はこいつを継承する、titleも同時に定義しているため、継承するだけで中身の処理もついてくる
# TaskCreateとTaskクラスの定義が重複していたものをまとめたクラス
class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを撮りに行く") #1つ目の引数はデフォルト値, 2つ目の引数にはexmaple（例えばの値）

# TaskBaseを継承したcreateクラス
class TaskCreate(TaskBase):
    pass

# createのレスポンス用
class TaskCreateResponse(TaskBase):
    id: int
    
    class Config:
        orm_mode = True

# Routerで定義してるTaskクラス
class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ") #1つ目の引数のデフォルトはfalse, 2つ目の引数でフィールドの説明を入れてる
    
    class Config:
        orm_mode = True
    