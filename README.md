# ECOMERCE Task
ERP Max Task Management System for Inventory Management Web Application

## Technologies
Language - [Python](https://www.python.org/)<br />
Web framework - [Flask](http://flask.pocoo.org/)<br />
Html tepmlate - [Jinja 2](http://jinja.pocoo.org/docs/dev/)<br />
Database - [MySQL](https://www.mysql.com/)<br />
visual code studio - [Code Editer](https://code.visualstudio.com/)<br/>


## Workspace
Your workspace should look like:
```
python-flask-mysql-template/
    static/
        css/
            style.css       # css style
    templates/
        index.html          # html template
    server.py                  # main Python app code
    mysqlconnection.sql     # MySQL database dump
    README.md
    LICENSE

```





###  in this page i can add new Location and show whole documented locations in the systems
![alt text](https://github.com/AlihTamrawe/ERPMax-Task/blob/main/media/ERPMax-Task%20-%20Google%20Chrome%205_14_2023%2011_17_02%20PM.png)

### in this page i can also add product and location / origin of product 
![alt text](https://github.com/AlihTamrawe/ERPMax-Task/blob/main/media/ERPMax-Task%20-%20Google%20Chrome%205_14_2023%2011_17_47%20PM.png)

### here i can Make Movement of product specify the location to and from to direction

![alt text](https://github.com/AlihTamrawe/ERPMax-Task/blob/main/media/ERPMax-Task%20-%20Google%20Chrome%205_15_2023%2012_05_38%20AM.png)
### here is the report of balance product in each location with Quantity

![alt text](https://github.com/AlihTamrawe/ERPMax-Task/blob/main/media/ERPMax-Task%20-%20Google%20Chrome%205_14_2023%2011_16_39%20PM.png)

### all Movement and able to change ( move out and move into )and delete
![alt text](https://github.com/AlihTamrawe/ERPMax-Task/blob/main/media/ERPMax-Task%20-%20Google%20Chrome%205_14_2023%2011_18_00%20PM.png)



### other photos
![alt text](https://github.com/AlihTamrawe/ERPMax-Task/blob/main/media/ERPMax-Task%20-%20Google%20Chrome%205_14_2023%2011_18_08%20PM.png)
### advanced option you can print
![alt text](https://github.com/AlihTamrawe/ERPMax-Task/blob/main/media/ERPMax-Task%20-%20Google%20Chrome%205_14_2023%2011_18_18%20PM.png)



## the flow is descripe in bellow link Video
-- https://drive.google.com/file/d/1JGcifIo3EmNd9KK3NMbgF3CgjFdNxnfI/view?usp=sharing



## Sql Quesris used : 
```
-- INSERT INTO inventory_management.location (location_name  ) values (%(l_name)s );
-- INSERT INTO inventory_management.product (product_name , location_id ) values (%(p_name)s,%(loca_id)s )
-- SELECT * FROM location JOIN product where location_id = idlocation ;
-- SELECT  product_name, to_location, SUM(quantity) as qa   FROM   product  JOIN  productmovement  ON     product_id_m = product_id Group By to_location ;
-- SELECT * FROM location;
-- SELECT * FROM product;
--INSERT INTO inventory_management.productmovement (product_id_m  , to_location , from_location , quantity , timestamp ) values (%(p_name)s,%(loca_t)s ,%(loca_f)s,%(qty)s ,%(timestamp)s );



