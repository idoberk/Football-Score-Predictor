# """FastAPI application entry point"""

# from contextlib import asynccontextmanager
# from typing import AsyncGenerator

# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse

# from app.core.config import settings
# from app.core.logging import setup_logging, get_logger
# from app.utils.common import generate_correlation_id, get_utc_now
# from app.api import mock

# # Setup logging
# setup_logging()
# logger = get_logger(__name__)


# @asynccontextmanager
# async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
#     """Application lifespan manager for startup and shutdown events"""
#     # Startup
#     logger.info(
#         "Starting application",
#         extra={
#             "app_name": settings.APP_NAME,
#             "version": settings.APP_VERSION,
#             "debug": settings.DEBUG
#         }
#     )
    
#     yield
    
#     # Shutdown
#     logger.info("Shutting down application")


# # Create FastAPI application
# app = FastAPI(
#     title=settings.APP_NAME,
#     version=settings.APP_VERSION,
#     description="Backend API for football match predictions with ML-powered insights",
#     lifespan=lifespan,
#     debug=settings.DEBUG
# )


# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.ALLOWED_ORIGINS,
#     allow_credentials=False,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["Content-Type", settings.API_KEY_HEADER],
# )


# @app.middleware("http")
# async def add_correlation_id(request: Request, call_next):
#     """Middleware to add correlation ID to each request"""
#     correlation_id = generate_correlation_id()
#     request.state.correlation_id = correlation_id
    
#     # Log incoming request
#     logger.info(
#         "Incoming request",
#         extra={
#             "correlation_id": correlation_id,
#             "method": request.method,
#             "path": request.url.path,
#             "client": request.client.host if request.client else None
#         }
#     )
    
#     response = await call_next(request)
    
#     # Add correlation ID to response headers
#     response.headers["X-Correlation-ID"] = correlation_id
    
#     # Log response
#     logger.info(
#         "Request completed",
#         extra={
#             "correlation_id": correlation_id,
#             "status_code": response.status_code
#         }
#     )
    
#     return response


# @app.get("/")
# async def root():
#     """Root endpoint"""
#     return {
#         "name": settings.APP_NAME,
#         "version": settings.APP_VERSION,
#         "status": "running",
#         "timestamp": get_utc_now().isoformat()
#     }


# @app.get("/health")
# async def health_check():
#     """Basic health check endpoint"""
#     return {
#         "status": "healthy",
#         "timestamp": get_utc_now().isoformat()
#     }


# # Include mock API routes
# app.include_router(mock.router)


# if __name__ == "__main__":
#     import uvicorn
    
#     uvicorn.run(
#         "app.main:app",
#         host="0.0.0.0",
#         port=8000,
#         reload=settings.DEBUG
#     )

from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend API for football match predictions with ML-powered insights",
    # lifespan=lifespan,
    debug=settings.DEBUG
)

@app.get("/")
def root():
    return {"message": "Hello World!"}
