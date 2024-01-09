from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import click
from models import Base, Patient, Appointment, Staff, engine
from datetime import datetime

def add_patient():
    #"""Add a new patient."""
    print("Add patient")
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

def schedule_appointment():
        """Schedule a new appointment."""
        print("Booking apointment: ")
        date = input('Enter appointment date (YYYY-MM-DD): ')
        type = input('Enter appointment type')
        patient_id = input('Enter patient ID: ')
        doctor_id = input('Enter doctor ID: ')

        session = Session()
        new_appointment = Appointment(appointment_date=date, appointment_type= type, patient_id=patient_id, medical_staff_id=doctor_id)
        session.add(new_appointment)
        session.commit()
        session.close()
        click.echo(f"Appointment scheduled successfully for Patient ID {patient_id} with Doctor ID {doctor_id}.")

def add_staff():
     print("Add medical staff")
     name= input("Enter staff name: ")
     role = input("Enter staff specialization: ")

     session=Session()
     new_staff = Staff(name=name,specialization =role)
     session.add(new_staff)
     session.commit()
    #  staff_id=new_staff.id
     click.echo(f'Staff with name {name} added successfully.')

if __name__ == "__main__":
    # DATABASE_URL = "sqlite:///hospital.db"
    # engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # session.query(Patient).delete()
    print("\nWelcome to out Hospital")
    print("\nWe are honoured to have you in our hospital")
    while True:
        print("\nSelect option: ")
        print("1. Add Patient")
        print("2. Schedule an Appointment")
        print("3. Add Medical Staff")
        print("4. Quit")
        choice = int(input("Please enter your option :"))
        if (choice==1):
            add_patient()
        elif (choice==2):
            schedule_appointment()
        elif(choice==3):
             add_staff()
        elif(choice==4):
             pass
        else:
             print("Invalid option")
        
    

    

