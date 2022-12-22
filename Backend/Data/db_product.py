from sqlalchemy.orm.session import Session
from schemas import ProductBase
from Data.models import DbProduct
from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm.session import Session

def Createproducts( request:ProductBase,db:Session):
    Product=DbProduct(
        Name=request.Name,
        description=request.description,
        price=request.price,
        user_id=request.user_id,
        Categories= request.Categories,
        image=request.image
    )
    db.add(Product)
    db.commit()
    db.refresh(Product)

    return Product

def Getproduct(id:int,db:Session):
    result= db.query(DbProduct).filter(DbProduct.id == id).first()
    if result is None:
        raise Exception(status_code=status.HTTP_404_NOT_FOUND,detail=f"Product {id} not found")
    return result

#get User
def getProduct(id:int,db:Session):
    return db.query(DbProduct).filter(DbProduct.id == id).first()

# update image product
def Update_Product_image(id:int,db:Session,image:str):
    product_res=db.query(DbProduct).filter(DbProduct.id == id)
    if  product_res is not None:

        product_res.update({
                    DbProduct.image:image,
            })
        db.commit()
        return 'product  image address successfully'

    return 'product is not found'

#update data product
def update_product(id:int, db:Session, request:ProductBase):
    product=db.query(DbProduct).filter(DbProduct.id == id)
    if product is not None:
        product.update({
                DbProduct.Name:request.Name,
                DbProduct.description:request.description,
                DbProduct.Categories:request.Categories,
                DbProduct.image:request.image,
                DbProduct.price:request.price,
                DbProduct.user_id:request.user_id
        })
        db.commit()
        return "update product "
    return "product not found"

#delete product
def delete_product(id:int,db:Session):
    product=getProduct(id,db)
    db.delete(product)
    db.commit()
    return "product deleted"

#get all products
def get_all_products(db:Session):
    return db.query(DbProduct).all()

#Serach Product
def Serach_Product(name:str,db:Session):
    return db.query(DbProduct).filter(DbProduct.Name.contains(name)).all()
