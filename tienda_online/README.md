# Proyecto: Tienda Online
## Funcionalidades:
El proyecto cuenta con una aplicacion **core**. Dentro de esta hay tres modelos principales: Pedidos, Articulos y Clientes.
- El modelo Pedidos almacena la información sobre los pedidos registrados a traves de un formulario. Estos pedidos cuentan con su respectivo **numero**, su **fecha de realizacion** y su **entregado/no entregado** el cual se representa con un dato de tipo booleano 
- El modelo Articulos almacena información sobre los artículos disponibles en la base de datos, como el **nombre**, la **seccion** (rubro) y el **precio** del producto. Estos datos se cargan a traves de un formulario 
- El modelo Clientes almacena información sobre los clientes, como el **nombre**, la **dirección** y la **información de contacto** (email y telefono). Estos datos se cargan a traves de un formulario.

La aplicación incluye varias vistas (10 en total), cada una con una funcionalidad específica. 
- La vista para agregar un producto (anadir_producto) permite agregar nuevos artículos a la base de datos, y la vista para buscar productos (buscar_producto), permite buscar artículos existentes por su nombre. 
- La vista para registrar clientes (registrar_cliente) permite agregar nuevos clientes a la base de datos
- La vista para registrar pedidos (registrar_pedido) permite registrar pedidos y su estado de entrega. 
- La vista del formulario de contacto (contacto) permite una simulacion de un envio de email, con un asunto y texto, a la administracion del servidor.
Las demas vistas cumplen la funcionalidad de renderizar las paginas principales y procesar/validar los datos.
