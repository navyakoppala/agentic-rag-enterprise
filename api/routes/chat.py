from fastapi import APIRouter

from orchestration.executors.workflow_executor import execute_workflow

router = APIRouter()

@router.post("/chat")

async def chat(query: str):

    result = execute_workflow(query)

    return result