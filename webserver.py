# encoding:utf-8
import toml
import uvicorn
import clr
clr.FindAssembly('/YukiAdamV.dll')
clr.AddReference('YukiAdamV')
from YukiAdamV import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


cfg_toml_file = "./config.toml"
cfg = toml.load(cfg_toml_file)


class Modebus_set(BaseModel):
    ip: str = ""
    port: str = ""
    

app = FastAPI()


# 跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/adam6050/{channelval}/{value}")
async def set_adam_value(channelval: int, value: int):
    adam_modbus = AdamClass()
    
    mbset = Modebus_set()
    mbset.ip = cfg["adam6050setting"]["ip"]
    mbset.port = cfg["adam6050setting"]["port"]
    
    if value == 0:
        try:
            adam_modbus.Adam6050Status(mbset.ip, mbset.port, channelval, 0)
            return {"msg": {"value ": str(value),"channel ": str(channelval)}}
        except Exception as ex:
            return {"error": ex}
    elif value == 1:
        try:
            adam_modbus.Adam6050Status(mbset.ip, mbset.port, channelval, 1)
            return {"msg": {"value ": str(value),"channel ": str(channelval)}}
        except Exception as ex:
            return {"error": ex}
    else:
        return {"msg": "error value"}
    

if __name__ == "__main__":
    server_ip = cfg["webserver"]["ip"]
    server_port = int(cfg["webserver"]["port"])
    uvicorn.run(app='webserver:app', host=server_ip, port=server_port, reload=True, debug=True)
