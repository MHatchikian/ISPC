//Mostrar s�lo los n�meros pares desde 0 hasta el n�mero ingresado (input). 
//Nota: para saber si un n�mero es par hacer i % 2 == 0)

Algoritmo  Ej_2
	Escribir "Ingrese un numero"
    Leer num
    Para i desde 0 hasta num hacer
        Si i % 2 == 0 entonces
            Escribir i
        Fin Si
    Fin Para
	Escribir "Numeros pares de 0 a " num
FinAlgoritmo
