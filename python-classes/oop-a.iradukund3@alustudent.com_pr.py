# Create a parent class
class Patient:
    def _init_(self, id, name, age, gender, admission_date, condition):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.condition = condition

    # Method to display patient details
    def get_details(self):
        return (f"Patient ID: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Admission Date: {self.admission_date}, Condition: {self.condition}"
)

# Create multiple patient objects and store them in a list
patient_1 = Patient(124, "X", 47, "Female", "31/October/2024", "High fever")
patient_2 = Patient(224, "Y", 57, "Male", "30/October/2024", "Diabetes")
patient_3 = Patient(324, "Z", 82, "Female", "21/October/2024", "Blood pressure")

patient_list = [patient_1, patient_2, patient_3]

# Function to count the number of patients
def count_patients(patient_list):
    return len(patient_list)

# Function to list all patient names
def list_patient_names(patient_list):
    return [patient.name for patient in patient_list]

# Function to search and print patient details by ID
def print_patient_by_id(patient_list):
    # Prompt user for patient ID
    patient_id = int(input("Enter Patient ID to search: "))
    
    # Search for the patient with the matching ID
    for patient in patient_list:
        if patient.id == patient_id:
            print(patient.get_details())
            return  # Exit the function if patient is found

    # If no patient was found with the given ID
    print("Patient not found.")

# Testing the functions
print("Patient Details:")
for patient in patient_list:
    print(patient.get_details())

print("\nTotal Number of Patients:", count_patients(patient_list))
print("List of Patient Names:", list_patient_names(patient_list))
# Test the print_patient_by_id function

print_patient_by_id(patient_list)
