#!/usr/bin/python3

class Patient:
    """
    Patient class represents a hospital patient with attributes like ID, name, age, gender, 
    admission date, and condition. The class includes a method to display patient details.
    """

    def __init__(self, id, name, age, gender, admission_date, condition):
        """
        Initialize the Patient object with ID, name, age, gender, admission date, and condition.
        """
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.condition = condition

    def get_details(self):
        """
        Return a summary of the patient's information as a formatted string.
        """
        return (f"Patient ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Admission Date: {self.admission_date}\n"
                f"Condition: {self.condition}\n")


# Creating multiple Patient instances
patient1 = Patient(1, "Alice Johnson", 30, "Female", "2023-01-01", "Flu")
patient2 = Patient(2, "Bob Smith", 45, "Male", "2023-02-15", "Pneumonia")
patient3 = Patient(3, "Charlie Davis", 29, "Male", "2023-03-10", "Broken Arm")

# Storing patients in a list
patients = [patient1, patient2, patient3]

def count_patients(patient_list):
    """
    Count and return the total number of patients in the list.
    """
    return len(patient_list)

def list_patient_names(patient_list):
    """
    Return a list of patient names from the given list of patients.
    """
    return [patient.name for patient in patient_list]

def print_patient_by_id(patient_list):
    """
    Prompt the user for a patient ID, search the patient list, 
    and print patient details if found; otherwise, print a 'not found' message.
    """
    try:
        patient_id = int(input("Enter the patient ID: "))
        for patient in patient_list:
            if patient.id == patient_id:
                print("\nPatient details:\n", patient.get_details())
                return
        print("Patient not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")


# Sample output demonstration
if __name__ == "__main__":
    # Testing count_patients function
    print("Total patients:", count_patients(patients))

    # Testing list_patient_names function
    print("List of patient names:", list_patient_names(patients))

    # Testing print_patient_by_id function
    print_patient_by_id(patients)
