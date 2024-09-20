from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from core.system.schemas import HealthResponse

router = APIRouter(tags=["System"])


@router.get("/", include_in_schema=False)
async def redirect_docs() -> RedirectResponse:
    return RedirectResponse(url="/docs")


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="UP")
