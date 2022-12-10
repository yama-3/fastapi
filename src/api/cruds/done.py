from typing import Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import models.task as task_model


async def get_done(db: AsyncSession, task_id: int) -> Optional[task_model.Done]:
    result: Result = await db.execute(
        select(task_model.Done).filter(task_model.Done.id == task_id)
    )
    done: Optional[Tuple[task_model.Done]] = result.first()
    return done[0] if done is not None else None

async def create_done(db: AsyncSession, task_id: int) -> task_model.Done:
    done = task_model.Done(id=task_id)
    db.add(done)
    await db.commit()
    await db.refresh(done)
    return done

async def delete_done(db: AsyncSession, original: task_model.Done) -> None:
    await db.delete(original)
    await db.commit()
