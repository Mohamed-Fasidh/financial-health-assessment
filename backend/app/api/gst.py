from fastapi import APIRouter
from app.integrations.gst.client import GSTClient
from app.integrations.gst.service import analyze_gst_compliance

router = APIRouter(prefix="/gst", tags=["GST"])

@router.get("/{gstin}")
def check_gst(gstin: str):
    client = GSTClient()
    gst_data = client.fetch_returns(gstin)
    compliance = analyze_gst_compliance(gst_data)

    return {
        "gstin": gstin,
        "gst_data": gst_data,
        "compliance": compliance
    }
