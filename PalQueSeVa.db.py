import sqlite3

conexion = sqlite3.connect('PalQueSeVa.db')

conexion.execute('CREATE TABLE rol ('
                 'identificaroRol INTEGER PRIMARY KEY,'
                 'tipoRol varchar(20));')

conexion.execute('CREATE TABLE administrador ('
                 'usuario varchar(50) PRIMARY KEY,'
                 'password varchar(50) NOT NULL, '
                 'fkIdentificadorRol integer NOT NULL);')

conexion.execute('CREATE TABLE usuarioFinal ('
                 'email varchar(50) PRIMARY KEY, '
                 'password varchar(50) NOT NULL,'
                 'nombre varchar(50) NOT NULL,'
                 'apellido varchar(50) NOT NULL,'
                 'telefono integer, '
                 'fechaNacimiento varchar(10) NOT NULL,'
                 'sexo varchar(1) NOT NULL, '
                 'fkIdentificadorRol integer NOT NULL);')

conexion.execute('CREATE TABLE residencia ('
                 'email varchar(50) PRIMARY KEY, '
                 'password varchar(50) NOT NULL,'
                 'nombre varchar(50) NOT NULL,'
                 'barrio varchar(50) NOT NULL,'
                 'tipoResidencia varchar(10),'
                 'tipoHabitaciones varchar(30),'
                 'maxResidentes integer,'
                 'telefono integer,'
                 'sitioWeb varchar(100),'
                 'ubicacion varchar(100),'
                 'descripcion varchar(300),'
                 'estadoLogico boolean NOT NULL DEFAULT TRUE,'
                 'fkIdentificadorRol integer NOT NULL);')

conexion.execute('CREATE TABLE pregunta ('
                 'idPreguntas INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'fecha varchar(10) NOT NULL,'
                 'descripcion varchar(300) NOT NULL,'
                 'usuario varchar(50),'
                 'residencia varchar(50));')

conexion.execute('CREATE TABLE visita ('
                 'idVisitas INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'tipoVisita varchar(10) NOT NULL,'
                 'fecha varchar(10) NOT NULL,'
                 'hora varchar(10) NOT NULL,'
                 'usuario varchar(50) NOT NULL,'
                 'residencia varchar(50)NOT NULL,'
                 'estadoLogico boolean NOT NULL DEFAULT TRUE);')

conexion.execute('CREATE TABLE ubicacion ('
                 'idPin INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'nombre varchar(10) NOT NULL,'
                 'residencia varchar(50) NOT NULL,'
                 'direccion varchar(100) NOT NULL);')

conexion.execute('CREATE TABLE opinion ('
                 'idOpinion INTEGER PRIMARY KEY AUTOINCREMENT, '
                 'fecha varchar(10) NOT NULL,'
                 'usuario varchar(50) NOT NULL,'
                 'puntaje INTEGER NOT NULL,'
                 'descripcion varchar(300));')




'''Aqui dejo a continuación lo que estaba en note++'''



)


CREATE TABLE residencia (
	email varchar(50) PRIMARY KEY, 
    password varchar(50) NOT NULL,
    nombre varchar(50) NOT NULL,
    barrio varchar(50) NOT NULL,
    tipoResidencia varchar(10), 
	tipoHabitaciones varchar(30),
    maxResidentes integer, 
	telefono integer, 
	sitioWeb varchar(100),
	ubicacion varchar(100),
    descripcion varchar(300) NOT NULL, 
	estadoLogico boolean NOT NULL DEFAULT TRUE,
	fkIdentificadorRol integer NOT NULL,
	FOREIGN KEY (fkIdentificadorRol) REFERENCES Rol(identificaroRol)
	
)

CREATE TABLE pregunta (
	idPreguntas INTEGER PRIMARY KEY AUTOINCREMENT, 
    fecha varchar(10) NOT NULL,
    descripcion varchar(300) NOT NULL, 
	usuario varchar(50),
	residencia varchar(50),
	FOREIGN KEY (usuario) REFERENCES usuarioFinal(email)
	FOREIGN KEY (residencia) REFERENCES residencia(email)
	
)

CREATE TABLE visita (
	idVisitas INTEGER PRIMARY KEY AUTOINCREMENT, 
    tipoVisita varchar(10) NOT NULL,
    fecha varchar(10) NOT NULL,
	hora varchar(10) NOT NULL,
	usuario varchar(50),
	residencia varchar(50),
	FOREIGN KEY (usuario) REFERENCES usuarioFinal(email)
	FOREIGN KEY (residencia) REFERENCES residencia(email)
	
)

CREATE TABLE ubicacion (
	idPin INTEGER PRIMARY KEY AUTOINCREMENT, 
    nombre varchar(10) NOT NULL,
	residencia varchar(50),
	direccion varchar(100)
	FOREIGN KEY (residencia) REFERENCES residencia(email)
	
)

CREATE TABLE opinion (
	idOpinion INTEGER PRIMARY KEY AUTOINCREMENT, 
    nombre varchar(10) NOT NULL,
	residencia varchar(50),
	direccion varchar(100)
	FOREIGN KEY (residencia) REFERENCES residencia(email)
	
)



'''AGREGAR UNA RELACIÓN ENTRE UBICACION Y RESIDENCIA   CHECK!!!
Agregar una tabla llamada SERVICIOS que haga referencia a la tabla Residencias, que contenga en cada columna la cantidad o si tiene el servicio o no.'''




CREATE TABLE Rol (identificaroRol INTEGER PRIMARY KEY,tipoRol varchar(20));
CREATE TABLE Administrador (usuario varchar(50) PRIMARY KEY,password varchar(50) NOT NULL, fkIdentificadorRol integer NOT NULL);
CREATE TABLE usuarioFinal (email varchar(50) PRIMARY KEY, password varchar(50) NOT NULL,nombre varchar(50) NOT NULL,apellido varchar(50) NOT NULL,telefono integer, fechaNacimiento varchar(10) NOT NULL, sexo varchar(1) NOT NULL, fkIdentificadorRol integer NOT NULL);
CREATE TABLE residencia (email varchar(50) PRIMARY KEY, password varchar(50) NOT NULL,nombre varchar(50) NOT NULL,barrio varchar(50) NOT NULL,tipoResidencia varchar(10), tipoHabitaciones varchar(30),maxResidentes integer, telefono integer, sitioWeb varchar(100),ubicacion varchar(100),descripcion varchar(300), estadoLogico boolean NOT NULL DEFAULT TRUE,fkIdentificadorRol integer NOT NULL);
CREATE TABLE pregunta (idPreguntas INTEGER PRIMARY KEY AUTOINCREMENT, fecha varchar(10) NOT NULL,descripcion varchar(300) NOT NULL, usuario varchar(50),residencia varchar(50));
CREATE TABLE visita (idVisitas INTEGER PRIMARY KEY AUTOINCREMENT, tipoVisita varchar(10) NOT NULL,fecha varchar(10) NOT NULL,hora varchar(10) NOT NULL,usuario varchar(50) NOT NULL,residencia varchar(50)NOT NULL, estadoLogico boolean NOT NULL DEFAULT TRUE);
CREATE TABLE ubicacion (idPin INTEGER PRIMARY KEY AUTOINCREMENT, nombre varchar(10) NOT NULL,residencia varchar(50) NOT NULL,direccion varchar(100) NOT NULL);
CREATE TABLE opinion (idOpinion INTEGER PRIMARY KEY AUTOINCREMENT, fecha varchar(10) NOT NULL,usuario varchar(50) NOT NULL, puntaje INTEGER NOT NULL, descripcion varchar(300));









CREATE TABLE noticia (idNoticia INTEGER PRIMARY KEY AUTOINCREMENT, titulo varchar(100) NOT NULL, descripcion varchar(1000) NOT NULL,fecha varchar(10) NOT NULL,estadoNoticia boolean NOT NULL DEFAULT TRUE,imagen varchar(100));
CREATE TABLE servicios (idServicios INTEGER PRIMARY KEY AUTOINCREMENT,banos INTEGER,cocinas INTEGER,microondas INTEGER,heladeras INTEGER,lavarropas INTEGERwifi boolean NOT NULL DEFAULT FALSE,servicioLimpieza boolean NOT NULL DEFAULT FALSE, parrillero boolean NOT NULL DEFAULT FALSE,servicioCocina boolean NOT NULL DEFAULT FALSE,computadoras boolean NOT NULL DEFAULT FALSE,tvCable boolean NOT NULL DEFAULT FALSE,lockers boolean NOT NULL DEFAULT FALSE,salaEstudio boolean NOT NULL DEFAULT FALSE,aireAcondicionado boolean NOT NULL DEFAULT FALSE,seguridad boolean NOT NULL DEFAULT FALSE,lugarBicicletas boolean NOT NULL DEFAULT FALSE,servicioEmergencia boolean NOT NULL DEFAULT FALSE);


CREATE TABLE rol-residencia(identificadorRol INTEGER,'falta una llave primaria para referenciar la llave foranea?' FOREIGN KEY(identificadorRol) REFERENCES rol(NUMERO), FOREIGN KEY(identificadorRol) REFERENCES residencia(fkIdentificadorRol))













