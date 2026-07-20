from fastapi import APIRouter
import stripe
from dotenv import load_dotenv
import os

load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

router = APIRouter(prefix="/payment", tags=["payment"])

@router.post("/create-subscription")
async def create_subscription(user_id: int, plan: str = "premium"):
    # Placeholder for Stripe session
    return {"checkout_url": "https://checkout.stripe.com/test", "message": "Subscription initiated for Superadmin features."}
