import os
import json
import random

from scryptlib import (
        compile_contract, build_contract_class, build_type_classes
        )

contract = './res/testPrimeField.scrypt' 

compiler_result = compile_contract(contract, debug=True)
desc = compiler_result.to_desc()

# Load desc instead:
#with open('./out/testPrimeField_desc.json', 'r') as f:
#    desc = json.load(f)

type_classes = build_type_classes(desc)

PrimeFieldTest = build_contract_class(desc)
prime_field_test = PrimeFieldTest()


#def test_fmul_0():
#    assert prime_field_test.testFmul(
#    ).verify()

