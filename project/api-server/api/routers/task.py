from fastapi import APIRouter  
# APIRotuerというのはfastapiモジュールのクラス
# fastapiモジュールのAPIRouterというクラスをimportして使用するというのがこの書き方 
# fastapiのAPIRouterを使うよ〜ということ
#モジュールとは部品みたいなもので、ファイルごとにモジュールを使用すると宣言すればモジュール内の関数などが使える、Laravelでいうrepositoryみたいなもの
from typing import List

import api.schemas.task as task_schema #api/schemas/task.pyをtask_schemaに読み替えてインポートしてる

router = APIRouter()
#tasksの基本的なCRUD処理です
#APIのレスポンスとリクエストを定義している

@router.get("/tasks", response_model=List[task_schema.Task]) #インポートしたtask_schemaのTaskクラスを使用し、リストにしてレスポンス形式で渡すための記述
async def list_tasks(): 
    return [task_schema.Task(id=1, title="1つ目のTODOタスク", done=True)] #Taskクラスで定義した各データモデルに値を渡している

@router.post("/tasks", response_model=task_schema.TaskCreateResponse) #response_modelにはCreateResponseのインスタンスがリターンされる
async def create_task(task_body: task_schema.TaskCreate): #TaskCreateの処理はTaskBaseのtitleの処理しか継承しないから、titleの定義をtask_bodyに渡して引数として所持する
    return task_schema.TaskCreateResponse(id=1, **task_body.dict()) #taskk_dbodyをdictに変換してid=1を持たせCreateResponseのインスタンスを作成 **を先頭につけるとTaskCreateResponseのコンストラクタにdictのkey/valueを渡すことができる
    # return task_schema.TaskCreateResponse(id=1, title=task_body.title, done=task_body.done)　上記の**dictを展開するとこうなる

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    return