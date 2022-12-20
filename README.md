# Proyecto_Django
En este repositorio se encuentran dos proyectos app_motos y app_blog 
el proyecto app_motos es back-end y provee datos de motos por medio de API web
![image](https://user-images.githubusercontent.com/101758866/208731235-8c1c8612-9710-44f3-80e0-2ac1c71ca678.png)
Este proyecto fue realizado en Django 
Aca como podemos observar  se crea la clase Moto para que esta cree una tabla llamada moto con los campos id que es la llave primaria, reference, trademark, model, price, image, supplier
![image](https://user-images.githubusercontent.com/101758866/208732452-c2613bce-312e-49c9-814f-64c52c70485d.png)
se crea la clase llamada ModelAdmin para representar el modelo en la interfaz de administracion
![image](https://user-images.githubusercontent.com/101758866/208732719-baf0d3b1-9391-49b2-b53a-baddc871e466.png)
esta clase modelSerializaer proporciona un acceso directo que permite crear una clase automaticamente una clase Serializercon los mismos campos que corresponden al modelo 
aca creamos la API view Class MotoListApiView 
a esta clase se accede a traves del endpoint y define dos metodos:
el primer responde a la peticion GET enviando el listado de registros almacenados en la base de datos 
el segundo metodo responde a la peticion POST almacenando regustros en la base de datos
aca se incluye el endpoint de la view class MotoListApiView y MotoDetailApiView
![image](https://user-images.githubusercontent.com/101758866/208737104-217a0649-efdd-4203-98d8-7dd6065af138.png)
aca se incluye las rutas de la aplicacion motos_api
![image](https://user-images.githubusercontent.com/101758866/208737242-435b4349-2341-40f3-ba74-14ac45d6e961.png)
![image](https://user-images.githubusercontent.com/101758866/208737279-3e4f558b-d03a-4386-8332-6632c8f4c303.png)
La clase DetailView se accede atraves del endpoint motos\api\<int:moto_id> y define tres metodos HTTP: Get este edita un registro, Put actualiza un registro, Delete borra un registro
