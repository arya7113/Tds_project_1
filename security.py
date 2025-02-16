# security.py
from pathlib import Path
from fastapi import Request, HTTPException
import os

class SecurityMiddleware:
    def __init__(self, data_directory: str = "/data"):
        self.data_directory = Path(data_directory)

    async def validate_path(self, path: str) -> bool:
        """Ensure path is within /data directory (requirement B1)"""
        try:
            absolute_path = Path(path).resolve()
            return self.data_directory in absolute_path.parents
        except Exception:
            return False

    async def __call__(self, request: Request, call_next):
        # Extract path from query parameters if present
        path = request.query_params.get('path', '')
        
        # Check if path is trying to access outside /data
        if path and not await self.validate_path(path):
            raise HTTPException(
                status_code=400,
                detail="Access denied: Can only access files within /data directory"
            )
        
        response = await call_next(request)
        return response