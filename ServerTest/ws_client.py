#coding: utf-8 



from suds import client
 
  
client = client("http://127.0.0.1:8000/SOAP/?wsdl")  
  
ret = client.service.make_project("Test", "1.0.0")  
