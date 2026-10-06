#Product Catalog Mini-API

##Endpoint Design Planning

###1.GET/products
*  **Client send    :- a basic get request over the network
*  **Server receive :- request directed at collection path 
*  **server do      :- access in-memory database array
*  **server return  :- array list of products as JSON
*  **go wrong       :- list is empty -return empty array


###2. GET /products?{product_id}
*  **Client send    :- get request with id embedded in url
*  **Server receive :- path variable casr as an integer
*  **Server do      :- scan using for loop to match product_id
*  **Server return  :- matching product dictionary
*  **go wrong       :- inputs non-existent id - safety net - return {"error"}


###3. POST /products
*  **Client send    :- post request directed to the resource
*  **Server receive :- request body with the data to add to the collection
*  **Server do      :- add the data to the resource
*  **Server return  :- return the added data with the id
*  **go wrong       :- unauthorised access to add data, omit mandatory field, invalid data types


###4. PUT /products/{product_id}
*  **Client send    :- put request with id to make changes to embedded in the ur 
*  **Server receive :- request with the data to update (complete data including the one not to update)
*  **Server do      :- use for loop - find the id - update the value 
*  **Server return  :- return the updated data
*  **go wrong       :- unauthorized access, wrong or invalid inputs


###5. DELETE /products/{product_id}
*  **Client send    :- delete request with the id od the product to delete embedded in the url
*  **Server receive :- request with the id of the product in the collection
*  **Server do      :- us for loop - find the id - delete the product data associated with that id
*  **Server return  :- it returns a deleted successfully message
*  **go wrong       :- product id does not exist, unauthorised data manipulation