import tkinter as tk
import tkinter.ttk as ttk
import sqlite3 as sql
from tkinter import messagebox
import calendar





class Inscripciones_2:
    def __init__(self, master=None):
         # Ventana principal
        self.db_name = 'db\Inscripciones.db'# se accede directamente al directorio que almacena la base de datos, si no existe se crea,si existe accede a la database  
        self.win = tk.Tk(master)
        self.win.configure(background="#f7f9fd", height=600, width=800)
        self.win.geometry("800x600")
        self.win.resizable(False, False)
        self.win.title("Inscripciones de Materias y Cursos")
        # Crea los frames
        self.frm_1 = tk.Frame(self.win, name="frm_1")
        self.frm_1.configure(background="#f7f9fd", height=600, width=800)
        self.lblNoInscripcion = ttk.Label(self.frm_1, name="lblnoinscripcion")
        self.lblNoInscripcion.configure(background="#f7f9fd",font="{Arial} 11 {bold}",
                                        justify="left",state="normal",
                                        takefocus=False,text='No.Inscripción')
         #Label No. Inscripción
        self.lblNoInscripcion.place(anchor="nw", x=680, y=20)
        #Entry No. Inscripción
        self.num_Inscripcion = ttk.Entry(self.frm_1, name="num_inscripcion")
        self.num_Inscripcion.configure(justify="right")
        self.num_Inscripcion.place(anchor="nw", width=100, x=682, y=42)
        
        #Label Fecha
        self.lblFecha = ttk.Label(self.frm_1, name="lblfecha")
        self.lblFecha.configure(background="#f7f9fd", text='Fecha:')
        self.lblFecha.place(anchor="nw", x=630, y=80)
        #Entry Fecha
        self.fecha = ttk.Entry(self.frm_1, name="fecha")
        self.fecha.insert(0,"dd/mm/aaaa") #Inserta el texto por defecto "dd/mm/aaaa"
        self.fecha.configure(justify="center")
        self.fecha.place(anchor="nw", width=90, x=680, y=80)
        #Label Alumno
        self.lblIdAlumno = ttk.Label(self.frm_1, name="lblidalumno")
        self.lblIdAlumno.configure(background="#f7f9fd", text='Id Alumno:')
        self.lblIdAlumno.place(anchor="nw", x=20, y=80)
        #Label Alumno
        self.lblNombres = ttk.Label(self.frm_1, name="lblnombres")
        self.lblNombres.configure(text='Nombre(s):')
        self.lblNombres.place(anchor="nw", x=20, y=130)
        #Entry Alumno
        self.nombres_Var= ttk.Entry(self.frm_1, name="nombres")
        self.nombres = ttk.Entry(self.frm_1, name="nombres", textvariable= self.nombres_Var)
        self.nombres.place(anchor="nw", width=200, x=100, y=130)
        #Label Apellidos
        self.lblApellidos = ttk.Label(self.frm_1, name="lblapellidos")
        self.lblApellidos.configure(text='Apellido(s):')
        self.lblApellidos.place(anchor="nw", x=400, y=130)
        #Entry Apellidos
        self.apellidos_Var= ttk.Entry(self.frm_1, name="apellidos")
        self.apellidos = ttk.Entry(self.frm_1, textvariable = self.apellidos_Var)
        self.apellidos.place(anchor="nw", width=200, x=485, y=130)
        #Label Curso
        self.lblIdCurso = ttk.Label(self.frm_1, name="lblidcurso")
        self.lblIdCurso.configure(background="#f7f9fd",state="normal",text='Id Curso:')
        self.lblIdCurso.place(anchor="nw", x=20, y=185)


        #Entry Curso
        self.id_Curso = ttk.Entry(self.frm_1, name="id_curso")
        self.id_Curso.configure(justify="left", width=166)
        self.id_Curso.place(anchor="nw", width=166, x=100, y=185)
        #Label Descripción del Curso
        self.lblDscCurso = ttk.Label(self.frm_1, name="lbldsccurso")
        self.lblDscCurso.configure(background="#f7f9fd",state="normal",text='Curso:')
        self.lblDscCurso.place(anchor="nw", x=275, y=185)
        #Entry de Descripción del Curso 
        self.descripc_Curso = ttk.Entry(self.frm_1, name="descripc_curso")
        self.descripc_Curso.configure(justify="left", width=166)
        self.descripc_Curso.place(anchor="nw", width=300, x=325, y=185)
        #Label Horario
        self.lblHorario = ttk.Label(self.frm_1, name="label3")
        self.lblHorario.configure(background="#f7f9fd",state="normal",text='Horario:')
        self.lblHorario.place(anchor="nw", x=635, y=185)
        #Entry del Horario
        self.horario = ttk.Entry(self.frm_1, name="entry3")
        self.horario.configure(justify="left", width=166)
        self.horario.place(anchor="nw", width=100, x=680, y=185)

        ''' Botones  de la Aplicación'''
        #Botón Guardar
        self.btnGuardar = ttk.Button(self.frm_1, name="btnguardar",command= self.guardar_inscritos)
        self.btnGuardar.configure(text='Guardar')
        self.btnGuardar.place(anchor="nw", x=150, y=260)
        
        #Botón Editar
        self.btnEditar = ttk.Button(self.frm_1, name="btneditar",command = self.editar_curso)
        self.btnEditar.configure(text='Editar')
        self.btnEditar.place(anchor="nw", x=250, y=260)
        #Botón Eliminar
        self.btnEliminar = ttk.Button(self.frm_1, name="btneliminar", command= self.abrir_widget_eliminar)
        self.btnEliminar.configure(text='Eliminar')
        self.btnEliminar.place(anchor="nw", x=350, y=260)
        #Botón Cancelar
        self.btnCancelar = ttk.Button(self.frm_1, name="btncancelar", command = self.cancelar)
        self.btnCancelar.configure(text='Cancelar')
        self.btnCancelar.place(anchor="nw", x=450, y=260)
        #Botón Consultar
        self.btnConsultar= ttk.Button(self.frm_1, name="btnconsultar",command = self.consultar)
        self.btnConsultar.configure(text='Consultar')
        self.btnConsultar.place(anchor="nw", x=550, y=260)
        #Separador
        separator1 = ttk.Separator(self.frm_1)
        separator1.configure(orient="horizontal")
        separator1.place(anchor="nw", width=796, x=2, y=245)

        ''' Treeview de la Aplicación'''
        #Treeview
        self.tView = ttk.Treeview(self.frm_1, name="tview")
        self.tView.configure(selectmode="extended")
        #Columnas del Treeview
        self.tView_cols = ['tV_descripción','horas']
        self.tView_dcols = ['tV_descripción','horas']
        self.tView.configure(columns=self.tView_cols,displaycolumns=self.tView_dcols)
        self.tView.column("#0",anchor="w",stretch=True,width=10,minwidth=10)#with = Ancho por defecto minwith=minimo que puede tener
        self.tView.column("tV_descripción",anchor="w",stretch=True,width=200,minwidth=50)
        self.tView.column("horas",anchor="w",stretch=True,width=200,minwidth=50)
        #Cabeceras
        self.tView.heading("#0", anchor="w", text='Curso')
        self.tView.heading("tV_descripción", anchor="w", text='Descripción')
        self.tView.heading("horas", anchor="w", text='Numero de Horas')
        self.tView.place(anchor="nw", height=300, width=790, x=4, y=300)
        #Scrollbars
        self.scroll_H = ttk.Scrollbar(self.frm_1, name="scroll_h")
        self.scroll_H.configure(orient="horizontal")
        self.scroll_H.place(anchor="s", height=12, width=1534, x=15, y=595)
        self.scroll_Y = ttk.Scrollbar(self.frm_1, name="scroll_y")
        self.scroll_Y.configure(orient="vertical")
        self.scroll_Y.place(anchor="s", height=275, width=12, x=790, y=582)
        self.frm_1.pack(side="top")
        self.frm_1.pack_propagate(0)

        # Main widget
        self.mainwindow = self.win
        self.mainwindow.iconbitmap('img/picachu.ico') # como estamos trabajando en el mismo directorio, puedo acceder directamente a la carpeta que almacena la img

        #Combobox Alumno
        self.cmbx_Id_Alumno = ttk.Combobox(self.frm_1, name="cmbx_id_alumno")
        self.cmbx_Id_Alumno.place(anchor="nw", width=112, x=100, y=80)
        #Widget de eliminar
        self.widget_eliminar = None
        self.editando = False

        #centrar ventana principal
        self.centrar_win()

        #EJECUTAR 

        self.tabla_alumnos()
        self.tabla_carreras()
        self.tabla_cursos()
        self.tabla_inscritos()
        self.tabla_inscritos2()
        self.dato_prueba()#tener presente el orden de ejecucion

        #-----------------------------------------------------
        self.mostrar_Cursos()#codigo compañero

        #--------------------------------------------------
        self.cargar_combobox()

        #----------------------------------------------------------------------------------
             #lo que hace es ejecutar una busqueda en la tabla Alummos cada vez que el usario presione una tecla y llena los entrys apellidos y nombres si lo suministrado en el campo existe en la db***
        self.cmbx_Id_Alumno.bind("<KeyRelease>", self.leer_campo_combobox) 
        #-----------------------------------------------------------------------------------
          #al seleccionar algun id de la lista desplegable llena los entrys apellidos nombres y apellidos 
        self.cmbx_Id_Alumno.bind("<<ComboboxSelected>>", self.mostrar_info_alumno) 

        #-----------------------------------------------------------------------------------
          #lo que hace es ejecutar una busqueda en la tabla Cursos cada vez que el usario presione una tecla y llena el entry descripc_Curso o id_Curso
        self.descripc_Curso.bind("<KeyRelease>", self.buscar_id_curso)
        self.id_Curso.bind("<KeyRelease>", self.buscar_descripCurso)
        
        #-----------------------------------------------------------------------------------
        self.fecha.bind("<FocusIn>", self.borrar_fecha) #Al hacer click se borra el texto por defect
        self.fecha.bind("<KeyRelease>", self.autoformateo_de_fecha) #Cuando se va escribiendo se añade el slash automaticamente
        self.fecha.bind("<FocusOut>", self.validar_fecha) #Cuando se cliquea fuera del recuadro de fecha se valida que esta tenga el formato correcto***
        
        #-----------------------------------------------
        self.validar_Tview()
    



    
    def ejecutar_consulta(self, consulta, parametros=None):
        try:
            with sql.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                if parametros is None:
                    cursor.execute(consulta)  # Ejecuta la consulta sin parámetros
                    return cursor.fetchall() 
                else:
                    cursor.execute(consulta, parametros)  # Ejecuta la consulta con parámetros
                    conexion.commit()
                    return cursor.fetchall()  # Devuelve una lista de tuplas con los resultados de la consulta
        except sql.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def tabla_alumnos(self): 
        sql = """CREATE TABLE IF NOT EXISTS Alumnos(
            id_Alumno VARCHAR(20) PRIMARY KEY NOT NULL,
            id_Carrera VARCHAR(10) NOT NULL,
            Nombres VARCHAR(50),
            Apellidos VARCHAR(50),
            Fecha_Ingreso DATE NOT NULL,
            Direccion VARCHAR(60),
            Telef_Cel VARCHAR(18),
            Telef_Fijo VARCHAR(15),
            Ciudad VARCHAR(60),
            Departamento VARCHAR(60),
            FOREIGN KEY (id_Carrera) REFERENCES Carreras(Codigo_Carrera)
            
              )"""
        self.ejecutar_consulta(sql)
        
    def tabla_carreras(self):
        sql = """CREATE TABLE IF NOT EXISTS  Carreras(
            Codigo_Carrera VARCHAR(10) PRIMARY KEY ,
            Descripcion VARCHAR(100),
            Num_Semestres SMALLINT(2) ) """
        self.ejecutar_consulta(sql)
        
    def tabla_cursos(self):
        sql = """ CREATE TABLE IF NOT EXISTS  Cursos(
            Codigo_Curso VARCHAR(20) PRIMARY KEY ,
            Descrip_Curso VARCHAR(60),
            Num_Horas SMALLINT(2),
            FOREIGN KEY (Codigo_Curso) REFERENCES Inscritos(Codigo_Curso)  ) """
        self.ejecutar_consulta(sql)
        sql2 = """ INSERT OR REPLACE INTO  Cursos(
            Codigo_Curso ,
            Descrip_Curso,
            Num_Horas)
            VALUES('100b','ESTRUCTURA','100') """ # descrip_curso despues de una cantidad de caracteres mas de 20 se agrega {}, no se por que jaja
        self.ejecutar_consulta(sql2)
        
    def tabla_inscritos(self):#un punto puede generar error
        sql = """ CREATE TABLE IF NOT EXISTS  Inscritos(
            No_Inscripcion INTEGER NOT NULL, 
            Id_Alumno VARCHAR(20) NOT NULL,
            Fecha_Inscripcion DATE NOT NULL,
            Codigo_Curso VARCHAR(20) NOT NULL,
            Curso VARCHAR(60),
            Horario VARCHAR(20),
            PRIMARY KEY(No_Inscripcion,Id_Alumno,Codigo_Curso))"""
        self.ejecutar_consulta(sql)#(Id_Alumno,Fecha_Inscripcion,Codigo_Curso,Curso,Horario)
        

    #tabla para manejar los numeros de inscripciones usados
    def tabla_inscritos2(self):
        sql = """ CREATE TABLE IF NOT EXISTS  Inscritos2(
            No_Inscripcion_Usado INTEGER NOT NULL,
            PRIMARY KEY(No_Inscripcion_Usado))"""
        self.ejecutar_consulta(sql)


    def dato_prueba(self):#insercion de prueba el OR REPLACE lo que hace es ignorar la primary key y actualiza(cambia) los valores de las columnas
        sql = """INSERT OR REPLACE INTO Alumnos(id_Alumno,id_Carrera,Nombres,Apellidos,Fecha_Ingreso,
        Direccion,Telef_Cel,Telef_Fijo,Ciudad,Departamento)
        VALUES('23','A0100I','PAULA SUSANA','CANTILLO RODRIGUEZ','25/02/2023','carrera5-b11','3212345635',
        '3112841561','leticia','amazonas' )""" 

        self.ejecutar_consulta(sql)

    def cargar_combobox(self):#
        #cargarCombobox
        sql="""SELECT id_Alumno FROM Alumnos"""
        filas = self.ejecutar_consulta(sql)
        
        llave= []
        for fila in filas:
            llaves= fila[0]
            llave.append(llaves)
        self.cmbx_Id_Alumno["values"] = llave

    def limpiar_entrys(self,opcion):
        #entrys nombre,apellido
        #-----------------------------------------------------
        # esto es exclusivamente creado para las funcion buscar_id_curso
        if opcion == '1':
            self.descripc_Curso.delete(0,'end')
            self.horario.delete(0,'end')
        # esto es exclusivamente creado para las funcion buscar_descripcCurso 
        elif opcion == '2':
            self.id_Curso.delete(0,'end')
            self.horario.delete(0,'end')
        #esto es exclusivamente creado para que cuando guardar_inscritos() se realice correctamente elimine lo que haya en el entry num_Inscripcion y se ejecute entry_num_inscripcion()
        elif opcion == '3':
            self.num_Inscripcion.delete(0,'end')
        #esto es exclusivamente creado para que cuando al guardar satisfactoriamente o cuando pase todo lo contrario los entrys descrip,id_curso,horario se limpien.
        elif opcion == '4':
            self.id_Curso.delete(0,'end')
            self.descripc_Curso.delete(0,'end')
            self.horario.delete(0,'end')
        #------------------------------------------------------
        else:
            self.apellidos_Var.delete(0,'end') # tambien es posible implementar o acceder a manipular los entrys mediante StringVar()
            self.nombres_Var.delete(0,'end')

    def mostrar_num_inscripcion(self):
        id_alumno = self.cmbx_Id_Alumno.get()
        sql="""SELECT No_Inscripcion FROM Inscritos WHERE id_Alumno = ?"""
        self.ejecutar_consulta(sql,(id_alumno))

    def mostrar_info_alumno(self,event): # en self.cmbx_Id_Alumno.bind("<<ComboboxSelected>>", self.mostrar_info_alumno ) .bin espera un parametro event como parametro de la funcion, sin el event en la funcion da error
        id_alumno = self.cmbx_Id_Alumno.get()
        
        # Obtener la información del alumno seleccionado de la base de datos
        sql =f"""SELECT Nombres,Apellidos FROM Alumnos WHERE id_Alumno = ?"""
        info_alumno = self.ejecutar_consulta(sql,(id_alumno,)) # el ejecutar_consulta,fetchall retorna una lista de  tuplas, es decir info_alumno contiene = [(Nombres,Apellidos)]
        #funcion que limpie los campos
        self.limpiar_entrys(7)

        #actualiza el entry num_inscripcion si el alumno ya tiene un num_inscripcion***--------------esto es nuevo
        sql4 = f""" SELECT No_Inscripcion FROM Inscritos WHERE Id_Alumno = ? LIMIT 1"""
        num_inscripcion_existente = self.ejecutar_consulta(sql4,(id_alumno,))
        if num_inscripcion_existente:
            num_inscripcion_existente = num_inscripcion_existente[0][0]#
            self.limpiar_entrys('3')
            self.num_Inscripcion.insert(0, num_inscripcion_existente)
        else:
            self.limpiar_entrys('3')

        #funcion que cargue los campos despues de seleccionar un id_alumno
        
        nombres, apellidos = info_alumno[0]  #se procede a desempaquetar, se elige hacer esta manera porque es seguro que el id_alumno seleccionado siempre va tener nombres y apellidos,utilizando la asignación múltiple.
        self.nombres.insert(0, nombres)  # Insertar el nombre en el Entry "nombres"
        self.apellidos.insert(0, apellidos) #Insertar el apellido en el Entry "apellidos"
        self.mostrar_num_inscripcion()
    def leer_campo_combobox(self,event):#permite leer las entradas(click en alguna tecla) y buscar mediante el id si existe el alumno en la base de datos 
        id_alumno = self.cmbx_Id_Alumno.get()

        sql =f"""SELECT Nombres,Apellidos FROM Alumnos WHERE id_Alumno = ?"""

        #se valida si la entrada son numeros
        
        info_alumno = self.ejecutar_consulta(sql,(id_alumno,)) # el ejecutar_consulta,fetchall retorna una lista de  tuplas, es decir info_alumno contiene = [(Nombres,Apellidos)]
        #funcion que limpie los campos
        self.limpiar_entrys(7)
        if info_alumno:# si los numeros suministrados existen como id , se ejecuta la siguiente isntruccion
            nombres, apellidos = info_alumno[0]#se procede a desempaquetar, se elige hacer esta manera porque es seguro que el id_alumno seleccionado siempre va tener nombres y apellidos,utilizando la asignación múltiple
            self.nombres.insert(0, nombres)  # Insertar el nombre en el Entry "nombres"
            self.apellidos.insert(0, apellidos) #Insertar el apellido en el Entry "apellidos"
        else:
            self.limpiar_entrys(7)

    def centrar_win(self):
        self.mainwindow.update_idletasks()#indagar mas sobre this
        width = self.mainwindow.winfo_width()
        height = self.mainwindow.winfo_height()
        x = (self.mainwindow.winfo_screenwidth() // 2) - (width // 2)
        y = (self.mainwindow.winfo_screenheight() // 2) - (height // 2)
        self.mainwindow.geometry(f"{width}x{height}+{x}+{y}")


#------------------------------------------------------------------------------------------------------------------------------------------
    #llenar campos entrys con el mismo enfoque del combobox(llenar campos) pero con "<KeyRelease>" como primer parametro de .bind
    def buscar_descripCurso(self,event):
        id_curso = self.id_Curso.get()
        sql = f"""SELECT Descrip_Curso,Num_Horas FROM Cursos WHERE Codigo_Curso = ? """ #importante que las comillas vayan en {} porque si la entrada son ejemplo 10 y b , sql lo tomara como entero+string y id_curso no admite numeros admie strings
        info_alumno = self.ejecutar_consulta(sql,(id_curso,)) # el ejecutar_consulta,fetchall retorna una lista de  tuplas, es decir info_alumno contiene = [(Nombres,Apellidos)]
        
        self.limpiar_entrys('1')
        if info_alumno:#si el id_curso es encontrado cumple la condicion y luego se le asignara el valor a descripc_Curso,num_horas ,es decir, la tupla que retorno ejecutar_consulta() estará almacenada en descripc_Curso,num_horas
            descripc_Curso,num_horas= info_alumno[0]  #se procede a desempaquetar, se elige hacer de esta manera porque es seguro que al ejecutar la consulta el fetchall retorna [(descripc_curso,Num_Horas)], se usa asignacion multiple
            self.descripc_Curso.insert(0, descripc_Curso) 
            self.horario.insert(0,num_horas)
         
        else:
            self.limpiar_entrys('1')
        
    def buscar_id_curso(self,event):
        descripc_Curso = self.descripc_Curso.get()
        sql = f"""SELECT Codigo_Curso,Num_Horas FROM Cursos WHERE Descrip_Curso = ?"""

        info_alumno = self.ejecutar_consulta(sql,(descripc_Curso,)) # el ejecutar_consulta,fetchall retorna una lista de  tuplas, es decir info_alumno contiene = [(Nombres,Apellidos)]
        self.limpiar_entrys('2')
        if info_alumno:
            codigo_curso,num_horas = info_alumno[0]#se procede a desempaquetar, se elige hacer de esta manera porque es seguro que al ejecutar la consulta el fetchall retorna [(descripc_curso,Num_Horas)], se usa asignacion multiple
            self.id_Curso.insert(0,codigo_curso)
            self.horario.insert(0,num_horas)

        else:
            self.limpiar_entrys('2')


#--------------------------------------------------------------------------------------------------------------------------
    #funciones para guardar inscritos***
    def guardar_inscritos(self):
        id_alumno = self.cmbx_Id_Alumno.get()
        fecha = self.fecha.get()
        codigo_curso = self.id_Curso.get()
        curso = self.descripc_Curso.get()
        horario = self.horario.get()
        if self.validar_campos_completos(id_alumno,fecha,codigo_curso):
            if self.validar_doble_inscripcion(id_alumno,codigo_curso):
                messagebox.showerror("Guardar Inscripcion", f"ERROR, el/la estudiante: {self.apellidos.get()} ya tiene inscrita la materia: {self.descripc_Curso.get() }.") 
                self.limpiar_entrys('4')                
            else:
                sql = f""" SELECT No_Inscripcion FROM Inscritos WHERE Id_Alumno = ? LIMIT 1"""# para verificar si el alumno ya tiene un numero de inscripcion asignado
                num_inscripcion_existente = self.ejecutar_consulta(sql,(id_alumno,))

                if  num_inscripcion_existente:
                    self.guardar_Mismo_No_Inscripcion_Tabla_Inscritos(num_inscripcion_existente,id_alumno,fecha,codigo_curso,curso,horario) 
                else:
                        sql2 = """ SELECT MAX(No_Inscripcion)
                        FROM Inscritos"""
                        num_max_inscripcion = self.ejecutar_consulta(sql2)
                        
                        sql4= """ SELECT MAX(No_Inscripcion_Usado)
                        FROM Inscritos2"""
                        num_max_inscripcion2 = self.ejecutar_consulta(sql4)
                         
                        if num_max_inscripcion[0][0]:# se accede a [(num_max_inscripcion,),] y si el valor es no None se le suma 1
                            num_inscripcion = num_max_inscripcion[0][0] + 1 
                            
                            if num_max_inscripcion2[0][0]:
                                num_inscripcion = self.validar_No_Usado(num_max_inscripcion2[0][0],num_inscripcion) 

                            else:
                                pass           
                        else:
                            num_inscripcion = 1  
                            num_inscripcion = self.validar_No_Usado(num_max_inscripcion2[0][0],num_inscripcion)
                            
                        self.guardar_Nueva_Inscripcion(num_inscripcion, id_alumno, fecha, codigo_curso, curso, horario)
        else:
            messagebox.showerror("Guardar Inscripcion", "Por favor complete todos los campos.")

    def validar_campos_completos(self,id_alumno,fecha,codigo_curso):
        if id_alumno and fecha and codigo_curso and self.validar_fecha():
            return True
        else:
            return False

    def validar_doble_inscripcion(self,id_alumno,codigo_curso):
        #si el id_alumno existe con el codigo_curso ,return True
        id_alumno = id_alumno
        codigo_curso = codigo_curso

        sql = f""" SELECT Codigo_Curso FROM Inscritos WHERE Id_Alumno = ? """
        info_inscripciones = self.ejecutar_consulta(sql,(id_alumno,))
        #print(info_inscripciones)
        
        for curso in info_inscripciones:# se itera en cada tupla retornada por ejecutar_consulta()
            if curso[0] == codigo_curso: # se compara la posicion sub0 de la tupla la cual esta siendo iterada
             return True  # El alumno ya está inscrito en este curso
            else:
                return False  # El alumno no está inscrito en este curso

    def validar_No_Usado(self,num_max_inscripcion2,num_inscripcion):
        sql3= """SELECT No_Inscripcion_Usado FROM Inscritos2"""
        num_inscripciones_usadas= self.ejecutar_consulta(sql3)
        
        for no_Usado in num_inscripciones_usadas:# se itera en cada tupla retornada por ejecutar_consulta()
            if no_Usado[0] == num_inscripcion and num_max_inscripcion2:# se compara la posicion sub0 de la tupla la cual esta siendo iterada..
                num_inscripcion = num_max_inscripcion2 + 1##
            else: 
                pass
        return num_inscripcion
        
    def guardar_Nueva_Inscripcion(self, num_inscripcion, id_alumno, fecha, codigo_curso, curso, horario):
        sql2 = f""" INSERT INTO Inscritos(No_Inscripcion,Id_Alumno,Fecha_Inscripcion,Codigo_Curso,Curso,Horario)
                        VALUES(?,?,?,?,?,?) """
        self.ejecutar_consulta(sql2,(num_inscripcion,id_alumno,fecha,codigo_curso,curso,horario))
        messagebox.showinfo("Guardar Inscripcion", "La inscripcion se guardo satisfactoriamente.")
        self.limpiar_entrys('4')
        self.limpiar_entrys('3')#limpia el entry num_inscripcion para que se actualice correctamente
        self.num_Inscripcion.insert(0,num_inscripcion) 
        
    def guardar_Mismo_No_Inscripcion_Tabla_Inscritos(self,num_inscripcion_existente,id_alumno,fecha,codigo_curso,curso,horario):
        num_inscripcion_existente = num_inscripcion_existente[0][0]#[(num_inscripcion,)] se extrae el num_inscripcion
        sql3 = f""" INSERT INTO Inscritos(No_Inscripcion,Id_Alumno,Fecha_Inscripcion,Codigo_Curso,Curso,Horario)
                        VALUES(?,?,?,?,?,?) """
        self.ejecutar_consulta(sql3,(num_inscripcion_existente,id_alumno,fecha,codigo_curso,curso,horario))
        messagebox.showinfo("Guardar Inscripcion", "La inscripcion se guardo satisfactoriamente.")
        self.limpiar_entrys('4')
        self.limpiar_entrys('3')#limpia el entry num_inscripcion para que se actualice correctamente
        self.num_Inscripcion.insert(0,num_inscripcion_existente) 

#------------------------------------------------------------------------------------------------------------------------------------------
    #estudiar codigo del compañero***  
    def limpia_TreeView(self):
         tabla = self.tView.get_children()
         for element in tabla:
              self.tView.delete(element)
    
    def mostrar_Cursos(self):
        self.limpia_TreeView()
        #Seleccionar los datos de la BD
        #parametros = (self.id_Curso.get(),)
        query = """SELECT * FROM Cursos ORDER BY Codigo_Curso DESC"""
        db_ColumnasCursos = self.ejecutar_consulta(query)

        #Insertar los datos en la tabla de la pantalla
        for row in db_ColumnasCursos:
            self.tView.insert('',0,text= row[0],values = [row[1],row[2]])
            print(row)

    def mostrar_info_cursos(self,event):
        # Obtener el índice seleccionado
        if self.tView.selection():
            selected_item = self.tView.selection()[0]
            # Obtener los valores de la fila seleccionada
            # Rellenar los campos de entrada
            self.id_Curso.delete(0, 'end')
            self.id_Curso.insert(0, self.tView.item(selected_item)['text'])  
            self.descripc_Curso.delete(0, 'end')
            self.descripc_Curso.insert(0, self.tView.item(selected_item)['values'][0])
    
    def validar_entry(self,funcion):
        return len(funcion.get()) != 0
    
    def agregar_curso(self):
        if self.validar_entry(self.id_Curso):
            codigo_curso = self.id_Curso.get()
            curso = self.descripc_Curso.get()
            hora = self.horario.get()
            nuevo_curso = (codigo_curso, curso, hora)
            self.tView.insert('',0,text= nuevo_curso[0],values = [nuevo_curso[1],nuevo_curso[2]])
            
#------------------------------------------------------------------------------------------------------------------------------------------   
    #estudiar codigo de compañero***
    #Funciones para el entry fecha
    def borrar_fecha(self, event):
        self.fecha.delete(0, 'end')

    def validar_fecha(self, event=None):
        fecha = self.fecha.get()

        if self.validar_formato_fecha(fecha):
            dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #Lista con los días máximos permitidos por mes
            
            dia, mes, year = map(int, fecha.split('/'))

            #Verificar si es un año bisiesto
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                dias_por_mes[1] = 29  #Febrero tiene 29 días en año bisiesto

            #Verificar si el mes es válido
            if mes < 1 or mes > 12:
                messagebox.showerror("Formato de fecha invalido", "El mes es inválido.")
                return
            #Verificar si el día es válido
            if dia < 1 or dia > dias_por_mes[mes - 1]:
                messagebox.showerror("Formato de fecha invalido", "El dia es inválido.")
                return
            #Verificar que el año sea 2024
            if year != 2024:
                messagebox.showerror("Formato de fecha invalido", "Solo se admiten incripciones de este año")
                return
            return True
        else:
            self.borrar_fecha(None)
            self.fecha.insert(0,"dd/mm/aaaa")
            messagebox.showerror("Formato de fecha invalido", "El formato de fecha debe ser DD/MM/AAA")
            return False

    def validar_formato_fecha(self, fecha):
        #Verificar si la fecha tiene el formato correcto (DD/MM/YYYY)
        if len(fecha) != 10 or fecha[2] != '/' or fecha[5] != '/':
            return False

        #Verificar si los componentes de la fecha son números
        try:
            dia, mes, year = map(int, fecha.split('/'))
        except ValueError:
            return False

        #Verificar si el año es un número de 4 dígitos
        if len(str(year)) != 4:
            return False

        return True
    
    def autoformateo_de_fecha(self, event):
        fecha = self.fecha.get()
        print(fecha[-1])
        if fecha[-1] == " ":
            self.fecha.delete(len(fecha)-1, 'end')
        if len(fecha) == 2 or len(fecha) == 5:
            self.fecha.insert(len(fecha),"/")
        if len(fecha) >= 10:
            self.fecha.delete(10,'end')
    
#------------------------------------------------------------------------------------------------------------------------------------------
    #Funciones para el Boton Eliminar
    def abrir_widget_eliminar(self):
        if self.widget_eliminar is None:
            self.widget_eliminar = tk.Toplevel(self.win)
            self.widget_eliminar.title("Eliminar Datos")

            for i in range(12):
                self.widget_eliminar.rowconfigure(i, weight=1, minsize=20)

            for j in range(5):
                self.widget_eliminar.columnconfigure(j, weight=1, minsize=40)
            
            tk.Label(self.widget_eliminar, text="Seleccione una opción:").grid(row=1, column=1, columnspan=3)

            self.widget_eliminar.geometry("300x200")

            window_width = self.widget_eliminar.winfo_reqwidth()
            window_height = self.widget_eliminar.winfo_reqheight()
            position_right = int(self.widget_eliminar.winfo_screenwidth()/2 - window_width/2)
            position_down = int(self.widget_eliminar.winfo_screenheight()/2 - window_height/2)
            self.widget_eliminar.geometry("+{}+{}".format(position_right, position_down))
            
            tipo_de_eliminacion = tk.IntVar()
            opcion1 = tk.Radiobutton(self.widget_eliminar, text="Borrar un curso", variable=tipo_de_eliminacion, value=1)
            opcion2 = tk.Radiobutton(self.widget_eliminar, text="Borrar registro", variable=tipo_de_eliminacion, value=2)
            
            opcion1.grid(row=3, column=1, columnspan=3, sticky='w')
            opcion2.grid(row=4, column=1, columnspan=3, sticky='w')

            btn_aceptar = tk.Button(self.widget_eliminar, text="Aceptar", command=lambda: self.eliminar_datos(tipo_de_eliminacion))
            btn_cancelar = tk.Button(self.widget_eliminar, text="Cancelar", command=self.cerrar_widget_eliminar)
            btn_aceptar.grid(row=7, column=1)
            btn_cancelar.grid(row=7, column=3)

            self.widget_eliminar.rowconfigure(7, weight=1)
            self.widget_eliminar.columnconfigure(5, weight=1)

            self.widget_eliminar.protocol("WM_DELETE_WINDOW", self.cerrar_widget_eliminar) #Corrige el bug que ocurria al cerrar la ventana con la x


    def eliminar_datos(self, opcion):
        if opcion.get() == 1:
            self.eliminar_curso()
        elif opcion.get() == 2:
            self.eliminar_registro()
        else:
            messagebox.showerror("Error al Eliminar", "Debe seleccionar al menos una opcion")

    def eliminar_curso(self):
        id_alumno = self.cmbx_Id_Alumno.get()
        codigo_curso = self.id_Curso.get()
        #Verifica que los datos esten completos
        if id_alumno.strip() == "" or codigo_curso.strip() == "":
            messagebox.showerror("Campos incompletos", "Verifique que los campos id_alumno y id_curso no esten en blanco")
            return
        
        #Si pasa la verificación de campos, verifica que el alumno este en el curso
        if self.validar_doble_inscripcion(id_alumno,codigo_curso): 
            try:
                #Intenta eliminar el alumno
                sql = """DELETE FROM Inscritos WHERE Id_Alumno = ? AND Codigo_Curso = ?"""
                self.ejecutar_consulta(sql,(id_alumno, codigo_curso))
                self.limpiar_entrys('4')
                self.cerrar_widget_eliminar()
                messagebox.showinfo("Eliminacion Correcta","La inscripción al curso fue eliminada correctamente")
                self.consultar()
            except Exception  as e: #Si hay un error eliminando el alumno, lo muestra en pantalla
                messagebox.showerror("Error al eliminar", str(e))
        else: #El alumno no esta inscrito en el curso
            messagebox.showerror("Error al eliminar", "El alumno no esta inscrito a este curso")


    def eliminar_registro(self):
        id_alumno = self.cmbx_Id_Alumno.get()
        if id_alumno.strip() == "":
            messagebox.showerror("Campos incompletos", "Verifique que los campos id_alumno y id_curso no esten en blanco")
            return
        try: #Intenta eliminar el alumno
            sql = """DELETE FROM Inscritos WHERE Id_Alumno = ?"""
            self.ejecutar_consulta(sql,(id_alumno,))
            self.limpiar_entrys('4')
            self.cerrar_widget_eliminar()
            self.obtener_No_Inscripcion_del_alumno(id_alumno)
            messagebox.showinfo("Eliminacion Correcta","Se han eliminado todos los cursos")
            self.consultar()
        except Exception  as e: #Si hay un error eliminando el alumno, lo muestra en pantalla
            messagebox.showerror("Error al eliminar", str(e))

    def cerrar_widget_eliminar(self):
        if self.widget_eliminar is not None:
            self.widget_eliminar.destroy()
            self.widget_eliminar = None

    #antes de eliminar la inscripcion total del alumno, se procede a acceder a su numero de inscripción para que no vuelva a ser usada
    def obtener_No_Inscripcion_del_alumno(self, id_alumno):
        sql2 = "SELECT No_Inscripcion FROM Inscritos WHERE Id_Alumno = ? LIMIT 1"
        no_Inscripcion_A_Eliminar = self.ejecutar_consulta(sql2, (id_alumno,))
        if no_Inscripcion_A_Eliminar:
            no_Inscripcion_A_Eliminar = no_Inscripcion_A_Eliminar[0][0]
            sql3 = "INSERT INTO Inscritos2(No_Inscripcion_Usado) VALUES(?)"
            self.ejecutar_consulta(sql3,(id_alumno,))
            
#----------------------------------------------------------------------------------------------------------------------------------------------------
    #Función para vaciar el treeview
    def limpiar_columnas_tView(self):
         #get_children selecciona todas las filas y el for las recorre y se van eliminando 
         for column in self.tView.get_children():
            self.tView.delete(column)
         self.tView_cols = ()
         self.tView_dcols = ()

#------------------------------------------------------------------------------------------------------------------------------------------------------
    #Función para cambiar las columnas del tview para el boton consultar
    def columnas_consultar(self, nuevas_columnas):
        # Agregar nuevas columnas al Treeview
        self.limpiar_columnas_tView()
        self.tView_cols = (nuevas_columnas)
        self.tView_dcols = (nuevas_columnas)
        self.tView.configure(columns=self.tView_cols,displaycolumns=self.tView_dcols)
        #Recorre las columnas y asigna su nombre y tamaño 
        for col in self.tView_cols:
            self.tView.heading(col, anchor="w", text=(f'{col}'))
            self.tView.column(col,anchor='w',stretch=True,width=217,minwidth=217)

#------------------------------------------------------------------------------------------------------------------------------------------------------
    #Función para rellenar los campos con los valores de los inscritos 
    def mostrar_info_inscritos(self,event):
        # Obtener el índice seleccionado
        if self.tView.selection():
            selected_item = self.tView.selection()[0]
            # Obtener los valores de la fila seleccionada
            # Rellenar los campos de entrada
            self.id_Curso.delete(0, 'end')
            self.id_Curso.insert(0, self.tView.item(selected_item)['text'])  
            self.descripc_Curso.delete(0, 'end')
            self.descripc_Curso.insert(0, self.tView.item(selected_item)['values'][0])

#------------------------------------------------------------------------------------------------------------------------------------------------------
    #Función para mostrar los inscritos con el boton consultar
    def mostrar_Inscritos(self):
        self.limpia_TreeView()
        #Seleccionar los datos de la BD
        #Obtiene el numero de inscripcion
        inscripcion = self.num_Inscripcion.get()
        #busqueda en base al numero de inscripcion obtenido 
        query = """SELECT * FROM Inscritos WHERE No_Inscripcion = ? ORDER BY Codigo_Curso DESC"""
        self.db_ColumnasCursos = self.ejecutar_consulta(query,(inscripcion))

        #Insertar los datos en la tabla de la pantalla
        if self.db_ColumnasCursos is None:
             messagebox.showerror("Error al consultar", "Indique el número de inscripción")
        else:
            for row in self.db_ColumnasCursos:
                self.tView.insert('',0,text= row[3],values = [row[1],row[4],row[5]])
                print(row)
 

#------------------------------------------------------------------------------------------------------------------------------------------------------
    #Función del boton consultar
    def consultar(self):
        #Se limpian los valores del treeview
        for item in self.tView.get_children():
            self.tView.delete(item)
        
        # Llenar el TreeView con información de inscritos
        columas_inscritos=('ID del estudiante','Curso','Horario')
        #self.limpiar_columnas_tview()
        self.columnas_consultar(columas_inscritos)        
        self.mostrar_Inscritos()
        self.validar_Tview()

#------------------------------------------------------------------------------------------------------------------------------------------------------
    #Función para validar que funcion debe ser usada segun la cantidad de columnas
    def validar_Tview(self):
        num_columnas = len(self.tView.get_children())
        if num_columnas > 3:
            self.tView.bind("<<TreeviewSelect>>", self.mostrar_info_inscritos)

        else: 
            self.tView.bind("<<TreeviewSelect>>", self.mostrar_info_cursos)
     
#------------------------------------------------------------------------------------------------------------------------------------------------------
    #Función del botón editar
    def editar_curso(self):
        self.validar_Tview()
        id_alumno = self.cmbx_Id_Alumno.get()
        id_curso = self.id_Curso.get()
        descripc_Curso = self.descripc_Curso.get()
        horario = self.horario.get()

        if id_curso.strip() == "" or descripc_Curso.strip() == "" or horario.strip() == "":
            messagebox.showerror("Error al Editar","Asegurese de tener los campos de curso completos")
            self.consultar()
            return
        
        if not self.validar_doble_inscripcion(id_alumno, id_curso): 
            messagebox.showerror("Error al Editar","No puede editar un curso al que no pertenece")
            return
        
        if not self.editando:
            self.bloquear_campos(self.id_Curso,self.descripc_Curso)
            self.editando = True
            return
        
        if self.editando:
            try:
                query = """UPDATE Inscritos SET Horario = ? WHERE id_Alumno = ? AND codigo_Curso = ?"""
                self.ejecutar_consulta(query,(horario, id_alumno,id_curso))
                self.desbloquear_campos(self.id_Curso,self.descripc_Curso)
                self.editando = False
                messagebox.showinfo("Edicion Correcta", "El curso se ha editado correctamente")
                self.consultar()
            except:
                messagebox.showerror("Error de Edicion", "Error editando el curso, intente mas tarde")

    def bloquear_campos(self,*entries):
        print(entries)
        try:
            for entry in entries:
                entry.config(state='disabled')
        except:
            messagebox.showerror("ERROR", "Error desconocido")
    
    def desbloquear_campos(self,*entries):
        try: 
            for entry in entries:
                entry.config(state='normal')
        except:
            messagebox.showerror("ERROR", "Error desconocido")

#----------------------------------------------------------------------------------------------------------
    def columnas_cursos(self,nuevas_columnas):
         # Agregar nuevas columnas al Treeview
        self.limpiar_columnas_tView()
        self.tView_cols = (nuevas_columnas)
        self.tView_dcols = (nuevas_columnas)
        self.tView.configure(columns=self.tView_cols,displaycolumns=self.tView_dcols)
        #Recorre las columnas y asigna su nombre y tamaño 
        for col in self.tView_cols:
            self.tView.heading(col, anchor="w", text=(f'{col}'))
            self.tView.column(col,anchor='w',stretch=True,width=74,minwidth=200)

    def cancelar(self):
        col_cursos = ['Descripción','Numero de horas']
        self.limpiar_columnas_tView()
        self.columnas_cursos(col_cursos)
        self.mostrar_Cursos()







        
            
                

        
            

                
            
            


        





        




       
    def run(self):
        self.mainwindow.mainloop()
    


    ''' A partir de este punto se deben incluir las funciones
     para el manejo de la base de datos '''

if __name__ == "__main__":
    app = Inscripciones_2()
    app.run()