from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import click
from models import Base, Patient, Appointment, Staff, engine
from datetime import datetime

def add_patient():
    try:
        #"""Add a new patient."""
        print("\nAdd patient")
        name = input('Enter patient name: ')
        dob_str = input("Enter date of birth (YYYY-MM-DD): ")
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        gender = input('Enter gender: ')
        contact = input('Enter contact number: ')

        new_patient = Patient(name=name, date_of_birth=dob, gender=gender, contact_number=contact)
        session.add(new_patient)
        session.commit()
        session.close()
        click.echo(f"Patient '{name}' added successfully.")
    except:
         print("Error occured")
         menu_options()

def schedule_appointment():
    try:
        """Schedule a new appointment."""
        print("\nBooking apointment: ")
        # date = input('Enter appointment date (YYYY-MM-DD): ')
        dob_str = input("Enter appointment date (YYYY-MM-DD): ")
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        type = input('Enter appointment type: ')
        patient_id = input('Enter patient ID: ')
        doctor_id = input('Enter doctor ID: ')

        session = Session()
        new_appointment = Appointment(appointment_date=dob, appointment_type= type, patient_id=patient_id, staff_id=doctor_id)
        session.add(new_appointment)
        session.commit()
        session.close()
        click.echo(f"Appointment scheduled successfully for Patient ID {patient_id} with Doctor ID {doctor_id}.")
    except:
            print("\nError occured")
            menu_options()

def add_staff():
    try:
        print("\nAdd medical staff")
        name= input("Enter staff name: ")
        role = input("Enter staff specialization: ")

        session=Session()
        new_staff = Staff(name=name,specialization =role)
        session.add(new_staff)
        session.commit()
    #  staff_id=new_staff.id
        click.echo(f'Staff with name {name} added successfully.')
    except:
         print("\nError occured")
         menu_options()

def display_doctors():
    """Display all doctors in the system."""
    session = Session()
    doctors = session.query(Staff.name).all()
    print(doctors)

#check appointments
def check_appointments():
    """Check upcoming and past appointments for patients."""
    while True:
        try:
            print("\nSelect option: ")
            print("1. Check appointment availability: ")
            print("2. Check appointment date: ")
            print("3. BACK")
            choice= int(input("\nSelect option: "))
            session = Session()
            if (choice==1):
                appt_id = input("\nEnter Appointment id: ")
                id= session.query(Appointment).filter(Appointment.id==appt_id).all()
                # print(id)
                if id!=[]:
                    print ("\n-----------------------------\nAppointment is available\n--------------------------------")
                else:
                    print("\n-----------------------------\nAppointment not available\n-----------------------------")
            elif (choice==2):
                app_id = input("\nEnter Appointment id: ")
                id= session.query(Appointment).filter(Appointment.id==app_id).all()
                print(id[0])  
            elif(choice==3):
                menu_options()
            else:
                print("Invalid option")
                menu_options()
        except:
             print("\nRecord not found")
#Menu option
def menu_options():
    print("\nSelect option: ")
    print("1. Add Patient")
    print("2. Schedule an Appointment")
    print("3. Add Medical Staff")
    print("4. Check appointment")
    print("5. Quit\n")
    choice = int(input("Please enter your option :"))
    if (choice==1):
        add_patient()
    elif (choice==2):
        schedule_appointment()
    elif(choice==3):
            add_staff()
    elif(choice==4):
          check_appointments()
    elif(choice==5):
            exit()
    else:
            print("Invalid option")

if __name__ == "__main__":
    DATABASE_URL = "sqlite:///hospital.db"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # session.query(Patient).delete()
    print("\nWelcome to our Hospital\n--------------------------------")
    print("\nWe are honoured to have you")
    while True:
          menu_options()
        
    

    

