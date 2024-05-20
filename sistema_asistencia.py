import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

class SistemaDeAsistencia:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Control de Asistencias")
        
        # Crear un notebook para organizar las pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)
        
        # Crear los frames para las pestañas
        self.frame_alumnos = tk.Frame(self.notebook, width=800, height=400)
        self.frame_asistencias = tk.Frame(self.notebook, width=800, height=400)
        
        self.frame_alumnos.pack(fill="both", expand=True)
        self.frame_asistencias.pack(fill="both", expand=True)
        
        # Añadir los frames al notebook
        self.notebook.add(self.frame_alumnos, text="Gestión de Alumnos")
        self.notebook.add(self.frame_asistencias, text="Registro de Asistencias")
        
        # Llamar a las funciones para crear el contenido de cada pestaña
        self.create_alumnos_tab()
        self.create_asistencias_tab()

    def create_alumnos_tab(self):
        # Widgets para gestión de alumnos
        self.label_nombres = tk.Label(self.frame_alumnos, text="Nombres")
        self.label_nombres.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombres = tk.Entry(self.frame_alumnos)
        self.entry_nombres.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_apellido = tk.Label(self.frame_alumnos, text="Apellido")
        self.label_apellido.grid(row=1, column=0, padx=10, pady=10)
        self.entry_apellido = tk.Entry(self.frame_alumnos)
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=10)
        
        self.label_grado = tk.Label(self.frame_alumnos, text="Grado")
        self.label_grado.grid(row=2, column=0, padx=10, pady=10)
        self.entry_grado = tk.Entry(self.frame_alumnos)
        self.entry_grado.grid(row=2, column=1, padx=10, pady=10)
        
        self.button_add_student = tk.Button(self.frame_alumnos, text="Agregar Alumno", command=self.add_student)
        self.button_add_student.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.button_view_students = tk.Button(self.frame_alumnos, text="Ver Alumnos", command=self.view_students)
        self.button_view_students.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.tree_students = ttk.Treeview(self.frame_alumnos, columns=("ID", "Nombres", "Apellido", "Grado"), show="headings")
        self.tree_students.heading("ID", text="ID")
        self.tree_students.heading("Nombres", text="Nombres")
        self.tree_students.heading("Apellido", text="Apellido")
        self.tree_students.heading("Grado", text="Grado")
        self.tree_students.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    
    def create_asistencias_tab(self):
        # Widgets para gestión de asistencias
        self.label_student_id = tk.Label(self.frame_asistencias, text="ID del Alumno")
        self.label_student_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_student_id = tk.Entry(self.frame_asistencias)
        self.entry_student_id.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_nombre = tk.Label(self.frame_asistencias, text="Nombre")
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)
        self.entry_nombre = tk.Entry(self.frame_asistencias)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)
        
        self.label_apellido = tk.Label(self.frame_asistencias, text="Apellido")
        self.label_apellido.grid(row=2, column=0, padx=10, pady=10)
        self.entry_apellido = tk.Entry(self.frame_asistencias)
        self.entry_apellido.grid(row=2, column=1, padx=10, pady=10)
        
        self.label_grado = tk.Label(self.frame_asistencias, text="Grado")
        self.label_grado.grid(row=3, column=0, padx=10, pady=10)
        self.entry_grado = tk.Entry(self.frame_asistencias)
        self.entry_grado.grid(row=3, column=1, padx=10, pady=10)
        
        self.label_fecha = tk.Label(self.frame_asistencias, text="Fecha (YYYY-MM-DD)")
        self.label_fecha.grid(row=4, column=0, padx=10, pady=10)
        self.entry_fecha = tk.Entry(self.frame_asistencias)
        self.entry_fecha.grid(row=4, column=1, padx=10, pady=10)
        
        self.label_hora = tk.Label(self.frame_asistencias, text="Hora (HH:MM:SS)")
        self.label_hora.grid(row=5, column=0, padx=10, pady=10)
        self.entry_hora = tk.Entry(self.frame_asistencias)
        self.entry_hora.grid(row=5, column=1, padx=10, pady=10)
        
        self.button_add_attendance = tk.Button(self.frame_asistencias, text="Registrar Asistencia", command=self.add_attendance)
        self.button_add_attendance.grid(row=6, column=0, columnspan=2, pady=10)
        
        self.button_view_attendance = tk.Button(self.frame_asistencias, text="Ver Asistencias", command=self.view_attendance)
        self.button_view_attendance.grid(row=7, column=0, columnspan=2, pady=10)
        
        self.tree_attendance = ttk.Treeview(self.frame_asistencias, columns=("ID", "Estudiante ID", "Nombre", "Apellido", "Grado", "Fecha", "Hora"), show="headings")
        self.tree_attendance.heading("ID", text="ID")
        self.tree_attendance.heading("Estudiante ID", text="Estudiante ID")
        self.tree_attendance.heading("Nombre", text="Nombre")
        self.tree_attendance.heading("Apellido", text="Apellido")
        self.tree_attendance.heading("Grado", text="Grado")
        self.tree_attendance.heading("Fecha", text="Fecha")
        self.tree_attendance.heading("Hora", text="Hora")
        self.tree_attendance.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def add_student(self):
        nombres = self.entry_nombres.get()
        apellido = self.entry_apellido.get()
        grado = self.entry_grado.get()
        
        print("Nombres:", nombres)
        print("Apellido:", apellido)
        print("Grado:", grado)
        
        print("Apellido vacío?", apellido == "")
        print("Grado vacío?", grado == "")
        
        if nombres and apellido and grado:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="colegio"
            )
            c = conn.cursor()
            c.execute("INSERT INTO estudiante (nombres_estudiante, apellido_estudiante, grado) VALUES (%s, %s, %s)", (nombres, apellido, grado))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Alumno agregado exitosamente")
            self.entry_nombres.delete(0, tk.END)
            self.entry_apellido.delete(0, tk.END)
            self.entry_grado.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")


    def view_students(self):
        for row in self.tree_students.get_children():
            self.tree_students.delete(row)
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="colegio"
        )
        c = conn.cursor()
        c.execute("SELECT * FROM estudiante")
        rows = c.fetchall()
        conn.close()
        
        for row in rows:
            self.tree_students.insert("", tk.END, values=row)

    def add_attendance(self):
        estudiante_id = self.entry_student_id.get()
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        grado = self.entry_grado.get()
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        
        if estudiante_id and nombre and apellido and grado and fecha and hora:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="colegio"
            )
            c = conn.cursor()
            c.execute("INSERT INTO asistencia (id_estudiante, nombre_estudiante, apellido_estudiante, grado_estudiante, fecha, hora) VALUES (%s, %s, %s, %s, %s, %s)", (estudiante_id, nombre, apellido, grado, fecha, hora))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Asistencia registrada exitosamente")
            self.entry_student_id.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_apellido.delete(0, tk.END)
            self.entry_grado.delete(0, tk.END)
            self.entry_fecha.delete(0, tk.END)
            self.entry_hora.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
    
    def view_attendance(self):
        for row in self.tree_attendance.get_children():
            self.tree_attendance.delete(row)
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="colegio"
        )
        c = conn.cursor()
        c.execute("SELECT * FROM asistencia")
        rows = c.fetchall()
        conn.close()
        
        for row in rows:
            self.tree_attendance.insert("", tk.END, values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaDeAsistencia(root)
    root.mainloop()
