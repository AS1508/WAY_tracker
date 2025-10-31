# WAY Tracker API ✈️

Un servicio API backend completo construido con **Python** y **FastAPI** que permite a los usuarios rastrear vuelos en tiempo real. Los usuarios pueden registrarse, gestionar sus perfiles y guardar vuelos de interés obtenidos de la API externa de AviationStack.

---

## 🚀 Características Principales

- 🔐 **Autenticación y Autorización:** Sistema completo de registro y login usando `passlib` (bcrypt) para hashing y tokens **JWT** para la seguridad de endpoints.
    
- 👤 **Gestión de Perfil:** Endpoints protegidos para que los usuarios vean (`GET /me`), actualicen (`PATCH /me/profile`) y eliminen (`DELETE /me/account`) sus propias cuentas.
    
- ✈️ **Datos de Vuelos en Vivo:** Integración con la API de **AviationStack** para obtener datos de vuelos por ICAO (`/flights/...`) o aeropuerto (`/airports/...`).
    
- ❤️ **Seguimiento de Vuelos:** Los usuarios autenticados pueden guardar (`POST /me/flights`) y gestionar una lista de vuelos de su interés.
    
- 🧱 **Arquitectura Profesional:** Implementación de un **patrón de 3 capas (Router, Service, Repository)** para una clara separación de responsabilidades y un código limpio y mantenible.
    

---

## 🏗️ Arquitectura del Proyecto

Este proyecto está construido sobre una arquitectura limpia de 3 capas:

- **Capa de Routers (Controlador):** Recibe peticiones HTTP y devuelve respuestas. Es la única capa que "habla" con el cliente.
    
- **Capa de Services (Lógica de Negocio):** Orquesta las operaciones. Llama al repositorio y a los módulos de seguridad. (Ej: "Para registrar un usuario, _primero_ comprueba si existe, _luego_ hashea la contraseña, _finalmente_ guárdalo").
    
- **Capa de Repository (Acceso a Datos):** El único módulo con permiso para hablar con la base de datos (PostgreSQL). Mantiene la lógica de SQL aislada.
    

---

## 🛠️ Stack Tecnológico

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (para la API), [Uvicorn](https://www.uvicorn.org/) (para el servidor ASGI)
- **Base de Datos:** [PostgreSQL](https://www.postgresql.org/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) (para interactuar con la BD)
- **Seguridad:** Passlib[bcrypt]
- **Hashing:**  python-jose[Cryptography]
- **Validación de Datos:** [Pydantic](https://docs.pydantic.dev/latest/) (usado por FastAPI)
- **Cliente HTTP:** [HTTPX](https://www.python-httpx.org/) (para consumir la API de AviationStack)

---

## 📚 Documentación de la API

La documentación interactiva completa de la API, generada automáticamente por **Swagger UI**, está disponible en `/docs` una vez que el servidor está en marcha.

**`http://127.0.0.1:8000/docs`**

---

## ⚙️ Instalación y Configuración Local

Sigue estos pasos para correr el proyecto en tu máquina local.

### 1. Prerrequisitos

- Tener **Python 3.10+** instalado.
    
- Tener un servidor **PostgreSQL** corriendo.
    
- Tener una **API Key** de [AviationStack](https://aviationstack.com/).
    

### 2. Clonar el Repositorio

Bash

```
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
```

### 3. Configurar el Entorno

**Crear y activar un entorno virtual:**

Bash

```
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**Instalar dependencias:**

Bash

```
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno

Este proyecto usa un archivo `.env` para manejar las claves secretas.

1. Crea un archivo llamado `.env` en la raíz del proyecto.
    
2. Copia y pega el contenido de abajo, reemplazando los valores.
    

Ini, TOML

```
# .env

# Configuración de la Base de Datos
# Reemplaza con tus credenciales de PostgreSQL
URL="postgresql://TU_USUARIO_POSTGRES:TU_CONTRASEÑA@localhost:5432/way_tracker_db"

# Configuración de Seguridad JWT
# Puedes generar una llave con: openssl rand -hex 32
SECRET_KEY="TU_LLAVE_SECRETA_SUPER_LARGA_Y_ALEATORIA"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
PWD_CONTEXT_SCHEMES="bcrypt" # (La dejaste como variable de entorno)

# API Externa
AVIATIONSTACK_API_KEY="TU_API_KEY_DE_AVIATIONSTACK"
```

_(**Nota:** Asegúrate de crear la base de datos `way_tracker_db` en PostgreSQL antes de iniciar)._

### 5. Iniciar el Servidor

Una vez configurado, inicia el servidor Uvicorn desde la carpeta raíz:

Bash

```
uvicorn app.main:app --reload
```

¡Listo! La API estará corriendo en `http://127.0.0.1:8000`.