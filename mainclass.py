import pandas as pd

class EmployeeDataAnalysis:
    def __init__(self, data):

        self.df = pd.DataFrame(data)

    def display_head(self):
        """Return the first 5 rows of the DataFrame."""
        return self.df.head()

    def dataframe_info(self):
        """Return DataFrame column names and data types."""
        return self.df.info()

    def get_employee_by_id(self, employee_id):
        """Retrieve employee details by Employee ID."""
        return self.df[self.df['Employee ID'] == employee_id]

    def get_employees_above_age(self, age):
        """Get employees whose age is greater than the specified value."""
        return self.df[self.df['Age'] > age]

    def save_to_csv(self, filename="employee_data1.csv"):
        """Save the DataFrame to a CSV file."""
        self.df.to_csv(filename, index=False)
