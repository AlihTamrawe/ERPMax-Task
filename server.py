from operator import index
from flask import Flask, render_template, request, redirect  
from  mysqlconnection import connectToMySQL
#----------------------------1-halloworld
f=0
app = Flask(__name__)   
@app.route("/one")
def index():
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
    product = mysql.query_db('SELECT * FROM product;')  # call the query_db function, pass in the query as a string
    print(product)
    f=1
    return render_template("index.html",all_products = product,flag =f)

@app.route("/two")
def index3():
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
    locations = mysql.query_db('SELECT * FROM location;')  # call the query_db function, pass in the query as a string
    print(locations)
    f=3
    return render_template("index.html",all_locations = locations,flag =f)

@app.route("/")
def index2():
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
    products = mysql.query_db('SELECT * FROM product;')  # call the query_db function, pass in the query as a string
    mysql2 = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
    locations = mysql2.query_db('SELECT * FROM location JOIN product where location_id = idlocation ;')  
    mysql3 = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
    allocations = mysql3.query_db('SELECT * FROM location  ;')  # call the query_db function, pass in the query as a string

    print(locations)
    f=2
    return render_template("index.html",all_products = products,locationsforprod=locations,all_locations=allocations,flag =f)# http://localhost:5000 - should display 8 by 8 checkerboard

@app.route("/create_product", methods=["POST"])
def add_product_to_db():
    is_valid = True		# assume True
    if len(request.form['pname']) < 4:
        is_valid = False
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
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
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
    QUERY = 'INSERT INTO inventory_management.location (location_name  ) values (%(l_name)s );'
    data = {
         "l_name": request.form["lname"]

    }
    print (data)
    new_location = mysql.query_db(QUERY,data)
    return redirect("/two") 


@app.route('/updatelocation/<id>') # update location form
def update_location_form(id):
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
    query = "SELECT * FROM location WHERE idlocation = %(id)s;"
    data = { 'id' : id }
    result = mysql.query_db(query, data)    
    print(result)
    f=8
    return render_template("index.html",loca = result[0],flag =f) 



@app.route("/update_location/<id>", methods=["POST"]) # update location Route
def edit_location_to_db(id):
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
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
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
    query = "SELECT * FROM product WHERE product_id = %(id)s;"
    data = { 'id' : id }
    result = mysql.query_db(query, data)    
    print(result)
    f=7
    return render_template("index.html",prod = result[0],flag =f) 



@app.route("/update_product/<id>", methods=["POST"]) # update prod Route
def edit_product_to_db(id):
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
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
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
    QUERY = 'DELETE FROM product WHERE product_id = %(id)s  ;'
    data = {
        "id" : id

    }
    print (data)
    new_location = mysql.query_db(QUERY,data)
    return redirect("/") 




@app.route("/delete_location/<id>") # DELETE location Route
def delete_location_to_db(id):
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
    QUERY = 'DELETE FROM location WHERE idlocation = %(id)s  ;'
    data = {
        "id" : id

    }
    print (data)
    new_location = mysql.query_db(QUERY,data)
    return redirect("/two") 




@app.route('/product/<id>') # Show prod
def show_product_profile(id):
    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
    query = "SELECT * FROM product WHERE product_id = %(id)s;"
   
    data = { 'id' : id }

    result = mysql.query_db(query, data)    
    print(result[0] )

    mysql = connectToMySQL('inventory_management')	        # call the function, passing in the name of our db
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

