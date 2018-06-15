"""
Created by Soumya Ranjan Rout on 6/15/2018
"""
class UserData:
    def __init__(self):
        """
        This class is to get input from a file of user data
        and convert the contain of user data in to two dimensional
        array
        """
        with open('Test_Input') as file:
            self.data = file.read()
        self.output = self.data.splitlines()
        self.user_transaction = list()
        self.data_store = list()
        self.data_process()

    def data_process(self):
        """
        Here I am going to read thr file
        It is assuming the file name is constant and
        Return a two dimensional list of input ATM file
        """
        self.output = self.data.splitlines()
        for line in self.output :
            if line != '':
                self.data_store.append(line)
            else:
                self.list_data = [l for l in self.data_store]
                self.user_transaction.append(self.list_data)
                del self.data_store[:]


    def get_user_details(self):
        """
        Here I am retuning the value which I
        retrieve from the ATM input file
        :return: It will return a multi dimention list with all user detail
        """
        return self.user_transaction


