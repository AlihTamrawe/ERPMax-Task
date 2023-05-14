from operator import index
from flask import Flask, render_template, request, redirect  
from  mysqlconnection import connectToMySQL
from datetime import datetime  
import itertools 


#----------------------------1-halloworld
f=100
app = Flask(__name__)  
@app.context_processor
def add_imports():
    return dict( itertools=itertools )
@app.route("/one")     #test
def index():
    mysql = connectToMySQL('inventory_management')	        
    product = mysql.query_db('SELECT * FROM product;')  
    print(product)
    f=1
    return render_template("index.html",all_products = product,flag =f)




@app.route("/move") 
def index_move():
    mysql = connectToMySQL('inventory_management')	        
    product = mysql.query_db('SELECT * FROM product;')  
    print(product)
    mysql2 = connectToMySQL('inventory_management')	        
    locations = mysql2.query_db('SELECT * FROM location;')  
    f=0
    return render_template("index.html",all_products = product,all_locations = locations,flag =f)


@app.route("/report")   # get product balance in each location 
def index_report():
    mysql = connectToMySQL('inventory_management')	        
    query = "SELECT  product_name, to_location, SUM(quantity) as qa   FROM   product  JOIN  productmovement  ON     product_id_m = product_id  Group By to_location ;"
    result = mysql.query_db(query)   
    mysql1 = connectToMySQL('inventory_management')	        
    query2 = "SELECT * FROM location ;"
    result2 = mysql1.query_db(query2)   
    dic = {}    # i had used Dictanary data structure to define location in same table
    for i in range (0,len(result2)):
        dic[result2[i]['idlocation']] = result2[i]['location_name']
        print(result2[i]['location_name'])
    f=10

    return render_template("index.html",all_movement =result ,all_location =dic ,flag =f) 

##################################################################################################


@app.route("/two")
def index3():
    mysql = connectToMySQL('inventory_management')	        
    locations = mysql.query_db('SELECT * FROM location;')  
    print(locations)
    f=3
    return render_template("index.html",all_locations = locations,flag =f)

@app.route("/")
def index2():
    mysql = connectToMySQL('inventory_management')	        
    products = mysql.query_db('SELECT * FROM product;')  
    mysql2 = connectToMySQL('inventory_management')	        
    locations = mysql2.query_db('SELECT * FROM location JOIN product where location_id = idlocation ;')  
    mysql3 = connectToMySQL('inventory_management')	        
    allocations = mysql3.query_db('SELECT * FROM location  ;')  

    print(locations)
    f=2
    return render_template("index.html",all_products = products,locationsforprod=locations,all_locations=allocations,flag =f)# http://localhost:5000 - should display 8 by 8 checkerboard

@app.route("/create_product", methods=["POST"]) # create pod
def add_product_to_db():
    is_valid = True		# assume True
    if len(request.form['pname']) < 4:
        is_valid = False
    mysql = connectToMySQL('inventory_management')	        
    QUERY = 'INSERT INTO inventory_management.product (product_name , location_id ) values (%(p_name)s,%(loca_id)s );'
    data = {
        "p_name": request.form["pname"],
        "loca_id": request.form["locations_id"]

    }
    print (data)
    if is_valid : 
        new_poduct = mysql.query_db(QUERY,data)
    else:
        print("not Valid")
        
    return redirect("/")




@app.route("/create_location", methods=["POST"])  # Create location form 
def add_location_to_db():
    mysql = connectToMySQL('inventory_management')	        
    QUERY = 'INSERT INTO inventory_management.location (location_name  ) values (%(l_name)s );'
    data = {
         "l_name": request.form["lname"]

    }
    print (data)
    new_location = mysql.query_db(QUERY,data)
    return redirect("/two") 



@app.route("/create_move", methods=["POST"]) # create move
def add_move_to_db():
    is_valid = True		# assume True
    if int(request.form['qty']) <  1:
        is_valid = False
    print(int(request.form['qty']))
    date_time = datetime.now()
    mysql = connectToMySQL('inventory_management')	        
    QUERY = 'INSERT INTO inventory_management.productmovement (product_id_m  , to_location , from_location , quantity , timestamp ) values (%(p_name)s,%(loca_t)s ,%(loca_f)s,%(qty)s ,%(timestamp)s );'
    data = {
        "p_name": request.form["pname"],
        "loca_f": request.form["locations_id_f"],
        "loca_t": request.form["locations_id_t"],
        "qty":request.form["qty"],
        "timestamp":datetime.now()
    }
    print (data)
    if is_valid : 
        new_poduct = mysql.query_db(QUERY,data)
    else:
        print("not Valid")
        
    return redirect("/")


# @app.route('/movement') # update move form
# def show_movement():
#     mysql = connectToMySQL('inventory_management')	        
#     query = "SELECT * FROM productmovement     INNER JOIN product   ON     product_id_m = product_id  ;"
#     result = mysql.query_db(query)   

#     mysql2 = connectToMySQL('inventory_management')	        
#     query2 = "SELECT * FROM productmovement     INNER JOIN location  ON     idlocation = to_location  "
#     result2 = mysql2.query_db(query2)   


#     mysql3 = connectToMySQL('inventory_management')	        
#     query3 = "SELECT * FROM productmovement     INNER JOIN location  ON     idlocation = from_location ;"
#     result3 = mysql3.query_db(query3)   
#     print(result)
#     f=11

#     return render_template("index.html",all_movement =result2 , all_product=result,all_location = result3 ,flag =f) 


@app.route('/movement') # update move form
def show_movement():
    mysql = connectToMySQL('inventory_management')	        
    query = "SELECT idproductmovement, product_name, to_location, quantity , timestamp ,from_location     FROM productmovement     LEFT JOIN product   ON     product_id_m = product_id   ;"
    result = mysql.query_db(query)   
    mysql1 = connectToMySQL('inventory_management')	        
    query2 = "SELECT * FROM location ;"
    result2 = mysql1.query_db(query2)   
    dic = {}    # i had used Dictanary data structure to define location in same table
    for i in range (0,len(result2)):
        dic[result2[i]['idlocation']] = result2[i]['location_name']
        print(result2[i]['location_name'])
    print(dic.get(1))
    f=11

    return render_template("index.html",all_movement =result ,all_location =dic ,flag =f) 

@app.route('/updatelocation/<id>') # update location form
def update_location_form(id):
    mysql = connectToMySQL('inventory_management')	        
    query = "SELECT * FROM location WHERE idlocation = %(id)s;"
    data = { 'id' : id }
    result = mysql.query_db(query, data)    
    print(result)
    f=8
    return render_template("index.html",loca = result[0],flag =f) 


@app.route("/move_into/<id>") # update location move out
def move_into_to_db(id):
    mysql = connectToMySQL('inventory_management')	        
    QUERY = ' UPDATE productmovement SET  from_location = %(l_name)s WHERE idproductmovement = %(id)s ;'
    data = {
         "l_name": None,
         "id" : id

    }
    print ("done o")
    new_location = mysql.query_db(QUERY,data)
    return redirect("/movement") 

@app.route("/move_out/<id>") # update location move out
def move_out_to_db(id):
    mysql = connectToMySQL('inventory_management')	        
    QUERY = ' UPDATE productmovement SET  to_location= %(l_name)s WHERE idproductmovement = %(id)s ;'
    data = {
         "l_name": None,
         "id" : id

    }
    print ("done")
    new_location = mysql.query_db(QUERY,data)
    return redirect("/movement") 



@app.route("/set_location_f/<id>",methods=["POST"]) # update location move out
def set_from_db(id):
    mysql = connectToMySQL('inventory_management')	        
    QUERY = ' UPDATE productmovement SET  from_location = %(loc_id)s WHERE idproductmovement = %(id)s ;'
    data = {
            "id" : id,
            "loc_id":request.form["location_f"]

    }
    print (request.form["location_f"])
    new_location = mysql.query_db(QUERY,data)
    return redirect("/movement") 

@app.route("/set_location_t/<id>",methods=["POST"]) # update location move out
def set_to_db(id):
    mysql = connectToMySQL('inventory_management')	        
    QUERY = ' UPDATE productmovement SET  to_location = %(loc_id)s WHERE idproductmovement = %(id)s ;'
    data = {
            "id" : id,
            "loc_id":request.form["location_to"]

    }
    print (request.form["location_to"])
    new_location = mysql.query_db(QUERY,data)
    return redirect("/movement") 


@app.route("/update_location/<id>", methods=["POST"]) # update location Route
def edit_location_to_db(id):
    mysql = connectToMySQL('inventory_management')	        
    QUERY = ' UPDATE location SET location_name = %(l_name)s WHERE idlocation = %(id)s ;'
    data = {
         "l_name": request.form["lname"],
         "id" : id

    }
    print (data)
    new_location = mysql.query_db(QUERY,data)
    return redirect("/two") 




@app.route('/updateproduct/<id>') # update prod form
def update_product_form(id):
    mysql = connectToMySQL('inventory_management')	        
    query = "SELECT * FROM product WHERE product_id = %(id)s;"
    data = { 'id' : id }
    result = mysql.query_db(query, data)    
    print(result)
    f=7
    return render_template("index.html",prod = result[0],flag =f) 



@app.route("/update_product/<id>", methods=["POST"]) # update prod Route
def edit_product_to_db(id):
    mysql = connectToMySQL('inventory_management')	        
    QUERY = ' UPDATE product SET product_name = %(p_name)s WHERE product_id = %(id)s ;'
    data = {
         "p_name": request.form["pname"],
         "id" : id

    }
    print (data)
    new_location = mysql.query_db(QUERY,data)
    return redirect("/") 

@app.route("/delete_product/<id>") # DELETE prod Route
def delete_product_to_db(id):
    mysql = connectToMySQL('inventory_management')	        
    QUERY = 'DELETE FROM product WHERE product_id = %(id)s  ;'
    data = {
        "id" : id

    }
    print (data)
    new_location = mysql.query_db(QUERY,data)
    return redirect("/") 




@app.route("/delete_location/<id>") # DELETE location Route
def delete_location_to_db(id):
    mysql = connectToMySQL('inventory_management')	        
    QUERY = 'DELETE FROM location WHERE idlocation = %(id)s  ;'
    data = {
        "id" : id

    }
    new_location = mysql.query_db(QUERY,data)
    print (new_location)

    return redirect("/two") 


@app.route("/delete_movement/<id>") # DELETE move Route
def delete_movement_to_db(id):
    mysql = connectToMySQL('inventory_management')	        
    QUERY = 'DELETE FROM productmovement WHERE idproductmovement = %(id)s  ;'
    data = {
        "id" : id

    }
    print (data)
    new_location = mysql.query_db(QUERY,data)
    return redirect("/movement") 







@app.route('/product/<id>') # Show prod
def show_product_profile(id):
    mysql = connectToMySQL('inventory_management')	        
    query = "SELECT * FROM product WHERE product_id = %(id)s;"
   
    data = { 'id' : id }

    result = mysql.query_db(query, data)    
    print(result[0] )

    mysql = connectToMySQL('inventory_management')	        
    query2 = "SELECT * FROM location WHERE idlocation = %(id2)s;"
    data1 = { 'id2' : result[0]["Location_id"] }
    result2 = mysql.query_db(query2, data1)    

    print(result[0]["product_name"])
    f=4
    return render_template("index.html",prods = result[0],location = result2[0],flag =f)

@app.route('/location/<locationname>/<id>') 
def show_locationnameproductname_profile(locationname, id):
    mysql = connectToMySQL('inventory_management')	      
    query = "SELECT * FROM location WHERE idlocation = %(id)s;"


    data = { 'id' : id }
    result = mysql.query_db(query, data)    
    print(result)

    mysql = connectToMySQL('inventory_management')	      
    query2 = "SELECT * FROM product WHERE location_id = %(id)s;"
    data = { 'id' : id }

    result2 = mysql.query_db(query2, data)   
    if  result2 == None :  # out of range error 
            print(result2[0])
            return render_template("index.html",prods = None,location = result[0],flag = 0)

    f=5
    return render_template("index.html",locationname=locationname,loca = result[0],all_product = result2,flag =f)# http://localhost:5000 - should display 8 by 8 checkerboard

if __name__=="__main__":   
    app.run(debug=True)    

