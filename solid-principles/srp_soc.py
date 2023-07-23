class Journal:
    """
    The primary responsibility of this Journal class is to either add or remove an entry
    SRP or SOC should make sure that the primary responsibility is not altered/changed; or that any other responsbility is added.
    """
    def __init__(self):
        self.entries = list()
        self.count = 0
    
    def add_entry(self, text):
        """
        Method to add a journal entry
        """
        self.count += 1
        self.entries.append(f'Entry Number {self.count}: {text}')
    
    def remove_entry(self, position):
        """
        Method to remove a journal entry
        """
        del self.entries[position]
    
    def __str__(self):
        return '\n'.join(self.entries)
    
    # def save_entry(self, filename):
    #     """
    #     The addition of this new functionality would break the SRP/SOC.
    #     Secondary responsibility would be to save the journal entry.
    #     To match with the SOLID principles, this has to be kept outside of the class.
    #     """
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    

class PersitanceManager:
    """
    The responsibility of this class is to saving the object to a file.
    """
    @staticmethod
    def save_entry_to_file(journal, filename):
        """
        Method to save journal entries into a file.
        """
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


if __name__ == "__main__":
    journal_obj = Journal()
    journal_obj.add_entry('Nothing is impossible.')
    journal_obj.add_entry('Patience is virtue.')
    print(f'Below are the journal entries: \n{journal_obj}')

    filename = r'C:\01_Data_Adithya\Practice_Code\Design_Patterns_Python\design-patterns-python\solid-principles\journal_entries.txt'
    PersitanceManager.save_entry_to_file(journal=journal_obj, filename=filename)
    with open(filename) as j_entries:
        print(f'\nNow printing the journal entries from the file... \n{j_entries.read()}')
