from fastapi import APIRouter, Query, Body, Path, Depends,File,UploadFile,Form
from pydantic import BaseModel
from typing import Optional, List, Dict
from  schemas import ProductBase, productDisplay
from Data import db_product
from schemas import UserBase
from auth.oauth2 import oauth2_scheme,get_current_user
from Data.Database import get_db
from Data import db_product
import shutil
router=APIRouter(prefix="/api/product",tags=['Products'])

# token=Depends(oauth2_scheme)
@router.post("/Create_product")#,response_model=productDisplay)
async def Create_products(product:ProductBase,db=Depends(get_db)):
    
    return db_product.Createproducts(product,db)


@router.get('')
def get_all(db=Depends(get_db)):
    return db_product.get_all_products(db)


@router.post('/upload_file')
def upload_file(id_product:int,file: UploadFile= File(...),db=Depends(get_db)):
    product= db_product.Getproduct(id_product,db)
    if  product is not None:
        name = file.filename
        type = file.content_type

        path = f'files/{name}'
        with open(path, 'w+b') as buffer:
            shutil.copyfileobj(file.file, buffer)

        product.image=path
        print(product.Name)
        res=db_product.Update_Product_image(id_product,db, product.image)
        return {
        'path': path,
        'type': type,
        'message':res
        }

@router.delete('/delete_product')
async def delete_product(id:int,db=Depends(get_db)):
    res=db_product.delete_product(id,db)
    return res

@router.put('/update_product')
async def update_product(id:int,request:ProductBase,db=Depends(get_db)):
    return db_product.update_product(id,db,request)



@router.get('/search')
def search(request:str, db=Depends(get_db)):
    print ("Searching")
    return db_product.Serach_Product(request,db)
#get product by id
@router.get('/product/{id}')
def search(request:str, db=Depends(get_db)):
    print ("Finding product")
    return db_product.Serach_Product(request,db)

@router.get("/{id}")
def get_product(id:int,db=Depends(get_db),current_user:UserBase=Depends(get_current_user)):
    return {
        "data":db_product.Getproduct(id,db),
        "current_user":current_user
    }
