from fastapi import APIRouter

from app.api.v1.activity import router as activity_router
from app.api.v1.building import router as building_router
from app.api.v1.organization import router as organization_router


router = APIRouter()

router.include_router(activity_router)
router.include_router(building_router)
router.include_router(organization_router)
