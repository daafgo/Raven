Feature: Usuarios
    Para tener acceso a la app el usuario deberá estar registrado
    El usuario debe poder acceder al registro
   
    Scenario: Se puede acceder al registro
        Puedo acceder al registo "/registro"

    Scenario: Se puede acceder al login
        Puedo acceder al registo "/login/"

    Scenario: Nuevo registro y login
        Me registro con el usuario "prueba", email "prueba@mail.com", password "1234"
        Me logueo con el usuario "prueba", password "1234"

    Scenario: Se puede acceder al perfil
        Puedo acceder al registo "/perfil/"

    Scenario: Seguir a un usuario
        El usuario "prueba", email "prueba@mail.com" password "1234" sigue al usuario "usuario", email "usuario@mail.com" password "1234"'