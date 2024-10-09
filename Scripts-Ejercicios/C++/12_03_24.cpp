//============================================================================
// Name        : POO-Ejercicio.cpp
// Author      : Acxel Martin Elizalde Camacho
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class Persona{
private:
	string nombre="Acxel", ap1="Fulano", ap2="Fulano2";
public:
	Persona(){}

	Persona(string nombre, string ap1, string ap2){
		this->nombre=nombre;
		this->ap1=ap1;
		this->ap2=ap2;
	}

	string getNombre(){
		return this->nombre;
	}
	string getAp1(){
			return this->ap1;
		}
	string getAp2(){
			return this->ap2;
		}

	//print Info only Class Persona
	void printInfo(){
		cout<<"\t Clase Persona"<<endl;
		cout<<"\t Nombre: "<<nombre<<endl;
		cout<<"\t Primer Apellido: "<<ap1<<endl;
		cout<<"\t Segundo Apellido: "<<ap2<<endl;
	}
};

class Empleado : public Persona{
private:
	int n_empleado=1234;
	float sueldo=100.0;
	string tipoContrato="indefinido";
public:
	Empleado(){}

	Empleado(int n_empleado, float sueldo, string tipoContrato){
				this->n_empleado=n_empleado;
				this->sueldo=sueldo;
				this->tipoContrato=tipoContrato;
	}

	Empleado(string nombre, string ap1, string ap2, int n_empleado, float sueldo, string tipoContrato)
	: Persona{nombre, ap1, ap2}{
		this->n_empleado=n_empleado;
		this->sueldo=sueldo;
		this->tipoContrato=tipoContrato;
	}

	int getN_empleado(){
		return this->n_empleado;
	}
	float getSueldo(){
			return this->sueldo;
		}
	string getTipoContrato(){
			return this->tipoContrato;
		}

	//print Info only Class Empleado
	void printInfo(){
		cout<<"\t Clase Empleado"<<endl;
		cout<<"\t Nombre: "<<this->getNombre()<<endl;
		cout<<"\t Primer Apellido: "<<this->getAp1()<<endl;
		cout<<"\t Segundo Apellido: "<<this->getAp2()<<endl;
		cout<<"\t Numero de Empleado: "<<n_empleado<<endl;
		cout<<"\t Sueldo: "<<sueldo<<endl;
		cout<<"\t Tipo de contrato: "<<tipoContrato<<endl;
	}
};

class Administrativo : public Empleado{
private:
	string puesto="N/A";
public:
	Administrativo(){}

	Administrativo(string nombre, string ap1, string ap2, int n_empleado, float sueldo, string tipoContrato, string puesto)
	: Empleado{nombre, ap1, ap2, n_empleado, sueldo, tipoContrato}{
		this->puesto=puesto;
	}

	string getPuesto(){
		return this->puesto;
	}

	//print Info only Class Administrativo
	void printInfo(){
		cout<<"\t Clase Administrativo"<<endl;
		cout<<"\t Nombre: "<<this->getNombre()<<endl;
		cout<<"\t Primer Apellido: "<<this->getAp1()<<endl;
		cout<<"\t Segundo Apellido: "<<this->getAp2()<<endl;
		cout<<"\t Numero de Empleado: "<<this->getN_empleado()<<endl;
		cout<<"\t Sueldo: "<<this->getSueldo()<<endl;
		cout<<"\t Tipo de contrato: "<<this->getTipoContrato()<<endl;
		cout<<"\t Puesto: "<<puesto<<endl;
	}
};

class Docente : public Empleado{
private:
	float horasTrabajo=40.0;
	string academia="N/A.";
public:
			Docente(){}

			Docente(string nombre, string ap1, string ap2, int n_empleado, float sueldo, string tipoContrato, float horasTrabajo, string academia)
			: Empleado{nombre, ap1, ap2, n_empleado, sueldo, tipoContrato}{
				this->horasTrabajo=horasTrabajo;
				this->academia=academia;
			}
			float getHorasTrabajo(){
				return this->horasTrabajo;
			}
			string getAcademia(){
				return this->academia;
			}

			//print Info only Class Docente
			void printInfo(){
					cout<<"\t Clase Docente"<<endl;
					cout<<"\t Nombre: "<<this->getNombre()<<endl;
					cout<<"\t Primer Apellido: "<<this->getAp1()<<endl;
					cout<<"\t Segundo Apellido: "<<this->getAp2()<<endl;
					cout<<"\t Numero de Empleado: "<<this->getN_empleado()<<endl;
					cout<<"\t Sueldo: "<<this->getSueldo()<<endl;
					cout<<"\t Tipo de contrato: "<<this->getTipoContrato()<<endl;
					cout<<"\t Horas de trabajo: "<<horasTrabajo<<endl;
					cout<<"\t Academia: "<<academia<<endl;
				}
};

class DocenteAsignatura : public Docente{
private:
	float horasGrupo=5.0;
	string materias="por asignar";
public:
	DocenteAsignatura(){}
	DocenteAsignatura(string nombre, string ap1, string ap2, int n_empleado, float sueldo, string tipoContrato, float horasTrabajo, string academia, float horasGrupo, string materias)
	: Docente{nombre, ap1, ap2, n_empleado, sueldo, tipoContrato, horasTrabajo, academia} {
		this->horasGrupo=horasGrupo;
		this->materias=materias;
	}
	float getHorasGrupo(){
					return this->horasGrupo;
				}
	string getMaterias(){
					return this->materias;
				}
			//print Info only Class DocenteAsignatura
			void printInfo(){
					cout<<"\t Clase DocenteAsignatura"<<endl;
					cout<<"\t Nombre: "<<this->getNombre()<<endl;
					cout<<"\t Primer Apellido: "<<this->getAp1()<<endl;
					cout<<"\t Segundo Apellido: "<<this->getAp2()<<endl;
					cout<<"\t Numero de Empleado: "<<this->getN_empleado()<<endl;
					cout<<"\t Sueldo: "<<this->getSueldo()<<endl;
					cout<<"\t Tipo de contrato: "<<this->getTipoContrato()<<endl;
					cout<<"\t Horas de trabajo: "<<this->getHorasTrabajo()<<endl;
					cout<<"\t Academia: "<<this->getAcademia()<<endl;
					cout<<"\t Horas de grupo: "<<horasGrupo<<endl;
					cout<<"\t Materias: "<<materias<<endl;
				}
};
class DocenteTiempoCompleto : public Docente{
private:
	float investigacion=20.0, asesoria=2.0, tutoria=2.0, horasGrupoTC=16.0;
	string materiasTC="por asignar";
public:
	DocenteTiempoCompleto(){}
	DocenteTiempoCompleto(string nombre, string ap1, string ap2, int n_empleado, float sueldo, string tipoContrato, float horasTrabajo, string academia, float horasGrupo, string materias, float investigacion, float asesoria, float tutoria, float horasGrupoTC,
	string materiasTC)
	: Docente{nombre, ap1, ap2, n_empleado, sueldo, tipoContrato, horasTrabajo, academia} {
		this->investigacion=investigacion;
		this->asesoria=asesoria;
		this->tutoria=tutoria;
		this->horasGrupoTC=horasGrupoTC;
		this->materiasTC=materiasTC;
	}
	float getInvestigacion(){
		return this->investigacion;
	}

	float getAsesoria(){
		return this->asesoria;
	}

	float getTutoria(){
		return this->tutoria;
	}

	float getHorasGrupoTC(){
					return this->horasGrupoTC;
				}
	string getMateriasTC(){
					return this->materiasTC;
				}
	//print Info only Class DocenteTiempoCompleto
	void printInfo(){
					cout<<"\t Clase DocenteTiempoCompleto"<<endl;
					cout<<"\t Nombre: "<<this->getNombre()<<endl;
					cout<<"\t Primer Apellido: "<<this->getAp1()<<endl;
					cout<<"\t Segundo Apellido: "<<this->getAp2()<<endl;
					cout<<"\t Numero de Empleado: "<<this->getN_empleado()<<endl;
					cout<<"\t Sueldo: "<<this->getSueldo()<<endl;
					cout<<"\t Tipo de contrato: "<<this->getTipoContrato()<<endl;
					cout<<"\t Horas de trabajo: "<<this->getHorasTrabajo()<<endl;
					cout<<"\t Academia: "<<this->getAcademia()<<endl;
					cout<<"\t Investigacion: "<<investigacion<<endl;
					cout<<"\t Asesoria: "<<asesoria<<endl;
					cout<<"\t Tutoria: "<<tutoria<<endl;
					cout<<"\t Horas de grupo TC: "<<horasGrupoTC<<endl;
					cout<<"\t Materias TC: "<<materiasTC<<endl;
				}
};

class Mantenimiento : public Empleado {
private:
	string turno="No Asignado", puestoM="indefinido";
public:
	Mantenimiento(){}
	Mantenimiento(string nombre, string ap1, string ap2, int n_empleado, float sueldo, string tipoContrato, string turno, string puestoM)
	: Empleado{nombre, ap1, ap2, n_empleado, sueldo, tipoContrato}{
		this->turno=turno;
		this->puestoM=puestoM;
	}
	string getTurno(){
		return this->turno;
	}
	string getPuestoM(){
			return this->puestoM;
		}
	void printInfo(){
						cout<<"\t Clase Mantenimiento"<<endl;
						cout<<"\t Nombre: "<<this->getNombre()<<endl;
						cout<<"\t Primer Apellido: "<<this->getAp1()<<endl;
						cout<<"\t Segundo Apellido: "<<this->getAp2()<<endl;
						cout<<"\t Numero de Empleado: "<<this->getN_empleado()<<endl;
						cout<<"\t Sueldo: "<<this->getSueldo()<<endl;
						cout<<"\t Tipo de contrato: "<<this->getTipoContrato()<<endl;
						cout<<"\t Turno: "<<turno<<endl;
						cout<<"\t Puesto M: "<<puestoM<<endl;
					}
};

class MantenimientoIntendencia : public Mantenimiento{
private:
	string asignacion="por definir";
public:
	MantenimientoIntendencia(){}
	MantenimientoIntendencia(string nombre, string ap1, string ap2, int n_empleado, float sueldo, string tipoContrato, string turno, string puestoM, string asignacion)
	: Mantenimiento{nombre, ap1, ap2, n_empleado, sueldo, tipoContrato, turno, puestoM}{
		this->asignacion=asignacion;
	}
	string getAsignacion(){
		return this->asignacion;
	}
	void printInfo(){
							cout<<"\t Clase MantenimientoIntendencia"<<endl;
							cout<<"\t Nombre: "<<this->getNombre()<<endl;
							cout<<"\t Primer Apellido: "<<this->getAp1()<<endl;
							cout<<"\t Segundo Apellido: "<<this->getAp2()<<endl;
							cout<<"\t Numero de Empleado: "<<this->getN_empleado()<<endl;
							cout<<"\t Sueldo: "<<this->getSueldo()<<endl;
							cout<<"\t Tipo de contrato: "<<this->getTipoContrato()<<endl;
							cout<<"\t Turno: "<<this->getTurno()<<endl;
							cout<<"\t Puesto M: "<<this->getPuestoM()<<endl;
							cout<<"\t Asignacion: "<<asignacion<<endl;
						}
};
class MantenimientoTecnico : public Mantenimiento{
private:
	string cargo="por definir";
public:
	MantenimientoTecnico(){}
	MantenimientoTecnico(string nombre, string ap1, string ap2, int n_empleado, float sueldo, string tipoContrato, string turno, string puestoM, string cargo)
	: Mantenimiento{nombre, ap1, ap2, n_empleado, sueldo, tipoContrato, turno, puestoM}{
		this->cargo=cargo;
	}
	string getCargo(){
		return this->cargo;
	}
	void printInfo(){
							cout<<"\t Clase MantenimientoTecnico"<<endl;
							cout<<"\t Nombre: "<<this->getNombre()<<endl;
							cout<<"\t Primer Apellido: "<<this->getAp1()<<endl;
							cout<<"\t Segundo Apellido: "<<this->getAp2()<<endl;
							cout<<"\t Numero de Empleado: "<<this->getN_empleado()<<endl;
							cout<<"\t Sueldo: "<<this->getSueldo()<<endl;
							cout<<"\t Tipo de contrato: "<<this->getTipoContrato()<<endl;
							cout<<"\t Turno: "<<this->getTurno()<<endl;
							cout<<"\t Puesto M: "<<this->getPuestoM()<<endl;
							cout<<"\t Cargo: "<<cargo<<endl;
						}
};

class AltaLaboral{
public:
	Persona persona;
	Empleado empleado;
};

int main() {
	Persona p1;
	p1.printInfo();
	cout<<"\t*************************************"<<endl;
	Empleado e1;
	e1.printInfo();
	cout<<"\t*************************************"<<endl;
	Administrativo a1;
	a1.printInfo();
	cout<<"\t*************************************"<<endl;
	Docente d1;
	d1.printInfo();
	cout<<"\t*************************************"<<endl;
	DocenteAsignatura da1;
	da1.printInfo();
	cout<<"\t*************************************"<<endl;
	DocenteTiempoCompleto dtc;
	dtc.printInfo();
	cout<<"\t*************************************"<<endl;
	Mantenimiento m;
	m.printInfo();
	cout<<"\t*************************************"<<endl;
	MantenimientoIntendencia m1;
	m1.printInfo();
	cout<<"\t*************************************"<<endl;
	MantenimientoTecnico m2;
	m2.printInfo();
	cout<<"\t*************************************"<<endl;

	return 0;
}
