from fastapi import APIRouter

router = APIRouter()

@router.put("/tasks/{task_id}/done")
async def mark_task_as_done():
    pass

@router.delete("/tasks/{task_id}/done")
async def unmask_task_as_done():
    pass