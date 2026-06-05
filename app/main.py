from fastapi import FastAPI, Request
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from app.config import settings

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()

app.state.limiter = limiter


@app.exception_handler(RateLimitExceeded)
async def custom_rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    """Rate limiter handler to handle if an IP exceeds the limit of calls.

    Arguments:
        request: The Request
        exc: RateLimitExceeded error from slowapi
    """
    return JSONResponse(
        status_code=429,
        content={"detail": "Too many requests. Please slow down and try again later."},
    )


host_list = [host.strip() for host in settings.allowed_hosts.split(",")]

app.add_middleware(TrustedHostMiddleware, allowed_hosts=host_list)


@app.get("/")
@limiter.limit("5/minute")
def read_root(request: Request):
    """The default root call to check for server health & status"""
    return {
        "message": "Hello",
        "env": settings.environment,
        "allowed": host_list,
    }
