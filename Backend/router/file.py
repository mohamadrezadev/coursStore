from fastapi import APIRouter,File,UploadFile
import shutil
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

router=APIRouter(prefix="/api" ,tags=['upload and download'])

@router.post('/file')
async def Upload1(file:bytes=File(...)):
    content=file.decode("utf8")
    content.split("\n")
    return {
        'data':content
    }

@router.post('/test_upload_file')
def upload_file(file: UploadFile= File(...)):
    name = file.filename
    type = file.content_type

    path = f'files/{name}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        'path': path,
        'type': type
    }



@router.get('/download{name}',response_class=FileResponse)
def download(name:str):
    path=f"files/{name}"
    return path
# @router.post('/file/upload_test ')
# def Upload(file:UploadFile=File(...)):
#     name=file.filename
#     type=file.content_type
#     path= f'f/{name}'
#     with open(path,'w+b')as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {
#         'path':path,
#         'type':type
#     }