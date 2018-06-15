"""
Created by Soumya Ranjan Rout on 6/15/2018
"""
from UserData import UserData as Atm
from collections import namedtuple

data_object=Atm()
input = data_object.get_user_details()
error_message_for_account_validation = "ACCOUNT_ERR"
error_message_for_funds_unavailability = "FUNDS_ERR "
error_message_for_out_of_cash = "ATM_ERR"
total_atm_cash = [int(input.pop(0)[0])]

def process_input(data):
    """
    Creating diffrent namedtuples for all user session
    :param data: ATM user data file
    """
    for atm_data in data:
        atm_number, correct_pin, entered_pin = set_atm_number_pin(atm_data[0])
        balance, overdraft = set_balance_overdradt(atm_data[1])
        Session = namedtuple('Session', 'atm_number correct_pin entered_pin balance overdraft')
        session = Session(atm_number, correct_pin, entered_pin, balance, overdraft)
        set_transaction(atm_data[2:], session)


def set_atm_number_pin(atm_number_pin):
    """
    :param atm_number_pin: Here I am passing correct pin and entered pin
    :return: It returns a tuple of account number, correct pin and entered pin EXMPLE(12345678, 1234, 1234)
    """
    return tuple([int(i) for i in atm_number_pin.split()])


def set_balance_overdradt(bal_overdraft):
    """
    :param bal_overdraft: Here I am passing balance and overdraft balance
    :return: It returns a tuple of balance and overdraft balance EXAMPLE(500,100)
    """
    return tuple([int(i) for i in bal_overdraft.split()])


def set_transaction(transaction, session):
    """
    :param transaction: Here I am passing all data after account number , pin and balance.
    :param session: Named tuple account number, correct pin and entered pin EXMPLE(12345678, 1234, 1234)
    :return: It will display all trascation to user
    """
    for data in transaction:
        if session.entered_pin != session.correct_pin:
            print(error_message_for_account_validation)
            return
        if data == 'B':
            print(session.balance)
        elif data.split(' ')[0] == 'W':
            withdrawl = int(data.split(' ')[1])
            if withdrawl <= int(session.balance)+int(session.overdraft) and withdrawl < total_atm_cash[0]:
                later_balance = int(session.balance) - withdrawl
                total_atm_cash[0] -=  withdrawl
                print(later_balance)
            elif withdrawl > int(session.balance)+int(session.overdraft) :
                print(error_message_for_funds_unavailability)
            else:
                print(error_message_for_out_of_cash)



if __name__ == '__main__':
    process_input(input)





