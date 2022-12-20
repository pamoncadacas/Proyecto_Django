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
APP_BLOG
En este proyecto contiene un inicio de sesion basico y  informacion sobre algunos lenguajes de programacion
Este proyecto esta realizado en DJANGO
![image](https://user-images.githubusercontent.com/101758866/208741400-2cf4ddca-4a49-4fcc-9a2d-9486be07bf4f.png)
La clase Post crea una tabla llamada Post con un campo llamado message
![image](https://user-images.githubusercontent.com/101758866/208741854-0c6d7e5f-78cc-42ba-ad29-c98269d71866.png)
en el campo DIRS ponemos la ubicacion nueva de las plantillas para que django busque en este nuevo directorio de plantillas
![image](https://user-images.githubusercontent.com/101758866/208742189-403699ad-9123-4504-a9a6-225098626d7b.png)
esta es la plantilla de inicio del blog aca se verifica si el usuario esta autenticado de estarlo, aparece el mensaje de saludo y se habilita el boton para realizar logout, si no esta autenticado se habilita el boton para iniciar el proceso de Login o registrarse en signUp
![image](https://user-images.githubusercontent.com/101758866/208742277-de3551b3-a8a9-4436-abf3-eaa1ab88771c.png)
![image](https://user-images.githubusercontent.com/101758866/208742389-a63689c0-bcc7-4a4d-b48a-239c05863d4b.png)
aca creamos la vista 
![image](https://user-images.githubusercontent.com/101758866/208742581-5b85903d-87c2-4040-8e48-75d5ad30547a.png)
![image](https://user-images.githubusercontent.com/101758866/208742625-714e7e0f-8c0e-4298-849e-2c7e3790c63c.png)
aca incluimos la APP de blog 
![image](https://user-images.githubusercontent.com/101758866/208742981-0b5a7e1f-f5be-4315-b444-70c7e8be9f6e.png)
este proporciona dos enlaces de redireccion cuando LoginView no obtiene el metodo GET: LOGIN_REDIRECT_URL y LOGOUT_REDIRECT_URL para realizar esta tarea debe ubicar primero la variable DEFAULT_AUTO_FIELD
![image](https://user-images.githubusercontent.com/101758866/208743353-11d0711a-6756-4781-95a4-cb93c5fc8ffe.png)
definimos un path "accounts/", django.contrib.auth.urls define las vistas por defecto para login, logout, password_change y password reset
![image](https://user-images.githubusercontent.com/101758866/208743725-d8b2a442-0d94-4c5c-a36c-1b46e5cdcd17.png)
esta plantilla es de login 
![image](https://user-images.githubusercontent.com/101758866/208744155-e114ccde-7ed4-426e-b58f-8bcb637b61c1.png)
esta plantilla es la de sign Up donde el usuario se podra registrar
![image](https://user-images.githubusercontent.com/101758866/208744263-3d7d101f-89b8-476d-8f4b-8f7f39161a7d.png)
incluimos la clase signUpView, reverse_lazy es util cuando se necesita usar una inversion de url antes que se cargue la URLConfig del proyecto
![image](https://user-images.githubusercontent.com/101758866/208744644-c056d168-daa3-462e-9860-053f806f30b0.png)
este archivo contiene una ruta a la vista SignUpView


