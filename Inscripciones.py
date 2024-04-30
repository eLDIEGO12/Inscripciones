import tkinter as tk 
import tkinter.ttk as ttk
import sqlite3 as sql
from tkinter import messagebox



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
        self.nombres_Var= tk.StringVar()#
        self.nombres = ttk.Entry(self.frm_1, name="nombres", textvariable= self.nombres_Var)
        self.nombres.place(anchor="nw", width=200, x=100, y=130)
        #Label Apellidos
        self.lblApellidos = ttk.Label(self.frm_1, name="lblapellidos")
        self.lblApellidos.configure(text='Apellido(s):')
        self.lblApellidos.place(anchor="nw", x=400, y=130)
        #Entry Apellidos
        self.apellidos_Var= tk.StringVar()#
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
        self.lblHorario.configure(background="#f7f9fd",state="normal",text='Hora:')
        self.lblHorario.place(anchor="nw", x=635, y=185)
        #Entry del Horario
        self.horario = ttk.Entry(self.frm_1, name="entry3")
        self.horario.configure(justify="left", width=166)
        self.horario.place(anchor="nw", width=100, x=680, y=185)

        ''' Botones  de la Aplicación'''
        #Botón Guardar
        self.btnGuardar = ttk.Button(self.frm_1, name="btnguardar",command= self.guardar_inscritos)
        self.btnGuardar.configure(text='Guardar')
        self.btnGuardar.place(anchor="nw", x=200, y=260)
        
        #Botón Editar
        self.btnEditar = ttk.Button(self.frm_1, name="btneditar")
        self.btnEditar.configure(text='Editar')
        self.btnEditar.place(anchor="nw", x=300, y=260)
        #Botón Eliminar
        self.btnEliminar = ttk.Button(self.frm_1, name="btneliminar")
        self.btnEliminar.configure(text='Eliminar')
        self.btnEliminar.place(anchor="nw", x=400, y=260)
        #Botón Cancelar
        self.btnCancelar = ttk.Button(self.frm_1, name="btncancelar")
        self.btnCancelar.configure(text='Cancelar')
        self.btnCancelar.place(anchor="nw", x=500, y=260)
        #Separador
        separator1 = ttk.Separator(self.frm_1)
        separator1.configure(orient="horizontal")
        separator1.place(anchor="nw", width=796, x=2, y=245)

        ''' Treeview de la Aplicación'''
        #Treeview
        self.tView = ttk.Treeview(self.frm_1, name="tview")
        self.tView.configure(selectmode="extended")
        #Columnas del Treeview
        self.tView_cols = ['tV_descripción']
        self.tView_dcols = ['tV_descripción']
        self.tView.configure(columns=self.tView_cols,displaycolumns=self.tView_dcols)
        self.tView.column("#0",anchor="w",stretch=True,width=10,minwidth=10)
        self.tView.column("tV_descripción",anchor="w",stretch=True,width=200,minwidth=50)
        #Cabeceras
        self.tView.heading("#0", anchor="w", text='Curso')
        self.tView.heading("tV_descripción", anchor="w", text='Descripción')
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

        #centrar ventana principal
        self.centrar_win()

        #EJECUTAR 

        self.tabla_alumnos()
        self.tabla_carreras()
        self.tabla_cursos()
        self.tabla_inscritos()
        self.dato_prueba()#tener presente el orden de ejecucion

        #-----------------------------------------------------
        self.mostrar_Cursos()#codigo compañero
        #--------------------------------------------------

        self.cargar_combobox()


        #--------------------------------------------------------------------------------
           #lee y actualiza el entry No_Inscripcion
        self.entry_num_inscripcion()
        #--------------------------------------------------------------------------------


        #----------------------------------------------------------------------------------
             #lo que hace es ejecutar una busqueda en la tabla Alummos cada vez que el usario presione una tecla y llena los entrys apellidos y nombres si lo suministrado en el campo existe en la db***
        self.cmbx_Id_Alumno.bind("<KeyRelease>", self.leer_campo_combobox) 
        #----------------------------------------------------------------------------------


        #-----------------------------------------------------------------------------------
          #al seleccionar algun id de la lista desplegable llena los entrys apellidos nombres y apellidos 
        self.cmbx_Id_Alumno.bind("<<ComboboxSelected>>", self.mostrar_info_alumno) 
        #-----------------------------------------------------------------------------------
        

        self.tView.bind("<<TreeviewSelect>>", self.mostrar_info_cursos)


        #-----------------------------------------------------------------------------------
          #lo que hace es ejecutar una busqueda en la tabla Cursos cada vez que el usario presione una tecla y llena el entry descripc_Curso o id_Curso
        self.descripc_Curso.bind("<KeyRelease>", self.buscar_id_curso)
        self.id_Curso.bind("<KeyRelease>", self.buscar_descripCurso)
        #-----------------------------------------------------------------------------------


        #---------------------------------------------
          #codigo compañero***
        self.fecha.bind("<Key>", self.validar_fecha)
        #-----------------------------------------------
        



    
    def ejecutar_consulta(self, consulta):
        try:
            with sql.connect(self.db_name) as conexion:
                cursor = conexion.cursor()
                cursor.execute(consulta) #se ejecutó el sql 
                conexion.commit()
                return cursor.fetchall()#devuleve una tupla de todas las filas de la columna(id_Alumn) ,(especifico par el combobox) ,pero se puede complementar para otras funciones,ejemplo : en la funcion mostrar_info_alumno 
        except sql.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def tabla_alumnos(self): #sin el () en el conexion generaria un error dado que el .cursor no se ejecuta, es decir, el cursor.execute no tendrá presente el .cursor

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
            No_Inscripcion INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_Alumno VARCHAR(20) NOT NULL,
            Fecha_Inscripcion DATE NOT NULL,
            Codigo_Curso VARCHAR(20) NOT NULL) """
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
            self.descripc_Curso.delete(0,tk.END)
            self.horario.delete(0,tk.END)

        # esto es exclusivamente creado para las funcion buscar_descripcCurso 
        elif opcion == '2':
            self.id_Curso.delete(0,tk.END)
            self.horario.delete(0,tk.END)
        #-------------------------------------------------

        #---------------------------------------------------
          #esto es exclusivamente creado para que cuando guardar_inscritos() se realice correctamente elimine lo que haya en el entry num_Inscripcion y se ejecute entry_num_inscripcion()
        elif opcion == '3':
            self.num_Inscripcion.delete(0,tk.END)
        #--------------------------------------------------------
        
        #-------------------------------------------------------
           #esto es exclusivamente creado para que cuando al guardar satisfactoriamente o cuando pase todo lo contrario los entrys descrip,id_curso,horario se limpien.
        elif opcion == '4':
            self.id_Curso.delete(0,tk.END)
            self.descripc_Curso.delete(0,tk.END)
            self.horario.delete(0,tk.END)
        #------------------------------------------------------
        else:
            self.apellidos_Var.set("") # tambien es posible implementar o acceder a manipular los entrys mediante StringVar()
            self.nombres_Var.set("")

    def mostrar_info_alumno(self,event): # en self.cmbx_Id_Alumno.bind("<<ComboboxSelected>>", self.mostrar_info_alumno ) .bin espera un parametro event como parametro de la funcion, sin el event en la funcion da error
        id_alumno = self.cmbx_Id_Alumno.get()
        
        # Obtener la información del alumno seleccionado de la base de datos
        sql =f"""SELECT Nombres,Apellidos FROM Alumnos WHERE id_Alumno = '{id_alumno}'"""
        info_alumno = self.ejecutar_consulta(sql) # el ejecutar_consulta,fetchall retorna una lista de  tuplas, es decir info_alumno contiene = [(Nombres,Apellidos)]
        #funcion que limpie los campos
        self.limpiar_entrys(7)

        #funcion que cargue los campos despues de seleccionar un id_alumno
        
        nombres, apellidos = info_alumno[0]  #se procede a desempaquetar, se elige hacer esta manera porque es seguro que el id_alumno seleccionado siempre va tener nombres y apellidos,utilizando la asignación múltiple.
        self.nombres.insert(0, nombres)  # Insertar el nombre en el Entry "nombres"
        self.apellidos.insert(0, apellidos) #Insertar el apellido en el Entry "apellidos"

    def leer_campo_combobox(self,event):#permite leer las entradas(click en alguna tecla) y buscar mediante el id si existe el alumno en la base de datos 
        id_alumno = self.cmbx_Id_Alumno.get()

        sql =f"""SELECT Nombres,Apellidos FROM Alumnos WHERE id_Alumno = '{id_alumno}'"""

        #se valida si la entrada son numeros
        
        info_alumno = self.ejecutar_consulta(sql) # el ejecutar_consulta,fetchall retorna una lista de  tuplas, es decir info_alumno contiene = [(Nombres,Apellidos)]
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
        sql = f"""SELECT Descrip_Curso,Num_Horas FROM Cursos WHERE Codigo_Curso = '{id_curso}'""" #importante que las comillas vayan en {} porque si la entrada son ejemplo 10 y b , sql lo tomara como entero+string y id_curso no admite numeros admie strings
        info_alumno = self.ejecutar_consulta(sql) # el ejecutar_consulta,fetchall retorna una lista de  tuplas, es decir info_alumno contiene = [(Nombres,Apellidos)]
        #funcion que limpie los campos
        self.limpiar_entrys('1')
        if info_alumno:#si el id_curso es encontrado cumple la condicion y luego se le asignara el valor a descripc_Curso,num_horas ,es decir, la tupla que retorno ejecutar_consulta() estará almacenada en descripc_Curso,num_horas
            descripc_Curso,num_horas= info_alumno[0]  #se procede a desempaquetar, se elige hacer de esta manera porque es seguro que al ejecutar la consulta el fetchall retorna [(descripc_curso,Num_Horas)], se usa asignacion multiple
            self.descripc_Curso.insert(0, descripc_Curso) 
            self.horario.insert(0,num_horas)
         
        else:
            self.limpiar_entrys('1')
        
    def buscar_id_curso(self,event):
        descripc_Curso = self.descripc_Curso.get()
        sql = f"""SELECT Codigo_Curso,Num_Horas FROM Cursos WHERE Descrip_Curso ='{descripc_Curso}'"""

        info_alumno = self.ejecutar_consulta(sql)
        self.limpiar_entrys('2')
        if info_alumno:
            codigo_curso,num_horas = info_alumno[0]#se procede a desempaquetar, se elige hacer de esta manera porque es seguro que al ejecutar la consulta el fetchall retorna [(descripc_curso,Num_Horas)], se usa asignacion multiple
            self.id_Curso.insert(0,codigo_curso)
            self.horario.insert(0,num_horas)

        else:
            self.limpiar_entrys('2')


#--------------------------------------------------------------------------------------------------------------------------
    #guardar informacion en la tabla inscritos***
    def guardar_inscritos(self):
        #validar que los campos esten con la informacion correcta (id_exisa,fechavalidad,materias existan)(con ventana emergente si falta informacion,hay columnas que no deben ser null)
        #validar si el estudiante ya inscribio esa materia
        #que hacer con el numero de inscripcion = autoincrement
        id_alumno = self.cmbx_Id_Alumno.get()
        fecha = self.fecha.get()
        codigo_curso = self.id_Curso.get()

        if self.validar_campos_completos(id_alumno,fecha,codigo_curso):
            sql2 = f""" INSERT INTO Inscritos(Id_Alumno,Fecha_Inscripcion,Codigo_Curso)
            VALUES('{id_alumno}','{fecha}','{codigo_curso}') """

            if self.validar_doble_inscripcion(id_alumno,codigo_curso):
                messagebox.showerror("Guardar Inscripcion", f"ERROR, el/la estudiante: {self.apellidos.get()} ya tiene inscrita la materia: {self.descripc_Curso.get() }.") 
                self.limpiar_entrys('4')

        
            else:
                try:
                    self.ejecutar_consulta(sql2)
                    messagebox.showinfo("Guardar Inscripcion", "La inscripcion se guardo satisfactoriamente.")
                    self.limpiar_entrys('4')
                    self.limpiar_entrys('3')#limpia el entry num_inscripcion para que se actualice correctamente
                    self.entry_num_inscripcion()
            
            
                except Exception as e:
                    messagebox.showerror("Guardar Inscripcion", f"Ocurrió un error al guardar los inscritos: {e}")
        else:
            messagebox.showerror("Guardar Inscripcion", "Por favor complete todos los campos.")


    def validar_campos_completos(self,id_alumno,fecha,codigo_curso):

        if id_alumno and fecha and codigo_curso:
            return True
        else:
            return False
   
    #validar que el estudiante no escriba la misma materia
    def validar_doble_inscripcion(self,id_alumno,codigo_curso):
        #si el id_alumno existe con el codigo_curso ,return True
        id_alumno = id_alumno
        codigo_curso = codigo_curso

        sql = f""" SELECT Codigo_Curso FROM Inscritos WHERE Id_Alumno = '{id_alumno}'  """
        info_inscripciones = self.ejecutar_consulta(sql)
        
        for curso in info_inscripciones:# se itera en cada tupla retornada por ejecutar_consulta()
            if curso[0] == codigo_curso: # se compara la posicion sub0 de la tupla la cual esta siendo iterada
             return True  # El alumno ya está inscrito en este curso
    
        return False  # El alumno no está inscrito en este curso
#------------------------------------------------------------------------------------------------------------------------------------------


     
#------------------------------------------------------------------------------------------------------------------------------------------
    #Leer y actualizar No_inscripcion***
    def entry_num_inscripcion(self):
        sql = f"""SELECT COUNT(*) FROM Inscritos"""
        num_inscripcion = self.ejecutar_consulta(sql)
        self.num_Inscripcion.insert(0,num_inscripcion) 
#-----------------------------------------------------------------------------------------------------------------------------------        
    


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
        selected_item = self.tView.selection()[0]
        # Obtener los valores de la fila seleccionada
        # Rellenar los campos de entrada
        self.id_Curso.delete(0, tk.END)
        self.id_Curso.insert(0, self.tView.item(selected_item)['text'])  # Suponiendo que el primer valor es para entry1
        self.descripc_Curso.delete(0, tk.END)
        self.descripc_Curso.insert(0, self.tView.item(selected_item)['values'][0])# Suponiendo que el segundo valor es para en
    
    def validar_entry(self,funcion):
        return len(funcion.get()) != 0
    
    def agregar_curso(self):
        if self.validar_entry(self.id_Curso):
            codigo_curso = self.id_Curso.get()
            curso = self.descripc_Curso.get()
            hora = self.horario.get()
            nuevo_curso = (codigo_curso, curso, hora)
            self.tView.insert('',0,text= nuevo_curso[0],values = [nuevo_curso[1],nuevo_curso[2]])
            
#--------------------------------------------------------------------------------------------------------------        
    
    
#------------------------------------------------------------------------------------------------------------------------------------------   
    #estudiar codigo de compañero***
    


#------------------------------------------------------------------------------------------------------------------------------------------
          

#-----------------------------------------------------------------------------------------------
    def validar_fecha(self, event):
        fecha = self.fecha.get()
        largo = len(fecha)

        # Si el usuario ingresó el día y aún no ha ingresado el mes, agregar automáticamente el '/'
        if largo == 2 and event.char != "/":
            self.fecha.insert(tk.END, "/")
        # Si el usuario ingresó el mes y aún no ha ingresado el año, agregar automáticamente el '/'
        elif largo == 5 and event.char != "/":
            self.fecha.insert(tk.END, "/")

        # Validación de la fecha
        if self.validar_formato_fecha(fecha):
            pass
        else:
            messagebox('validacion Fecha',"Formato de fecha inválido")

    def validar_formato_fecha(self, fecha):
        # Implementa tu lógica de validación de fecha aquí
        return True  # Por ahora, siempre devuelve True para la demostración



        
            
                

        
            

                
            
            


        





        




       
    def run(self):
        self.mainwindow.mainloop()
    


    ''' A partir de este punto se deben incluir las funciones
     para el manejo de la base de datos '''

if __name__ == "__main__":
    app = Inscripciones_2()
    app.run()