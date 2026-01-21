# test_unit.py

import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility

def test_deposit_valid():
    assert deposit(1000, 500) == 1500

def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, -100)

def test_withdraw_valid():
    assert withdraw(1000, 500) == 500

def test_withdraw_insufficient():
    with pytest.raises(ValueError):
        withdraw(500, 1000)

def test_calculate_interest_valid():
    result = calculate_interest(1000, 10, 2)
    assert round(result, 2) == 1210.00

def test_calculate_interest_invalid():
    with pytest.raises(ValueError):
        calculate_interest(-1000, 5, 2)

def test_check_loan_eligible():
    assert check_loan_eligibility(6000, 750) is True

def test_check_loan_not_eligible():
    assert check_loan_eligibility(3000, 650) is False
