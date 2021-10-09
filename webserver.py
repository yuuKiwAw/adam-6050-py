# encoding:utf-8
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import clr
clr.FindAssembly('/YukiAdamV.dll')
clr.AddReference('YukiAdamV')
from YukiAdamV import *


app = FastAPI()


class Modebus_set(BaseModel):
    ip: str = "192.168.0.198"
    port: str = "502"
    channel: str = "22"


# 跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/adam6050/{value}")
async def set_adam_value(value: int):
    adam_modbus = AdamClass()
    mbset = Modebus_set()
    
    if value == 0:
        try:
            adam_modbus.Adam6050Status(mbset.ip, mbset.port, mbset.channel, 0)
            return {"msg": "set value " + str(value)}
        except Exception as ex:
            return {"error": ex}
    elif value == 1:
        try:
            adam_modbus.Adam6050Status(mbset.ip, mbset.port, mbset.channel, 1)
            return {"msg": "set value " + str(value)}
        except Exception as ex:
            return {"error": ex}
    else:
        return {"msg": "error value"}
    

if __name__ == "__main__":
    uvicorn.run(app='webserver:app', host='localhost', port=8000, reload=True, debug=True)
