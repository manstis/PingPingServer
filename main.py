from fastapi import FastAPI, APIRouter, Request
from starlette.responses import PlainTextResponse

import requests
router = APIRouter(tags=["api"])
app = FastAPI(
    title="PingPingServer",
    description="Pong's your message by relaying it to the PingServer.",
    version="0.1.0",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

@router.get("/pingping")
def handler(request: Request, message: str) -> PlainTextResponse:
    # curl http://ping-server-service.manstis:8080/ping?message=a (when separate Pods/Deployments/Services)
    # return PlainTextResponse(content=requests.request('GET', f"http://ping-server-service.manstis:8080/ping?message={message}", verify=False).text)
    # curl http://localhost:8080/ping?message=a (when sidecar Container)
    return PlainTextResponse(content=requests.request('GET', f"http://localhost:8080/ping?message={message}", verify=False).text)

app.include_router(router)