from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/stats")
async def get_stats():
    return {"active_users": 42, "total_installs": 15, "issues_detected": 2}
