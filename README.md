# Módulo de Taller de Reparación de Vehículos

## Subir una instancia con `docker-compose`

1. Ubicado en la carpeta del módulo, ejecutar:
  1. `docker-compose up -d`

## Subir un ambiente de desarrollo `docker-compose` en **Visual Studio Code**

> Debe tener instalado el paquete de extensiones de desarrollo remoto de **Visual Studio Code**:
> `ms-vscode-remote.vscode-remote-extensionpack`

1. Abrir carpeta con **Visual Studio Code**
1. Abrir la paleta de comandos:  
  ![image](https://user-images.githubusercontent.com/12959163/145419269-070e44f4-29d4-49d9-99d3-b870c5e6c8aa.png)
1. Buscar y ejecutar: `>Remote-Containers: Open Folder in Container`
1. Seguir las instrucciones y esperar

## Configuración Inicial

1. Visitar http://localhost:8069 e introducir los datos de configuración necesario
  ![image](https://user-images.githubusercontent.com/12959163/145413082-7dce7f90-ee7b-4597-b14a-7cee369d135a.png)

1. En el listado de aplicaciones, buscar e instalar "Car Repair Workshop
  ![image](https://user-images.githubusercontent.com/12959163/145413493-a465c1e9-470a-4b9e-b43d-4eebfbb4d4fa.png)

## Uso / Funciones

### Ir a Menú / Taller

![image](https://user-images.githubusercontent.com/12959163/145416469-ce1035ce-725e-455c-ab98-687f17cb8e43.png)
![image](https://user-images.githubusercontent.com/12959163/145416606-f169aaf9-3c82-4742-9157-45c6a9d2944a.png)

### Al crear una nueva cotización de reparación
1. Seleccionar el cliente
1. Seleccionar el vehículo del cliente
![image](https://user-images.githubusercontent.com/12959163/145414666-0334fd79-2a9d-41b8-a797-bd7f793032da.png)
- Si el cliente no tiene vehículos, crear uno
  ![image](https://user-images.githubusercontent.com/12959163/145415154-5dfabe35-8f14-4575-81d4-df8b99c32f1e.png)

### Al completar los datos de la cotización, confirmar
- ![image](https://user-images.githubusercontent.com/12959163/145499615-8014c84a-9f12-4cd3-ae3b-0df65355dbb0.png)
- ![image](https://user-images.githubusercontent.com/12959163/145416091-eb9dc871-1410-42f1-9d29-22c862fa66cd.png)
> Una vez creada la factura, la cotización se considera como "Facturada" y se incluye en la reportería
  
### Reportes

![image](https://user-images.githubusercontent.com/12959163/145416862-338e6068-f6fe-4323-a2d3-5b63847c61b2.png)

#### Servicio Más Vendido

Archivo PDF con el detalle del servicio que más ha sido vendido:

![image](https://user-images.githubusercontent.com/12959163/145417236-ecc0cd95-0a1c-4834-a7d6-07995a2aa61d.png)


#### Servicios de Vehículo

Archivo PDF con listado de los vehículos y los servicios que se le han aplicado:

![image](https://user-images.githubusercontent.com/12959163/145417469-1e5b0dc3-7ffc-44cd-9177-57925eeda036.png)
