def Cancelar(self):
    entry_list = [self.fecha, self.nombres, self.apellidos, self.id_Curso, self.descripc_Curso, self.horario]

    for entry in entry_list:
        if entry != self.num_Inscripcion: 
            entry.delete(0, tk.END)
            