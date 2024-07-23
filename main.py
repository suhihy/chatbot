from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/')
def read_root(request: Request):
    
    print(request)

    return {'Hello': 'World'}